-- Clear existing data
DELETE FROM base_billing;
DELETE FROM base_prescription;
DELETE FROM base_labtest;
DELETE FROM base_medicalrecord;
DELETE FROM base_appointment;
DELETE FROM base_service_available_doctors;
DELETE FROM base_service;
DELETE FROM patient_notification;
DELETE FROM doctor_notification;
DELETE FROM patient_patient;
DELETE FROM doctor_doctor;
DELETE FROM userauths_user;

-- Create Users
-- First create doctor users
INSERT INTO userauths_user (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, email, username, user_type) VALUES
(1, 'password=', NULL, false, 'John', 'Smith', false, true, '2024-02-28', 'doctor1@example.com', 'doctor1', 'Doctor'),
(2, 'password=', NULL, false, 'Sarah', 'Johnson', false, true, '2024-02-28', 'doctor2@example.com', 'doctor2', 'Doctor'),
(3, 'password=', NULL, false, 'Michael', 'Lee', false, true, '2024-02-28', 'doctor3@example.com', 'doctor3', 'Doctor'),
(4, 'password=', NULL, false, 'Emily', 'Chen', false, true, '2024-02-28', 'doctor4@example.com', 'doctor4', 'Doctor'),
(5, 'password=', NULL, false, 'David', 'Wilson', false, true, '2024-02-28', 'doctor5@example.com', 'doctor5', 'Doctor'),
(6, 'password=', NULL, false, 'Olivia', 'Brown', false, true, '2024-02-28', 'doctor6@example.com', 'doctor6', 'Doctor'),
(7, 'password=', NULL, false, 'James', 'Davis', false, true, '2024-02-28', 'doctor7@example.com', 'doctor7', 'Doctor'),
(8, 'password=', NULL, false, 'Sophia', 'Martinez', false, true, '2024-02-28', 'doctor8@example.com', 'doctor8', 'Doctor'),
(9, 'password=', NULL, false, 'Robert', 'Garcia', false, true, '2024-02-28', 'doctor9@example.com', 'doctor9', 'Doctor'),
(10, 'password=', NULL, false, 'Emma', 'Rodriguez', false, true, '2024-02-28', 'doctor10@example.com', 'doctor10', 'Doctor');

-- Then create patient users
INSERT INTO userauths_user (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, email, username, user_type) VALUES
(11, 'password=', NULL, false, 'Thomas', 'Anderson', false, true, '2024-02-28', 'patient1@example.com', 'patient1', 'Patient'),
(12, 'password=', NULL, false, 'Maria', 'Garcia', false, true, '2024-02-28', 'patient2@example.com', 'patient2', 'Patient'),
(13, 'password=', NULL, false, 'Kevin', 'Robinson', false, true, '2024-02-28', 'patient3@example.com', 'patient3', 'Patient'),
(14, 'password=', NULL, false, 'Linda', 'Wright', false, true, '2024-02-28', 'patient4@example.com', 'patient4', 'Patient'),
(15, 'password=', NULL, false, 'Carlos', 'Lopez', false, true, '2024-02-28', 'patient5@example.com', 'patient5', 'Patient'),
(16, 'password=', NULL, false, 'Susan', 'Hill', false, true, '2024-02-28', 'patient6@example.com', 'patient6', 'Patient'),
(17, 'password=', NULL, false, 'Mark', 'Taylor', false, true, '2024-02-28', 'patient7@example.com', 'patient7', 'Patient'),
(18, 'password=', NULL, false, 'Patricia', 'Clark', false, true, '2024-02-28', 'patient8@example.com', 'patient8', 'Patient'),
(19, 'password=', NULL, false, 'Joseph', 'Lewis', false, true, '2024-02-28', 'patient9@example.com', 'patient9', 'Patient'),
(20, 'password=', NULL, false, 'Nancy', 'Walker', false, true, '2024-02-28', 'patient10@example.com', 'patient10', 'Patient');

