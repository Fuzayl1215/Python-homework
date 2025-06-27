-- 1. Create the Roster table
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

-- 2. Insert data into the Roster table
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

-- 3. Update Jadzia Dax to Ezri Dax
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

-- 4. Select Name and Age of Bajoran individuals
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
