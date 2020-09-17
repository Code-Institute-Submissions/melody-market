var picPaths = [
                'media/elguitar1.jpg',
                'media/acguitar1.jpg',
                'media/flute.jpg',
                'media/keyboard.jpg',
                'media/sax.jpg',
                'media/acguitar6.jpg',
                'media/piano6.jpg',
                'media/marimba.jpg',
                ];

function selectedPicks() {

Array.prototype.shuffle = function() {
        var s = [];
        while (this.length) s.push(this.splice(Math.random() * this.length, 1));
        while (s.length) this.push(s.pop());
        return this;}

picPaths.shuffle();

picO = new Array();

for(i=0; i < picPaths.length; i++){
    picO[i] = new Image();
    picO[i].src = picPaths[i];
    }



window.onload=function(){
                
var mainImgs = document.getElementById('feature-pics').getElementsByTagName('img');
    for(i=0; i < mainImgs.length; i++){
        mainImgs[i].src = picO[i].src;
        }
    }
}

selectedPicks();

/*                
var features = new Array('media/acguitar1.jpg','media/acguitar6.jpg','media/elguitar1.jpg','media/keyboard.jpg','media/piano6.jpg')

function choosePic1() {
     var randomNum = Math.floor(Math.random() * features.length);
     document.getElementById("feature1").src = features[randomNum];
    }

function choosePic2() {
     var randomNum = Math.floor(Math.random() * features.length);
     document.getElementById("feature2").src = features[randomNum];
    }

function choosePic3() {
     var randomNum = Math.floor(Math.random() * features.length);
     document.getElementById("feature3").src = features[randomNum];
    }

window.onload = function() {
    var img1 = choosePic1() ;
    var img2 = choosePic2() ;
    var img3 = choosePic3() ;
}

*/
