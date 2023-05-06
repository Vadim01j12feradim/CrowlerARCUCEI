<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="JS/jquery.min.js"></script>
    <script src="JS/instascan.min.js"></script>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="anim"></div>
    <video id="preview"></video>
    
    <script type='text/javascript'>

      function getRealDay(day) {
        switch (day) {
          case 1:
              return "L";  
            break;
          case 2:
              return "M";  
            break;
          case 3:
              return "I";  
            break;
          case 4:
              return "J";  
            break;
          case 5:
              return "V";  
            break;
          case 6:
              return "S";  
            break;
          case 7:
              return "D";  
            break;
          default:
            return "error";
        }
      }
      function enviarParametros(EDIFICEP,ROOMP,DAYP,TIMEP) {
        $.ajax({
          url: "PHP/query.php",
          type: "POST",
          data: {
            EDIFICE: EDIFICEP,
            ROOM:ROOMP,
            DAY:DAYP,
            TIME:TIMEP
          },
          success: function(response) {
            alert(response);
            let url = "PHP/showInfo.php?data=" + encodeURIComponent(response);// + "&param2=" + encodeURIComponent(param2);
            window.location.href = url;
            
          },
          error: function(xhr, status, error) {
            alert("Has error: "+xhr.responseText);
          }
        });
      }

        let scanner = new Instascan.Scanner({ video: document.getElementById('preview') });
        scanner.addListener('scan', function (content) {
          var string = content;
          var EDIFICE = string.substring(0, string.indexOf(" "));
          var ROOM = string.substring(EDIFICE.length+1);

          var date = new Date();


          // var TIME = date.getHours().toString().padStart(2, '0')+""+date.getMinutes().toString().padStart(2, '0');
          var TIME = date.getHours()+":"+date.getMinutes()+":"+date.getSeconds();
          var DAY = date.getDay()
          DAY = getRealDay(DAY)
          enviarParametros(EDIFICE,ROOM,DAY,TIME);
          // alert(content);
        });
        Instascan.Camera.getCameras().then(function (cameras) {
          if (cameras.length > 0) {
            scanner.start(cameras[0]);
          } else {
            console.error('No cameras found.');
          }
        }).catch(function (e) {
          console.error(e);
        });
    </script>
</body>
</html>