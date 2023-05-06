<?php
            $EDIFICE = $_POST['EDIFICE'];
            $ROOM = $_POST['ROOM'];//A034
            //$ROOM = "A034";//A034
            //$DAY = $_POST['DAY'];
            //$TIME = $_POST['TIME'];
            $DAY = "I";
            $TIME = "00:05:00";
            // $EDIFICE = "DESV1";

            $servername = "localhost";
            $username = "username";
            $password = "password";
            $dbname = "SIIAU2";

            try {
                $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
                // set the PDO error mode to exception
                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            } catch(PDOException $e) {
                echo "Connection failed: " . $e->getMessage();
            }

            
            $sql = "SELECT c.Clave, c.Materia, c.Sec, c.CR, c.CUP,c.DIS, h.Dia, h.Hora_inicio, h.Hora_fin, a.Nombre, e.Nombre AS Edificio,p.Nombre
            FROM Curso c
            INNER JOIN Curso_Horario ch ON c.Clave = ch.Curso_Clave
            INNER JOIN Horario h ON ch.Horario_ID = h.ID
            INNER JOIN Aula a ON ch.Aula_ID = a.ID
            INNER JOIN Edificio e ON a.Edificio_ID = e.ID
            INNER JOIN Curso_Profesor cp ON c.Clave = cp.Curso_Clave
            INNER JOIN Profesor p ON p.ID = cp.Profesor_ID
            WHERE e.Nombre = :NombreE
            AND h.Dia = :Dia
            AND a.Nombre = :NombreA
            AND h.Hora_inicio <= '00:05:00'
            AND h.Hora_fin >= '00:05:00'";
            
            
            
            $stmt = $conn->prepare($sql);
            //echo "I respond: ".$EDIFICE."-".$ROOM."-".$DAY."-".$TIME;
            $stmt->bindParam(":NombreE", $EDIFICE);
            $stmt->bindParam(":Dia", $DAY);
            $stmt->bindParam(":NombreA", $ROOM);
            // $stmt->bindParam(":Hora", $TIME);
           
            $stmt->execute();
            $rows = $stmt->fetchAll();
            foreach ($rows as $row) {
              // echo $row['Clave'] . "-" . $row['Materia'];
              $data = array(
                'Clave' => $row['Clave'],
                'Materia' => $row['Materia'],
                'Sec' => $row['Sec'],
                'CR' => $row['CR'],
                'CUP' => $row['CUP'],
                'DIS' => $row['DIS'],
                'Dia' => $row['Dia'],
                'Hora_inicio' => $row['Hora_inicio'],
                'Hora_fin' => $row['Hora_fin'],
                'NombreRoom' => $row['Nombre'],
                'Edificio' => $row['Edificio'],
                'NombreTeacher' => $row['Nombre'],
            );
            echo json_encode($data);
            }
          
          
          ?>