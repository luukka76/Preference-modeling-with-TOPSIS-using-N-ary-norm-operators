function [c,Dplus,Dminus]=topsis(data,p,w,w2,crit)
x=data;
[m,n]=size(x);
a=zeros(m,n);
%Normalization to unit interval:
a=normalization(x);

%Positive and negative ideal solutions:
PIS=zeros(1,n);
NIS=zeros(1,n);
for j=1:n
     if crit(j)==1   
        PIS(j)=recursivetconorm(a(:,j)',w);
        NIS(j)=recursivetnorm(a(:,j),w2);
     else
        NIS(j)=recursivetconorm(a(:,j)',w);
        PIS(j)=recursivetnorm(a(:,j),w2);    
     end
end

%Distances to PIS and NIS
 DPISB=zeros(1,m);
 DNISB=zeros(1,m);
for i=1:m
   Dplus(i)=distM(PIS,a(i,:),p); 
   Dminus(i)=distM(NIS,a(i,:),p); 
end
%Closeness coefficient: 
 c=zeros(1,m);
 for i=1:m
     c(i)=Dminus(i)/(Dplus(i)+Dminus(i));
 end
