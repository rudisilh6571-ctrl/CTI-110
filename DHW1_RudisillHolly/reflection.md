# Holly Rudisill
# 11/10/2026
# DHW1
# create a table and user database using sql in python. 


# DHW2 – Query Analysis Questions

After you run `run_queries.py`, review your output and answer the questions below in complete sentences.

> **Important:** Your exact answers will be different from your classmates because each student may enter different fake user data.  
> Focus on explaining what your own query results show.

## 1) All Users (`SELECT * FROM users`)
How many total rows (users) are displayed in your output?  
Does this match the number of users you intended to insert?

# ANSWER: 10 and yes it does match what was intended

## 2) Name + Email (`SELECT first_name, last_name, email FROM users`)
What information is shown in this query that is different from Query #1?  

# ANSWER: Just the firstnames, lastnames, and email addresses

## 3) Users from USA (`WHERE country = 'USA'`)
How many users from the USA appear in your results?

# ANSWER: 3

## 4) Total User Count (`COUNT(*)`)
What value did your `total_users` query return?  
How can this query help you check whether your data was inserted correctly?

# ANSWER: the number of total unique user in the database probably identified by user_id.  If the answer comes back something you werent expecting that might tell you your value are not set correctly or some data in the table is missing. 

## 5) 3 Most Recent Signups (`ORDER BY signup_date DESC LIMIT 3`)
Which 3 usernames appear as the most recent in **your** output?  

# ANSWER:   cable_knit_life', '2024-10-30, heather_yarns', '2024-09-19, bobbin_along', '2024-08-14

---

> What should be in your zipped folder when you turn it in to Canvas -> create_signup_db.py, run_queries.py, signup_he.db, and reflection.md