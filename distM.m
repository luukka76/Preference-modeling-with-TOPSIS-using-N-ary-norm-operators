function d=distM(x,y,p)
[m,n]=size(x);
d=1/n*(sum(abs(x-y ).^p).^(1/p));