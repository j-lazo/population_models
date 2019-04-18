%%%-----Population with Cellular Automaton--------
% This program plots the results of several simulations under the same conditions
clear all
close all
clc

dir=cd;
total_num=10;
name='results/100x100_s1:2500_s2:2501_s3:2401_';
d1=importdata('results/100x100_s1:2500_s2:2501_s3:2401_0');

D=zeros(length(d1(:,1)),4,total_num);
t=0;
stop=1;

for x=1:total_num
    D(:,:,x)=importdata(strcat(name,int2str(x-1)));
end



A=zeros(length(d1(:,1)),6);

for i=1:length(d1(:,1))
    for j=1:total_num
    A(i,1)=mean([D(i,2,:)]);
    A(i,2)=std([D(i,2,:)]);
    A(i,3)=mean([D(i,3,:)]);
    A(i,4)=std([D(i,3,:)]);
    A(i,5)=mean([D(i,4,:)]);
    A(i,6)=std([D(i,4,:)]);
    end
end

figure(1)
plot(d1(:,1),A(:,1))
errorbar(d1(:,1),A(:,1),A(:,2))
hold on
plot(d1(:,1),A(:,3))
errorbar(d1(:,1),A(:,3),A(:,4))
hold on
plot(d1(:,1),A(:,5))
errorbar(d1(:,1),A(:,5),A(:,6))
grid on
legend('prey','predator 1','predator 2')
xlabel('Simulation Steps')
ylabel('Population')
save1=strcat(dir,name,'.png');
saveas(figure(1),save1);