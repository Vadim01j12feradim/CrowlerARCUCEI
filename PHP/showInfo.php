<!DOCTYPE html>
<html>  
  <head>
    <!-- <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script> -->
    <script src="../JS/aframe.min.js"></script>

    <!-- <script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script> -->
    <script src="../JS/aframe-ar.js"></script>

  </head>   

  <body>
    <?php
      $data = $_GET['data'];
      $data = json_decode($data, true);
    ?>
    <a-scene embedded arjs>
      <a-marker preset="hiro">
      <a-entity scale=".2 .2 .2" position="-1 0 0" rotation="-85 0 0"> 
        <a-entity gltf-model="../models/7.glb" scale="9 9 9" crossOrigin="anonymous"></a-entity>
        <a-entity position="0 22 0">
          <a-text value="<?php echo $data['Clave']; ?>" align="center" color="white" width="35"></a-text>
        </a-entity>
      </a-entity>
    
      <a-entity scale=".2 .2 .2" position="0 0 0" rotation="-93 0 0"> 
        <a-entity position="0 8 3">
          <a-text value="<?php echo $data['Materia']; ?>" align="center" color="white" width="35"></a-text>
        </a-entity>
        <a-entity gltf-model="../models/7.glb" scale="9 9 9" crossOrigin="anonymous"></a-entity>
        
      </a-entity>

      <a-entity scale=".2 .2 .2" position="1 0 0" rotation="-93 0 0"> 
        <a-entity gltf-model="../models/7.glb" scale="9 9 9" crossOrigin="anonymous"></a-entity>
        <a-entity position="0 22 0">
          <a-text value="<?php echo $data['NombreTeacher']; ?>" align="center" color="white" width="35"></a-text>
        </a-entity>
      </a-entity>
    </a-marker>

    <a-entity camera></a-entity>
    
      <!-- <a-marker-camera preset='hiro'></a-marker-camera> -->
    </a-scene>
    
      </body>
    </html>
