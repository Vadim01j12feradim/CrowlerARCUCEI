
<!DOCTYPE html>
<html>  
  <head>
    <!-- <script src='https://aframe.io/releases/1.2.0/aframe.min.js'></script> -->
    <script src='./JS/aframe.min.js'></script>

    <!-- <script src='https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js'></script> -->
    <script src='./JS/aframe-ar.js'></script>
    <script src='JSProject/Grapics.js'></script>

  </head>   

  <body>
    <?php
        include_once('DB/conn.php');
        echo "<a-scene embedded arjs>
        <a-marker preset='Hiro'>
        <a-entity scale='.2 .2 .2' position='-1 0 0' rotation='-85 0 0'> 
          <a-entity gltf-model='models/7.glb' scale='8 8 8' crossOrigin='anonymous'></a-entity>
          <a-entity position='0 22 0'>
            <a-text value='Hello' align='center' color='white' width='35'></a-text>
          </a-entity>
        </a-entity>
        
        <a-entity scale='.2 .2 .2' position='0 0 0' rotation='-93 0 0'> 
          <a-entity position='0 8 3'>
            <a-text value='IAM' align='center' color='white' width='35'></a-text>
          </a-entity>
          <a-entity gltf-model='models/7.glb' scale='8 8 8' crossOrigin='anonymous'></a-entity>
          
        </a-entity>
        
        <a-entity scale='.2 .2 .2' position='1 0 0' rotation='-93 0 0'> 
          <a-entity gltf-model='models/7.glb' scale='8 8 8' crossOrigin='anonymous'></a-entity>
          <a-entity position='0 22 0'>
            <a-text value='Izmael' align='center' color='white' width='35'></a-text>t
          </a-entity>
        </a-entity>
        </a-marker>
        
        <a-entity camera></a-entity>
        </a-scene>";
    ?>
    <!-- <a-marker-camera preset='hiro'></a-marker-camera> -->
      </body>
    </html>