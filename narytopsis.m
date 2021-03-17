function [c,Dplus,Dminus]=topsis(data,p,w,w2,crit,we)
x=data;
[m,n]=size(x);
if nargin<6
we=ones(1,n);
elseif nargin<5
crit=ones(1,n);
end

a=zeros(m,n);
%Normalization to unit interval:
%a=normalization(x);
a=normalize(x,'range'); %matlab's own normalization function
%weigted normalized decision matrix:
r=we.*a;
%Positive and negative ideal solutions:
PIS=zeros(1,n);
NIS=zeros(1,n);
for j=1:n
     if crit(j)==1   
        PIS(j)=recursivetconorm(r(:,j)',w);
        NIS(j)=recursivetnorm(r(:,j),w2);
     else
        NIS(j)=recursivetconorm(r(:,j)',w);
        PIS(j)=recursivetnorm(r(:,j),w2);    
     end
end

%Distances to PIS and NIS
 DPISB=zeros(1,m);
 DNISB=zeros(1,m);
for i=1:m
   Dplus(i)=distM(PIS,r(i,:),p); 
   Dminus(i)=distM(NIS,r(i,:),p); 
end
%Closeness coefficient: 
 c=zeros(1,m);
 for i=1:m
     c(i)=Dminus(i)/(Dplus(i)+Dminus(i));
 end