-- Create Doctors
INSERT INTO doctor_doctor (id, full_name, image, mobile, country, bio, specialization, qualifications, years_of_experience, next_available_appointment_date, user_id) VALUES
(1, 'Dr. John Smith', 'images/doctor1.jpg', '+1234567890', 'USA', 'Experienced doctor with focus on patient care', 'Cardiology', 'MD, FACC', '15 years', '2024-03-01 10:00:00', 1),
(2, 'Dr. Sarah Johnson', 'images/doctor2.jpg', '+1234567891', 'UK', 'Specialist in pediatric care', 'Pediatrics', 'MD, FAAP', '10 years', '2024-03-01 11:00:00', 2),
(3, 'Dr. Michael Lee', 'images/doctor3.jpg', '+1234567892', 'Canada', 'Expert in orthopedic surgery', 'Orthopedics', 'MD, FAAOS', '12 years', '2024-03-02 09:00:00', 3),
(4, 'Dr. Emily Chen', 'images/doctor4.jpg', '+1234567893', 'Australia', 'Dermatology specialist with research background', 'Dermatology', 'MD, PhD', '8 years', '2024-03-02 13:00:00', 4),
(5, 'Dr. David Wilson', 'images/doctor5.jpg', '+1234567894', 'Germany', 'Neurologist with focus on neurodegenerative diseases', 'Neurology', 'MD, PhD', '20 years', '2024-03-03 10:00:00', 5),
(6, 'Dr. Olivia Brown', 'images/doctor6.jpg', '+1234567895', 'France', 'Obstetrics and gynecology specialist', 'OB/GYN', 'MD, FACOG', '9 years', '2024-03-03 14:00:00', 6),
(7, 'Dr. James Davis', 'images/doctor7.jpg', '+1234567896', 'Spain', 'Psychiatry expert focusing on adolescents', 'Psychiatry', 'MD, DFAPA', '14 years', '2024-03-04 11:00:00', 7),
(8, 'Dr. Sophia Martinez', 'images/doctor8.jpg', '+1234567897', 'Italy', 'Specialist in internal medicine', 'Internal Medicine', 'MD, FACP', '11 years', '2024-03-04 15:00:00', 8),
(9, 'Dr. Robert Garcia', 'images/doctor9.jpg', '+1234567898', 'Brazil', 'Experienced ophthalmologist', 'Ophthalmology', 'MD, FAAO', '16 years', '2024-03-05 09:00:00', 9),
(10, 'Dr. Emma Rodriguez', 'images/doctor10.jpg', '+1234567899', 'Mexico', 'Endocrinology specialist with research focus', 'Endocrinology', 'MD, PhD', '7 years', '2024-03-05 13:00:00', 10);

-- Create Patients
INSERT INTO patient_patient (id, image, full_name, email, mobile, address, gender, dob, blood_group, user_id) VALUES
(1, 'images/patient1.jpg', 'Thomas Anderson', 'patient1@example.com', '+2234567890', '123 Main St, Boston, MA', 'Male', '1975-06-15', 'O+', 11),
(2, 'images/patient2.jpg', 'Maria Garcia', 'patient2@example.com', '+2234567891', '456 Oak Ave, Chicago, IL', 'Female', '1988-03-22', 'A-', 12),
(3, 'images/patient3.jpg', 'Kevin Robinson', 'patient3@example.com', '+2234567892', '789 Pine Rd, Miami, FL', 'Male', '1990-11-08', 'B+', 13),
(4, 'images/patient4.jpg', 'Linda Wright', 'patient4@example.com', '+2234567893', '321 Elm St, Seattle, WA', 'Female', '1982-07-30', 'AB+', 14),
(5, 'images/patient5.jpg', 'Carlos Lopez', 'patient5@example.com', '+2234567894', '654 Cedar Ln, Austin, TX', 'Male', '1971-09-17', 'O-', 15),
(6, 'images/patient6.jpg', 'Susan Hill', 'patient6@example.com', '+2234567895', '987 Maple Dr, Denver, CO', 'Female', '1995-01-25', 'A+', 16),
(7, 'images/patient7.jpg', 'Mark Taylor', 'patient7@example.com', '+2234567896', '741 Birch Blvd, Portland, OR', 'Male', '1968-12-03', 'B-', 17),
(8, 'images/patient8.jpg', 'Patricia Clark', 'patient8@example.com', '+2234567897', '852 Walnut St, Atlanta, GA', 'Female', '1992-05-19', 'AB-', 18),
(9, 'images/patient9.jpg', 'Joseph Lewis', 'patient9@example.com', '+2234567898', '963 Spruce Ave, Philadelphia, PA', 'Male', '1983-08-11', 'O+', 19),
(10, 'images/patient10.jpg', 'Nancy Walker', 'patient10@example.com', '+2234567899', '159 Willow Rd, San Diego, CA', 'Female', '1979-04-27', 'A+', 20);

