-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Open database
sqlite3 fiftyville.db

-- Get informations stored in database
.tables

/*
airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers
*/

-- Search for description of crime scene
.schema crime_scene_reports
SELECT description FROM crime_scene_reports WHERE year = 2025 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Search for interviews (all witnesses mentions the bakery in their transcript.)
.schema interviews
SELECT name, transcript FROM interviews WHERE year = 2025 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- Check bakery_security_logs
.schema bakery_security_logs
SELECT * FROM bakery_security_logs WHERE year = 2025 AND month = 7 AND day = 28 AND hour = 10;

/*
SUSPECT license_plate
| 5P2BI95       |
| 94KL13X       |
| 6P58WS2       |
| 4328GD8       |
| G412CB7       |
| L93JTIZ       |
| 322W7JE       |
| 0NTHK55       |
*/

-- Associate license_plate with name
.schema people
SELECT p.name, b.license_plate FROM bakery_security_logs b JOIN people p ON b.license_plate = p.license_plate
WHERE b.year = 2025 AND b.month = 7 AND b.day = 28 AND b.minute >= 16 AND b.minute <= 23 AND b.activity = 'exit';

/*
SUSPECT LIST (ASSOCIATED WITH SUSPECT license_plate)
| Vanessa | 5P2BI95       |
| Bruce   | 94KL13X       |
| Barry   | 6P58WS2       |
| Luca    | 4328GD8       |
| Sofia   | G412CB7       |
| Iman    | L93JTIZ       |
| Diana   | 322W7JE       |
| Kelsey  | 0NTHK55       |
| Ethan   | NAW9653       |
| Vincent | 94MV71O       |
| Jeremy  | V47T75I       |
| Brandon | R3G7486       |
*/

-- The thief called someone shortly after the heist
.schema phone_calls
SELECT caller_p.name AS caller, receiver_p.name AS receiver, c.duration
FROM phone_calls c JOIN people caller_p ON c.caller = caller_p.phone_number JOIN people receiver_p ON c.receiver = receiver_p.phone_number
WHERE c.year = 2025 AND c.month = 7 AND c.day = 28 AND c.duration < 60;

/*
SUSPECT LIST UPDATE
| Sofia   | Jack       |
| Kelsey  | Larry      |
| Bruce   | Robin      |
| Kelsey  | Melissa    |
| Diana   | Philip     |
*/

-- Then the thief and their complice took the earliest flight out of fiftyville the day after the heist
.schema airports
SELECT id FROM airports WHERE city = 'Fiftyville'; -- Return id = 8

.schema flights
SELECT id, destination_airport_id, hour, minute FROM flights
WHERE origin_airport_id = 8 AND year = 2025 AND month = 7 AND day = 29
ORDER BY hour, minute LIMIT 1; -- Return id = 36 and destination_airport_id = 4

-- Check passengers of flight id = 36
.schema passengers
SELECT p.name FROM passengers pa JOIN people p ON pa.passport_number = p.passport_number
WHERE pa.flight_id = 36;

/*
PASSENGERS OF FLIGHT ID = 36
| Doris  |
| Sofia  |
| Bruce  |
| Edward |
| Kelsey |
| Taylor |
| Kenny  |
| Luca   |
*/

/*
SUSPECT LIST UPDATE
| Bruce   | Robin      |
*/

-- QUERY : Check destination
SELECT a.city FROM airports a JOIN flights f ON f.destination_airport_id = a.id
WHERE f.destination_airport_id = 4 and f.id = 36;

/*
CITY
| New York City |
*/

-- Conclusion
-- The thief is Bruce, his complice is Robin and they went to New York City
