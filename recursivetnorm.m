function inorm=tnormstandardn(A,w)
[n,m]=size(A);
inorm=i_yager(A(1),A(2),w);
for i=2:n
    inorm=i_yager(A(i),inorm,w);
end
