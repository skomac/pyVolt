This file is meant to inform about units of constants
used in json configuration files.

{
  "name": "sample name of test suite", // name of test suite
  "amount_of_curves": 10, // amount of curves to be prepared in test suite
  "shape": // vector of base peaks defining the shape of whole curve
  [
    {
      "base_peak": "var_no_of_electrons/1_electron",
      "position": -100, //mV
      "height": 3, //mA
      "height_stderr": 0.2 /mA
    },
    {
      "base_peak": "var_no_of_electrons/2_electron",
      "position": -100,
      "height": 3,
      "height_stderr": 0.2
    }
  ],
  "noise_fraction": 0.02, // Gaussian noise (by fraction of maximum height) added to each curve
  "baseline": {} // definition of baseline
}