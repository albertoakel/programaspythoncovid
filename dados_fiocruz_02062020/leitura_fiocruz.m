close all
%read files covid- fiocruz

% CA1=table2array(C1);
% CA2=table2array(C2);
% CA3=table2array(C3);

% CN1=table2array(C1(:,2:end))
% CN2=table2array(C2(:,2:end))
% CN3=table2array(C3(:,2:end))
% % 
 
% temp(1:85,[2:11])=CN1(:,1:10);
% temp(1:87,[12:21])=CN2(:,1:10);
% temp(1:91,[22:28])=CN3(:,1:7);
% 
% Estados=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA", ...
%     "MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS",...
%     "RO","RR","SC","SP","SE","TO"]

ON1=obitos_novos(1:85,[2:11])
ON2=obitos_novos(1:87,[12:21])
ON3=obitos_novos(1:91,[22:28])

temp=zeros(91,28);
temp(1:91,1)=[1:91];

temp(1+6:85+6,[2:11])=ON1(:,1:10)
temp(1+4:87+4,[12:21])=ON2(:,1:10)
temp(1:91,[22:28])=ON3(:,1:7)
