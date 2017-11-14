function initImageLoop( images, modelVar, datetimeId, sliderId ) {
   // Make a list of dates of all images
   var regexDateTime=/_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})(_UTC)?\./;
   var dateTimes = new Array(images.length);
   for( var i=0; i<images.length; ++i) {
      var res = regexDateTime.exec(images[i]);
      if( res != null ) {
         dateTimes[i] = res[1]+'-'+res[2]+'-'+res[3]+' '+res[4]+':'+res[5]+':'+res[6]+' UTC';
      } else {
         dateTimes[i] = i+1;
      }
   }

   var il = new ImageLoop(images, modelVar, dateTimes, datetimeId, sliderId, 500);

   document.getElementById(datetimeId).innerHTML = "Date/time: "+dateTimes[il.index];
   return il;
}

// Object that manages the animation
function ImageLoop( images, modelVar, dateTimes, datetimeId, sliderId, speed ) {
   this.images    = images;
   this.dateTimes = dateTimes;
   this.speed     = speed;
   this.interval  = false;
   this.play      = false;
   this.index     = 0;
   this.idxStart  = 0;
   this.idxEnd    = images.length - 1;
   this.direction = "forward";

   function preloadImages() {
      for (i in this.images) {
         var img = new Image();
         img.src = this.images[i];
      }
   }
   preloadImages();

   var thisObj = this;
   function onInterval() {
      if( thisObj.direction == "forward" ) {
         thisObj.next();
      } else {
         thisObj.previous();
      }
   }

   function setIndex(index) {
      var im = document.getElementById(modelVar);
      im.src = images[index];
      this.index = index;
      document.getElementById(datetimeId).innerHTML = "Date/time: " + this.dateTimes[index];
      if( this.sl ) {
         this.sl.setIndex('handle', index);
      }
   }

   function next() {
      var idx = (this.index < this.idxEnd) ? this.index+1 : this.idxStart;
      if (this.play) {
         this.setIndex(idx);
      }
      return idx;
   }

   function previous() {
      var idx = (this.index > this.idxStart) ? this.index-1 : this.idxEnd;
      if (this.play) {
         this.setIndex(idx);
      }
      return idx;
   }

   function start() {
      this.play = true;
      if (!this.interval) {
         this.interval = setInterval(onInterval, this.speed);
      }
   }

   function stop() {
      this.play = false;
      if (this.interval) {
         clearInterval(this.interval);
         this.interval = null;
      }
   }

   function changeSpeed( adjust ) {
      this.speed += adjust;
      clearInterval(this.interval);
      this.interval = setInterval(onInterval, this.speed);
   }

   function goto( place ) {
      this.stop();
      var idx;

      switch (place) {
         case "beginning":
            idx = this.idxStart;
            break;
         case "left":
            idx = this.previous();
            break;
         case "right":
            idx = this.next();
            break;
         case "end":
            idx = this.idxEnd;
            break;
      }

      this.setIndex(idx);
   }


   function toggleDirection() {
      this.direction = (this.direction == "forward") ? "backward" : "forward";
      return this.direction;
   }

   // Setup
   var d = document.getElementById(modelVar+"_image_loop_canvas");
   d.innerHTML = "<img src='" + this.images[this.index] + "' id='" + modelVar + "' class='img-responsive' />";

   // Add Functions
   this.preloadImages = preloadImages;
   this.setIndex = setIndex;
   this.next = next;
   this.previous = previous;
   this.start = start;
   this.stop = stop;
   this.changeSpeed = changeSpeed;
   this.goto = goto;
   this.toggleDirection = toggleDirection;
   this.sl = new Slider(sliderId, this, images.length-1);
}

