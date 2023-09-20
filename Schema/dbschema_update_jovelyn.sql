CREATE DATABASE IF NOT EXISTS ChatGPTSEPA_DB;
USE ChatGPTSEPA_DB;
CREATE TABLE IF NOT EXISTS Request
(
    Prompt_ID INT NOT NULL AUTO_INCREMENT,
    Created DATETIME NOT NULL,
    Model VARCHAR(255) NOT NULL,
    Message_System_Role ENUM('System', 'User', 'Assistant') NOT NULL,
    Message_Content TEXT NOT NULL,
    Max_Tokens INT NOT NULL,
    Temperature FLOAT NOT NULL,
    Top_Probability FLOAT NOT NULL,
    Frequency_penalty FLOAT NOT NULL,
    Presence_penalty FLOAT NOT NULL,
    Stop TEXT,
    -- Api_request_count INT NOT NULL

    PRIMARY KEY (Prompt_ID)
);a

CREATE TABLE IF NOT EXISTS Response
(
    Response_ID INT NOT NULL AUTO_INCREMENT,
    Prompt_ID INT NOT NULL,
    ID VARCHAR(255) NOT NULL,
    Response TEXT NOT NULL,
    Created DATETIME NOT NULL,
    Prompt_tokens INT NOT NULL,
    Completion_tokens INT NOT NULL,
    Total_tokens INT NOT NULL,
    
    UNIQUE (Prompt_ID, ID),
    PRIMARY KEY (Response_ID),
    FOREIGN KEY (Prompt_ID) REFERENCES Request (Prompt_ID)
);

CREATE TABLE IF NOT EXISTS Analytics_Performance
(
    Analytics_ID INT NOT NULL AUTO_INCREMENT,
    Prompt_ID INT NOT NULL,
    Response_ID INT NOT NULL,
    Response_time VARCHAR(255) NOT NULL,
    
    PRIMARY KEY (Analytics_ID),
    FOREIGN KEY (Prompt_ID) REFERENCES Request (Prompt_ID),
    FOREIGN KEY (Response_ID) REFERENCES Response (Response_ID)
);

CREATE TABLE IF NOT EXISTS API_Request_Count
(
    Count_ID INT NOT NULL AUTO_INCREMENT,
    Api_request_count INT NOT NULL,

    PRIMARY KEY (Count_ID)
);

-- CREATE TABLE IF NOT EXISTS History
-- (
--     Conversation_ID INT NOT NULL AUTO_INCREMENT,
--     Message_Content  TEXT NOT NULL,
--     Response TEXT NOT NULL,
--     Prompt_ID INT NOT NULL AUTO_INCREMENT,
--     Response_ID INT NOT NULL AUTO_INCREMENT,

--     PRIMARY KEY (Conversation_ID),
--     FOREIGN KEY (Prompt_ID) REFERENCES Request (Prompt_ID),
--     FOREIGN KEY (Response_ID) REFERENCES Response (Response_ID)
-- );

--CREATE TABLE IF NOT EXISTS Metamorphic_Testing_Questions
--(
--    Question_ID INT NOT NULL AUTO_INCREMENT,
--    Question_Content TEXT NOT NULL,
--    PRIMARY KEY (Question_ID)
--);
--
--CREATE TABLE IF NOT EXISTS Metamorphic_Testing_Similar_Questions
--(
--    Similar_ID INT NOT NULL AUTO_INCREMENT,
--    Question_ID1 INT NOT NULL,
--    Question_ID2 INT NOT NULL,
--    Similarity FLOAT NOT NULL,
--
--    PRIMARY KEY (Similar_ID),
--    FOREIGN KEY (Question_ID1) REFERENCES Metamorphic_Testing_Questions (Question_ID),
--    FOREIGN KEY (Question_ID2) REFERENCES Metamorphic_Testing_Questions (Question_ID)
--);