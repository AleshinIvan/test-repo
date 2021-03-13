close all
clear variables
spectra = importdata('spectra.csv');
lambdaStart = importdata('lambda_start.csv');
lambdaDelta = importdata('lambda_delta.csv');
starNames = importdata("star_names.csv");

lambdaPr = 656.28; %нм
speedOfLight = 299792.458; %км/c

nObs = size(spectra, 1);
nStars = size(starNames, 1);
lambdaEnd = lambdaStart + (nObs - 1) * lambdaDelta;
lambda = (lambdaStart : lambdaDelta : lambdaEnd)';

[sHa, idx] = min(spectra);
lamdaHa = lambda(idx);

z = (lamdaHa / lambdaPr) - 1;
speed = z * speedOfLight;
movaway = starNames(speed > 0);

fg1 = figure;
hold on;
for i = 1:nStars
if speed(i)>0
plot(lambda, spectra(:,i), 'LineWidth', 3);
else
plot(lambda, spectra(:,i), "--", 'LineWidth', 1);
end 
end
hold off
set(fg1, 'visible', 'on');
xlabel('Длина волны, нм');
ylabel(['Интенсивность, эрг/см^2/с/', char(197)]);
title('Спектры здёзд');
text(lambdaEnd - 45, max(spectra(:, 1)), 'Алешин Иван Б04-006');
legend(starNames);
grid on;
saveas(fg1, 'spectra.png');