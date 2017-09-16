// Make sure the start and end date are consistent with one another
function updateStartEnd() {
   var start = document.getElementById('indexStart');
   var end   = document.getElementById('indexEnd');
   var from  = start.selectedIndex;
   var to    = end.selectedIndex;

   // Ultimate check because some browsers don't disable options...
   if( from > to ) {
      alert("The starting date must be prior to the end date.");
      start.selectedIndex = il.idxStart;
      end.selectedIndex = il.idxEnd; 
      return;
   }

   // Disable all unwanted options
   for(var i=0; i<dateTimes.length; ++i) {
      // Prevent user from selecting a starting date after the end date.
      start.options[i].disabled = (i > to) ? true : false;

      // Prevent user from selecting an end date prior to the starting date.
      end.options[i].disabled = (i < from) ? true : false;
   }

   il.setStartEnd(from, to);
   if( sl ) {
      sl.setIndex('borneMin', from);
      sl.setIndex('borneMax', to);
   }
}


function initImageLoop(images) {
   // Set our global object 'il' to be an image loop
   // varname = new ImageLoop(imagesArray, intervalInMilliseconds);
   il = new ImageLoop(images, 500);

   // Make a list of dates of all images (used by indexStart and indexEnd)
   // and add it as options for start/end index
   var regexDateTime=/_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})(_UTC)?\./;
   var start = document.getElementById('indexStart').options;
   var end   = document.getElementById('indexEnd').options;
   dateTimes = new Array(images.length);
   var opt = null;
   for( var i=0; i<images.length; ++i) {
      if( imgType == "dateTimes" ) {
         var res = regexDateTime.exec(images[i]);
         if( res != null ) {
            dateTimes[i] = res[1]+'-'+res[2]+'-'+res[3]+' '+res[4]+':'+res[5]+':'+res[6]+' UTC';
         } else {
            if( i == 0 ) {
               imgType = "unknown";
            }
            dateTimes[i] = i+1;
         }
      } else {
         dateTimes[i] = i+1;
      }

      var opt = document.createElement('option');
      opt.text = dateTimes[i];
      start[i] = opt;

      opt = document.createElement('option');
      opt.text = dateTimes[i];
      end[i] = opt;
   }
   start.selectedIndex = 0;
   end.selectedIndex = dateTimes.length - 1;

   sl = new Slider('slider', images.length-1);

   il.setStartEnd(start.selectedIndex, end.selectedIndex);
   if( imgType == "dateTimes" ) {
      document.getElementById('datetime').innerHTML = "Date/time: "+dateTimes[il.index];
   } else {
      document.getElementById('datetime').innerHTML = "Image #"+dateTimes[il.index]+' : '+images[il.index];
   }
}

