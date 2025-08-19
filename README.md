# NYRailSyncDB: Centralized Database for Modern Railway Management - CSE-560-Data-Management-And-Query-Language

The project seeks to establish a centralised relational database for the New York Railway System. Constructed using SQL in Postgres, this database manages all data related to the railway system. It has been designed to resolve issues faced by the previous manual system. The database continually links the railway system to multiple destinations. The objective is to enhance scheduling, maintenance, and asset management while adhering to regulatory standards and safety protocols.


# Tech Stack Used - Python, PostgreSQL, CockroachDB, Docker Compose, PowerBI

### Features -

- Normalisation - It is done to remove the redundant elements
- Data Ingestion - It is done to further connect the incoming and outgoing data flowing from and to the multiple sources.
- Centralisation, Automated Data handling, Vertical Scalable - It is done using PostgreSQL
- Decentralisation, Horizontal Scalable - It is done using CockroachDB, as all the queries of the project of PostgreSQL 4.0 are compatible with CockroachDB. 

#### The stored data is visualized further on PowerBI to gather insights and analysis for future works using the - <a href="https://app.powerbi.com/signin#code=1.AUYAikpGlu34sUCZ4l9rUKICUA8BHIdhXrFPg6yYYQp-kRDxALxGAA.AgABBAIAAABVrSpeuWamRam2jAF1XRQEAwDs_wUA9P_gKXniUA5nTTL3JoqxKAZ6dP18T8nuLDyJynDobU-k5QIKD868aSmySEBQjwyucnB0Yw675dG_emxEHUPTCOe2Fbgb2IpFXxKafjoSt_vYKkII6T4m-IWarULKbnBvumkPRaNdPxjh2GZx9R2jhmAE49b4iDZbskCpIbWSYDSPJHkyNvYetatd68kWxp9h4d28ZoqmoRR-lE9x5_E-I7__S4JdfN3PmQUDKM1rKgbNGWeiB91EIZq0VoDYOaI6q3TiSVgugFFqe9i-UpPczpgwYm7dU8XadePqb57AWvfFFYZkUvbaIVKbQH8wjOih_eI8f_XNy7-DF71BpTHZhw8cMCfzdFW7HRxaCm_yk7Th9M4tPP-GS5-aIGkOhdUS799FXZWOewr5S0z0uiC6RadDCDghqvkjeRcUu4_LcWUIfgx2Xv0tKCSWQ4YYUN2ydEynduwMpknSmUS74bDJVDYJe-9ThbEVg5wqNSGi9OlLGGHDpk7hBLHJkoQHzxmxztRwJPFdLi0rM_Pwk1OTJK3N2-5AqCOBO801rEPqcFShpM4Lq1MVkuy91PsezW9Hyy-UqVwzrbZa1Qh75cM76I2tEFL8giBCbqXGlhhAvZE_9I7t4HAG32V5QZmuM6bf2nLHnEIU0ewKhvj8BYjKIKE8y1IdlpsJjpfBXFPRzov8h_zKLQMEybkaZwzO1fCDc4FU4Nk02Wo-FyCGmdXX3NgWZF-ksFHQ0grjV9jV7dz9JguhYT1AH_l1gXmIskm0fSQziaKe5-k5w9vUJdt2y_cwYp483kXqkt-feSOYLe0gZfTGtqhmUZuzPmhuTn0WkrOwyosyeWUVAICvqLFn99fkExvPnN6zea3pamO1Z6jZzxqA7vTCXxzWo8H5Vygd2Jomkuccoj5q0NDj2XpxWngmDa3t&client_info=eyJ1aWQiOiIxYTZmMmZlNi1iMmMwLTRmZDItODExMS1lNzA2YTM2MmFlZTgiLCJ1dGlkIjoiOTY0NjRhOGEtZjhlZC00MGIxLTk5ZTItNWY2YjUwYTIwMjUwIn0&state=eyJpZCI6IjQ4NDIyZGFkLWQyYmYtNDdkNS1iM2I5LWU5MjhmM2M2MGRkNiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3d%7c1736447405021.5999%3b1736447405022.3%3b1736447404290.2&session_state=ad8489a0-1587-44c3-bfaf-93b024944a74&correlation_id=9529244a-d075-41d4-8aee-1b2ff7646013" target="_blank">link<href/>



## Steps to start Docker Compose and CockroachDB for decentralisation

```bash
docker compose up -d cockroach crdb-init
```

```
docker compose up --build loader
```
```bash
docker compose exec cockroach cockroach sql --insecure
```
```bash
SHOW DATABASES;
USE nyrailsyncdb;
```
