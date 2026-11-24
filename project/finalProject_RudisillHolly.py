# Holly Rudisill
# 11/19/2026
# Final Project
# Final Project Gamifies to-do list using Claude to build the code  

"""
Gamified To-Do List Manager
===========================
Turn your to-do list into a game: earn points for finishing tasks, keep a
weekly streak going, level up, collect badges, open mystery chests, and spend
your points on rewards (TV time, crochet time, yarn, and more).

Only Python's built-in (standard library) modules are used:
    random -> critical hits, mystery chest drops, encouragement messages
    time   -> dates/timestamps, time of day, and suspense pauses
    json, os, sys, datetime, copy -> saving files and date math

Run it with:  python gamified_todo.py
"""

import copy
import json
import os
import random
import sys
import time
from datetime import date, datetime, timedelta

# Make sure emojis print correctly on terminals that support UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

# ----------------------------------------------------------------------
# FILES
# ----------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, "gamified_tasks.json")   # your tasks
GAME_FILE = os.path.join(BASE_DIR, "gamified_game.json")    # points, streaks, etc.

# ----------------------------------------------------------------------
# SETTINGS (change numbers here to rebalance the game)
# ----------------------------------------------------------------------
PAUSE = 0.8                 # seconds between lines in animations
CRIT_CHANCE = 10            # 1 in 10 -> 10% critical hit (double points)
STREAK_ACTIVE_DAYS = 4      # active days needed in a week to keep the streak
FIFTH_DAY_BONUS = 25        # flat bonus points for a 5th active day in a week
QUEST_MAX_TARGET = 10       # weekly quest: finish up to this many tasks
QUEST_MIN_DUE = 3           # need at least this many tasks due to get a quest
PITY_LIMIT = 5              # chests in a row without Gold+ before a Gold is guaranteed
YARN_WEEKLY_CAP = 20.0      # max dollars of yarn per week (shop + chests)

# Emojis live in one place so they are easy to change.
E = {
    "todo": "⬜", "done": "✅", "overdue": "⚠️", "today": "📅",
    "points": "⭐", "streak": "🔥", "level": "🏆", "party": "🎉",
    "chest": "🎁", "quest": "🎯", "spark": "✨", "lock": "🔒",
    "full": "🟩", "empty": "⬜", "badge": "🏅", "crit": "💥",
}

# Task sizes: points and a short description of how much effort they take.
SIZES = {
    "small":  {"label": "Small",  "emoji": "🟢", "points": 10,
               "effort": "under 30 minutes"},
    "medium": {"label": "Medium", "emoji": "🟡", "points": 20,
               "effort": "30 minutes to 2 hours"},
    "large":  {"label": "Large",  "emoji": "🔴", "points": 50,
               "effort": "2 to 6 hours, or spread over several days"},
    "boss":   {"label": "Boss",   "emoji": "👑", "points": 300,
               "effort": "weeks of work or a major milestone"},
}
SIZE_KEYS = ["small", "medium", "large", "boss"]

# Levels are based on lifetime points earned. They never go down.
LEVELS = [
    (0,    "Chain Starter",     "🧵"),
    (150,  "Stitch Apprentice", "🪡"),
    (400,  "Yarn Collector",    "🧶"),
    (800,  "Pattern Weaver",    "🔶"),
    (1400, "Granny Square Pro", "🏅"),
    (2200, "Blanket Builder",   "🧥"),
    (3500, "Yarn Master",       "👑"),
]

# Reward tiers: cost in points, level needed, and the rewards in each tier.
TIERS = {
    "bronze": {"name": "Bronze", "emoji": "🥉", "cost": 30, "min_level": 1,
               "rewards": ["30 minutes of scrolling", "A favorite snack",
                           "One episode of a show"]},
    "silver": {"name": "Silver", "emoji": "🥈", "cost": 80, "min_level": 2,
               "rewards": ["Watch TV for 2 hours", "Crochet for 2 hours"]},
    "gold": {"name": "Gold", "emoji": "🥇", "cost": 150, "min_level": 3,
             "rewards": ["Crochet for 4 hours", "Yarn shopping (max $20)"]},
    "platinum": {"name": "Platinum", "emoji": "💎", "cost": 300, "min_level": 5,
                 "rewards": ["A full crochet day",
                             "A bigger treat of your choice"]},
}
TIER_KEYS = ["bronze", "silver", "gold", "platinum"]

