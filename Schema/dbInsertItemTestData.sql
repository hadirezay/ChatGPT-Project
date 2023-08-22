INSERT INTO Questions (Question, Model_version, parameter)
VALUES
    ('What is the capital of France?', 'v1.0', 'geo'),
    ('Who wrote Romeo and Juliet?', 'v1.0', 'lit'),
    ('What is the square root of 25?', 'v1.0', 'math');

INSERT INTO Answers (Question_ID, Answer, Grading, Comments)
VALUES
    (1, 'The capital of France is Paris.', 10, NULL),
    (2, 'Romeo and Juliet was written by William Shakespeare.', 9, 'Great answer, but could be more detailed.'),
    (3, 'The square root of 25 is 5.', 8, 'Correct, but remember to mention both positive and negative roots.');

INSERT INTO History (Question_ID, Answer_ID, Question, Answer, Grading, Comments, Model_version, parameter, time_stamp)
VALUES
    (1, 1, 'What is the capital of France?', 'The capital of France is Paris.', 10, NULL, 'v1.0', 'geo', NOW()),
    (2, 2, 'Who wrote Romeo and Juliet?', 'Romeo and Juliet was written by William Shakespeare.', 9, 'Great answer, but could be more detailed.', 'v1.0', 'lit', NOW()),
    (3, 3, 'What is the square root of 25?', 'The square root of 25 is 5.', 8, 'Correct, but remember to mention both positive and negative roots.', 'v1.0', 'math', NOW());
