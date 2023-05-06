<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="JS/jquery.min.js"></script>
    <script src="JS/instascan.min.js"></script>
</head>
<body>
    <video id="preview"></video>
    <script type="text/javascript">
        let scanner = new Instascan.Scanner({ video: document.getElementById('preview') });
        scanner.addListener('scan', function (content) {
          alert(content);});
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







/* <a-scene embedded arjs>
<a-marker preset="Hiro">
<a-entity scale=".2 .2 .2" position="-1 0 0" rotation="-85 0 0"> 
  <a-entity gltf-model="models/7.glb" scale="8 8 8" crossOrigin="anonymous"></a-entity>
  <a-entity position="0 22 0">
    <a-text value="Hello" align="center" color="white" width="35"></a-text>
  </a-entity>
</a-entity>

<a-entity scale=".2 .2 .2" position="0 0 0" rotation="-93 0 0"> 
  <a-entity position="0 8 3">
    <a-text value="I'm" align="center" color="white" width="35"></a-text>
  </a-entity>
  <a-entity gltf-model="models/7.glb" scale="8 8 8" crossOrigin="anonymous"></a-entity>
  
</a-entity>

<a-entity scale=".2 .2 .2" position="1 0 0" rotation="-93 0 0"> 
  <a-entity gltf-model="models/7.glb" scale="8 8 8" crossOrigin="anonymous"></a-entity>
  <a-entity position="0 22 0">
    <a-text value="Izmael" align="center" color="white" width="35"></a-text>
  </a-entity>
</a-entity>
</a-marker>

<a-entity camera></a-entity>
</a-scene> */