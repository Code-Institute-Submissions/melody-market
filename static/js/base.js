var picPaths = [
                'media/elguitsale1.jpg',
                'media/elguitsale2.jpg',
                'media/keysale1.jpg',
                'media/keysale2.jpg',
                'media/banjo.jpg',
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
