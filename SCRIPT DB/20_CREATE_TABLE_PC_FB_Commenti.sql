CREATE TABLE FALC_FB_Commenti (
   Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, 
   IdPost INT NOT NULL FOREIGN KEY REFERENCES FALC_FB_Post(Id),
   Autore VARCHAR(50) NOT NULL,
   Testo VARCHAR(255) NOT NULL);