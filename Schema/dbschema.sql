CREATE DATABASE IF NOT EXISTS ChatGPTSEPA_DB;
USE ChatGPTSEPA_DB;
CREATE TABLE IF NOT EXISTS Questions
(
    Question_ID INT NOT NULL AUTO_INCREMENT,
    Question TEXT NOT NULL, 
    Model_version VARCHAR(255) NOT NULL,
    parameter VARCHAR(255) NOT NULL,

    PRIMARY KEY (Question_ID)
);

CREATE TABLE IF NOT EXISTS Answers
(
    Answer_ID INT NOT NULL AUTO_INCREMENT,
    Question_ID INT NOT NULL,
    Answer TEXT NOT NULL, 
    Grading INT NOT NULL,
    Comments TEXT,

    PRIMARY KEY (Answer_ID),
    FOREIGN KEY (Question_ID) REFERENCES Questions (Question_ID)
);

CREATE TABLE IF NOT EXISTS History
(
    Chat_ID INT NOT NULL AUTO_INCREMENT,
    Question_ID INT NOT NULL,
    Answer_ID INT NOT NULL, 
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL,
    Grading INT NOT NULL, 
    Comments TEXT,
    Model_version VARCHAR(255) NOT NULL,
    parameter VARCHAR(255) NOT NULL,
    time_stamp DATETIME,

    PRIMARY KEY (Chat_ID),
    FOREIGN KEY (Question_ID) REFERENCES Questions (Question_ID),
    FOREIGN KEY (Answer_ID) REFERENCES Answers (Answer_ID)
);
