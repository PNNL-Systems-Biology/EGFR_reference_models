Last update: 09/08/2008
william_chen@hms.harvard.edu

In this archive, there are several files that make up the ErbB model of A431 cell line.

1  ErbB-Chen_et_al_2008-A431.xml  -  An SBML implementation.
2  ErbB-Chen_et_al_2008-A431.sbproj  -  The MATLAB Simbiology implementation.
3  stepfunc.m  -  A required file for the model (see below).  This one is a MATLAB implementation.
4  ErbB-Chen_et_al_2008-A431-RunModelScript.m  -  A simple script to run the MATLAB implementation.
5  README.txt  -  This file.
6  ErbB-Chen_et_al_2008-A431-norules.xml - An SBML implementation with no rules (see below).

In addition, the SBML model A431-ErbB-Model-Chen_et_al_2008.xml requires one 
externally defined function to run.  The function is called 'stepfunc' in 
the SBML model file, but the implementation will vary between 
integrators/simulators/systems.  'Stepfunc' is a way of turning on parameters 
mid-simulation, and mimics experimental or biological effects that are external 
to the ErbB system, e.g. addition of an inhibitor during the time course.

Note: If the modeling platform is not expressive enough to support the 
'stepfunc' function, there is also an SBML version 
'ErbB-Chen_et_al_2008-A431-norules.xml' that does not contain such a function 
which user can try.  The drawback of using this version is that one cannot 
simulate preincubation of the system an inhibitor; otherwise, the output 
between this version of the full SBML version is almost identical.  This SBML
has been tested in MATLAB Simbiology, and COPASI.  In COPASI, although
there are errors about 'boundary conditions' of species that are displayed
during loading, the model will run fine.

The stepfunc function can be defined in meta-code as follows:
  stepfunc(time, time_start, val_start, time_end, val_end)
'time' is the time point of a simulation at which the function is called.
'Time_start' and 'time_end' define the period of time between which the value 
of the function changes from 'val_start' to 'val_end'.  Before 'time_start', 
the function returns 'val_start', and after 'time_end', the function returns 
'val_end'.  In between, 'stepfunc' will find an interpolated value.  This 
prescription is similar to a Heaviside function.

An implementation of 'stepfunc' in MATLAB is given here.  The sine function
is used to turn the return value from 'val_start' to 'val_end'

%BEGIN STEPFUNC
function y = stepfunc(time , time_start, val_start, time_end, val_end)
%STEPFUNC Step function
%

%   Copyright 2004-2006 The MathWorks, Inc.
%   $Revision: 1.1.4.2 $  $Date: 2005/07/02 04:51:02 $
%   Special SimBiology function.

if (nargin ~= 5)
    error('SimBiology:INVALID_INPUT_STEPFUNC',...
          'sbiostepf requires five arguments and all are mandatory');
end

if (~isnumeric(time))
    error('SimBiology:INVALID_FIRST_ARGUMENT',...
          'The first argument to stepfunc must be a valid MATLAB expression');
end

if (~isnumeric(time_start) || ~isnumeric(val_start) || ~isnumeric(time_end) || ~isnumeric(val_end))
    error('SimBiology:INVALID_ARGUMENT_TYPE',...
          'The last four arguments time_start, val_start, time_end, val_end must be all numeric');
end

if (length(time_start) ~= 1 || length(val_start) ~= 1 || length(time_end) ~= 1 || length(val_end) ~= 1)
    error('SimBiology:INVALID_ARGUMENT_LENGTH',...
          'The last four arguments time_start, val_start, time_end, val_end must be all scalars');
end

% Compute the value of y
if (time < time_start)
    y = val_start;
elseif (time > time_end)
    y = val_end;
else
    y = ((val_start+val_end)/2) + ((val_end-val_start)/2)*sin((pi/2)*(2*time-time_end-time_start)/(time_end-time_start));
end
%END STEPFUNC
