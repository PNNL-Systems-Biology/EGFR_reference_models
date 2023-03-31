% Function plots time course of A431 model using MATLAB Simbiology implementation
% Place this function in current path and invoke from MATLAB command line.
% Make sure A431-ErbB-Chen_et_al_2008.sbproj is in current path also.
% Simbiology Toolbox must be installed.
function plot_timecourses(tsarray)

sbioloadproject A431-ErbB-Model-Chen_et_al_2008.sbproj;
feature('SimBioODEFcnHandles',1);

timeseriesObj=sbiosimulate(m1);
[T, Y, names] = sbiogetnamedstate(timeseriesObj);

%%      
%initial amount of ErbB1
c1 = sbioselect([m1], 'Type', 'species', 'Where', 'Notes', '==i', 'ErbB1'); 
EGFRt=get(c1,'InitialAmount');

%Calculate dynamic pErbB1 dimer number 
p2ErbB1= sbioselect(m1, 'Type', 'species', 'Where', 'Notes', 'regexpi', '2\(EGF:ErbB1\)#P');
b=get(p2ErbB1,{'name'});
n=length(b);
Y_p2erbb1=0;
Y_ind=[];
for i=1:n
  [t1,Y_ind] = sbiogetnamedstate(timeseriesObj, b(i));
  Y_p2erbb1=Y_p2erbb1+Y_ind;
end;

%Calculate dynamic pErbB1/ErbB2 heterodimer number
pErbB1ErbB2= sbioselect(m1, 'Type', 'species', 'Where', 'Notes', 'regexpi', '\(ErbB1:ErbB2\)#P');
a=get(pErbB1ErbB2,{'name'});
n=length(a);
Y_perbb1erbb2=0;
Y_ind=[];
for i=1:n
  [t1,Y_ind] = sbiogetnamedstate(timeseriesObj, a(i));
  Y_perbb1erbb2=Y_perbb1erbb2+Y_ind;
end;

%Calculate dynamic pErbB1/ErbB3 heterodimer number
pErbB1ErbB3= sbioselect(m1, 'Type', 'species', 'Where', 'Notes', 'regexpi', '(ErbB1:ErbB3\)#P');
a=get(pErbB1ErbB3,{'name'});
n=length(a);
Y_perbb1erbb3=0;
Y_ind=[];
for i=1:n
  [t1,Y_ind] = sbiogetnamedstate(timeseriesObj, a(i)); 
  Y_perbb1erbb3=Y_perbb1erbb3+Y_ind;
end;

%Calculate dynamic pErbB1/ErbB4 heterodimer number
pErbB1ErbB4= sbioselect(m1, 'Type', 'species', 'Where', 'Notes', 'regexpi', '(ErbB1:ErbB4\)#P');
a=get(pErbB1ErbB4,{'name'});
n=length(a);
Y_perbb1erbb4=0;
Y_ind=[];
for i=1:n
  [t1,Y_ind] = sbiogetnamedstate(timeseriesObj, a(i));
  Y_perbb1erbb4=Y_perbb1erbb4+Y_ind;
end;

%%
%initial amount of ERK
c55 = sbioselect([m1], 'Type', 'species', 'Where', 'Notes', '==i', 'ERK'); 
ERKt=get(c55,'InitialAmount');

%Calculate dynamic pERK number
ERKp= sbioselect([m1], 'Type', 'species', 'Where', 'Notes', 'regexpi', 'ERK#P#P');
a=get(ERKp,{'name'});
n=length(a);
Y_perk=0;
Y_ind=[];
for i=1:n
  [t1,Y_ind] = sbiogetnamedstate(timeseriesObj, a(i));
  Y_perk=Y_perk+Y_ind;
end;

%%
%initial amount of Akt
c107 = sbioselect([m1], 'Type', 'species', 'Where', 'Notes', '==i', 'AKT'); 
AKTt=get(c107,'InitialAmount');
    
%Calculate dynamic pAkt number
AKTp= sbioselect([m1], 'Type', 'species', 'Where', 'Notes', 'regexpi', 'AKT:P:P');
a=get(AKTp,{'name'}); 
n=length(a);
Y_pakt=0;
Y_ind=[];
for i=1:n
  [t2,Y_ind] = sbiogetnamedstate(timeseriesObj, a(i));
  Y_pakt=Y_pakt+Y_ind;
end;

%Plot 3 times
set(0,'DefaultAxesLineWidth',2,'DefaultAxesFontSize',12, ...
      'DefaultAxesFontWeight','bold');
figure;
subplot(3,1,1),plot(t1,(2*Y_p2erbb1+Y_perbb1erbb2+Y_perbb1erbb3+Y_perbb1erbb4),'b');
xlabel('time(min)');
%xlim([0 9000]);
ylabel('pEGFR [%]');
%ylim([0 10]);
hold on;

subplot(3,1,2),plot(t1,(Y_perk),'Color',[ 0 1 0 ],...
    'MarkerFaceColor',[0 0 1],'Color',[0 1 0],'LineWidth',1,'Markersize',3);
xlabel('time(min)');
%xlim([0 9000]);
ylabel('pErk [%]');
%ylim([0 10]);

subplot(3,1,3),plot(t1,(Y_pakt),'Color',[1 0 0]);
xlabel('time(min)');
%xlim([0 9000]);
ylabel('pAkt [%]');
%ylim([0 10]);
hold on;

