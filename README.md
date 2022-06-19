# SUEPGen

To generate SUEP samples:

```bash
cmsrel CMSSW_12_3_0_pre6
cd CMSSW_12_3_0_pre6/src
cmsenv
git clone https://github.com/chrispap95/SUEPGen.git
scram b

cmsDriver.py SUEPGen/Generator/SUEPdarkPho_cff \
    -s GEN,SIM -n 10 \
    --datatier GEN-SIM --eventcontent RAWSIM \
    --conditions auto:phase1_2021_realistic \
    --beamspot Run3RoundOptics25ns13TeVLowSigmaZ \
    --geometry DB:Extended --era Run3 \
    --fileout file:step1.root

cmsDriver.py step2 \
    -s DIGI,L1,DIGI2RAW,HLT -n 10 \
    --conditions auto:phase1_2021_realistic \
    --datatier GEN-SIM-DIGI-RAW --eventcontent RAWSIM \
    --geometry DB:Extended --era Run3 \
    --pileup Run3_Flat55To75_PoissonOOTPU \
    --pileup_input das:/RelValMinBias_14TeV/CMSSW_12_0_0_pre4-120X_mcRun3_2021_realistic_v2-v1/GEN-SIM \
    --filein  file:step1.root --fileout file:step2.root
```