-- Create Services
INSERT INTO base_service (id, image, name, description, cost) VALUES
(1, 'images/cardiology.jpg', 'Cardiology Consultation', 'Comprehensive heart health assessment and consultation', 250.00),
(2, 'images/pediatric.jpg', 'Pediatric Checkup', 'Complete health examination for children', 150.00),
(3, 'images/orthopedic.jpg', 'Orthopedic Consultation', 'Evaluation and treatment of musculoskeletal issues', 200.00),
(4, 'images/dermatology.jpg', 'Dermatology Screening', 'Skin examination and treatment consultation', 180.00),
(5, 'images/neurology.jpg', 'Neurology Assessment', 'Evaluation of neurological conditions and disorders', 300.00),
(6, 'images/obgyn.jpg', 'OB/GYN Services', 'Women's health consultation and examinations', 220.00),
(7, 'images/psychiatry.jpg', 'Psychiatric Evaluation', 'Mental health assessment and treatment planning', 280.00),
(8, 'images/internalmedicine.jpg', 'General Medical Checkup', 'Comprehensive health evaluation and preventive care', 190.00),
(9, 'images/ophthalmology.jpg', 'Vision Examination', 'Complete eye health and vision assessment', 170.00),
(10, 'images/endocrinology.jpg', 'Endocrinology Consultation', 'Hormone and metabolic health evaluation', 260.00);

-- Link Services to Doctors (many-to-many)
INSERT INTO base_service_available_doctors (id, service_id, doctor_id) VALUES
(1, 1, 1),  -- Cardiology - Dr. John Smith
(2, 2, 2),  -- Pediatrics - Dr. Sarah Johnson 
(3, 3, 3),  -- Orthopedics - Dr. Michael Lee
(4, 4, 4),  -- Dermatology - Dr. Emily Chen
(5, 5, 5),  -- Neurology - Dr. David Wilson
(6, 6, 6),  -- OB/GYN - Dr. Olivia Brown
(7, 7, 7),  -- Psychiatry - Dr. James Davis
(8, 8, 8),  -- Internal Medicine - Dr. Sophia Martinez
(9, 9, 9),  -- Ophthalmology - Dr. Robert Garcia
(10, 10, 10), -- Endocrinology - Dr. Emma Rodriguez
(11, 1, 8),  -- Cardiology - Dr. Sophia Martinez (cross-specialization)
(12, 8, 1),  -- General Medical - Dr. John Smith (cross-specialization)
(13, 5, 10), -- Neurology - Dr. Emma Rodriguez (cross-specialization)
(14, 7, 5);  -- Psychiatry - Dr. David Wilson (cross-specialization)

-- Create Appointments
INSERT INTO base_appointment (id, appointment_date, issues, symptoms, appointment_id, status, doctor_id, patient_id, service_id) VALUES
(1, '2024-03-01 10:30:00', 'Chest pain and shortness of breath', 'Occasional chest tightness when climbing stairs', '123456', 'Scheduled', 1, 1, 1),
(2, '2024-03-01 14:00:00', 'Regular checkup for 5-year-old', 'No major issues, preventive care visit', '234567', 'Scheduled', 2, 2, 2),
(3, '2024-03-02 11:30:00', 'Knee pain after sports injury', 'Swelling and limited mobility in right knee', '345678', 'Scheduled', 3, 3, 3),
(4, '2024-03-03 09:15:00', 'Persistent skin rash', 'Itchy red patches on arms and legs', '456789', 'Scheduled', 4, 4, 4),
(5, '2024-03-04 13:45:00', 'Chronic headaches', 'Severe migraines 2-3 times per week', '567890', 'Scheduled', 5, 5, 5),
(6, '2024-03-04 15:30:00', 'Prenatal care visit', 'Routine pregnancy checkup, currently 20 weeks', '678901', 'Scheduled', 6, 6, 6),
(7, '2024-03-05 10:00:00', 'Depression and anxiety symptoms', 'Trouble sleeping, loss of interest in activities', '789012', 'Scheduled', 7, 7, 7),
(8, '2024-03-05 16:00:00', 'Annual physical examination', 'No specific issues, routine health monitoring', '890123', 'Scheduled', 8, 8, 8),
(9, '2024-03-06 11:00:00', 'Vision problems, blurry sight', 'Difficulty reading and driving at night', '901234', 'Scheduled', 9, 9, 9),
(10, '2024-03-06 14:30:00', 'Weight gain and fatigue', 'Unexplained weight gain and constant tiredness', '012345', 'Scheduled', 10, 10, 10);

-- Create Medical Records
INSERT INTO base_medicalrecord (id, diagnosis, treatment, appointment_id) VALUES
(1, 'Mild angina pectoris, stress-induced', 'Prescribed nitroglycerin for acute episodes, scheduled stress test, recommended lifestyle modifications', 1),
(2, 'Healthy child, normal development', 'Routine vaccinations administered, vitamin D supplement recommended', 2),
(3, 'Grade II MCL sprain', 'Rest, ice, compression, elevation (RICE protocol), prescribed anti-inflammatory medication, physical therapy referral', 3),
(4, 'Contact dermatitis', 'Topical corticosteroid cream, antihistamine for itching, allergen patch testing scheduled', 4),
(5, 'Chronic migraine, possibly tension-related', 'Prescribed sumatriptan for acute episodes, amitriptyline for prevention, stress management techniques discussed', 5),
(6, 'Healthy pregnancy, normal progression', 'Prenatal vitamins continued, iron supplement added, scheduled 24-week ultrasound', 6),
(7, 'Major depressive disorder with anxiety features', 'Started on sertraline 50mg daily, weekly therapy sessions recommended, sleep hygiene measures discussed', 7),
(8, 'Generally healthy, mild hypertension noted', 'Diet and exercise program recommended, blood pressure monitoring, follow-up in 3 months', 8),
(9, 'Moderate myopia, early cataracts', 'New corrective lens prescription, UV protection recommended, cataract monitoring plan established', 9),
(10, 'Hypothyroidism', 'Started on levothyroxine 75mcg daily, dietary adjustments recommended, follow-up blood work in 6 weeks', 10);

-- Create Lab Tests
INSERT INTO base_labtest (id, test_name, description, result, appointment_id) VALUES
(1, 'Cardiac Enzyme Panel', 'Test for heart attack markers including Troponin and CK-MB', 'All enzymes within normal ranges, no evidence of acute cardiac injury', 1),
(2, 'Complete Blood Count', 'Standard pediatric blood screening', 'All values within normal range for age', 2),
(3, 'Knee MRI', 'Imaging of right knee to assess ligament damage', 'Grade II sprain of the medial collateral ligament, no complete tear observed', 3),
(4, 'Skin Allergen Panel', 'Testing for common contact allergens', 'Positive reaction to nickel and certain laundry detergent compounds', 4),
(5, 'Brain MRI', 'Imaging to rule out structural causes of headaches', 'No structural abnormalities detected, normal brain imaging', 5),
(6, 'Prenatal Panel', 'Standard 20-week pregnancy blood tests', 'Normal glucose levels, adequate iron, all screening tests negative for abnormalities', 6),
(7, 'Thyroid Function Test', 'Screening for thyroid contribution to depression', 'TSH, T3, and T4 all within normal ranges', 7),
(8, 'Lipid Panel', 'Cholesterol screening', 'Total cholesterol 210 mg/dL (slightly elevated), LDL 130 mg/dL (borderline), HDL 45 mg/dL', 8),
(9, 'Vision Field Test', 'Assessment of peripheral vision', 'Normal visual fields, no evidence of glaucoma or neurological issues', 9),
(10, 'Thyroid Function Panel', 'Comprehensive thyroid assessment', 'Elevated TSH (7.8 mIU/L), low T4 (0.7 ng/dL), consistent with hypothyroidism', 10);

-- Create Prescriptions
INSERT INTO base_prescription (id, medications, appointment_id) VALUES
(1, 'Nitroglycerin 0.4mg sublingual tablets PRN for chest pain; Aspirin 81mg daily; Atorvastatin 10mg daily', 1),
(2, 'Vitamin D drops 400 IU daily', 2),
(3, 'Ibuprofen 600mg every 6 hours PRN for pain and inflammation; Naproxen 500mg twice daily with food', 3),
(4, 'Hydrocortisone 1% cream applied to affected areas twice daily; Cetirizine 10mg daily for itching', 4),
(5, 'Sumatriptan 50mg at onset of migraine; Amitriptyline 25mg daily at bedtime; Ibuprofen 400mg PRN for breakthrough pain', 5),
(6, 'Prenatal vitamin daily; Ferrous sulfate 325mg daily; Calcium 500mg twice daily', 6),
(7, 'Sertraline 50mg daily in the morning; Lorazepam 0.5mg PRN for acute anxiety (not to exceed 3 times weekly)', 7),
(8, 'Lifestyle modifications advised; no prescription medications at this time', 8),
(9, 'Artificial tears as needed for dry eyes; new eyeglass prescription provided separately', 9),
(10, 'Levothyroxine 75mcg daily on empty stomach; take at least 30 minutes before breakfast', 10);

-- Create Billings
INSERT INTO base_billing (id, sub_total, tax, total, status, billing_id, date, appointment_id, patient_id) VALUES
(1, 250.00, 20.00, 270.00, 'Paid', '654321', '2024-03-01 11:30:00', 1, 1),
(2, 150.00, 12.00, 162.00, 'Paid', '765432', '2024-03-01 15:00:00', 2, 2),
(3, 200.00, 16.00, 216.00, 'Unpaid', '876543', '2024-03-02 12:30:00', 3, 3),
(4, 180.00, 14.40, 194.40, 'Paid', '987654', '2024-03-03 10:15:00', 4, 4),
(5, 300.00, 24.00, 324.00, 'Unpaid', '098765', '2024-03-04 14:45:00', 5, 5),
(6, 220.00, 17.60, 237.60, 'Paid', '109876', '2024-03-04 16:30:00', 6, 6),
(7, 280.00, 22.40, 302.40, 'Unpaid', '210987', '2024-03-05 11:00:00', 7, 7),
(8, 190.00, 15.20, 205.20, 'Paid', '321098', '2024-03-05 17:00:00', 8, 8),
(9, 170.00, 13.60, 183.60, 'Paid', '432109', '2024-03-06 12:00:00', 9, 9),
(10, 260.00, 20.80, 280.80, 'Unpaid', '543210', '2024-03-06 15:30:00', 10, 10);

-- Create Notifications for doctors
INSERT INTO doctor_notification (id, type, seen, date, appointment_id, doctor_id) VALUES
(1, 'New Appointment', false, '2024-02-28 09:30:00', 1, 1),
(2, 'New Appointment', false, '2024-02-28 10:15:00', 2, 2),
(3, 'New Appointment', false, '2024-02-28 11:00:00', 3, 3),
(4, 'New Appointment', true, '2024-02-28 13:45:00', 4, 4),
(5, 'New Appointment', true, '2024-02-28 14:30:00', 5, 5),
(6, 'New Appointment', false, '2024-02-28 15:20:00', 6, 6),
(7, 'New Appointment', false, '2024-02-28 16:10:00', 7, 7),
(8, 'New Appointment', true, '2024-02-28 17:05:00', 8, 8),
(9, 'New Appointment', false, '2024-02-29 09:15:00', 9, 9),
(10, 'New Appointment', true, '2024-02-29 10:00:00', 10, 10);

-- Create Notifications for patients
INSERT INTO patient_notification (id, type, seen, date, appointment_i-- Clear existing data
DELETE FROM base_billing;
DELETE FROM base_prescription;
DELETE FROM base_labtest;
DELETE FROM base_medicalrecord;
DELETE FROM base_appointment;
DELETE FROM base_service_available_doctors;
DELETE FROM base_service;
DELETE FROM patient_notification;
DELETE FROM doctor_notification;
DELETE FROM patient_patient;
DELETE FROM doctor_doctor;
DELETE FROM userauths_user;

-- Create Users
-- First create doctor users
INSERT INTO userauths_user (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, email, username, user_type) VALUES
(1, 'password=', NULL, false, 'John', 'Smith', false, true, '2024-02-28', 'doctor1@example.com', 'doctor1', 'Doctor'),
(2, 'password=', NULL, false, 'Sarah', 'Johnson', false, true, '2024-02-28', 'doctor2@example.com', 'doctor2', 'Doctor'),
(3, 'password=', NULL, false, 'Michael', 'Lee', false, true, '2024-02-28', 'doctor3@example.com', 'doctor3', 'Doctor'),
(4, 'password=', NULL, false, 'Emily', 'Chen', false, true, '2024-02-28', 'doctor4@example.com', 'doctor4', 'Doctor'),
(5, 'password=', NULL, false, 'David', 'Wilson', false, true, '2024-02-28', 'doctor5@example.com', 'doctor5', 'Doctor'),
(6, 'password=', NULL, false, 'Olivia', 'Brown', false, true, '2024-02-28', 'doctor6@example.com', 'doctor6', 'Doctor'),
(7, 'password=', NULL, false, 'James', 'Davis', false, true, '2024-02-28', 'doctor7@example.com', 'doctor7', 'Doctor'),
(8, 'password=', NULL, false, 'Sophia', 'Martinez', false, true, '2024-02-28', 'doctor8@example.com', 'doctor8', 'Doctor'),
(9, 'password=', NULL, false, 'Robert', 'Garcia', false, true, '2024-02-28', 'doctor9@example.com', 'doctor9', 'Doctor'),
(10, 'password=', NULL, false, 'Emma', 'Rodriguez', false, true, '2024-02-28', 'doctor10@example.com', 'doctor10', 'Doctor');

-- Then create patient users
INSERT INTO userauths_user (id, password, last_login, is_superuser, first_name, last_name, is_staff, is_active, date_joined, email, username, user_type) VALUES
(11, 'password=', NULL, false, 'Thomas', 'Anderson', false, true, '2024-02-28', 'patient1@example.com', 'patient1', 'Patient'),
(12, 'password=', NULL, false, 'Maria', 'Garcia', false, true, '2024-02-28', 'patient2@example.com', 'patient2', 'Patient'),
(13, 'password=', NULL, false, 'Kevin', 'Robinson', false, true, '2024-02-28', 'patient3@example.com', 'patient3', 'Patient'),
(14, 'password=', NULL, false, 'Linda', 'Wright', false, true, '2024-02-28', 'patient4@example.com', 'patient4', 'Patient'),
(15, 'password=', NULL, false, 'Carlos', 'Lopez', false, true, '2024-02-28', 'patient5@example.com', 'patient5', 'Patient'),
(16, 'password=', NULL, false, 'Susan', 'Hill', false, true, '2024-02-28', 'patient6@example.com', 'patient6', 'Patient'),
(17, 'password=', NULL, false, 'Mark', 'Taylor', false, true, '2024-02-28', 'patient7@example.com', 'patient7', 'Patient'),
(18, 'password=', NULL, false, 'Patricia', 'Clark', false, true, '2024-02-28', 'patient8@example.com', 'patient8', 'Patient'),
(19, 'password=', NULL, false, 'Joseph', 'Lewis', false, true, '2024-02-28', 'patient9@example.com', 'patient9', 'Patient'),
(20, 'password=', NULL, false, 'Nancy', 'Walker', false, true, '2024-02-28', 'patient10@example.com', 'patient10', 'Patient');

-- Create Doctors
INSERT INTO doctor_doctor (id, full_name, image, mobile, country, bio, specialization, qualifications, years_of_experience, next_available_appointment_date, user_id) VALUES
(1, 'Dr. John Smith', 'images/doctor1.jpg', '+1234567890', 'USA', 'Experienced doctor with focus on patient care', 'Cardiology', 'MD, FACC', '15 years', '2024-03-01 10:00:00', 1),
(2, 'Dr. Sarah Johnson', 'images/doctor2.jpg', '+1234567891', 'UK', 'Specialist in pediatric care', 'Pediatrics', 'MD, FAAP', '10 years', '2024-03-01 11:00:00', 2),
(3, 'Dr. Michael Lee', 'images/doctor3.jpg', '+1234567892', 'Canada', 'Expert in orthopedic surgery', 'Orthopedics', 'MD, FAAOS', '12 years', '2024-03-02 09:00:00', 3),
(4, 'Dr. Emily Chen', 'images/doctor4.jpg', '+1234567893', 'Australia', 'Dermatology specialist with research background', 'Dermatology', 'MD, PhD', '8 years', '2024-03-02 13:00:00', 4),
(5, 'Dr. David Wilson', 'images/doctor5.jpg', '+1234567894', 'Germany', 'Neurologist with focus on neurodegenerative diseases', 'Neurology', 'MD, PhD', '20 years', '2024-03-03 10:00:00', 5),
(6, 'Dr. Olivia Brown', 'images/doctor6.jpg', '+1234567895', 'France', 'Obstetrics and gynecology specialist', 'OB/GYN', 'MD, FACOG', '9 years', '2024-03-03 14:00:00', 6),
(7, 'Dr. James Davis', 'images/doctor7.jpg', '+1234567896', 'Spain', 'Psychiatry expert focusing on adolescents', 'Psychiatry', 'MD, DFAPA', '14 years', '2024-03-04 11:00:00', 7),
(8, 'Dr. Sophia Martinez', 'images/doctor8.jpg', '+1234567897', 'Italy', 'Specialist in internal medicine', 'Internal Medicine', 'MD, FACP', '11 years', '2024-03-04 15:00:00', 8),
(9, 'Dr. Robert Garcia', 'images/doctor9.jpg', '+1234567898', 'Brazil', 'Experienced ophthalmologist', 'Ophthalmology', 'MD, FAAO', '16 years', '2024-03-05 09:00:00', 9),
(10, 'Dr. Emma Rodriguez', 'images/doctor10.jpg', '+1234567899', 'Mexico', 'Endocrinology specialist with research focus', 'Endocrinology', 'MD, PhD', '7 years', '2024-03-05 13:00:00', 10);

-- Create Patients
INSERT INTO patient_patient (id, image, full_name, email, mobile, address, gender, dob, blood_group, user_id) VALUES
(1, 'images/patient1.jpg', 'Thomas Anderson', 'patient1@example.com', '+2234567890', '123 Main St, Boston, MA', 'Male', '1975-06-15', 'O+', 11),
(2, 'images/patient2.jpg', 'Maria Garcia', 'patient2@example.com', '+2234567891', '456 Oak Ave, Chicago, IL', 'Female', '1988-03-22', 'A-', 12),
(3, 'images/patient3.jpg', 'Kevin Robinson', 'patient3@example.com', '+2234567892', '789 Pine Rd, Miami, FL', 'Male', '1990-11-08', 'B+', 13),
(4, 'images/patient4.jpg', 'Linda Wright', 'patient4@example.com', '+2234567893', '321 Elm St, Seattle, WA', 'Female', '1982-07-30', 'AB+', 14),
(5, 'images/patient5.jpg', 'Carlos Lopez', 'patient5@example.com', '+2234567894', '654 Cedar Ln, Austin, TX', 'Male', '1971-09-17', 'O-', 15),
(6, 'images/patient6.jpg', 'Susan Hill', 'patient6@example.com', '+2234567895', '987 Maple Dr, Denver, CO', 'Female', '1995-01-25', 'A+', 16),
(7, 'images/patient7.jpg', 'Mark Taylor', 'patient7@example.com', '+2234567896', '741 Birch Blvd, Portland, OR', 'Male', '1968-12-03', 'B-', 17),
(8, 'images/patient8.jpg', 'Patricia Clark', 'patient8@example.com', '+2234567897', '852 Walnut St, Atlanta, GA', 'Female', '1992-05-19', 'AB-', 18),
(9, 'images/patient9.jpg', 'Joseph Lewis', 'patient9@example.com', '+2234567898', '963 Spruce Ave, Philadelphia, PA', 'Male', '1983-08-11', 'O+', 19),
(10, 'images/patient10.jpg', 'Nancy Walker', 'patient10@example.com', '+2234567899', '159 Willow Rd, San Diego, CA', 'Female', '1979-04-27', 'A+', 20);

-- Create Services
INSERT INTO base_service (id, image, name, description, cost) VALUES
(1, 'images/cardiology.jpg', 'Cardiology Consultation', 'Comprehensive heart health assessment and consultation', 250.00),
(2, 'images/pediatric.jpg', 'Pediatric Checkup', 'Complete health examination for children', 150.00),
(3, 'images/orthopedic.jpg', 'Orthopedic Consultation', 'Evaluation and treatment of musculoskeletal issues', 200.00),
(4, 'images/dermatology.jpg', 'Dermatology Screening', 'Skin examination and treatment consultation', 180.00),
(5, 'images/neurology.jpg', 'Neurology Assessment', 'Evaluation of neurological conditions and disorders', 300.00),
(6, 'images/obgyn.jpg', 'OB/GYN Services', 'Women's health consultation and examinations', 220.00),
(7, 'images/psychiatry.jpg', 'Psychiatric Evaluation', 'Mental health assessment and treatment planning', 280.00),
(8, 'images/internalmedicine.jpg', 'General Medical Checkup', 'Comprehensive health evaluation and preventive care', 190.00),
(9, 'images/ophthalmology.jpg', 'Vision Examination', 'Complete eye health and vision assessment', 170.00),
(10, 'images/endocrinology.jpg', 'Endocrinology Consultation', 'Hormone and metabolic health evaluation', 260.00);

-- Link Services to Doctors (many-to-many)
INSERT INTO base_service_available_doctors (id, service_id, doctor_id) VALUES
(1, 1, 1),  -- Cardiology - Dr. John Smith
(2, 2, 2),  -- Pediatrics - Dr. Sarah Johnson 
(3, 3, 3),  -- Orthopedics - Dr. Michael Lee
(4, 4, 4),  -- Dermatology - Dr. Emily Chen
(5, 5, 5),  -- Neurology - Dr. David Wilson
(6, 6, 6),  -- OB/GYN - Dr. Olivia Brown
(7, 7, 7),  -- Psychiatry - Dr. James Davis
(8, 8, 8),  -- Internal Medicine - Dr. Sophia Martinez
(9, 9, 9),  -- Ophthalmology - Dr. Robert Garcia
(10, 10, 10), -- Endocrinology - Dr. Emma Rodriguez
(11, 1, 8),  -- Cardiology - Dr. Sophia Martinez (cross-specialization)
(12, 8, 1),  -- General Medical - Dr. John Smith (cross-specialization)
(13, 5, 10), -- Neurology - Dr. Emma Rodriguez (cross-specialization)
(14, 7, 5);  -- Psychiatry - Dr. David Wilson (cross-specialization)

-- Create Appointments
INSERT INTO base_appointment (id, appointment_date, issues, symptoms, appointment_id, status, doctor_id, patient_id, service_id) VALUES
(1, '2024-03-01 10:30:00', 'Chest pain and shortness of breath', 'Occasional chest tightness when climbing stairs', '123456', 'Scheduled', 1, 1, 1),
(2, '2024-03-01 14:00:00', 'Regular checkup for 5-year-old', 'No major issues, preventive care visit', '234567', 'Scheduled', 2, 2, 2),
(3, '2024-03-02 11:30:00', 'Knee pain after sports injury', 'Swelling and limited mobility in right knee', '345678', 'Scheduled', 3, 3, 3),
(4, '2024-03-03 09:15:00', 'Persistent skin rash', 'Itchy red patches on arms and legs', '456789', 'Scheduled', 4, 4, 4),
(5, '2024-03-04 13:45:00', 'Chronic headaches', 'Severe migraines 2-3 times per week', '567890', 'Scheduled', 5, 5, 5),
(6, '2024-03-04 15:30:00', 'Prenatal care visit', 'Routine pregnancy checkup, currently 20 weeks', '678901', 'Scheduled', 6, 6, 6),
(7, '2024-03-05 10:00:00', 'Depression and anxiety symptoms', 'Trouble sleeping, loss of interest in activities', '789012', 'Scheduled', 7, 7, 7),
(8, '2024-03-05 16:00:00', 'Annual physical examination', 'No specific issues, routine health monitoring', '890123', 'Scheduled', 8, 8, 8),
(9, '2024-03-06 11:00:00', 'Vision problems, blurry sight', 'Difficulty reading and driving at night', '901234', 'Scheduled', 9, 9, 9),
(10, '2024-03-06 14:30:00', 'Weight gain and fatigue', 'Unexplained weight gain and constant tiredness', '012345', 'Scheduled', 10, 10, 10);

-- Create Medical Records
INSERT INTO base_medicalrecord (id, diagnosis, treatment, appointment_id) VALUES
(1, 'Mild angina pectoris, stress-induced', 'Prescribed nitroglycerin for acute episodes, scheduled stress test, recommended lifestyle modifications', 1),
(2, 'Healthy child, normal development', 'Routine vaccinations administered, vitamin D supplement recommended', 2),
(3, 'Grade II MCL sprain', 'Rest, ice, compression, elevation (RICE protocol), prescribed anti-inflammatory medication, physical therapy referral', 3),
(4, 'Contact dermatitis', 'Topical corticosteroid cream, antihistamine for itching, allergen patch testing scheduled', 4),
(5, 'Chronic migraine, possibly tension-related', 'Prescribed sumatriptan for acute episodes, amitriptyline for prevention, stress management techniques discussed', 5),
(6, 'Healthy pregnancy, normal progression', 'Prenatal vitamins continued, iron supplement added, scheduled 24-week ultrasound', 6),
(7, 'Major depressive disorder with anxiety features', 'Started on sertraline 50mg daily, weekly therapy sessions recommended, sleep hygiene measures discussed', 7),
(8, 'Generally healthy, mild hypertension noted', 'Diet and exercise program recommended, blood pressure monitoring, follow-up in 3 months', 8),
(9, 'Moderate myopia, early cataracts', 'New corrective lens prescription, UV protection recommended, cataract monitoring plan established', 9),
(10, 'Hypothyroidism', 'Started on levothyroxine 75mcg daily, dietary adjustments recommended, follow-up blood work in 6 weeks', 10);

-- Create Lab Tests
INSERT INTO base_labtest (id, test_name, description, result, appointment_id) VALUES
(1, 'Cardiac Enzyme Panel', 'Test for heart attack markers including Troponin and CK-MB', 'All enzymes within normal ranges, no evidence of acute cardiac injury', 1),
(2, 'Complete Blood Count', 'Standard pediatric blood screening', 'All values within normal range for age', 2),
(3, 'Knee MRI', 'Imaging of right knee to assess ligament damage', 'Grade II sprain of the medial collateral ligament, no complete tear observed', 3),
(4, 'Skin Allergen Panel', 'Testing for common contact allergens', 'Positive reaction to nickel and certain laundry detergent compounds', 4),
(5, 'Brain MRI', 'Imaging to rule out structural causes of headaches', 'No structural abnormalities detected, normal brain imaging', 5),
(6, 'Prenatal Panel', 'Standard 20-week pregnancy blood tests', 'Normal glucose levels, adequate iron, all screening tests negative for abnormalities', 6),
(7, 'Thyroid Function Test', 'Screening for thyroid contribution to depression', 'TSH, T3, and T4 all within normal ranges', 7),
(8, 'Lipid Panel', 'Cholesterol screening', 'Total cholesterol 210 mg/dL (slightly elevated), LDL 130 mg/dL (borderline), HDL 45 mg/dL', 8),
(9, 'Vision Field Test', 'Assessment of peripheral vision', 'Normal visual fields, no evidence of glaucoma or neurological issues', 9),
(10, 'Thyroid Function Panel', 'Comprehensive thyroid assessment', 'Elevated TSH (7.8 mIU/L), low T4 (0.7 ng/dL), consistent with hypothyroidism', 10);

-- Create Prescriptions
INSERT INTO base_prescription (id, medications, appointment_id) VALUES
(1, 'Nitroglycerin 0.4mg sublingual tablets PRN for chest pain; Aspirin 81mg daily; Atorvastatin 10mg daily', 1),
(2, 'Vitamin D drops 400 IU daily', 2),
(3, 'Ibuprofen 600mg every 6 hours PRN for pain and inflammation; Naproxen 500mg twice daily with food', 3),
(4, 'Hydrocortisone 1% cream applied to affected areas twice daily; Cetirizine 10mg daily for itching', 4),
(5, 'Sumatriptan 50mg at onset of migraine; Amitriptyline 25mg daily at bedtime; Ibuprofen 400mg PRN for breakthrough pain', 5),
(6, 'Prenatal vitamin daily; Ferrous sulfate 325mg daily; Calcium 500mg twice daily', 6),
(7, 'Sertraline 50mg daily in the morning; Lorazepam 0.5mg PRN for acute anxiety (not to exceed 3 times weekly)', 7),
(8, 'Lifestyle modifications advised; no prescription medications at this time', 8),
(9, 'Artificial tears as needed for dry eyes; new eyeglass prescription provided separately', 9),
(10, 'Levothyroxine 75mcg daily on empty stomach; take at least 30 minutes before breakfast', 10);

-- Create Billings
INSERT INTO base_billing (id, sub_total, tax, total, status, billing_id, date, appointment_id, patient_id) VALUES
(1, 250.00, 20.00, 270.00, 'Paid', '654321', '2024-03-01 11:30:00', 1, 1),
(2, 150.00, 12.00, 162.00, 'Paid', '765432', '2024-03-01 15:00:00', 2, 2),
(3, 200.00, 16.00, 216.00, 'Unpaid', '876543', '2024-03-02 12:30:00', 3, 3),
(4, 180.00, 14.40, 194.40, 'Paid', '987654', '2024-03-03 10:15:00', 4, 4),
(5, 300.00, 24.00, 324.00, 'Unpaid', '098765', '2024-03-04 14:45:00', 5, 5),
(6, 220.00, 17.60, 237.60, 'Paid', '109876', '2024-03-04 16:30:00', 6, 6),
(7, 280.00, 22.40, 302.40, 'Unpaid', '210987', '2024-03-05 11:00:00', 7, 7),
(8, 190.00, 15.20, 205.20, 'Paid', '321098', '2024-03-05 17:00:00', 8, 8),
(9, 170.00, 13.60, 183.60, 'Paid', '432109', '2024-03-06 12:00:00', 9, 9),
(10, 260.00, 20.80, 280.80, 'Unpaid', '543210', '2024-03-06 15:30:00', 10, 10);

-- Create Notifications for doctors
INSERT INTO doctor_notification (id, type, seen, date, appointment_id, doctor_id) VALUES
(1, 'New Appointment', false, '2024-02-28 09:30:00', 1, 1),
(2, 'New Appointment', false, '2024-02-28 10:15:00', 2, 2),
(3, 'New Appointment', false, '2024-02-28 11:00:00', 3, 3),
(4, 'New Appointment', true, '2024-02-28 13:45:00', 4, 4),
(5, 'New Appointment', true, '2024-02-28 14:30:00', 5, 5),
(6, 'New Appointment', false, '2024-02-28 15:20:00', 6, 6),
(7, 'New Appointment', false, '2024-02-28 16:10:00', 7, 7),
(8, 'New Appointment', true, '2024-02-28 17:05:00', 8, 8),
(9, 'New Appointment', false, '2024-02-29 09:15:00', 9, 9),
(10, 'New Appointment', true, '2024-02-29 10:00:00', 10, 10);

-- Create Notifications for patients
INSERT INTO patient_notification (id, type, seen, date, appointment_i