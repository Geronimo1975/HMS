-- Create medical services
INSERT INTO base_service (id, image, name, description, cost)
VALUES
(1, 'images/cardiology.jpg', 'Cardiology Consultation', 'Complete heart health evaluation including ECG and consultation with a cardiologist', 250.00),
(2, 'images/pediatrics.jpg', 'Pediatric Check-up', 'Comprehensive health assessment for children including growth monitoring and vaccinations', 150.00),
(3, 'images/orthopedics.jpg', 'Orthopedic Evaluation', 'Evaluation of bone, joint, or muscle injuries and conditions', 200.00),
(4, 'images/dermatology.jpg', 'Dermatology Consultation', 'Skin examination and treatment for various skin conditions', 180.00),
(5, 'images/neurology.jpg', 'Neurology Consultation', 'Comprehensive brain and nervous system evaluation', 275.00),
(6, 'images/obstetrics.jpg', 'Prenatal Care', 'Comprehensive pregnancy care including ultrasound and health monitoring', 225.00),
(7, 'images/psychiatry.jpg', 'Psychiatric Evaluation', 'Mental health assessment and treatment planning', 220.00),
(8, 'images/family-medicine.jpg', 'Annual Physical', 'Comprehensive yearly health check-up', 175.00),
(9, 'images/ophthalmology.jpg', 'Vision Assessment', 'Complete eye examination and vision testing', 160.00),
(10, 'images/endocrinology.jpg', 'Endocrinology Consultation', 'Evaluation of hormone-related conditions', 240.00);

-- Link doctors to services they provide
INSERT INTO base_service_available_doctors (id, service_id, doctor_id)
VALUES
-- Cardiology
(1, 1, 1),

-- Pediatrics
(2, 2, 2),

-- Orthopedics
(3, 3, 3),

-- Dermatology
(4, 4, 4),

-- Neurology
(5, 5, 5),

-- Obstetrics
(6, 6, 6),

-- Psychiatry
(7, 7, 7),

-- Family Medicine
(8, 8, 8),

-- Ophthalmology
(9, 9, 9),

-- Endocrinology
(10, 10, 10);