// Slider Object
function Slider(container, il, maxIdx) {
   // dimensions (pixels)
   this.sliderHeight   = 15;
   this.sliderWidth    = 500;
   this.handleWidth    = 6;
   this.handleBorder   = 2;
   this.trackThickness = 3;

   this.il = il;
   this.sliderMinIdx   = 0;
   this.sliderMaxIdx   = maxIdx;
   this.targetInitPos  = -1;
   this.items          = {};
   this.idxs           = { 'handle':-1, 'borneMin':-1, 'borneMax':-1 };
   this.target         = "";
   this.mousedown      = 0;

   this.fitInto = function(value, min, max) {
      return value<min ? min : (value>max ? max : value);
   }

   this.style2value = function(style) {
      var pos = parseInt(style);
      return isNaN(pos) ? 0 : pos;
   }

   this.adjustPos = function(item, pos, how) {
      // Ajust pos in function of the width of the item (center it)
      var width  = this.style2value(this.items[item].style.width);
      var border = this.style2value(this.items[item].style.borderWidth);

      if( how == 'plus' ) {
         return pos + Math.round( (width+border)/2 );
      } else {
         return pos - Math.round( (width+border)/2 );
      }
   }

   this.setPos = function(item, pos) {
      this.items[item].style.left = this.adjustPos(item, pos, 'minux')+'px';
   }

   this.setIndex = function(item, idx) {
      if( idx<this.sliderMinIdx || idx>this.sliderMaxIdx ) {
         return;
      }

      var pos = Math.round((idx-this.sliderMinIdx)/(this.sliderMaxIdx-this.sliderMinIdx) * this.sliderWidth);
      this.setPos(item, pos);

      if( idx != this.idxs[item] ) {
         this.idxs[item] = idx;
         this.il.setIndex(idx);
      }
   }

   this.init = function(container) {
      // Define dimensions of the slider

      // Generate slider components
      var div = '<div id="'+container+'_track"></div>\n';
         div += '<div id="'+container+'_borneMin"></div>\n';
         div += '<div id="'+container+'_borneMax"></div>\n';
         div += '<div id="'+container+'_handle"></div>\n';

      // Slider (container)
      var slider = document.getElementById(container);
      slider.innerHTML        = div;
      slider.style.height     = this.sliderHeight+'px';
      slider.style.width      = this.sliderWidth+'px';
      slider.style.position   = 'relative';
      slider.style.padding    = '0px';

      // Slider track
      var track = document.getElementById(container+'_track');
      track.style.width             = this.sliderWidth+'px';
      track.style.height            = this.trackThickness+'px';
      track.style.backgroundColor   = '#000000';
      track.style.padding           = '0px';
      track.style.position          = 'absolute';
      track.style.top               = ((this.sliderHeight-this.trackThickness)/2+this.handleBorder)+'px';
      track.style.left              = '0px';

      // Slider handle
      var handle = document.getElementById(container+'_handle');
      handle.style.height           = this.sliderHeight+'px';
      handle.style.width            = this.handleWidth+'px';
      handle.style.borderWidth      = this.handleBorder+'px';
      handle.style.borderStyle      = 'outset';
      handle.style.borderColor      = '#999999 #666666 #666666 #999999';
      handle.style.backgroundColor  = '#888888';
      handle.style.position         = 'absolute';
      handle.style.top              = '0px';

      // Slider min indicator
      var borneMin = document.getElementById(container+'_borneMin');
      borneMin.style.height            = this.sliderHeight+'px';
      borneMin.style.width             = '2px';
      borneMin.style.position          = 'absolute';
      borneMin.style.top               = this.handleBorder+'px';
      borneMin.style.backgroundColor   = '#000000';

      // Slider max indicator
      var borneMax = document.getElementById(container+'_borneMax');
      borneMax.style.height            = this.sliderHeight+'px';
      borneMax.style.width             = '2px';
      borneMax.style.position          = 'absolute';
      borneMax.style.top               = this.handleBorder+'px';
      borneMax.style.backgroundColor   = '#000000';

      // Place structures into 'items'
      this.items['slider']   = slider;
      this.items['track']    = track;
      this.items['handle']   = handle;
      this.items['borneMin'] = borneMin;
      this.items['borneMax'] = borneMax;

      this.setIndex('handle', 0);
      this.setIndex('borneMin', 0);
      this.setIndex('borneMax', maxIdx);
   }
   this.init(container);
}
