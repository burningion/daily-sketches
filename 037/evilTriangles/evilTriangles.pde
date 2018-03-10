// barely modified from bees and bombs to fit video resolution
// https://gist.github.com/beesandbombs/78bdf5e42cc70d8bcca2cd29c66566a3
int[][] result;
float t, c;

float ease(float p) {
  return 3*p*p - 2*p*p*p;
}

float ease(float p, float g) {
  if (p < 0.5) 
    return 0.5 * pow(2*p, g);
  else
    return 1 - 0.5 * pow(2*(1 - p), g);
}

float mn = .5*sqrt(3), ia = atan(sqrt(.5));

void push() {
  pushMatrix();
  pushStyle();
}

void pop() {
  popStyle();
  popMatrix();
}

float c01(float g) {
  return constrain(g, 0, 1);
}

void draw() {

  if (!recording) {
    t = mouseX*1.0/width;
    c = mouseY*1.0/height;
    if (mousePressed)
      println(c);
    draw_();
  } else {
    for (int i=0; i<width*height; i++)
      for (int a=0; a<3; a++)
        result[i][a] = 0;

    c = 0;
    for (int sa=0; sa<samplesPerFrame; sa++) {
      t = map(frameCount-1 + sa*shutterAngle/samplesPerFrame, 0, numFrames, 0, 1);
      draw_();
      loadPixels();
      for (int i=0; i<pixels.length; i++) {
        result[i][0] += pixels[i] >> 16 & 0xff;
        result[i][1] += pixels[i] >> 8 & 0xff;
        result[i][2] += pixels[i] & 0xff;
      }
    }

    loadPixels();
    for (int i=0; i<pixels.length; i++)
      pixels[i] = 0xff << 24 | 
        int(result[i][0]*1.0/samplesPerFrame) << 16 | 
        int(result[i][1]*1.0/samplesPerFrame) << 8 | 
        int(result[i][2]*1.0/samplesPerFrame);
    updatePixels();

    saveFrame("f###.png");
    if (frameCount==numFrames)
      exit();
  }
}

//////////////////////////////////////////////////////////////////////////////

int samplesPerFrame = 12;
int numFrames = 360;        
float shutterAngle = 1;

boolean recording = true;

void setup() {
  size(1280, 720, P3D);
  smooth(8);
  result = new int[width*height][3];
  rectMode(CENTER);
  fill(255);
  noStroke();
  blendMode(EXCLUSION);
}

float x, y, z, tt;
int N = 22;
float r = 60, sp = 2*r*mn;

PImage f1, f2, f3;

void tri(){
  beginShape();
  for(int i=0; i<3; i++)
    vertex(r*sin(TWO_PI*i/3), r*cos(TWO_PI*i/3));
  endShape();
}

void drawTris(){
  for (int i=-N; i<N; i++) {
    for (int j=-N; j<N; j++) {
      x = i*sp;
      y = j*mn*sp;
      if(j%2 != 0)
        x += .5*sp;
      push();
      translate(x,y);
      rotate(HALF_PI);
      scale(pow(2,0.5+0.5*cos(TWO_PI*t - 0.01*dist(x,y,0,0))));
      tri();
      pop();
    }
  }
}

void draw_() {
  blendMode(EXCLUSION);
  background(0); 
  push();
  translate(width/2, height/2);
  rotate(-HALF_PI);
  
  drawTris();
  f1 = get();
  
  background(0);
  push();
  scale(1.006);
  drawTris();
  pop();
  f2 = get();
  
  background(0);
  push();
  scale(1.012);
  drawTris();
  pop();
  f3 = get();
  
  pop();
  
  background(0);
  loadPixels();
  f1.loadPixels();
  f2.loadPixels();
  f3.loadPixels();
  
  for(int i=0; i<pixels.length; i++)
    pixels[i] = color(20+.9*red(f1.pixels[i]),20+.9*green(f2.pixels[i]),20+.9*blue(f3.pixels[i]));
  updatePixels();
}