# Badges are cosmetic only (no points).
BADGES = {
    "early_bird":    ("🌅", "Early Bird",    "Finish a task before 9 AM"),
    "four_alive":    ("🔥", "Four Alive",    "Complete a streak week (4 active days)"),
    "five_alive":    ("⭐", "Five Alive",    "Earn your first 5th-day bonus"),
    "lucky_strike":  ("💥", "Lucky Strike",  "Land your first critical hit"),
    "right_on_time": ("🎯", "Right on Time", "Finish 5 tasks by their due dates"),
    "overachiever":  ("📚", "Overachiever",  "Complete 5 tasks in one day"),
    "clean_slate":   ("🛡️", "Clean Slate",   "End a week with zero overdue tasks"),
    "comeback_kid":  ("🔄", "Comeback Kid",  "Complete a task after missing a streak week"),
    "chest_opener":  ("🎁", "Chest Opener",  "Open 5 mystery chests"),
    "boss_slayer":   ("👑", "Boss Slayer",   "Defeat your first Boss task"),
}

ENCOURAGEMENT = [
    "Nice work!", "You're on a roll!", "One more down!", "Look at you go!",
    "That's how it's done!", "Keep that momentum going!", "Another win!",
    "Stitch by stitch, task by task!", "Well done, you earned that!",
]


# ----------------------------------------------------------------------
# SMALL HELPERS (dates, input, saving)
# ----------------------------------------------------------------------
def today():
    """Today's date, read with the time library."""
    return date.fromisoformat(time.strftime("%Y-%m-%d"))


def current_hour():
    """Hour of the day (0-23), used for the Early Bird badge."""
    return time.localtime().tm_hour


def week_start(d):
    """The Sunday on or before date d (weeks run Sunday through Saturday)."""
    return d - timedelta(days=(d.weekday() + 1) % 7)


def to_date(text):
    return date.fromisoformat(text)


def fmt_date(d):
    return d.strftime("%a %b %d")


def parse_date(text):
    """Accept YYYY-MM-DD or MM/DD/YYYY. Returns a date or None."""
    for pattern in ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y"):
        try:
            return datetime.strptime(text.strip(), pattern).date()
        except ValueError:
            continue
    return None


def round_points(x):
    """Round half up to a whole number of points."""
    return int(x + 0.5 + 1e-9)


def ask(prompt):
    return input(prompt).strip()


def pause(seconds=None):
    time.sleep(PAUSE if seconds is None else seconds)


def bar(done, total):
    """A simple emoji progress bar, like 🟩🟩⬜⬜."""
    done = max(0, min(done, total))
    return E["full"] * done + E["empty"] * (total - done)


def load_json(path, default):
    """Load a JSON file. If it is missing or damaged, return the default."""
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        backup = path + ".bak"
        try:
            os.replace(path, backup)
            print(f"⚠️  Couldn't read {os.path.basename(path)}; "
                  f"saved a copy as {os.path.basename(backup)} and started fresh.")
        except OSError:
            pass
        return default


