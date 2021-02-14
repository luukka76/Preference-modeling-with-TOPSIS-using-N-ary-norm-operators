function mu=i_bd(a,b,w)
mu=1-min([1,((1-a)^w+(1-b)^w)^(1/w)]);
