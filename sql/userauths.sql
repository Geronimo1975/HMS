-- Active: 1738662164036@@127.0.0.1@5432@hms_db
-- Create users (both doctors and patients)
INSERT INTO userauths_user (id, password, is_superuser, email, username, first_name, last_name, is_staff, is_active, date_joined, user_type)
VALUES
-- Admin user
(1, '!hashed_password_placeholder!', 1, 'admin@hms.com', 'admin', 'System', 'Admin', 1, 1, '2024-02-01 10:00:00', NULL),

-- Doctor users (IDs 2-11)
(2, '!hashed_password_placeholder!', 0, 'doctor1@hms.com', 'doctor1', 'James', 'Wilson', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(3, '!hashed_password_placeholder!', 0, 'doctor2@hms.com', 'doctor2', 'Sarah', 'Johnson', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(4, '!hashed_password_placeholder!', 0, 'doctor3@hms.com', 'doctor3', 'Michael', 'Brown', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(5, '!hashed_password_placeholder!', 0, 'doctor4@hms.com', 'doctor4', 'Emily', 'Davis', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(6, '!hashed_password_placeholder!', 0, 'doctor5@hms.com', 'doctor5', 'David', 'Miller', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(7, '!hashed_password_placeholder!', 0, 'doctor6@hms.com', 'doctor6', 'Linda', 'Wilson', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(8, '!hashed_password_placeholder!', 0, 'doctor7@hms.com', 'doctor7', 'Robert', 'Taylor', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(9, '!hashed_password_placeholder!', 0, 'doctor8@hms.com', 'doctor8', 'Jennifer', 'Anderson', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(10, '!hashed_password_placeholder!', 0, 'doctor9@hms.com', 'doctor9', 'William', 'Thomas', 0, 1, '2024-02-01 10:00:00', 'Doctor'),
(11, '!hashed_password_placeholder!', 0, 'doctor10@hms.com', 'doctor10', 'Elizabeth', 'Jackson', 0, 1, '2024-02-01 10:00:00', 'Doctor'),

-- Patient users (IDs 12-21)
(12, '!hashed_password_placeholder!', 0, 'patient1@example.com', 'patient1', 'John', 'Doe', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(13, '!hashed_password_placeholder!', 0, 'patient2@example.com', 'patient2', 'Jane', 'Smith', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(14, '!hashed_password_placeholder!', 0, 'patient3@example.com', 'patient3', 'Robert', 'Johnson', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(15, '!hashed_password_placeholder!', 0, 'patient4@example.com', 'patient4', 'Maria', 'Garcia', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(16, '!hashed_password_placeholder!', 0, 'patient5@example.com', 'patient5', 'James', 'Brown', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(17, '!hashed_password_placeholder!', 0, 'patient6@example.com', 'patient6', 'Patricia', 'Miller', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(18, '!hashed_password_placeholder!', 0, 'patient7@example.com', 'patient7', 'Michael', 'Davis', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(19, '!hashed_password_placeholder!', 0, 'patient8@example.com', 'patient8', 'Linda', 'Wilson', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(20, '!hashed_password_placeholder!', 0, 'patient9@example.com', 'patient9', 'David', 'Martinez', 0, 1, '2024-02-01 10:00:00', 'Patient'),
(21, '!hashed_password_placeholder!', 0, 'patient10@example.com', 'patient10', 'Elizabeth', 'Anderson', 0, 1, '2024-02-01 10:00:00', 'Patient');
