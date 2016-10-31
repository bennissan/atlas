#!/bin/bash
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM LinearHardTraining LinearHardTestingAll Results/LinearHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM LinearHardTraining LinearHardTestingSignal Results/LinearHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM LinearHardTraining LinearHardTestingBackground Results/LinearHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM LinearSoftTraining LinearSoftTestingAll Results/LinearSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM LinearSoftTraining LinearSoftTestingSignal Results/LinearSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM LinearSoftTraining LinearSoftTestingBackground Results/LinearSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestCircleHardTraining TestCircleHardTestingAll Results/CircleHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestCircleHardTraining TestCircleHardTestingSignal Results/CircleHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestCircleHardTraining TestCircleHardTestingBackground Results/CircleHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestCircleSoftTraining TestCircleSoftTestingAll Results/CircleSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestCircleSoftTraining TestCircleSoftTestingSignal Results/CircleSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestCircleSoftTraining TestCircleSoftTestingBackground Results/CircleSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoCircleHardTraining TestTwoCircleHardTestingAll Results/TwoCircleHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoCircleHardTraining TestTwoCircleHardTestingSignal Results/TwoCircleHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoCircleHardTraining TestTwoCircleHardTestingBackground Results/TwoCircleHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoCircleSoftTraining TestTwoCircleSoftTestingAll Results/TwoCircleSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoCircleSoftTraining TestTwoCircleSoftTestingSignal Results/TwoCircleSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoCircleSoftTraining TestTwoCircleSoftTestingBackground Results/TwoCircleSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM PlaneHardTraining PlaneHardTestingAll Results/PlaneHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM PlaneHardTraining PlaneHardTestingSignal Results/PlaneHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM PlaneHardTraining PlaneHardTestingBackground Results/PlaneHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM PlaneSoftTraining PlaneSoftTestingAll Results/PlaneSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM PlaneSoftTraining PlaneSoftTestingSignal Results/PlaneSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM PlaneSoftTraining PlaneSoftTestingBackground Results/PlaneSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestSphereHardTraining TestSphereHardTestingAll Results/SphereHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestSphereHardTraining TestSphereHardTestingSignal Results/SphereHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestSphereHardTraining TestSphereHardTestingBackground Results/SphereHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestSphereSoftTraining TestSphereSoftTestingAll Results/SphereSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestSphereSoftTraining TestSphereSoftTestingSignal Results/SphereSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestSphereSoftTraining TestSphereSoftTestingBackground Results/SphereSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoSphereHardTraining TestTwoSphereHardTestingAll Results/TwoSphereHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoSphereHardTraining TestTwoSphereHardTestingSignal Results/TwoSphereHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoSphereHardTraining TestTwoSphereHardTestingBackground Results/TwoSphereHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoSphereSoftTraining TestTwoSphereSoftTestingAll Results/TwoSphereSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoSphereSoftTraining TestTwoSphereSoftTestingSignal Results/TwoSphereSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM TestTwoSphereSoftTraining TestTwoSphereSoftTestingBackground Results/TwoSphereSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM 8DHyperplaneHardTraining 8DHyperplaneHardTestingAll Results/8DHyperplaneHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM 8DHyperplaneHardTraining 8DHyperplaneHardTestingSignal Results/8DHyperplaneHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM 8DHyperplaneHardTraining 8DHyperplaneHardTestingBackground Results/8DHyperplaneHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM 8DHyperplaneSoftTraining 8DHyperplaneSoftTestingAll Results/8DHyperplaneSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM 8DHyperplaneSoftTraining 8DHyperplaneSoftTestingSignal Results/8DHyperplaneSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM 8DHyperplaneSoftTraining 8DHyperplaneSoftTestingBackground Results/8DHyperplaneSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DHypersphereHardTraining Test8DHypersphereHardTestingAll Results/8DHypersphereHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DHypersphereHardTraining Test8DHypersphereHardTestingSignal Results/8DHypersphereHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DHypersphereHardTraining Test8DHypersphereHardTestingBackground Results/8DHypersphereHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DHypersphereSoftTraining Test8DHypersphereSoftTestingAll Results/8DHypersphereSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DHypersphereSoftTraining Test8DHypersphereSoftTestingSignal Results/8DHypersphereSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DHypersphereSoftTraining Test8DHypersphereSoftTestingBackground Results/8DHypersphereSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DTwoHypersphereHardTraining Test8DTwoHypersphereHardTestingAll Results/8DTwoHypersphereHardTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DTwoHypersphereHardTraining Test8DTwoHypersphereHardTestingSignal Results/8DTwoHypersphereHardTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DTwoHypersphereHardTraining Test8DTwoHypersphereHardTestingBackground Results/8DTwoHypersphereHardTestingBackground1031

sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DTwoHypersphereSoftTraining Test8DTwoHypersphereSoftTestingAll Results/8DTwoHypersphereSoftTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DTwoHypersphereSoftTraining Test8DTwoHypersphereSoftTestingSignal Results/8DTwoHypersphereSoftTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM Test8DTwoHypersphereSoftTraining Test8DTwoHypersphereSoftTestingBackground Results/8DTwoHypersphereSoftTestingBackground1031


sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM MonteCarloTraining MonteCarloTestingAll Results/MonteCarloTestingAll1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM MonteCarloTraining MonteCarloTestingSignal Results/MonteCarloTestingSignal1031
sbatch -p largemem -c 4 --time=10080 --mem=50000 --output=SVM.%J.out --error=SVM.%J.err --mail-type=END,FAIL --mail-user=ben.nissan@tufts.edu RunSVM MonteCarloTraining MonteCarloTestingBackground Results/MonteCarloTestingBackground1031