def save_json(path, data):
    """Write to a temporary file first so a crash can't damage your save."""
    temp = path + ".tmp"
    with open(temp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(temp, path)


def save_all(tasks, game):
    save_json(TASK_FILE, tasks)
    save_json(GAME_FILE, game)


# ----------------------------------------------------------------------
# LOADING / CREATING SAVE DATA
# ----------------------------------------------------------------------
def new_game():
    return {
        "vault": 0,                 # points you can spend
        "lifetime": 0,              # total points earned (drives your level)
        "level": 1,                 # highest level reached (never goes down)
        "streak_weeks": 0,          # consecutive streak weeks completed
        "week_start": week_start(today()).isoformat(),
        "fifth_paid": False,        # 5th-day bonus paid this week?
        "quest_target": 0,          # tasks to finish for this week's chest
        "quest_awarded": False,
        "chests": [],               # unopened chests: "boss" or "quest"
        "pity": 0,                  # chests in a row without Gold or better
        "inventory": [],            # rewards bought/won but not used yet
        "claimed": [],              # rewards you've used, with dates
        "yarn_spent": 0.0,          # yarn dollars spent this week
        "badges": {},               # badge key -> date earned
        "stats": {"crits": 0, "chests_opened": 0, "fifth_ever": False},
        "comeback_pending": False,
        "done_log": [],             # one entry per currently checked-off task
        "next_id": 1,
    }


def load_game():
    game = load_json(GAME_FILE, None)
    base = new_game()
    if not isinstance(game, dict):
        return base
    for key, value in base.items():
        game.setdefault(key, copy.deepcopy(value))
    for key, value in base["stats"].items():
        game["stats"].setdefault(key, value)
    return game


def load_tasks(game):
    """Load tasks. Older files without a size or points are given defaults."""
    raw = load_json(TASK_FILE, [])
    tasks = []
    if not isinstance(raw, list):
        return tasks
    for item in raw:
        if not isinstance(item, dict):
            continue
        title = item.get("title") or item.get("task") or item.get("name")
        due_text = item.get("due") or item.get("due_date")
        due = parse_date(str(due_text)) if due_text else None
        if not title or due is None:
            continue
        size = item.get("size", "medium")
        if size not in SIZES:
            size = "medium"          # old tasks default to Medium
        done = bool(item.get("done", item.get("completed", False)))
        tasks.append({
            "id": item.get("id", 0),
            "title": str(title),
            "size": size,
            "due": due.isoformat(),
            "done": done,
            "added_on": item.get("added_on", today().isoformat()),
            "completed_on": item.get("completed_on"),
            "completed_at": item.get("completed_at"),
            "points_earned": item.get("points_earned", 0),
            "chest_awarded": item.get("chest_awarded", False),
        })
    # Make sure every task has a unique id.
    used = set()
    top = max([t["id"] for t in tasks if t["id"]] + [game["next_id"] - 1, 0])
    for t in tasks:
        if not t["id"] or t["id"] in used:
            top += 1
            t["id"] = top
        used.add(t["id"])
    game["next_id"] = max(game["next_id"], top + 1)
    return tasks


# ----------------------------------------------------------------------
# GAME RULES
# ----------------------------------------------------------------------
def level_for(lifetime):
    """Level number (1-based) for a lifetime point total."""
    level = 1
    for i, (threshold, _name, _emoji) in enumerate(LEVELS):
        if lifetime >= threshold:
            level = i + 1
    return level


def level_info(level):
    _threshold, name, emoji = LEVELS[level - 1]
    return name, emoji


def update_level(game):
    """Raise the stored level if lifetime points earned a new one."""
    earned = level_for(game["lifetime"])
    if earned > game["level"]:
        old = game["level"]
        game["level"] = earned
        name, emoji = level_info(earned)
        print(f"\n{E['party']}{E['party']} LEVEL UP! {E['party']}{E['party']}")
        pause()
        print(f"   You reached Level {earned}: {emoji} {name}!")
        unlocked = [t for t in TIER_KEYS
                    if old < TIERS[t]["min_level"] <= earned]
        for key in unlocked:
            print(f"   {TIERS[key]['emoji']} {TIERS[key]['name']} rewards unlocked!")
        if earned in (4, 6, 7):
            print(f"   {E['chest']} Your mystery chest odds just got better!")


def streak_bonus_pct(streak_weeks):
    """Bonus percentage based on consecutive streak weeks."""
    if streak_weeks >= 12:
        return 0.20
    if streak_weeks >= 8:
        return 0.15
    if streak_weeks >= 4:
        return 0.10
    if streak_weeks >= 2:
        return 0.05
    return 0.0


def timing_factor(days_early):
    """Return (multiplier, description) based on how early/late a task is."""
    if days_early >= 1:
        return 1.10, "early bonus +10%"
    if days_early == 0:
        return 1.00, "on time"
    if days_early >= -3:
        return 0.75, "1-3 days late (75%)"
    return 0.50, "4+ days late (50%)"


def active_days(game, ws):
    """Set of dates (as text) with at least one completion in the week of ws."""
    days = set()
    for entry in game["done_log"]:
        d = to_date(entry["date"])
        if ws <= d <= ws + timedelta(days=6):
            days.add(entry["date"])
    return days


def current_ws(game):
    return to_date(game["week_start"])


def due_ids_this_week(tasks, game):
    ws = current_ws(game)
    we = ws + timedelta(days=6)
    ids = set()
    for t in tasks:
        if ws <= to_date(t["due"]) <= we:
            ids.add(t["id"])
    for entry in game["done_log"]:
        if ws <= to_date(entry["due"]) <= we:
            ids.add(entry["id"])
    return ids


def quest_progress(game):
    ws = current_ws(game)
    we = ws + timedelta(days=6)
    return len([e for e in game["done_log"] if ws <= to_date(e["due"]) <= we])


def refresh_quest(game, tasks):
    """Quest target = min(10, tasks due this week). It can go up, never down."""
    count = len(due_ids_this_week(tasks, game))
    if count >= QUEST_MIN_DUE:
        game["quest_target"] = max(game["quest_target"],
                                   min(QUEST_MAX_TARGET, count))


def award_badge(game, key):
    if key in game["badges"]:
        return False
    game["badges"][key] = today().isoformat()
    emoji, name, _desc = BADGES[key]
    print(f"\n{E['badge']} BADGE UNLOCKED: {emoji} {name}!")
    return True


def check_badges(game):
    log = game["done_log"]
    if any(e["hour"] < 9 for e in log):
        award_badge(game, "early_bird")
    weeks = {}
    for e in log:
        ws = week_start(to_date(e["date"]))
        weeks.setdefault(ws, set()).add(e["date"])
    if any(len(days) >= STREAK_ACTIVE_DAYS for days in weeks.values()):
        award_badge(game, "four_alive")
    if game["stats"]["fifth_ever"]:
        award_badge(game, "five_alive")
    if game["stats"]["crits"] >= 1:
        award_badge(game, "lucky_strike")
    if len([e for e in log if e["on_time"]]) >= 5:
        award_badge(game, "right_on_time")
    per_day = {}
    for e in log:
        per_day[e["date"]] = per_day.get(e["date"], 0) + 1
    if any(n >= 5 for n in per_day.values()):
        award_badge(game, "overachiever")
    if game["stats"]["chests_opened"] >= 5:
        award_badge(game, "chest_opener")
    if any(e["size"] == "boss" for e in log):
        award_badge(game, "boss_slayer")


def roll_week(game, tasks):
    """
    Close out any finished weeks (Sunday-Saturday), update the streak, and
    start the current week. Returns a list of messages to show the player.
    """
    messages = []
    now_ws = week_start(today())
    while current_ws(game) < now_ws:
        ws = current_ws(game)
        we = ws + timedelta(days=6)
        days = len(active_days(game, ws))
        if days >= STREAK_ACTIVE_DAYS:
            game["streak_weeks"] += 1
            messages.append(f"{E['streak']} Last week ({fmt_date(ws)}): {days} active "
                            f"days. Streak extended to {game['streak_weeks']} "
                            f"week{'s' if game['streak_weeks'] != 1 else ''}!")
        else:
            if game["streak_weeks"] > 0:
                messages.append(f"💤 Last week ({fmt_date(ws)}): only {days} active "
                                f"day{'s' if days != 1 else ''}, so your streak "
                                f"reset. Your points and level are safe!")
            game["streak_weeks"] = 0
            game["comeback_pending"] = True
        # Clean Slate badge: a week with tasks due and nothing overdue at its end.
        had_tasks = any(ws <= to_date(t["due"]) <= we for t in tasks) or any(
            ws <= to_date(e["due"]) <= we for e in game["done_log"])
        overdue = [t for t in tasks
                   if not t["done"] and to_date(t["due"]) <= we]
        if had_tasks and not overdue:
            award_badge(game, "clean_slate")
        # Start the next week with fresh weekly settings.
        game["week_start"] = (ws + timedelta(days=7)).isoformat()
        game["fifth_paid"] = False
        game["quest_target"] = 0
        game["quest_awarded"] = False
        game["yarn_spent"] = 0.0
    refresh_quest(game, tasks)
    return messages


def sync_fifth_day(game):
    """Pay (or take back) the +25 bonus based on this week's active days."""
    n = len(active_days(game, current_ws(game)))
    if n >= 5 and not game["fifth_paid"]:
        game["fifth_paid"] = True
        game["stats"]["fifth_ever"] = True
        game["vault"] += FIFTH_DAY_BONUS
        game["lifetime"] += FIFTH_DAY_BONUS
        print(f"\n{E['points']} 5th active day this week! +{FIFTH_DAY_BONUS} bonus points!")
    elif n < 5 and game["fifth_paid"]:
        game["fifth_paid"] = False
        game["vault"] -= FIFTH_DAY_BONUS
        game["lifetime"] = max(0, game["lifetime"] - FIFTH_DAY_BONUS)
        print(f"\n↩️  Fewer than 5 active days now, so the "
              f"{FIFTH_DAY_BONUS}-point 5th-day bonus was taken back.")


def sync_quest(game):
    """Award the weekly quest chest (or take back an unopened one)."""
    target = game["quest_target"]
    progress = quest_progress(game)
    if target > 0 and progress >= target and not game["quest_awarded"]:
        game["quest_awarded"] = True
        game["chests"].append("quest")
        print(f"\n{E['quest']} WEEKLY QUEST COMPLETE ({progress}/{target})! "
              f"{E['chest']} You earned a mystery chest!")
    elif game["quest_awarded"] and progress < target and "quest" in game["chests"]:
        game["chests"].remove("quest")
        game["quest_awarded"] = False
        print(f"\n↩️  Weekly quest is below its target again, so the unopened "
              f"quest chest was taken back.")


# ----------------------------------------------------------------------
# DISPLAY
# ----------------------------------------------------------------------
def show_stats(game, tasks):
    level = game["level"]
    name, emoji = level_info(level)
    print("\n" + "=" * 60)
    print(f"{E['level']} Level {level}: {emoji} {name}")
    if level < len(LEVELS):
        nxt = LEVELS[level][0]
        prev = LEVELS[level - 1][0]
        span = nxt - prev
        done = min(10, max(0, int(10 * (game["lifetime"] - prev) / span)))
        print(f"   {bar(done, 10)}  {game['lifetime']}/{nxt} lifetime points "
              f"to Level {level + 1}")
    else:
        print(f"   Max level reached! {game['lifetime']} lifetime points")
    print(f"{E['points']} Vault: {game['vault']} points to spend")
    if game["vault"] < 0:
        print("   (Your vault is negative because points were taken back. "
              "Earn it back before buying rewards.)")

    pct = int(streak_bonus_pct(game["streak_weeks"]) * 100)
    bonus_text = f", +{pct}% task bonus" if pct else ""
    print(f"{E['streak']} Streak: {game['streak_weeks']} week"
          f"{'s' if game['streak_weeks'] != 1 else ''}{bonus_text}")
    n = len(active_days(game, current_ws(game)))
    slots = E["streak"] * min(n, STREAK_ACTIVE_DAYS) + \
        E["todo"] * max(0, STREAK_ACTIVE_DAYS - n)
    slots += " ⭐" if n >= 5 else " ⬜"
    print(f"   This week: {slots}  {n} active day{'s' if n != 1 else ''} "
          f"(need {STREAK_ACTIVE_DAYS} to keep the streak, 5th day = "
          f"+{FIFTH_DAY_BONUS})")

    target = game["quest_target"]
    if target > 0:
        prog = quest_progress(game)
        print(f"{E['quest']} Weekly quest: {bar(prog, target)}  {min(prog, target)}/{target} "
              f"tasks due this week{'  ✅' if game['quest_awarded'] else ''}")
    else:
        print(f"{E['quest']} Weekly quest: needs {QUEST_MIN_DUE}+ tasks due this week")

    overdue = [t for t in tasks if not t["done"] and to_date(t["due"]) < today()]
    extras = []
    if game["chests"]:
        extras.append(f"{E['chest']} {len(game['chests'])} unopened chest"
                      f"{'es' if len(game['chests']) != 1 else ''}")
    if game["inventory"]:
        extras.append(f"🧺 {len(game['inventory'])} reward"
                      f"{'s' if len(game['inventory']) != 1 else ''} ready to use")
    if overdue:
        extras.append(f"{E['overdue']} {len(overdue)} overdue")
    if extras:
        print("   " + "   ".join(extras))
    print("=" * 60)


def show_tasks(tasks):
    print("\n" + "=" * 60)
    print("📋 YOUR TASKS")
    print("=" * 60)
    if not tasks:
        print("No tasks yet. Add one from the menu!")
        return
    t0 = today()
    this_ws = week_start(t0)
    weeks = {}
    for t in tasks:
        weeks.setdefault(week_start(to_date(t["due"])), []).append(t)
    for ws in sorted(weeks):
        if ws == this_ws:
            tag = "  ⬅ this week"
        elif ws < this_ws:
            tag = "  (past)"
        else:
            tag = ""
        print(f"\n📆 {fmt_date(ws)} - {fmt_date(ws + timedelta(days=6))}{tag}")
        for t in sorted(weeks[ws], key=lambda x: (x["due"], x["id"])):
            due = to_date(t["due"])
            if t["done"]:
                icon = E["done"]
            elif due < t0:
                icon = E["overdue"]
            elif due == t0:
                icon = E["today"]
            else:
                icon = E["todo"]
            size = SIZES[t["size"]]
            line = (f"  [{t['id']:>2}] {icon} {size['emoji']} {size['label']:<6} "
                    f"{t['title']}  - due {fmt_date(due)}")
            if t["done"]:
                line += f"  (+{t['points_earned']} pts)"
            print(line)
    done = len([t for t in tasks if t["done"]])
    print(f"\n{E['done']} {done} of {len(tasks)} tasks complete")
    print("Key: ⬜ to-do  ✅ done  ⚠️ overdue  📅 due today")


def show_badges(game):
    print("\n🏅 BADGES")
    for key, (emoji, name, desc) in BADGES.items():
        if key in game["badges"]:
            print(f"  {emoji} {name:<14} - {desc} (earned {game['badges'][key]})")
        else:
            print(f"  ❓ {'???':<14} - {desc}")
    if game["claimed"]:
        print("\n🧾 RECENTLY USED REWARDS")
        for item in game["claimed"][-5:]:
            extra = f" (${item['spent']:.2f} on yarn)" if item.get("spent") else ""
            print(f"  {item['date']}: {item['name']}{extra}")


# ----------------------------------------------------------------------
# TASK ACTIONS
# ----------------------------------------------------------------------
def pick_task(candidates, prompt):
    """Show a list of tasks and return the one the player picks (or None)."""
    if not candidates:
        return None
    print()
    for t in sorted(candidates, key=lambda x: (x["due"], x["id"])):
        size = SIZES[t["size"]]
        print(f"  [{t['id']:>2}] {size['emoji']} {t['title']}  - due "
              f"{fmt_date(to_date(t['due']))}")
    while True:
        choice = ask(f"\n{prompt} (task number, or Enter to cancel): ")
        if choice == "":
            return None
        if choice.isdigit():
            for t in candidates:
                if t["id"] == int(choice):
                    return t
        print("That's not one of the numbers above. Try again.")


def add_task(tasks, game):
    title = ask("\nTask name (Enter to cancel): ")
    if not title:
        return
    print("\nHow big is this task?")
    for i, key in enumerate(SIZE_KEYS, start=1):
        s = SIZES[key]
        print(f"  {i}. {s['emoji']} {s['label']:<6} {s['points']:>3} pts  - {s['effort']}")
    while True:
        choice = ask("Pick 1-4 (Enter to cancel): ")
        if choice == "":
            return
        if choice in ("1", "2", "3", "4"):
            size = SIZE_KEYS[int(choice) - 1]
            break
        print("Please enter 1, 2, 3, or 4.")
    if size == "boss":
        sure = ask("Boss tasks are for weeks of work or a big milestone "
                   "(like a whole course). Still a Boss? (y/n): ").lower()
        if sure != "y":
            print("No problem. Try again and pick a different size.")
            return
    while True:
        text = ask("Due date (YYYY-MM-DD or MM/DD/YYYY): ")
        due = parse_date(text)
        if due:
            break
        print("I couldn't read that date. Example: 2026-12-04")
    if due < today():
        print(f"{E['overdue']} That date is in the past, so this task starts out overdue.")
    task = {
        "id": game["next_id"], "title": title, "size": size,
        "due": due.isoformat(), "done": False,
        "added_on": today().isoformat(), "completed_on": None,
        "completed_at": None, "points_earned": 0, "chest_awarded": False,
    }
    game["next_id"] += 1
    tasks.append(task)
    refresh_quest(game, tasks)
    print(f"\n{E['done']} Added: {SIZES[size]['emoji']} {title} "
          f"(worth {SIZES[size]['points']} base points, due {fmt_date(due)})")


def check_off(tasks, game):
    open_tasks = [t for t in tasks if not t["done"]]
    if not open_tasks:
        print("\nNothing to check off. Add a task first!")
        return
    task = pick_task(open_tasks, "Which task did you finish?")
    if task is None:
        return

    is_boss = task["size"] == "boss"
    base = SIZES[task["size"]]["points"]
    days_early = (to_date(task["due"]) - today()).days

    # Step 1: timing (Boss tasks are exempt)
    if is_boss:
        factor, timing_note = 1.0, "Boss task (no timing adjustment)"
    else:
        factor, timing_note = timing_factor(days_early)
    adjusted = base * factor

    # Step 2: critical hit (random!)
    crit = random.randint(1, CRIT_CHANCE) == 1
    multiplier = 2 if crit else 1

    # Step 3: streak bonus (Boss tasks are exempt, and it is never doubled)
    pct = 0.0 if is_boss else streak_bonus_pct(game["streak_weeks"])
    streak_bonus = adjusted * pct

    total = round_points(adjusted * multiplier + streak_bonus)

    # Remember how many active days there were before this check-off.
    ws = current_ws(game)
    before_days = len(active_days(game, ws))

    # Update the task and the game.
    now_text = time.strftime("%Y-%m-%d %H:%M")
    task["done"] = True
    task["completed_on"] = today().isoformat()
    task["completed_at"] = now_text
    task["points_earned"] = total
    game["vault"] += total
    game["lifetime"] += total
    game["done_log"].append({
        "id": task["id"], "date": today().isoformat(), "due": task["due"],
        "size": task["size"], "on_time": days_early >= 0, "hour": current_hour(),
    })

    print(f"\n{E['done']} Completed: {task['title']}")
    print(f"   Base {base} pts ({SIZES[task['size']]['label']}) - {timing_note}")
    if crit:
        pause(0.4)
        print(f"   {E['crit']} CRITICAL HIT! Points doubled!")
        game["stats"]["crits"] += 1
    if streak_bonus > 0:
        print(f"   {E['streak']} Streak bonus: +{int(pct * 100)}%")
    print(f"   {E['points']} You earned {total} points!  Vault: {game['vault']}")
    print(f"   {random.choice(ENCOURAGEMENT)}")

    # Streak progress
    after_days = len(active_days(game, ws))
    if before_days < STREAK_ACTIVE_DAYS <= after_days:
        print(f"\n{E['party']} Streak secured for the week! "
              f"({STREAK_ACTIVE_DAYS} active days)")
    elif after_days > before_days and after_days < STREAK_ACTIVE_DAYS:
        print(f"\n{E['streak']} Active day {after_days} of {STREAK_ACTIVE_DAYS} this week.")
    sync_fifth_day(game)

    # Comeback Kid badge
    if game["comeback_pending"]:
        game["comeback_pending"] = False
        award_badge(game, "comeback_kid")

    # Boss chest and weekly quest chest
    if is_boss:
        task["chest_awarded"] = True
        game["chests"].append("boss")
        print(f"\n👑 BOSS DEFEATED! {E['chest']} You earned a mystery chest!")
    sync_quest(game)

    update_level(game)
    check_badges(game)


def uncheck(tasks, game):
    done_tasks = [t for t in tasks if t["done"]]
    if not done_tasks:
        print("\nNo completed tasks to uncheck.")
        return
    task = pick_task(done_tasks, "Which task should be unchecked?")
    if task is None:
        return
    points = task["points_earned"]
    game["vault"] -= points
    game["lifetime"] = max(0, game["lifetime"] - points)
    game["done_log"] = [e for e in game["done_log"] if e["id"] != task["id"]]
    if task.get("chest_awarded") and "boss" in game["chests"]:
        game["chests"].remove("boss")
        print("↩️  The unopened Boss chest was taken back.")
    task["chest_awarded"] = False
    task["done"] = False
    task["completed_on"] = None
    task["completed_at"] = None
    task["points_earned"] = 0
    print(f"\n↩️  Unchecked: {task['title']}  (-{points} points)  Vault: {game['vault']}")
    sync_fifth_day(game)
    sync_quest(game)


def remove_task(tasks, game):
    if not tasks:
        print("\nNo tasks to remove.")
        return
    task = pick_task(tasks, "Which task should be removed?")
    if task is None:
        return
    if ask(f"Remove '{task['title']}'? (y/n): ").lower() != "y":
        print("Okay, it stays on your list.")
        return
    tasks.remove(task)
    print(f"\n🗑️  Removed: {task['title']}  (removing never earns points)")


# ----------------------------------------------------------------------
# REWARDS (shop, inventory, chests)
# ----------------------------------------------------------------------
def reward_shop(game):
    while True:
        print("\n🛍️  REWARD SHOP" + f"   {E['points']} Vault: {game['vault']} points"
              f"   Level {game['level']}")
        options = []
        for tier_key in TIER_KEYS:
            tier = TIERS[tier_key]
            locked = game["level"] < tier["min_level"]
            lock_note = f"  {E['lock']} unlocks at Level {tier['min_level']}" if locked else ""
            print(f"\n{tier['emoji']} {tier['name']} - {tier['cost']} points{lock_note}")
            for reward in tier["rewards"]:
                options.append((tier_key, reward, locked))
                print(f"   {len(options)}. {reward}")
        choice = ask("\nBuy which reward? (number, or Enter to leave): ")
        if choice == "":
            return
        if not (choice.isdigit() and 1 <= int(choice) <= len(options)):
            print("That's not one of the numbers above.")
            continue
        tier_key, reward, locked = options[int(choice) - 1]
        tier = TIERS[tier_key]
        if locked:
            print(f"{E['lock']} {tier['name']} unlocks at Level {tier['min_level']}.")
        elif game["vault"] < tier["cost"]:
            print(f"Not enough points yet: you need {tier['cost']} and have {game['vault']}.")
        else:
            game["vault"] -= tier["cost"]
            game["inventory"].append({"name": reward, "tier": tier_key,
                                      "source": "shop",
                                      "earned": today().isoformat()})
            print(f"\n{tier['emoji']} Bought: {reward}!  Vault: {game['vault']}")
            print("   It's in your inventory. Use it from the menu when you're ready.")
            return


def use_reward(game):
    if not game["inventory"]:
        print("\nYour inventory is empty. Buy rewards in the shop or win them in chests!")
        return
    print("\n🧺 YOUR REWARDS")
    for i, item in enumerate(game["inventory"], start=1):
        tier = TIERS[item["tier"]]
        print(f"  {i}. {tier['emoji']} {item['name']}  (from the {item['source']})")
    choice = ask("\nUse which reward? (number, or Enter to cancel): ")
    if not (choice.isdigit() and 1 <= int(choice) <= len(game["inventory"])):
        return
    item = game["inventory"][int(choice) - 1]
    spent = None
    if "yarn" in item["name"].lower():
        remaining = YARN_WEEKLY_CAP - game["yarn_spent"]
        if remaining <= 0:
            print(f"\n🧶 You've reached the ${YARN_WEEKLY_CAP:.0f} yarn limit for this "
                  f"week. Try again next week (Sunday).")
            return
        print(f"\n🧶 Yarn budget left this week: ${remaining:.2f}")
        while True:
            text = ask("How much did you spend? (Enter to cancel): ").replace("$", "")
            if text == "":
                return
            try:
                spent = round(float(text), 2)
            except ValueError:
                print("Please enter a dollar amount, like 12.50")
                continue
            if spent <= 0:
                print("Please enter an amount above $0.")
            elif spent > remaining:
                print(f"That's over your remaining ${remaining:.2f} for the week.")
            else:
                break
        game["yarn_spent"] = round(game["yarn_spent"] + spent, 2)
    game["inventory"].remove(item)
    game["claimed"].append({"name": item["name"], "tier": item["tier"],
                            "date": time.strftime("%Y-%m-%d %H:%M"),
                            "spent": spent})
    print(f"\n{E['party']} Enjoy: {item['name']}! Logged on {time.strftime('%Y-%m-%d')}.")


def chest_odds(level, boss):
    """Drop weights for [bronze, silver, gold, platinum] at a given level."""
    if level >= 7:
        weights = [50, 30, 15, 5]
    elif level == 6:
        weights = [55, 30, 12, 3]
    elif level >= 4:
        weights = [60, 28, 10, 2]
    else:
        weights = [65, 25, 8, 2]
    if boss:                      # Boss chests never drop Bronze
        weights = [0, weights[1] + weights[0], weights[2], weights[3]]
    return weights


def open_chest(game):
    if not game["chests"]:
        print("\nNo chests to open. Defeat a Boss task or finish a weekly quest!")
        return
    index = 0
    if len(game["chests"]) > 1:
        print("\nYou have several chests:")
        for i, kind in enumerate(game["chests"], start=1):
            label = "Boss chest" if kind == "boss" else "Weekly quest chest"
            print(f"  {i}. {E['chest']} {label}")
        choice = ask("Open which one? (number, or Enter to cancel): ")
        if not (choice.isdigit() and 1 <= int(choice) <= len(game["chests"])):
            return
        index = int(choice) - 1
    kind = game["chests"].pop(index)
    boss = kind == "boss"
    weights = chest_odds(game["level"], boss)

    print(f"\n{E['chest']} Opening a {'Boss' if boss else 'weekly quest'} chest! "
          f"Today's odds (Level {game['level']}):")
    for key, w in zip(TIER_KEYS, weights):
        print(f"   {TIERS[key]['emoji']} {TIERS[key]['name']:<9} {w}%")
    if game["pity"] >= PITY_LIMIT:
        print(f"   {E['spark']} Lucky streak protection: this chest is a guaranteed Gold or better!")
    pause()
    print(f"\n{E['chest']} Opening chest...")
    pause()
    print("...")
    pause()
    print(E["spark"])
    pause()

    if game["pity"] >= PITY_LIMIT:
        tier_key = "gold"
    else:
        tier_key = random.choices(TIER_KEYS, weights=weights)[0]
    reward = random.choice(TIERS[tier_key]["rewards"])
    tier = TIERS[tier_key]
    if tier_key in ("gold", "platinum"):
        game["pity"] = 0
    else:
        game["pity"] += 1
    game["stats"]["chests_opened"] += 1
    game["inventory"].append({"name": reward, "tier": tier_key, "source": "chest",
                              "earned": today().isoformat()})
    print(f"{tier['emoji']} You got: {reward}  ({tier['name']})!")
    print("   It's in your inventory.")
    check_badges(game)


# ----------------------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------------------
MENU = """
==================== MAIN MENU ====================
  1. Add a task
  2. View tasks
  3. Check off a task
  4. Uncheck a task
  5. Remove a task
  6. Reward shop
  7. Use a reward
  8. Open a mystery chest
  9. Stats and badges
  0. Save and quit
==================================================="""


def main():
    game = load_game()
    tasks = load_tasks(game)
    messages = roll_week(game, tasks)
    save_all(tasks, game)

    print("\n🧶 Welcome to your Gamified To-Do List! 🧶")
    for m in messages:
        print(m)
    show_stats(game, tasks)

    while True:
        print(MENU)
        try:
            choice = ask("Choose an option: ")
        except (EOFError, KeyboardInterrupt):
            print()
            choice = "0"

        if choice == "1":
            add_task(tasks, game)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            check_off(tasks, game)
        elif choice == "4":
            uncheck(tasks, game)
        elif choice == "5":
            remove_task(tasks, game)
        elif choice == "6":
            reward_shop(game)
        elif choice == "7":
            use_reward(game)
        elif choice == "8":
            open_chest(game)
        elif choice == "9":
            show_stats(game, tasks)
            show_badges(game)
        elif choice == "0":
            break
        else:
            print("Please choose a number from the menu.")
            continue
        save_all(tasks, game)

    save_all(tasks, game)
    print("\n" + "=" * 60)
    print("📋 FINAL TO-DO LIST")
    show_tasks(tasks)
    show_stats(game, tasks)
    print("\nYour progress is saved. See you next time! 🧶")


if __name__ == "__main__":
    main()