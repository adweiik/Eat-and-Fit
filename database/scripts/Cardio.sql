CREATE TABLE if not exists Cardio (
	Stage int not null,
    Body int not null,
    Sex int not null,
    Sessions int,
    Time varchar(255),
    primary key (Stage, Body, Sex)
);

/*
Stage: 0, 1
Body: underweight: 0
normal: 1
overweight: 2
pre-obese: 3
obese: 4
Sex: male: 0,
female: 1
*/
 
 /* Query:
 SELECT * FROM eatandfit.Cardio WHERE Stage = ? and Body = ? and Sex = ?;
 */
 
INSERT INTO Cardio VALUES (0, 2, 0, 3, '12, 15, 12 minute'),
					      (1, 2, 0, 4, '22, 25, 22, 25 minute'),
					      (0, 3, 0, 3, '15, 20, 15 minute'),
					      (1, 3, 0, 4, '27, 30, 27, 30 minute'),
					      (0, 4, 0, 3, '20, 20, 20 minute'),
					      (1, 4, 0, 4, '35, 40, 30, 45 minute'),
					      (0, 2, 1, 3, '12, 15, 12 minute'),
					      (1, 2, 1, 4, '20, 22, 20, 22 minute'),
					      (0, 3, 1, 3, '15, 20, 15 minute'),
					      (1, 3, 1, 4, '25, 27, 25, 27 minute'),
					      (0, 4, 1, 3, '20, 20, 20 minute'),
					      (1, 4, 1, 4, '30, 35, 30, 35 minute');