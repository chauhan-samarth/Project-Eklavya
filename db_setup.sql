CREATE DATABASE project_eklavya_db;

USE project_eklavya_db;

CREATE TABLE faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);

CREATE TABLE user_profiles (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    preferences TEXT
);

CREATE TABLE conversation_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    bot_response TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    conversation_log_id INT,
    feedback TEXT,
    rating INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);