// Object that manages the animation
function ImageLoop( images, speed ) {
   this.images    = images;
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

   thisObj = this;
   function onInterval() {
      if( thisObj.direction == "forward" ) {
         thisObj.next();
      } else {
         thisObj.previous();
      }
   }

   function setIndex(index) {
      var im = document.getElementById("imageloop");
      im.src = images[index];
      this.index = index;
      if( imgType == "dateTimes" ) {
         document.getElementById('datetime').innerHTML = "Date/time: "+dateTimes[index];
      } else {
         document.getElementById('datetime').innerHTML = "Image #"+dateTimes[index]+' : '+images[index];
      }
      if( sl ) {
         sl.setIndex('handle', index);
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

   function setStartEnd(Start, End) {
      this.idxStart  = (Start>=0 && Start<this.images.length) ? Start : 0;
      this.idxEnd    = (End>=0 && End<this.images.length) ? End : this.images.length-1;

      if( this.index < this.idxStart ) {
         this.setIndex(this.idxStart);
      } else if( this.index > this.idxEnd ) {
         this.setIndex(this.idxEnd);
      }
   }

   function toggleDirection() {
      this.direction = (this.direction == "forward") ? "backward" : "forward";
      return this.direction;
   }

   // Setup
   var d = document.getElementById("il"); 
   d.innerHTML = "<img src='" + this.images[this.index] + "' id='imageloop' class='img-responsive' />";

   // Add Functions
   this.preloadImages = preloadImages;
   this.setIndex = setIndex;
   this.next = next;
   this.previous = previous;
   this.start = start;
   this.stop = stop;
   this.changeSpeed = changeSpeed;
   this.goto = goto;
   this.setStartEnd = setStartEnd;
   this.toggleDirection = toggleDirection;
}

// Slider Object
function Slider(container, maxIdx) {
   // dimensions (pixels)
   this.sliderHeight   = 15;
   this.sliderWidth    = 500;
   this.handleWidth    = 6;
   this.handleBorder   = 2;
   this.trackThickness = 3;

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

   this.getPos = function(item) {
      return this.adjustPos(item, this.style2value(this.items[item].style.left), 'plus');
   }

   this.setIndex = function(item, idx) {
      if( idx<this.sliderMinIdx || idx>this.sliderMaxIdx ) {
         return;
      }

      var pos = Math.round((idx-this.sliderMinIdx)/(this.sliderMaxIdx-this.sliderMinIdx) * this.sliderWidth);
      this.setPos(item, pos);

      if( idx != this.idxs[item] ) {
         this.idxs[item] = idx;
         switch(item) {
            case 'handle' :
               il.setIndex(idx);
               break;
            case 'borneMin' :
               document.getElementById('indexStart').selectedIndex = idx;
               updateStartEnd();
               break;
            case 'borneMax' :
               document.getElementById('indexEnd').selectedIndex = idx;
               updateStartEnd();
               break;
         }
      }
   }

   this.pos2idx = function(pos, option) {
      var idx = pos/this.sliderWidth * (this.sliderMaxIdx-this.sliderMinIdx) + this.sliderMinIdx;

      if( option ) {
         switch(option) {
            case 'forceHigh' :
               idx = Math.round(idx + 0.5);
               break;
            case 'forceLow' :
               idx = Math.round(idx - 0.5);
               break;
         }
      } else {
         idx = Math.round(idx);
      }

      return this.fitInto(idx, this.sliderMinIdx, this.sliderMaxIdx);
   }

   this.getRevisedPos = function(item, pos) {
      var max = this.getPos('borneMax');
      var min = this.getPos('borneMin');

      switch(item) {
         case 'handle' :
            // Make sure handle is between min and max
            pos = this.fitInto(pos, min, max);
            break;
         case 'borneMin' :
            // Make sure the min and max are not inversed
            pos = (pos>max) ? max : pos;
            break;
         case 'borneMax' :
            // Make sure the min and max are not inversed
            pos = (pos<min) ? min : pos;
            break;
      }

      return pos;
   }

   this.onMouseDown = function(e, item) {
      il.stop();

      // stop event bubbling
      if( e.stopPropagation != null ) {
         e.stopPropagation();
      } else {
         e.cancelBubble = true;
      }

      this.mousedown = 1;
      this.target = item;
      // Pos is relative to screenX because it seems to be the only coherent cross-platform coordinate.
      this.targetInitPos = this.getPos(this.target) - e.screenX;
   }

   this.onMouseUp = function(e) {
      if( this.mousedown ) {
         this.mousedown = 0;

         if( this.target != "" ) {
            // Find target's revised new position
            var newPos = this.fitInto(this.targetInitPos+e.screenX, 0, this.sliderWidth);
            newPos = this.getRevisedPos(this.target, newPos);

            // snap the target back to nearest tick
            this.setIndex(this.target, this.pos2idx(newPos));
            
            this.target = "";
         }
      }
   }

   this.onMouseMove = function(e) {
      if(!e || !this.mousedown || this.target=="" ) {
         return
      }

      // find new target position
      var newPos = this.fitInto(this.targetInitPos+e.screenX, 0, this.sliderWidth);
      newPos = this.getRevisedPos(this.target, newPos);

      switch(this.target) {
         case 'handle' :
            // Adjust animation index
            var idx = this.pos2idx(newPos);
            if( idx != this.idxs['handle'] ) {
               il.setIndex(idx);
               this.idxs['handle'] = idx;
            }
            break;
         case 'borneMin' :
            // Make the handle follow (handle can't be left of borneMin)
            var handle = this.getPos('handle');
            if( handle < newPos ) {
               this.setIndex('handle', this.pos2idx(newPos, 'forceHigh'));
            }
            break;
         case 'borneMax' :
            // Make the handle follow (handle can't be left of borneMin)
            var handle = this.getPos('handle');
            if( handle > newPos ) {
               this.setIndex('handle', this.pos2idx(newPos, 'forceLow'));
            }
            break;
      }

      this.setPos(this.target, newPos);
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

      // bind events to components
      var mysl = this;
      handle.onmousedown = function(e) { e=e||event; mysl.onMouseDown(e, 'handle'); };
      borneMin.onmousedown = function(e) { e=e||event; mysl.onMouseDown(e, 'borneMin'); };
      borneMax.onmousedown = function(e) { e=e||event; mysl.onMouseDown(e, 'borneMax'); };
      var body = document.getElementsByTagName('body')[0];
      body.onmousemove = function(e) { e=e||event; mysl.onMouseMove(e); };
      body.onmouseup = function(e) { e=e||event; mysl.onMouseUp(e); };

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
