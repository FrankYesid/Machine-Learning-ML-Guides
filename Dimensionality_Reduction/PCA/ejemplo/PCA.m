%% Ejemplo de PCA
clear all; clc

X = rand(10,20); % La señal de 5 canales R(NxP).

% Paso 1. Centralizamos la señal.
Xm = mean(X,2);
X_ = X-Xm;

% Paso 2. Matriz de correlación
R = X_'*X_;

% Paso 3. Matriz de covarianza.
S = (1/size(X_,1))*R;

% Paso 4. Se puede hacer descomposición en valores singulares (SVD)
