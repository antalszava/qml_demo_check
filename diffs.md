Last update: 2022-05-17  15:41:54 (All times shown in Eastern time)
# List of differences in demonstration outputs

# Table of contents

1. [tutorial_gbs.html](#demo0)
2. [tutorial_qaoa_intro.html](#demo1)
3. [tutorial_adaptive_circuits.html](#demo2)
4. [tutorial_falqon.html](#demo3)
5. [tutorial_quantum_natural_gradient.html](#demo4)
6. [tutorial_pasqal.html](#demo5)
7. [tutorial_jax_transformations.html](#demo6)
8. [tutorial_quantum_transfer_learning.html](#demo7)
9. [tutorial_measurement_optimize.html](#demo8)
10. [tutorial_general_parshift.html](#demo9)
11. [tutorial_vqe_parallel.html](#demo10)
12. [tutorial_noisy_circuits.html](#demo11)
13. [tutorial_quantum_chemistry.html](#demo12)
14. [tutorial_rosalin.html](#demo13)
15. [tutorial_multiclass_classification.html](#demo14)
16. [tutorial_QGAN.html](#demo15)
17. [tutorial_backprop.html](#demo16)
18. [tutorial_qnn_module_tf.html](#demo17)
19. [tutorial_vqe_qng.html](#demo18)
20. [tutorial_doubly_stochastic.html](#demo19)
21. [tutorial_quanvolution.html](#demo20)
22. [tutorial_ensemble_multi_qpu.html](#demo21)


Number of demos different/all demos: 22/54

## 1. tutorial_gbs.html <a name="demo0"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_gbs.html):

```
/home/runner/work/qml/qml/demonstrations/tutorial_gbs.py:165: UserWarning: 'Interferometer' is deprecated and will be renamed 'InterferometerUnitary'
(10, 10, 10, 10)
|0000>: 0.17637844761413501
|1100>: 0.034732936494202844
|0101>: 0.011870900427255577
|1111>: 0.005957399165336121
|2000>: 0.029573843083205452
[[ 0.19343159-0.54582922j  0.43418269-0.09169615j]
 [ 0.43418269-0.09169615j -0.27554025-0.46222197j]]
0.1763784476141347
0.17637844761413501
0.03473293649420271
0.034732936494202844
0.011870900427255547
0.011870900427255577
0.005957399165336084
0.005957399165336121
0.02957384308320539
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_gbs.html):

```
(10, 10, 10, 10)
|0000>: 0.17637844761413501
|1100>: 0.034732936494202844
|0101>: 0.011870900427255577
|1111>: 0.005957399165336121
|2000>: 0.029573843083205452
[[ 0.19343159-0.54582922j  0.43418269-0.09169615j]
 [ 0.43418269-0.09169615j -0.27554025-0.46222197j]]
0.1763784476141347
0.17637844761413501
0.03473293649420271
0.034732936494202844
0.011870900427255547
0.011870900427255577
0.005957399165336084
0.005957399165336121
0.02957384308320539
0.029573843083205452
```

---

## 2. tutorial_qaoa_intro.html <a name="demo1"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_qaoa_intro.html):

```
[[0.5980635175924566, 0.9419848542526791], [0.5279728111755442, 0.855528453707565]]
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_qaoa_intro.html):

```
[[0.5980635175924566, 0.9419848542526791], [0.5279728111755442, 0.8555284537075651]]
```

---

## 3. tutorial_adaptive_circuits.html <a name="demo2"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_adaptive_circuits.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Excitation : [0, 1, 2, 3], Gradient: -0.012782175157672729
Excitation : [0, 1, 2, 5], Gradient: -1.219727444046192e-19
Excitation : [0, 1, 2, 7], Gradient: 1.2197274440461927e-19
Excitation : [0, 1, 2, 9], Gradient: 0.03426451170169312
Excitation : [0, 1, 3, 4], Gradient: 9.486769009248161e-20
Excitation : [0, 1, 3, 6], Gradient: 1.8973538018496328e-19
Excitation : [0, 1, 3, 8], Gradient: -0.034264511701692896
Excitation : [0, 1, 4, 5], Gradient: -0.02358152902067931
Excitation : [0, 1, 5, 8], Gradient: 1.7618285302889495e-19
Excitation : [0, 1, 6, 7], Gradient: -0.023581529020679316
Excitation : [0, 1, 7, 8], Gradient: -1.2197274440461896e-19
Excitation : [0, 1, 8, 9], Gradient: -0.12362273485598377
Excitation : [0, 2], Gradient: -0.005062536239322769
Excitation : [0, 4], Gradient: 9.846150643917213e-18
Excitation : [0, 6], Gradient: -6.111754024320012e-20
Excitation : [0, 8], Gradient: -0.0009448044625747746
Excitation : [1, 3], Gradient: 0.00492661687699176
Excitation : [1, 5], Gradient: 4.58393739042404e-19
Excitation : [1, 7], Gradient: 2.0748028483987315e-18
Excitation : [1, 9], Gradient: 0.0014535534854003965
n = 0,  E = -7.86266587 H, t = 2.13 s
n = 1,  E = -7.87094621 H, t = 2.67 s
n = 2,  E = -7.87563100 H, t = 2.23 s
n = 3,  E = -7.87829146 H, t = 2.67 s
n = 4,  E = -7.87981705 H, t = 2.16 s
n = 5,  E = -7.88070477 H, t = 2.69 s
n = 6,  E = -7.88123143 H, t = 2.22 s
n = 7,  E = -7.88155161 H, t = 2.65 s
n = 9,  E = -7.88188237 H, t = 2.63 s
n = 10,  E = -7.88197041 H, t = 2.70 s
n = 11,  E = -7.88203267 H, t = 2.18 s
n = 12,  E = -7.88207879 H, t = 2.73 s
n = 13,  E = -7.88211452 H, t = 2.20 s
n = 14,  E = -7.88214335 H, t = 2.62 s
n = 15,  E = -7.88216743 H, t = 2.17 s
n = 16,  E = -7.88218814 H, t = 2.69 s
n = 17,  E = -7.88220634 H, t = 2.21 s
n = 18,  E = -7.88222261 H, t = 2.82 s
n = 19,  E = -7.88223734 H, t = 2.18 s
n = 0,  E = -7.86266587 H, t = 0.13 s
n = 1,  E = -7.87094621 H, t = 0.12 s
n = 2,  E = -7.87563100 H, t = 0.12 s
n = 3,  E = -7.87829146 H, t = 0.12 s
n = 4,  E = -7.87981705 H, t = 0.12 s
n = 5,  E = -7.88070477 H, t = 0.12 s
n = 6,  E = -7.88123143 H, t = 0.12 s
n = 7,  E = -7.88155161 H, t = 0.12 s
n = 8,  E = -7.88175217 H, t = 0.14 s
n = 9,  E = -7.88188237 H, t = 0.12 s
n = 10,  E = -7.88197041 H, t = 0.12 s
n = 11,  E = -7.88203267 H, t = 0.12 s
n = 12,  E = -7.88207879 H, t = 0.13 s
n = 13,  E = -7.88211452 H, t = 0.13 s
n = 14,  E = -7.88214335 H, t = 0.13 s
n = 15,  E = -7.88216743 H, t = 0.13 s
n = 16,  E = -7.88218814 H, t = 0.13 s
n = 17,  E = -7.88220634 H, t = 0.12 s
n = 18,  E = -7.88222261 H, t = 0.12 s
n = 19,  E = -7.88223734 H, t = 0.13 s
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_adaptive_circuits.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Excitation : [0, 1, 2, 3], Gradient: -0.012782175157669547
Excitation : [0, 1, 2, 5], Gradient: -1.4230153513872238e-19
Excitation : [0, 1, 2, 7], Gradient: 2.303929616531697e-19
Excitation : [0, 1, 2, 9], Gradient: 0.034264511701689204
Excitation : [0, 1, 3, 4], Gradient: 6.098637220230964e-20
Excitation : [0, 1, 3, 6], Gradient: 4.0657581468206416e-20
Excitation : [0, 1, 3, 8], Gradient: -0.03426451170168905
Excitation : [0, 1, 4, 5], Gradient: -0.02358152902067854
Excitation : [0, 1, 5, 8], Gradient: 1.4230153513872282e-19
Excitation : [0, 1, 6, 7], Gradient: -0.023581529020678525
Excitation : [0, 1, 7, 8], Gradient: 1.2197274440461954e-19
Excitation : [0, 1, 8, 9], Gradient: -0.12362273485598566
Excitation : [0, 2], Gradient: -0.005062536239326924
Excitation : [0, 4], Gradient: -1.5093771830667583e-17
Excitation : [0, 6], Gradient: -3.3988206614764893e-18
Excitation : [0, 8], Gradient: -0.0009448044625765868
Excitation : [1, 3], Gradient: 0.004926616876995651
Excitation : [1, 5], Gradient: -2.900203988058343e-18
Excitation : [1, 7], Gradient: -5.145790640403441e-19
Excitation : [1, 9], Gradient: 0.0014535534854024951
n = 0,  E = -7.86266587 H, t = 2.08 s
n = 1,  E = -7.87094621 H, t = 2.12 s
n = 2,  E = -7.87563100 H, t = 1.60 s
n = 3,  E = -7.87829146 H, t = 2.12 s
n = 4,  E = -7.87981705 H, t = 1.59 s
n = 5,  E = -7.88070477 H, t = 2.09 s
n = 6,  E = -7.88123143 H, t = 2.13 s
n = 7,  E = -7.88155161 H, t = 1.59 s
n = 9,  E = -7.88188237 H, t = 1.57 s
n = 10,  E = -7.88197041 H, t = 2.10 s
n = 11,  E = -7.88203267 H, t = 1.57 s
n = 12,  E = -7.88207879 H, t = 2.08 s
n = 13,  E = -7.88211452 H, t = 1.57 s
n = 14,  E = -7.88214335 H, t = 2.06 s
n = 15,  E = -7.88216743 H, t = 2.12 s
n = 16,  E = -7.88218814 H, t = 1.59 s
n = 17,  E = -7.88220634 H, t = 2.11 s
n = 18,  E = -7.88222261 H, t = 1.59 s
n = 19,  E = -7.88223734 H, t = 2.10 s
n = 0,  E = -7.86266587 H, t = 0.09 s
n = 1,  E = -7.87094621 H, t = 0.09 s
n = 2,  E = -7.87563100 H, t = 0.09 s
n = 3,  E = -7.87829146 H, t = 0.08 s
n = 4,  E = -7.87981705 H, t = 0.09 s
n = 5,  E = -7.88070477 H, t = 0.09 s
n = 6,  E = -7.88123143 H, t = 0.09 s
n = 7,  E = -7.88155161 H, t = 0.09 s
n = 8,  E = -7.88175217 H, t = 0.09 s
n = 9,  E = -7.88188237 H, t = 0.09 s
n = 10,  E = -7.88197041 H, t = 0.09 s
n = 11,  E = -7.88203267 H, t = 0.09 s
n = 12,  E = -7.88207879 H, t = 0.09 s
n = 13,  E = -7.88211452 H, t = 0.09 s
n = 14,  E = -7.88214335 H, t = 0.09 s
n = 15,  E = -7.88216743 H, t = 0.09 s
n = 16,  E = -7.88218814 H, t = 0.09 s
n = 17,  E = -7.88220634 H, t = 0.09 s
n = 18,  E = -7.88222261 H, t = 0.09 s
n = 19,  E = -7.88223734 H, t = 0.09 s
 </code>
 </pre>
 </details>

---

## 4. tutorial_falqon.html <a name="demo3"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_falqon.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Step 1, Cost = -2.4265436197783425
Step 2, Cost = -5.45183841811118
Step 3, Cost = -5.058939064534102
Step 4, Cost = 0.666377989107735
Step 5, Cost = -3.961765919151042
Step 6, Cost = -6.012336027057502
Step 7, Cost = -6.383828240291059
Step 8, Cost = -6.568581722318154
Step 9, Cost = -6.652767426710378
Step 10, Cost = -6.718062615729133
Step 11, Cost = -6.7639477436093
Step 12, Cost = -6.8048574666097235
Step 13, Cost = -6.8394030587361705
Step 14, Cost = -6.8714592635528415
Step 15, Cost = -6.8997469754809675
Step 16, Cost = -6.925884328592705
Step 17, Cost = -6.9492295078855975
Step 18, Cost = -6.97059412505724
Step 19, Cost = -6.989907329921377
Step 20, Cost = -7.007623105822664
Step 21, Cost = -7.0239860498803415
Step 22, Cost = -7.039304856521962
Step 23, Cost = -7.053894937286077
Step 24, Cost = -7.067988454154516
Step 25, Cost = -7.081842534715257
Step 26, Cost = -7.095617260802714
Step 27, Cost = -7.109472588274413
Step 28, Cost = -7.123480825409048
Step 29, Cost = -7.137684426026884
Step 30, Cost = -7.152041022693121
Step 31, Cost = -7.166453310287251
Step 32, Cost = -7.1807483416093705
Step 33, Cost = -7.194694917926645
Step 34, Cost = -7.208028603663313
Step 35, Cost = -7.22045639587035
Step 36, Cost = -7.231727330032172
Step 37, Cost = -7.241565955502995
Step 38, Cost = -7.249767410209228
Step 39, Cost = -7.255782895664823
Step 40, Cost = -7.258987907014075
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_falqon.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Step 1, Cost = -2.4265436197783448
Step 2, Cost = -5.451838418111176
Step 3, Cost = -5.05893906453409
Step 4, Cost = 0.6663779891077449
Step 5, Cost = -3.9617659191509746
Step 6, Cost = -6.012336027057521
Step 7, Cost = -6.383828240291071
Step 8, Cost = -6.5685817223181155
Step 9, Cost = -6.652767426710387
Step 10, Cost = -6.718062615729132
Step 11, Cost = -6.763947743609312
Step 12, Cost = -6.80485746660975
Step 13, Cost = -6.8394030587362
Step 14, Cost = -6.871459263552881
Step 15, Cost = -6.899746975480981
Step 16, Cost = -6.925884328592719
Step 17, Cost = -6.949229507885613
Step 18, Cost = -6.970594125057218
Step 19, Cost = -6.989907329921348
Step 20, Cost = -7.007623105822645
Step 21, Cost = -7.023986049880396
Step 22, Cost = -7.03930485652197
Step 23, Cost = -7.053894937286083
Step 24, Cost = -7.067988454154528
Step 25, Cost = -7.081842534715245
Step 26, Cost = -7.095617260802699
Step 27, Cost = -7.109472588274404
Step 28, Cost = -7.123480825409055
Step 29, Cost = -7.137684426026871
Step 30, Cost = -7.152041022693112
Step 31, Cost = -7.166453310287315
Step 32, Cost = -7.1807483416093865
Step 33, Cost = -7.194694917926691
Step 34, Cost = -7.208028603663316
Step 35, Cost = -7.22045639587038
Step 36, Cost = -7.231727330032204
Step 37, Cost = -7.241565955502979
Step 38, Cost = -7.249767410209168
Step 39, Cost = -7.255782895664824
Step 40, Cost = -7.258987907014076
 </code>
 </pre>
 </details>

---

## 5. tutorial_quantum_natural_gradient.html <a name="demo4"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_quantum_natural_gradient.html):

```
[[0.125      0.         0.         0.        ]
 [0.         0.1875     0.         0.        ]
 [0.         0.         0.24973433 0.        ]
 [0.         0.         0.         0.20293623]]
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_quantum_natural_gradient.html):

```
/opt/hostedtoolcache/Python/3.7.12/x64/lib/python3.7/site-packages/pennylane/transforms/metric_tensor.py:192: UserWarning: The keyword argument diag_approx is deprecated. Please use approx='diag' instead.
[[0.125      0.         0.         0.        ]
 [0.         0.1875     0.         0.        ]
 [0.         0.         0.24973433 0.        ]
```

---

## 6. tutorial_pasqal.html <a name="demo5"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_pasqal.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Step 0: cost=0.0001672286566463592
Step 5: cost=0.9979047620889769
Step 10: cost=0.6109142342375409
Step 15: cost=0.9989467692733883
Step 20: cost=0.006048046345186867
Step 25: cost=0.8941419709966564
Step 30: cost=0.6746950251504293
Step 35: cost=7.001036075480078e-07
Step 40: cost=0.6766725857506097
Step 45: cost=0.3557129296721806
Step 50: cost=0.02749132423642614
Step 55: cost=0.09109423901502911
Step 60: cost=0.3024013456684429
Step 65: cost=0.01987428630678778
Step 70: cost=0.007314119488719198
Step 75: cost=0.0005591169242113734
Step 80: cost=0.00048827164327969966
Step 85: cost=6.396804707814799e-07
Step 90: cost=5.587668130241363e-05
Step 95: cost=7.117522822325351e-07
Final cost value: 1.230815538836673e-05
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_pasqal.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Step 0: cost=0.00016714805870154947
Step 5: cost=0.996033675363325
Step 10: cost=0.6155194682134244
Step 15: cost=0.999094333759448
Step 20: cost=0.005043049850429249
Step 25: cost=0.8981007649191639
Step 30: cost=0.6573246599021019
Step 35: cost=8.465054293083085e-07
Step 40: cost=0.6788142780522586
Step 45: cost=0.3556685123234262
Step 50: cost=0.026910206671360015
Step 55: cost=0.08898491577262835
Step 60: cost=0.31026489878494545
Step 65: cost=0.02024610375919167
Step 70: cost=0.007934105929226831
Step 75: cost=0.0005895204131158849
Step 80: cost=0.0005427646474345238
Step 85: cost=8.379720526363599e-07
Step 90: cost=5.347187868043335e-05
Step 95: cost=8.521633398927975e-07
Final cost value: 1.044140829353779e-05
 </code>
 </pre>
 </details>

---

## 7. tutorial_jax_transformations.html <a name="demo6"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_jax_transformations.html):

```
No jit time: 0.0125 seconds
First run time: 0.0617 seconds
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_jax_transformations.html):

```
No jit time: 0.0096 seconds
First run time: 0.0528 seconds
```

---

## 8. tutorial_quantum_transfer_learning.html <a name="demo7"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_quantum_transfer_learning.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
  0%|          | 224k/44.7M [00:00<00:20, 2.23MB/s]
  3%|3         | 1.44M/44.7M [00:00<00:05, 8.36MB/s]
 12%|#1        | 5.31M/44.7M [00:00<00:01, 23.0MB/s]
 21%|##        | 9.18M/44.7M [00:00<00:01, 29.9MB/s]
 34%|###4      | 15.4M/44.7M [00:00<00:00, 42.4MB/s]
 43%|####3     | 19.4M/44.7M [00:00<00:00, 40.5MB/s]
 53%|#####3    | 23.8M/44.7M [00:00<00:00, 42.1MB/s]
 71%|#######1  | 31.8M/44.7M [00:00<00:00, 54.9MB/s]
 88%|########8 | 39.5M/44.7M [00:00<00:00, 62.9MB/s]
100%|##########| 44.7M/44.7M [00:00<00:00, 46.8MB/s]
Training started:
Phase: train Epoch: 1/1 Iter: 1/62 Batch time: 0.4626
Phase: train Epoch: 1/1 Iter: 2/62 Batch time: 0.4727
Phase: train Epoch: 1/1 Iter: 3/62 Batch time: 0.4232
Phase: train Epoch: 1/1 Iter: 4/62 Batch time: 0.4490
Phase: train Epoch: 1/1 Iter: 5/62 Batch time: 0.4340
Phase: train Epoch: 1/1 Iter: 6/62 Batch time: 0.4508
Phase: train Epoch: 1/1 Iter: 7/62 Batch time: 0.4421
Phase: train Epoch: 1/1 Iter: 8/62 Batch time: 0.4568
Phase: train Epoch: 1/1 Iter: 9/62 Batch time: 0.4577
Phase: train Epoch: 1/1 Iter: 10/62 Batch time: 0.4552
Phase: train Epoch: 1/1 Iter: 11/62 Batch time: 0.4390
Phase: train Epoch: 1/1 Iter: 12/62 Batch time: 0.4403
Phase: train Epoch: 1/1 Iter: 13/62 Batch time: 0.4436
Phase: train Epoch: 1/1 Iter: 14/62 Batch time: 0.4458
Phase: train Epoch: 1/1 Iter: 15/62 Batch time: 0.4426
Phase: train Epoch: 1/1 Iter: 16/62 Batch time: 0.4343
Phase: train Epoch: 1/1 Iter: 17/62 Batch time: 0.4366
Phase: train Epoch: 1/1 Iter: 18/62 Batch time: 0.4471
Phase: train Epoch: 1/1 Iter: 19/62 Batch time: 0.4568
Phase: train Epoch: 1/1 Iter: 20/62 Batch time: 0.4426
Phase: train Epoch: 1/1 Iter: 21/62 Batch time: 0.4262
Phase: train Epoch: 1/1 Iter: 22/62 Batch time: 0.4400
Phase: train Epoch: 1/1 Iter: 23/62 Batch time: 0.4327
Phase: train Epoch: 1/1 Iter: 24/62 Batch time: 0.4135
Phase: train Epoch: 1/1 Iter: 25/62 Batch time: 0.4126
Phase: train Epoch: 1/1 Iter: 26/62 Batch time: 0.4185
Phase: train Epoch: 1/1 Iter: 27/62 Batch time: 0.4177
Phase: train Epoch: 1/1 Iter: 28/62 Batch time: 0.4291
Phase: train Epoch: 1/1 Iter: 29/62 Batch time: 0.4322
Phase: train Epoch: 1/1 Iter: 30/62 Batch time: 0.4175
Phase: train Epoch: 1/1 Iter: 31/62 Batch time: 0.4324
Phase: train Epoch: 1/1 Iter: 32/62 Batch time: 0.4243
Phase: train Epoch: 1/1 Iter: 33/62 Batch time: 0.4374
Phase: train Epoch: 1/1 Iter: 34/62 Batch time: 0.4194
Phase: train Epoch: 1/1 Iter: 35/62 Batch time: 0.4023
Phase: train Epoch: 1/1 Iter: 36/62 Batch time: 0.4265
Phase: train Epoch: 1/1 Iter: 37/62 Batch time: 0.4302
Phase: train Epoch: 1/1 Iter: 38/62 Batch time: 0.4274
Phase: train Epoch: 1/1 Iter: 39/62 Batch time: 0.4239
Phase: train Epoch: 1/1 Iter: 40/62 Batch time: 0.4197
Phase: train Epoch: 1/1 Iter: 41/62 Batch time: 0.4418
Phase: train Epoch: 1/1 Iter: 42/62 Batch time: 0.4135
Phase: train Epoch: 1/1 Iter: 43/62 Batch time: 0.4476
Phase: train Epoch: 1/1 Iter: 44/62 Batch time: 0.4256
Phase: train Epoch: 1/1 Iter: 45/62 Batch time: 0.4456
Phase: train Epoch: 1/1 Iter: 46/62 Batch time: 0.4235
Phase: train Epoch: 1/1 Iter: 47/62 Batch time: 0.4247
Phase: train Epoch: 1/1 Iter: 48/62 Batch time: 0.4205
Phase: train Epoch: 1/1 Iter: 49/62 Batch time: 0.4350
Phase: train Epoch: 1/1 Iter: 50/62 Batch time: 0.4214
Phase: train Epoch: 1/1 Iter: 51/62 Batch time: 0.4111
Phase: train Epoch: 1/1 Iter: 52/62 Batch time: 0.4217
Phase: train Epoch: 1/1 Iter: 53/62 Batch time: 0.4168
Phase: train Epoch: 1/1 Iter: 54/62 Batch time: 0.4459
Phase: train Epoch: 1/1 Iter: 55/62 Batch time: 0.4257
Phase: train Epoch: 1/1 Iter: 56/62 Batch time: 0.4404
Phase: train Epoch: 1/1 Iter: 57/62 Batch time: 0.4234
Phase: train Epoch: 1/1 Iter: 58/62 Batch time: 0.4138
Phase: train Epoch: 1/1 Iter: 59/62 Batch time: 0.4119
Phase: train Epoch: 1/1 Iter: 60/62 Batch time: 0.4144
Phase: train Epoch: 1/1 Iter: 61/62 Batch time: 0.4361
Phase: train Epoch: 1/1 Loss: 0.6993 Acc: 0.5246
Phase: validation Epoch: 1/1 Iter: 1/39 Batch time: 0.3435
Phase: validation Epoch: 1/1 Iter: 2/39 Batch time: 0.3967
Phase: validation Epoch: 1/1 Iter: 3/39 Batch time: 0.3526
Phase: validation Epoch: 1/1 Iter: 4/39 Batch time: 0.3537
Phase: validation Epoch: 1/1 Iter: 5/39 Batch time: 0.3680
Phase: validation Epoch: 1/1 Iter: 6/39 Batch time: 0.3601
Phase: validation Epoch: 1/1 Iter: 7/39 Batch time: 0.3758
Phase: validation Epoch: 1/1 Iter: 8/39 Batch time: 0.3546
Phase: validation Epoch: 1/1 Iter: 9/39 Batch time: 0.3474
Phase: validation Epoch: 1/1 Iter: 10/39 Batch time: 0.3489
Phase: validation Epoch: 1/1 Iter: 11/39 Batch time: 0.3444
Phase: validation Epoch: 1/1 Iter: 12/39 Batch time: 0.3566
Phase: validation Epoch: 1/1 Iter: 13/39 Batch time: 0.3396
Phase: validation Epoch: 1/1 Iter: 14/39 Batch time: 0.3447
Phase: validation Epoch: 1/1 Iter: 15/39 Batch time: 0.3584
Phase: validation Epoch: 1/1 Iter: 16/39 Batch time: 0.3468
Phase: validation Epoch: 1/1 Iter: 17/39 Batch time: 0.3605
Phase: validation Epoch: 1/1 Iter: 18/39 Batch time: 0.3695
Phase: validation Epoch: 1/1 Iter: 19/39 Batch time: 0.3431
Phase: validation Epoch: 1/1 Iter: 20/39 Batch time: 0.3586
Phase: validation Epoch: 1/1 Iter: 21/39 Batch time: 0.3451
Phase: validation Epoch: 1/1 Iter: 22/39 Batch time: 0.3520
Phase: validation Epoch: 1/1 Iter: 23/39 Batch time: 0.3548
Phase: validation Epoch: 1/1 Iter: 24/39 Batch time: 0.3577
Phase: validation Epoch: 1/1 Iter: 25/39 Batch time: 0.3562
Phase: validation Epoch: 1/1 Iter: 26/39 Batch time: 0.3332
Phase: validation Epoch: 1/1 Iter: 27/39 Batch time: 0.3630
Phase: validation Epoch: 1/1 Iter: 28/39 Batch time: 0.3619
Phase: validation Epoch: 1/1 Iter: 29/39 Batch time: 0.3651
Phase: validation Epoch: 1/1 Iter: 30/39 Batch time: 0.3429
Phase: validation Epoch: 1/1 Iter: 31/39 Batch time: 0.3518
Phase: validation Epoch: 1/1 Iter: 32/39 Batch time: 0.3513
Phase: validation Epoch: 1/1 Iter: 33/39 Batch time: 0.3525
Phase: validation Epoch: 1/1 Iter: 34/39 Batch time: 0.3361
Phase: validation Epoch: 1/1 Iter: 35/39 Batch time: 0.3544
Phase: validation Epoch: 1/1 Iter: 36/39 Batch time: 0.3479
Phase: validation Epoch: 1/1 Iter: 37/39 Batch time: 0.3338
Phase: validation Epoch: 1/1 Iter: 38/39 Batch time: 0.3633
Phase: validation Epoch: 1/1 Iter: 39/39 Batch time: 0.0975
Phase: validation   Epoch: 1/1 Loss: 0.6432 Acc: 0.6536
Training completed in 0m 43s
Best test loss: 0.6432 | Best test accuracy: 0.6536
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_quantum_transfer_learning.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
  6%|6         | 2.88M/44.7M [00:00<00:01, 27.4MB/s]
 17%|#7        | 7.60M/44.7M [00:00<00:00, 39.9MB/s]
 26%|##5       | 11.5M/44.7M [00:00<00:00, 39.9MB/s]
 34%|###4      | 15.3M/44.7M [00:00<00:00, 38.5MB/s]
 43%|####2     | 19.0M/44.7M [00:00<00:00, 38.5MB/s]
 54%|#####4    | 24.2M/44.7M [00:00<00:00, 43.5MB/s]
 65%|######4   | 29.0M/44.7M [00:00<00:00, 45.8MB/s]
 75%|#######4  | 33.4M/44.7M [00:00<00:00, 44.9MB/s]
 85%|########5 | 38.0M/44.7M [00:00<00:00, 45.7MB/s]
 98%|#########7| 43.7M/44.7M [00:01<00:00, 49.9MB/s]
100%|##########| 44.7M/44.7M [00:01<00:00, 44.7MB/s]
Training started:
Phase: train Epoch: 1/1 Iter: 1/62 Batch time: 0.2939
Phase: train Epoch: 1/1 Iter: 2/62 Batch time: 0.2765
Phase: train Epoch: 1/1 Iter: 3/62 Batch time: 0.2697
Phase: train Epoch: 1/1 Iter: 4/62 Batch time: 0.2709
Phase: train Epoch: 1/1 Iter: 5/62 Batch time: 0.2671
Phase: train Epoch: 1/1 Iter: 6/62 Batch time: 0.2680
Phase: train Epoch: 1/1 Iter: 7/62 Batch time: 0.2706
Phase: train Epoch: 1/1 Iter: 8/62 Batch time: 0.2686
Phase: train Epoch: 1/1 Iter: 9/62 Batch time: 0.2671
Phase: train Epoch: 1/1 Iter: 10/62 Batch time: 0.2661
Phase: train Epoch: 1/1 Iter: 11/62 Batch time: 0.2706
Phase: train Epoch: 1/1 Iter: 12/62 Batch time: 0.2650
Phase: train Epoch: 1/1 Iter: 13/62 Batch time: 0.2656
Phase: train Epoch: 1/1 Iter: 14/62 Batch time: 0.2632
Phase: train Epoch: 1/1 Iter: 15/62 Batch time: 0.2641
Phase: train Epoch: 1/1 Iter: 16/62 Batch time: 0.2648
Phase: train Epoch: 1/1 Iter: 17/62 Batch time: 0.2672
Phase: train Epoch: 1/1 Iter: 18/62 Batch time: 0.2674
Phase: train Epoch: 1/1 Iter: 19/62 Batch time: 0.2642
Phase: train Epoch: 1/1 Iter: 20/62 Batch time: 0.2632
Phase: train Epoch: 1/1 Iter: 21/62 Batch time: 0.2646
Phase: train Epoch: 1/1 Iter: 22/62 Batch time: 0.2638
Phase: train Epoch: 1/1 Iter: 23/62 Batch time: 0.2685
Phase: train Epoch: 1/1 Iter: 24/62 Batch time: 0.2663
Phase: train Epoch: 1/1 Iter: 25/62 Batch time: 0.2691
Phase: train Epoch: 1/1 Iter: 26/62 Batch time: 0.2665
Phase: train Epoch: 1/1 Iter: 27/62 Batch time: 0.2676
Phase: train Epoch: 1/1 Iter: 28/62 Batch time: 0.2677
Phase: train Epoch: 1/1 Iter: 29/62 Batch time: 0.2664
Phase: train Epoch: 1/1 Iter: 30/62 Batch time: 0.2708
Phase: train Epoch: 1/1 Iter: 31/62 Batch time: 0.2677
Phase: train Epoch: 1/1 Iter: 32/62 Batch time: 0.2696
Phase: train Epoch: 1/1 Iter: 33/62 Batch time: 0.2681
Phase: train Epoch: 1/1 Iter: 34/62 Batch time: 0.2686
Phase: train Epoch: 1/1 Iter: 35/62 Batch time: 0.2717
Phase: train Epoch: 1/1 Iter: 36/62 Batch time: 0.2720
Phase: train Epoch: 1/1 Iter: 37/62 Batch time: 0.2719
Phase: train Epoch: 1/1 Iter: 38/62 Batch time: 0.2714
Phase: train Epoch: 1/1 Iter: 39/62 Batch time: 0.2688
Phase: train Epoch: 1/1 Iter: 40/62 Batch time: 0.2756
Phase: train Epoch: 1/1 Iter: 41/62 Batch time: 0.2769
Phase: train Epoch: 1/1 Iter: 42/62 Batch time: 0.2700
Phase: train Epoch: 1/1 Iter: 43/62 Batch time: 0.2695
Phase: train Epoch: 1/1 Iter: 44/62 Batch time: 0.2692
Phase: train Epoch: 1/1 Iter: 45/62 Batch time: 0.2708
Phase: train Epoch: 1/1 Iter: 46/62 Batch time: 0.2681
Phase: train Epoch: 1/1 Iter: 47/62 Batch time: 0.2675
Phase: train Epoch: 1/1 Iter: 48/62 Batch time: 0.2700
Phase: train Epoch: 1/1 Iter: 49/62 Batch time: 0.2636
Phase: train Epoch: 1/1 Iter: 50/62 Batch time: 0.2681
Phase: train Epoch: 1/1 Iter: 51/62 Batch time: 0.2667
Phase: train Epoch: 1/1 Iter: 52/62 Batch time: 0.2705
Phase: train Epoch: 1/1 Iter: 53/62 Batch time: 0.2714
Phase: train Epoch: 1/1 Iter: 54/62 Batch time: 0.2715
Phase: train Epoch: 1/1 Iter: 55/62 Batch time: 0.2712
Phase: train Epoch: 1/1 Iter: 56/62 Batch time: 0.2687
Phase: train Epoch: 1/1 Iter: 57/62 Batch time: 0.2714
Phase: train Epoch: 1/1 Iter: 58/62 Batch time: 0.2778
Phase: train Epoch: 1/1 Iter: 59/62 Batch time: 0.2717
Phase: train Epoch: 1/1 Iter: 60/62 Batch time: 0.2800
Phase: train Epoch: 1/1 Iter: 61/62 Batch time: 0.2848
Phase: train Epoch: 1/1 Loss: 0.6993 Acc: 0.5246
Phase: validation Epoch: 1/1 Iter: 1/39 Batch time: 0.2110
Phase: validation Epoch: 1/1 Iter: 2/39 Batch time: 0.2021
Phase: validation Epoch: 1/1 Iter: 3/39 Batch time: 0.2028
Phase: validation Epoch: 1/1 Iter: 4/39 Batch time: 0.2037
Phase: validation Epoch: 1/1 Iter: 5/39 Batch time: 0.2079
Phase: validation Epoch: 1/1 Iter: 6/39 Batch time: 0.2040
Phase: validation Epoch: 1/1 Iter: 7/39 Batch time: 0.2036
Phase: validation Epoch: 1/1 Iter: 8/39 Batch time: 0.2049
Phase: validation Epoch: 1/1 Iter: 9/39 Batch time: 0.2033
Phase: validation Epoch: 1/1 Iter: 10/39 Batch time: 0.2052
Phase: validation Epoch: 1/1 Iter: 11/39 Batch time: 0.2032
Phase: validation Epoch: 1/1 Iter: 12/39 Batch time: 0.2023
Phase: validation Epoch: 1/1 Iter: 13/39 Batch time: 0.1991
Phase: validation Epoch: 1/1 Iter: 14/39 Batch time: 0.1969
Phase: validation Epoch: 1/1 Iter: 15/39 Batch time: 0.2032
Phase: validation Epoch: 1/1 Iter: 16/39 Batch time: 0.1988
Phase: validation Epoch: 1/1 Iter: 17/39 Batch time: 0.1993
Phase: validation Epoch: 1/1 Iter: 18/39 Batch time: 0.1988
Phase: validation Epoch: 1/1 Iter: 19/39 Batch time: 0.1998
Phase: validation Epoch: 1/1 Iter: 20/39 Batch time: 0.2018
Phase: validation Epoch: 1/1 Iter: 21/39 Batch time: 0.1998
Phase: validation Epoch: 1/1 Iter: 22/39 Batch time: 0.2031
Phase: validation Epoch: 1/1 Iter: 23/39 Batch time: 0.1998
Phase: validation Epoch: 1/1 Iter: 24/39 Batch time: 0.2002
Phase: validation Epoch: 1/1 Iter: 25/39 Batch time: 0.1985
Phase: validation Epoch: 1/1 Iter: 26/39 Batch time: 0.1997
Phase: validation Epoch: 1/1 Iter: 27/39 Batch time: 0.1996
Phase: validation Epoch: 1/1 Iter: 28/39 Batch time: 0.1978
Phase: validation Epoch: 1/1 Iter: 29/39 Batch time: 0.2033
Phase: validation Epoch: 1/1 Iter: 30/39 Batch time: 0.2055
Phase: validation Epoch: 1/1 Iter: 31/39 Batch time: 0.2073
Phase: validation Epoch: 1/1 Iter: 32/39 Batch time: 0.2008
Phase: validation Epoch: 1/1 Iter: 33/39 Batch time: 0.2065
Phase: validation Epoch: 1/1 Iter: 34/39 Batch time: 0.2044
Phase: validation Epoch: 1/1 Iter: 35/39 Batch time: 0.2000
Phase: validation Epoch: 1/1 Iter: 36/39 Batch time: 0.2002
Phase: validation Epoch: 1/1 Iter: 37/39 Batch time: 0.2019
Phase: validation Epoch: 1/1 Iter: 38/39 Batch time: 0.1992
Phase: validation Epoch: 1/1 Iter: 39/39 Batch time: 0.0699
Phase: validation   Epoch: 1/1 Loss: 0.6432 Acc: 0.6536
Training completed in 0m 27s
 </code>
 </pre>
 </details>

---

## 9. tutorial_measurement_optimize.html <a name="demo8"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_measurement_optimize.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
+ (-0.04207897647782277) [I0]
+ (0.12293305056183801) [Z0 Z2]
+ (0.12293305056183801) [Z1 Z3]
+ (0.1762764080431959) [Z2 Z3]
   (-46.46390678868894) [I0]
+ (0.7829661725950183) [Z10]
+ (0.7829661725950183) [Z11]
+ (0.808458196172048) [Z12]
+ (0.8084581961720482) [Z13]
+ (1.2034402289145631) [Z4]
+ (1.2034402289145631) [Z5]
+ (1.3096862988615452) [Z7]
+ (1.3096862988615456) [Z6]
+ (1.3693525634718184) [Z9]
+ (1.6538942226831712) [Z3]
+ (1.6538942226831714) [Z2]
+ (12.412630742111766) [Z0]
+ (12.412630742111766) [Z1]
+ (-8.194261371363487e-06) [Y10 Y12]
+ (-8.194261371363487e-06) [X10 X12]
+ (-1.8540608580269639e-06) [Y5 Y7]
+ (-1.8540608580269639e-06) [X5 X7]
+ (-7.764994118720698e-07) [Y3 Y5]
+ (-7.764994118720698e-07) [X3 X5]
+ (-5.929765816486099e-07) [Y4 Y6]
+ (-5.929765816486099e-07) [X4 X6]
+ (1.6021167405648476e-06) [Y2 Y4]
+ (1.6021167405648476e-06) [X2 X4]
+ (7.95441317560359e-06) [Y11 Y13]
+ (7.95441317560359e-06) [X11 X13]
+ (0.003276971931231673) [Y1 Y3]
+ (0.003276971931231673) [X1 X3]
+ (0.1043306478065142) [Y0 Y2]
+ (0.1043306478065142) [X0 X2]
+ (0.11270386920332201) [Z10 Z12]
+ (0.11270386920332201) [Z11 Z13]
+ (0.11383573679388657) [Z4 Z12]
+ (0.11383573679388657) [Z5 Z13]
+ (0.11952438964682663) [Z6 Z10]
+ (0.11952438964682663) [Z7 Z11]
+ (0.12489990917237578) [Z4 Z10]
+ (0.12489990917237578) [Z5 Z11]
+ (0.12495807739503222) [Z2 Z4]
+ (0.12495807739503222) [Z3 Z5]
+ (0.12799502492468395) [Z2 Z10]
+ (0.12799502492468395) [Z3 Z11]
+ (0.13401715261963712) [Z6 Z12]
+ (0.13401715261963712) [Z7 Z13]
+ (0.1370119167404076) [Z4 Z6]
+ (0.1370119167404076) [Z5 Z7]
+ (0.13734953064261304) [Z6 Z11]
+ (0.13734953064261304) [Z7 Z10]
+ (0.13739104762683238) [Z2 Z6]
+ (0.13739104762683238) [Z3 Z7]
+ (0.13766872645852554) [Z8 Z10]
+ (0.13766872645852554) [Z9 Z11]
+ (0.14011289865354817) [Z2 Z12]
+ (0.14011289865354817) [Z3 Z13]
+ (0.14257997712485732) [Z4 Z11]
+ (0.14257997712485732) [Z5 Z10]
+ (0.14722943218766144) [Z8 Z11]
+ (0.14722943218766144) [Z9 Z10]
+ (0.14899430575065553) [Z4 Z7]
+ (0.14899430575065553) [Z5 Z6]
+ (0.14926355147388862) [Z10 Z11]
+ (0.14960702684445296) [Z4 Z8]
+ (0.14960702684445296) [Z5 Z9]
+ (0.14973486803496927) [Z8 Z12]
+ (0.14973486803496927) [Z9 Z13]
+ (0.15071408121008295) [Z2 Z8]
+ (0.15071408121008295) [Z3 Z9]
+ (0.15138327161428852) [Z6 Z13]
+ (0.15138327161428852) [Z7 Z12]
+ (0.15215040708869046) [Z4 Z13]
+ (0.15215040708869046) [Z5 Z12]
+ (0.15337968243314132) [Z2 Z11]
+ (0.15337968243314132) [Z3 Z10]
+ (0.1543574865722364) [Z12 Z13]
+ (0.1556901067175246) [Z2 Z13]
+ (0.1556901067175246) [Z3 Z12]
+ (0.1558226905155311) [Z8 Z13]
+ (0.1558226905155311) [Z9 Z12]
+ (0.15676396176430993) [Z4 Z9]
+ (0.15676396176430993) [Z5 Z8]
+ (0.15755314797985653) [Z4 Z5]
+ (0.16079764534838564) [Z2 Z5]
+ (0.16079764534838564) [Z3 Z4]
+ (0.16756653265461283) [Z6 Z8]
+ (0.16756653265461283) [Z7 Z9]
+ (0.1685348656157995) [Z2 Z7]
+ (0.1685348656157995) [Z3 Z6]
+ (0.18143991440303894) [Z6 Z9]
+ (0.18143991440303894) [Z7 Z8]
+ (0.18189085790751375) [Z2 Z3]
+ (0.18690820476912562) [Z2 Z9]
+ (0.18690820476912562) [Z3 Z8]
+ (0.1929972393536418) [Z0 Z10]
+ (0.1929972393536418) [Z1 Z11]
+ (0.19392534613270232) [Z6 Z7]
+ (0.19661770890342137) [Z0 Z4]
+ (0.19661770890342137) [Z1 Z5]
+ (0.19936354537360818) [Z0 Z5]
+ (0.19936354537360818) [Z1 Z4]
+ (0.20072866460441702) [Z0 Z11]
+ (0.20072866460441702) [Z1 Z10]
+ (0.21102659849791483) [Z0 Z12]
+ (0.21102659849791483) [Z1 Z13]
+ (0.21631037498631778) [Z0 Z13]
+ (0.21631037498631778) [Z1 Z12]
+ (0.2200397733437609) [Z8 Z9]
+ (0.2367108078383042) [Z0 Z2]
+ (0.2367108078383042) [Z1 Z3]
+ (0.24164663936017203) [Z0 Z6]
+ (0.24164663936017203) [Z1 Z7]
+ (0.2485348337131426) [Z0 Z7]
+ (0.2485348337131426) [Z1 Z6]
+ (0.25129445674591694) [Z0 Z3]
+ (0.25129445674591694) [Z1 Z2]
+ (1.1861763734860475) [Z0 Z1]
+ (-1.2260484989271274e-05) [Y5 Z6 Y7]
+ (-1.2260484989271274e-05) [X5 Z6 X7]
+ (-1.2260484989271272e-05) [Y4 Z5 Y6]
+ (-1.2260484989271272e-05) [X4 Z5 X6]
+ (-1.0722312156951719e-05) [Y10 Z11 Y12]
+ (-1.0722312156951719e-05) [X10 Z11 X12]
+ (-1.0722312156951719e-05) [Y11 Z12 Y13]
+ (-1.0722312156951719e-05) [X11 Z12 X13]
+ (-3.887051673532508e-06) [Y2 Z3 Y4]
+ (-3.887051673532508e-06) [X2 Z3 X4]
+ (-3.887051673532508e-06) [Y3 Z4 Y5]
+ (-3.887051673532508e-06) [X3 Z4 X5]
+ (0.1250703257977234) [Y1 Z2 Y3]
+ (0.1250703257977234) [X1 Z2 X3]
+ (0.12507032579772348) [Y0 Z1 Y2]
+ (0.12507032579772348) [X0 Z1 X2]
+ (-0.03831467029480388) [Y4 Y5 X12 X13]
+ (-0.03831467029480388) [X4 X5 Y12 Y13]
+ (-0.03619412355904266) [Y2 Y3 X8 X9]
+ (-0.03619412355904266) [X2 X3 Y8 Y9]
+ (-0.03583956795335344) [Y2 Y3 X4 X5]
+ (-0.03583956795335344) [X2 X3 Y4 Y5]
+ (-0.031143817988967128) [Y2 Y3 X6 X7]
+ (-0.031143817988967128) [X2 X3 Y6 Y7]
+ (-0.028685183716106014) [Y10 Y11 X12 X13]
+ (-0.028685183716106014) [X10 X11 Y12 Y13]
+ (-0.02599617759802124) [Y3 Z4 Z5 Y7]
+ (-0.02599617759802124) [X3 Z4 Z5 X7]
+ (-0.02538465750845734) [Y2 Y3 X10 X11]
+ (-0.02538465750845734) [X2 X3 Y10 Y11]
+ (-0.01902824244384726) [Y3 Y4 X11 X12]
+ (-0.01902824244384726) [X3 X4 Y11 Y12]
+ (-0.01782514099578641) [Y6 Y7 X10 X11]
+ (-0.01782514099578641) [X6 X7 Y10 Y11]
+ (-0.0176800679524815) [Y4 Y5 X10 X11]
+ (-0.0176800679524815) [X4 X5 Y10 Y11]
+ (-0.01736611899465138) [Y6 Y7 X12 X13]
+ (-0.01736611899465138) [X6 X7 Y12 Y13]
+ (-0.015577208063976429) [Y2 Y3 X12 X13]
+ (-0.015577208063976429) [X2 X3 Y12 Y13]
+ (-0.01458364890761273) [Y0 Y1 X2 X3]
+ (-0.01458364890761273) [X0 X1 Y2 Y3]
+ (-0.013873381748426113) [Y6 Y7 X8 X9]
+ (-0.013873381748426113) [X6 X7 Y8 Y9]
+ (-0.011982389010247934) [Y4 Y5 X6 X7]
+ (-0.011982389010247934) [X4 X5 Y6 Y7]
+ (-0.011285190200840898) [Y5 X6 X11 Y12]
+ (-0.011285190200840898) [X5 Y6 Y11 X12]
+ (-0.0095607057291359) [Y8 Y9 X10 X11]
+ (-0.0095607057291359) [X8 X9 Y10 Y11]
+ (-0.008125251921381043) [Y1 X2 X8 Y9]
+ (-0.008125251921381043) [Y1 Y2 Y8 Y9]
+ (-0.008125251921381043) [X1 X2 X8 X9]
+ (-0.008125251921381043) [X1 Y2 Y8 X9]
+ (-0.007731425250775262) [Y0 Y1 X10 X11]
+ (-0.007731425250775262) [X0 X1 Y10 Y11]
+ (-0.0071569349198569564) [Y4 Y5 X8 X9]
+ (-0.0071569349198569564) [X4 X5 Y8 Y9]
+ (-0.0068881943529705714) [Y0 Y1 X6 X7]
+ (-0.0068881943529705714) [X0 X1 Y6 Y7]
+ (-0.006509361201177239) [Y0 Y1 X8 X9]
+ (-0.006509361201177239) [X0 X1 Y8 Y9]
+ (-0.006087822480561846) [Y8 Y9 X12 X13]
+ (-0.006087822480561846) [X8 X9 Y12 Y13]
+ (-0.005283776488402954) [Y0 Y1 X12 X13]
+ (-0.005283776488402954) [X0 X1 Y12 Y13]
+ (-0.005143391768825037) [Y3 X4 X5 Y6]
+ (-0.005143391768825037) [X3 Y4 Y5 X6]
+ (-0.0046849033881552204) [Y1 X2 X6 Y7]
+ (-0.0046849033881552204) [Y1 Y2 Y6 Y7]
+ (-0.0046849033881552204) [X1 X2 X6 X7]
+ (-0.0046849033881552204) [X1 Y2 Y6 X7]
+ (-0.004575007626639198) [Y1 X2 X12 Y13]
+ (-0.004575007626639198) [Y1 Y2 Y12 Y13]
+ (-0.004575007626639198) [X1 X2 X12 X13]
+ (-0.004575007626639198) [X1 Y2 Y12 X13]
+ (-0.004424855449441869) [Y1 X2 X4 Y5]
+ (-0.004424855449441869) [Y1 Y2 Y4 Y5]
+ (-0.004424855449441869) [X1 X2 X4 X5]
+ (-0.004424855449441869) [X1 Y2 Y4 X5]
+ (-0.0034795118903343312) [Y2 Z3 Z5 Y6]
+ (-0.0034795118903343312) [X2 Z3 Z5 X6]
+ (-0.0034795118903343312) [Y3 Z4 Z6 Y7]
+ (-0.0034795118903343312) [X3 Z4 Z6 X7]
+ (-0.002745836470186819) [Y0 Y1 X4 X5]
+ (-0.002745836470186819) [X0 X1 Y4 Y5]
+ (-0.001799219493663012) [Y1 X2 X10 Y11]
+ (-0.001799219493663012) [Y1 Y2 Y10 Y11]
+ (-0.001799219493663012) [X1 X2 X10 X11]
+ (-0.001799219493663012) [X1 Y2 Y10 X11]
+ (-0.0002921986261110536) [Y7 Y8 X9 X10]
+ (-0.0002921986261110536) [X7 X8 Y9 Y10]
+ (-8.194261371363485e-06) [Z10 Y11 Z12 Y13]
+ (-8.194261371363485e-06) [Z10 X11 Z12 X13]
+ (-7.801707499755374e-06) [Y2 Z3 Y4 Z11]
+ (-7.801707499755374e-06) [X2 Z3 X4 Z11]
+ (-7.801707499755374e-06) [Y3 Z4 Y5 Z10]
+ (-7.801707499755374e-06) [X3 Z4 X5 Z10]
+ (-4.643051068028934e-06) [Y3 X4 X10 Y11]
+ (-4.643051068028934e-06) [Y3 Y4 Y10 Y11]
+ (-4.643051068028934e-06) [X3 X4 X10 X11]
+ (-4.643051068028934e-06) [X3 Y4 Y10 X11]
+ (-4.588855155332776e-06) [Y4 Z5 Y6 Z13]
+ (-4.588855155332776e-06) [X4 Z5 X6 Z13]
+ (-4.588855155332776e-06) [Y5 Z6 Y7 Z12]
+ (-4.588855155332776e-06) [X5 Z6 X7 Z12]
+ (-4.556569217660564e-06) [Y5 X6 X12 Y13]
+ (-4.556569217660564e-06) [Y5 Y6 Y12 Y13]
+ (-4.556569217660564e-06) [X5 X6 X12 X13]
+ (-4.556569217660564e-06) [X5 Y6 Y12 X13]
+ (-3.694513294075345e-06) [Y4 X5 X11 Y12]
+ (-3.694513294075345e-06) [Y4 Y5 Y11 Y12]
+ (-3.694513294075345e-06) [X4 X5 X11 X12]
+ (-3.694513294075345e-06) [X4 Y5 Y11 X12]
+ (-3.3440815565858803e-06) [Z0 Y5 Z6 Y7]
+ (-3.3440815565858803e-06) [Z0 X5 Z6 X7]
+ (-3.3440815565858803e-06) [Z1 Y4 Z5 Y6]
+ (-3.3440815565858803e-06) [Z1 X4 Z5 X6]
+ (-3.158656431726441e-06) [Y2 Z3 Y4 Z10]
+ (-3.158656431726441e-06) [X2 Z3 X4 Z10]
+ (-3.158656431726441e-06) [Y3 Z4 Y5 Z11]
+ (-3.158656431726441e-06) [X3 Z4 X5 Z11]
+ (-3.0993492436994905e-06) [Z0 Y4 Z5 Y6]
+ (-3.0993492436994905e-06) [Z0 X4 Z5 X6]
+ (-3.0993492436994905e-06) [Z1 Y5 Z6 Y7]
+ (-3.0993492436994905e-06) [Z1 X5 Z6 X7]
+ (-2.8909678814064697e-06) [Z6 Y11 Z12 Y13]
+ (-2.8909678814064697e-06) [Z6 X11 Z12 X13]
+ (-2.8909678814064697e-06) [Z7 Y10 Z11 Y12]
+ (-2.8909678814064697e-06) [Z7 X10 Z11 X12]
+ (-2.1776646045898024e-06) [Z0 Y10 Z11 Y12]
+ (-2.1776646045898024e-06) [Z0 X10 Z11 X12]
+ (-2.1776646045898024e-06) [Z1 Y11 Z12 Y13]
+ (-2.1776646045898024e-06) [Z1 X11 Z12 X13]
+ (-1.881850183277559e-06) [Y4 Z5 Y6 Z9]
+ (-1.881850183277559e-06) [X4 Z5 X6 Z9]
+ (-1.881850183277559e-06) [Y5 Z6 Y7 Z8]
+ (-1.881850183277559e-06) [X5 Z6 X7 Z8]
+ (-1.8551201212309932e-06) [Z6 Y10 Z11 Y12]
+ (-1.8551201212309932e-06) [Z6 X10 Z11 X12]
+ (-1.8551201212309932e-06) [Z7 Y11 Z12 Y13]
+ (-1.8551201212309932e-06) [Z7 X11 Z12 X13]
+ (-1.8540608580269639e-06) [Y4 Z5 Y6 Z7]
+ (-1.8540608580269639e-06) [X4 Z5 X6 Z7]
+ (-1.816303169454619e-06) [Z4 Y11 Z12 Y13]
+ (-1.816303169454619e-06) [Z4 X11 Z12 X13]
+ (-1.816303169454619e-06) [Z5 Y10 Z11 Y12]
+ (-1.816303169454619e-06) [Z5 X10 Z11 X12]
+ (-1.6923978284721703e-06) [Y4 Z5 Y6 Z10]
+ (-1.6923978284721703e-06) [X4 Z5 X6 Z10]
+ (-1.6923978284721703e-06) [Y5 Z6 Y7 Z11]
+ (-1.6923978284721703e-06) [X5 Z6 X7 Z11]
+ (-1.614879413485907e-06) [Z0 Y11 Z12 Y13]
+ (-1.614879413485907e-06) [Z0 X11 Z12 X13]
+ (-1.614879413485907e-06) [Z1 Y10 Z11 Y12]
+ (-1.614879413485907e-06) [Z1 X10 Z11 X12]
+ (-1.597317197514219e-06) [Z8 Y10 Z11 Y12]
+ (-1.597317197514219e-06) [Z8 X10 Z11 X12]
+ (-1.597317197514219e-06) [Z9 Y11 Z12 Y13]
+ (-1.597317197514219e-06) [Z9 X11 Z12 X13]
+ (-1.4548424491035123e-06) [Y3 X4 X6 Y7]
+ (-1.4548424491035123e-06) [Y3 Y4 Y6 Y7]
+ (-1.4548424491035123e-06) [X3 X4 X6 X7]
+ (-1.4548424491035123e-06) [X3 Y4 Y6 X7]
+ (-1.398044908178067e-06) [Y4 Z5 Y6 Z8]
+ (-1.398044908178067e-06) [X4 Z5 X6 Z8]
+ (-1.398044908178067e-06) [Y5 Z6 Y7 Z9]
+ (-1.398044908178067e-06) [X5 Z6 X7 Z9]
+ (-1.195489010036633e-06) [Y2 Z3 Y4 Z7]
+ (-1.195489010036633e-06) [X2 Z3 X4 Z7]
+ (-1.195489010036633e-06) [Y3 Z4 Y5 Z6]
+ (-1.195489010036633e-06) [X3 Z4 X5 Z6]
+ (-1.1908508084519596e-06) [Z0 Y3 Z4 Y5]
+ (-1.1908508084519596e-06) [Z0 X3 Z4 X5]
+ (-1.1908508084519596e-06) [Z1 Y2 Z3 Y4]
+ (-1.1908508084519596e-06) [Z1 X2 Z3 X4]
+ (-1.1708301370589338e-06) [Z2 Y5 Z6 Y7]
+ (-1.1708301370589338e-06) [Z2 X5 Z6 X7]
+ (-1.1708301370589338e-06) [Z3 Y4 Z5 Y6]
+ (-1.1708301370589338e-06) [Z3 X4 Z5 X6]
+ (-1.0632283420967044e-06) [Z2 Y10 Z11 Y12]
+ (-1.0632283420967044e-06) [Z2 X10 Z11 X12]
+ (-1.0632283420967044e-06) [Z3 Y11 Z12 Y13]
+ (-1.0632283420967044e-06) [Z3 X11 Z12 X13]
+ (-1.0358477601754768e-06) [Y6 X7 X11 Y12]
+ (-1.0358477601754768e-06) [Y6 Y7 Y11 Y12]
+ (-1.0358477601754768e-06) [X6 X7 X11 X12]
+ (-1.0358477601754768e-06) [X6 Y7 Y11 X12]
+ (-9.509249752235663e-07) [Z2 Y4 Z5 Y6]
+ (-9.509249752235663e-07) [Z2 X4 Z5 X6]
+ (-9.509249752235663e-07) [Z3 Y5 Z6 Y7]
+ (-9.509249752235663e-07) [Z3 X5 Z6 X7]
+ (-9.344557774031568e-07) [Z8 Y11 Z12 Y13]
+ (-9.344557774031568e-07) [Z8 X11 Z12 X13]
+ (-9.344557774031568e-07) [Z9 Y10 Z11 Y12]
+ (-9.344557774031568e-07) [Z9 X10 Z11 X12]
+ (-8.337746755311486e-07) [Z0 Y2 Z3 Y4]
+ (-8.337746755311486e-07) [Z0 X2 Z3 X4]
+ (-8.337746755311486e-07) [Z1 Y3 Z4 Y5]
+ (-8.337746755311486e-07) [Z1 X3 Z4 X5]
+ (-7.956895372726861e-07) [Y3 X4 X8 Y9]
+ (-7.956895372726861e-07) [Y3 Y4 Y8 Y9]
+ (-7.956895372726861e-07) [X3 X4 X8 X9]
+ (-7.956895372726861e-07) [X3 Y4 Y8 X9]
+ (-7.764994118720698e-07) [Y2 Z3 Y4 Z5]
+ (-7.764994118720698e-07) [X2 Z3 X4 Z5]
+ (-5.929765816486099e-07) [Z4 Y5 Z6 Y7]
+ (-5.929765816486099e-07) [Z4 X5 Z6 X7]
+ (-5.770052995689446e-07) [Y2 Z3 Y4 Z9]
+ (-5.770052995689446e-07) [X2 Z3 X4 Z9]
+ (-5.770052995689446e-07) [Y3 Z4 Y5 Z8]
+ (-5.770052995689446e-07) [X3 Z4 X5 Z8]
+ (-5.47164774415228e-07) [Y1 Y2 X11 X12]
+ (-5.47164774415228e-07) [X1 X2 Y11 Y12]
+ (-4.838052750994922e-07) [Y5 X6 X8 Y9]
+ (-4.838052750994922e-07) [Y5 Y6 Y8 Y9]
+ (-4.838052750994922e-07) [X5 X6 X8 X9]
+ (-4.838052750994922e-07) [X5 Y6 Y8 X9]
+ (-3.5707613292081075e-07) [Y0 X1 X3 Y4]
+ (-3.5707613292081075e-07) [Y0 Y1 Y3 Y4]
+ (-3.5707613292081075e-07) [X0 X1 X3 X4]
+ (-3.5707613292081075e-07) [X0 Y1 Y3 X4]
+ (-2.4473231288638956e-07) [Y0 X1 X5 Y6]
+ (-2.4473231288638956e-07) [Y0 Y1 Y5 Y6]
+ (-2.4473231288638956e-07) [X0 X1 X5 X6]
+ (-2.4473231288638956e-07) [X0 Y1 Y5 X6]
+ (-2.1990516183536765e-07) [Y2 X3 X5 Y6]
+ (-2.1990516183536765e-07) [Y2 Y3 Y5 Y6]
+ (-2.1990516183536765e-07) [X2 X3 X5 X6]
+ (-2.1990516183536765e-07) [X2 Y3 Y5 X6]
+ (-1.933241277135696e-07) [Y1 X2 X3 Y4]
+ (-1.933241277135696e-07) [X1 Y2 Y3 X4]
+ (-1.2919694862202636e-07) [Y1 Z2 Z3 Y5]
+ (-1.2919694862202636e-07) [X1 Z2 Z3 X5]
+ (1.737933262435942e-07) [Y0 Z1 Z3 Y4]
+ (1.737933262435942e-07) [X0 Z1 Z3 X4]
+ (1.737933262435942e-07) [Y1 Z2 Z4 Y5]
+ (1.737933262435942e-07) [X1 Z2 Z4 X5]
+ (1.933241277135696e-07) [Y1 Y2 X3 X4]
+ (1.933241277135696e-07) [X1 X2 Y3 Y4]
+ (2.1868423770374148e-07) [Y2 Z3 Y4 Z8]
+ (2.1868423770374148e-07) [X2 Z3 X4 Z8]
+ (2.1868423770374148e-07) [Y3 Z4 Y5 Z9]
+ (2.1868423770374148e-07) [X3 Z4 X5 Z9]
+ (2.5935343906687927e-07) [Y2 Z3 Y4 Z6]
+ (2.5935343906687927e-07) [X2 Z3 X4 Z6]
+ (2.5935343906687927e-07) [Y3 Z4 Y5 Z7]
+ (2.5935343906687927e-07) [X3 Z4 X5 Z7]
+ (3.606071868005349e-07) [Y0 Z1 Z2 Y4]
+ (3.606071868005349e-07) [X0 Z1 Z2 X4]
+ (3.606071868005349e-07) [Y1 Z3 Z4 Y5]
+ (3.606071868005349e-07) [X1 Z3 Z4 X5]
+ (5.47164774415228e-07) [Y1 X2 X11 Y12]
+ (5.47164774415228e-07) [X1 Y2 Y11 X12]
+ (5.627851911038957e-07) [Y0 X1 X11 Y12]
+ (5.627851911038957e-07) [Y0 Y1 Y11 Y12]
+ (5.627851911038957e-07) [X0 X1 X11 X12]
+ (5.627851911038957e-07) [X0 Y1 Y11 X12]
+ (6.628614201110622e-07) [Y8 X9 X11 Y12]
+ (6.628614201110622e-07) [Y8 Y9 Y11 Y12]
+ (6.628614201110622e-07) [X8 X9 X11 X12]
+ (6.628614201110622e-07) [X8 Y9 Y11 X12]
+ (1.109440759243866e-06) [Z2 Y11 Z12 Y13]
+ (1.109440759243866e-06) [Z2 X11 Z12 X13]
+ (1.109440759243866e-06) [Z3 Y10 Z11 Y12]
+ (1.109440759243866e-06) [Z3 X10 Z11 X12]
+ (1.6021167405648476e-06) [Z2 Y3 Z4 Y5]
+ (1.6021167405648476e-06) [Z2 X3 Z4 X5]
+ (1.8782101246207256e-06) [Z4 Y10 Z11 Y12]
+ (1.8782101246207256e-06) [Z4 X10 Z11 X12]
+ (1.8782101246207256e-06) [Z5 Y11 Z12 Y13]
+ (1.8782101246207256e-06) [Z5 X11 Z12 X13]
+ (2.1726691013405704e-06) [Y2 X3 X11 Y12]
+ (2.1726691013405704e-06) [Y2 Y3 Y11 Y12]
+ (2.1726691013405704e-06) [X2 X3 X11 X12]
+ (2.1726691013405704e-06) [X2 Y3 Y11 X12]
+ (3.1174479461774806e-06) [Y0 Z2 Z3 Y4]
+ (3.1174479461774806e-06) [X0 Z2 Z3 X4]
+ (3.5390541841496474e-06) [Y2 Z3 Y4 Z12]
+ (3.5390541841496474e-06) [X2 Z3 X4 Z12]
+ (3.5390541841496474e-06) [Y3 Z4 Y5 Z13]
+ (3.5390541841496474e-06) [X3 Z4 X5 Z13]
+ (4.2819138844367255e-06) [Y4 Z5 Y6 Z11]
+ (4.2819138844367255e-06) [X4 Z5 X6 Z11]
+ (4.2819138844367255e-06) [Y5 Z6 Y7 Z10]
+ (4.2819138844367255e-06) [X5 Z6 X7 Z10]
+ (5.2758831216445055e-06) [Y3 X4 X12 Y13]
+ (5.2758831216445055e-06) [Y3 Y4 Y12 Y13]
+ (5.2758831216445055e-06) [X3 X4 X12 X13]
+ (5.2758831216445055e-06) [X3 Y4 Y12 X13]
+ (5.974311712908897e-06) [Y5 X6 X10 Y11]
+ (5.974311712908897e-06) [Y5 Y6 Y10 Y11]
+ (5.974311712908897e-06) [X5 X6 X10 X11]
+ (5.974311712908897e-06) [X5 Y6 Y10 X11]
+ (7.95441317560359e-06) [Y10 Z11 Y12 Z13]
+ (7.95441317560359e-06) [X10 Z11 X12 Z13]
+ (8.814937305794155e-06) [Y2 Z3 Y4 Z13]
+ (8.814937305794155e-06) [X2 Z3 X4 Z13]
+ (8.814937305794155e-06) [Y3 Z4 Y5 Z12]
+ (8.814937305794155e-06) [X3 Z4 X5 Z12]
+ (0.0002921986261110536) [Y7 X8 X9 Y10]
+ (0.0002921986261110536) [X7 Y8 Y9 X10]
+ (0.0004956762314916402) [Y2 Z4 Z5 Y6]
+ (0.0004956762314916402) [X2 Z4 Z5 X6]
+ (0.0011059037691896886) [Y0 Z1 Y2 Z5]
+ (0.0011059037691896886) [X0 Z1 X2 Z5]
+ (0.0011059037691896886) [Y1 Z2 Y3 Z4]
+ (0.0011059037691896886) [X1 Z2 X3 Z4]
+ (0.0016638798784907051) [Y2 Z3 Z4 Y6]
+ (0.0016638798784907051) [X2 Z3 Z4 X6]
+ (0.0016638798784907051) [Y3 Z5 Z6 Y7]
+ (0.0016638798784907051) [X3 Z5 Z6 X7]
+ (0.0017560707018412296) [Y0 Z1 Y2 Z11]
+ (0.0017560707018412296) [X0 Z1 X2 Z11]
+ (0.0017560707018412296) [Y1 Z2 Y3 Z10]
+ (0.0017560707018412296) [X1 Z2 X3 Z10]
+ (0.002326230623158082) [Y0 Z1 Y2 Z13]
+ (0.002326230623158082) [X0 Z1 X2 Z13]
+ (0.002326230623158082) [Y1 Z2 Y3 Z12]
+ (0.002326230623158082) [X1 Z2 X3 Z12]
+ (0.002745836470186819) [Y0 X1 X4 Y5]
+ (0.002745836470186819) [X0 Y1 Y4 X5]
+ (0.002929768674751057) [Y0 Z1 Y2 Z9]
+ (0.002929768674751057) [X0 Z1 X2 Z9]
+ (0.002929768674751057) [Y1 Z2 Y3 Z8]
+ (0.002929768674751057) [X1 Z2 X3 Z8]
+ (0.0032769719312316726) [Y0 Z1 Y2 Z3]
+ (0.0032769719312316726) [X0 Z1 X2 Z3]
+ (0.003347617530666201) [Y0 Z1 Y2 Z7]
+ (0.003347617530666201) [X0 Z1 X2 Z7]
+ (0.003347617530666201) [Y1 Z2 Y3 Z6]
+ (0.003347617530666201) [X1 Z2 X3 Z6]
+ (0.0035552901955042417) [Y0 Z1 Y2 Z10]
+ (0.0035552901955042417) [X0 Z1 X2 Z10]
+ (0.0035552901955042417) [Y1 Z2 Y3 Z11]
+ (0.0035552901955042417) [X1 Z2 X3 Z11]
+ (0.005143391768825037) [Y3 Y4 X5 X6]
+ (0.005143391768825037) [X3 X4 Y5 Y6]
+ (0.005283776488402954) [Y0 X1 X12 Y13]
+ (0.005283776488402954) [X0 Y1 Y12 X13]
+ (0.005530759218631558) [Y0 Z1 Y2 Z4]
+ (0.005530759218631558) [X0 Z1 X2 Z4]
+ (0.005530759218631558) [Y1 Z2 Y3 Z5]
+ (0.005530759218631558) [X1 Z2 X3 Z5]
+ (0.006087822480561846) [Y8 X9 X12 Y13]
+ (0.006087822480561846) [X8 Y9 Y12 X13]
+ (0.006509361201177239) [Y0 X1 X8 Y9]
+ (0.006509361201177239) [X0 Y1 Y8 X9]
+ (0.0068881943529705714) [Y0 X1 X6 Y7]
+ (0.0068881943529705714) [X0 Y1 Y6 X7]
+ (0.006901238249797279) [Y0 Z1 Y2 Z12]
+ (0.006901238249797279) [X0 Z1 X2 Z12]
+ (0.006901238249797279) [Y1 Z2 Y3 Z13]
+ (0.006901238249797279) [X1 Z2 X3 Z13]
+ (0.0071569349198569564) [Y4 X5 X8 Y9]
+ (0.0071569349198569564) [X4 Y5 Y8 X9]
+ (0.007731425250775262) [Y0 X1 X10 Y11]
+ (0.007731425250775262) [X0 Y1 Y10 X11]
+ (0.008032520918821421) [Y0 Z1 Y2 Z6]
+ (0.008032520918821421) [X0 Z1 X2 Z6]
+ (0.008032520918821421) [Y1 Z2 Y3 Z7]
+ (0.008032520918821421) [X1 Z2 X3 Z7]
+ (0.0095607057291359) [Y8 X9 X10 Y11]
+ (0.0095607057291359) [X8 Y9 Y10 X11]
+ (0.0110550205961321) [Y0 Z1 Y2 Z8]
+ (0.0110550205961321) [X0 Z1 X2 Z8]
+ (0.0110550205961321) [Y1 Z2 Y3 Z9]
+ (0.0110550205961321) [X1 Z2 X3 Z9]
+ (0.011285190200840898) [Y5 Y6 X11 X12]
+ (0.011285190200840898) [X5 X6 Y11 Y12]
+ (0.011307274008848065) [Y7 Z8 Z9 Y11]
+ (0.011307274008848065) [X7 Z8 Z9 X11]
+ (0.011982389010247934) [Y4 X5 X6 Y7]
+ (0.011982389010247934) [X4 Y5 Y6 X7]
+ (0.013873381748426113) [Y6 X7 X8 Y9]
+ (0.013873381748426113) [X6 Y7 Y8 X9]
+ (0.01458364890761273) [Y0 X1 X2 Y3]
+ (0.01458364890761273) [X0 Y1 Y2 X3]
+ (0.015577208063976429) [Y2 X3 X12 Y13]
+ (0.015577208063976429) [X2 Y3 Y12 X13]
+ (0.01736611899465138) [Y6 X7 X12 Y13]
+ (0.01736611899465138) [X6 Y7 Y12 X13]
+ (0.0176800679524815) [Y4 X5 X10 Y11]
+ (0.0176800679524815) [X4 Y5 Y10 X11]
+ (0.01782514099578641) [Y6 X7 X10 Y11]
+ (0.01782514099578641) [X6 Y7 Y10 X11]
+ (0.01902824244384726) [Y3 X4 X11 Y12]
+ (0.01902824244384726) [X3 Y4 Y11 X12]
+ (0.02538465750845734) [Y2 X3 X10 Y11]
+ (0.02538465750845734) [X2 Y3 Y10 X11]
+ (0.028685183716106014) [Y10 X11 X12 Y13]
+ (0.028685183716106014) [X10 Y11 Y12 X13]
+ (0.029812424517345705) [Y6 Z7 Z8 Y10]
+ (0.029812424517345705) [X6 Z7 Z8 X10]
+ (0.029812424517345705) [Y7 Z9 Z10 Y11]
+ (0.029812424517345705) [X7 Z9 Z10 X11]
+ (0.03010462314345676) [Y6 Z7 Z9 Y10]
+ (0.03010462314345676) [X6 Z7 Z9 X10]
+ (0.03010462314345676) [Y7 Z8 Z10 Y11]
+ (0.03010462314345676) [X7 Z8 Z10 X11]
+ (0.030787505389143932) [Y6 Z8 Z9 Y10]
+ (0.030787505389143932) [X6 Z8 Z9 X10]
+ (0.031143817988967128) [Y2 X3 X6 Y7]
+ (0.031143817988967128) [X2 Y3 Y6 X7]
+ (0.03583956795335344) [Y2 X3 X4 Y5]
+ (0.03583956795335344) [X2 Y3 Y4 X5]
+ (0.03619412355904266) [Y2 X3 X8 Y9]
+ (0.03619412355904266) [X2 Y3 Y8 X9]
+ (0.03831467029480388) [Y4 X5 X12 Y13]
+ (0.03831467029480388) [X4 Y5 Y12 X13]
+ (0.1043306478065142) [Z0 Y1 Z2 Y3]
+ (0.1043306478065142) [Z0 X1 Z2 X3]
+ (-0.12133276911042358) [Y2 Z3 Z4 Z5 Y6]
+ (-0.12133276911042358) [X2 Z3 Z4 Z5 X6]
+ (-0.12133276911042358) [Y3 Z4 Z5 Z6 Y7]
+ (-0.12133276911042358) [X3 Z4 Z5 Z6 X7]
+ (3.2020768802919665e-06) [Y0 Z1 Z2 Z3 Y4]
+ (3.2020768802919665e-06) [X0 Z1 Z2 Z3 X4]
+ (3.2020768802919665e-06) [Y1 Z2 Z3 Z4 Y5]
+ (3.2020768802919665e-06) [X1 Z2 Z3 Z4 X5]
+ (0.22848106564918783) [Y6 Z7 Z8 Z9 Y10]
+ (0.22848106564918783) [X6 Z7 Z8 Z9 X10]
+ (0.22848106564918785) [Y7 Z8 Z9 Z10 Y11]
+ (0.22848106564918785) [X7 Z8 Z9 Z10 X11]
+ (-0.03276765782329041) [Z0 Y3 Z4 Z5 Z6 Y7]
+ (-0.03276765782329041) [Z0 X3 Z4 Z5 Z6 X7]
+ (-0.03276765782329041) [Z1 Y2 Z3 Z4 Z5 Y6]
+ (-0.03276765782329041) [Z1 X2 Z3 Z4 Z5 X6]
+ (-0.027115036845273055) [Z0 Y2 Z3 Z4 Z5 Y6]
+ (-0.027115036845273055) [Z0 X2 Z3 Z4 Z5 X6]
+ (-0.027115036845273055) [Z1 Y3 Z4 Z5 Z6 Y7]
+ (-0.027115036845273055) [Z1 X3 Z4 Z5 Z6 X7]
+ (-0.02599617759802124) [Y2 Z3 Z4 Z5 Y6 Z7]
+ (-0.02599617759802124) [X2 Z3 Z4 Z5 X6 Z7]
+ (-0.017561202409646152) [Y2 Z3 Z4 Z5 Y6 Z9]
+ (-0.017561202409646152) [X2 Z3 Z4 Z5 X6 Z9]
+ (-0.017561202409646152) [Y3 Z4 Z5 Z6 Y7 Z8]
+ (-0.017561202409646152) [X3 Z4 Z5 Z6 X7 Z8]
+ (-0.014564531231173034) [Y7 Z8 Z9 X10 X12 Y13]
+ (-0.014564531231173034) [Y7 Z8 Z9 Y10 Y12 Y13]
+ (-0.014564531231173034) [X7 Z8 Z9 X10 X12 X13]
+ (-0.014564531231173034) [X7 Z8 Z9 Y10 Y12 X13]
+ (-0.012215040997613925) [Y4 Z5 Y6 Y11 Z12 Y13]
+ (-0.012215040997613925) [Y4 Z5 Y6 X11 Z12 X13]
+ (-0.012215040997613925) [X4 Z5 X6 Y11 Z12 Y13]
+ (-0.012215040997613925) [X4 Z5 X6 X11 Z12 X13]
+ (-0.012215040997613925) [Y5 Z6 Y7 Y10 Z11 Y12]
+ (-0.012215040997613925) [Y5 Z6 Y7 X10 Z11 X12]
+ (-0.012215040997613925) [X5 Z6 X7 Y10 Z11 Y12]
+ (-0.012215040997613925) [X5 Z6 X7 X10 Z11 X12]
+ (-0.011756013419819245) [Y3 Z4 Z5 X6 X8 Y9]
+ (-0.011756013419819245) [Y3 Z4 Z5 Y6 Y8 Y9]
+ (-0.011756013419819245) [X3 Z4 Z5 X6 X8 X9]
+ (-0.011756013419819245) [X3 Z4 Z5 Y6 Y8 X9]
+ (-0.00876482757568875) [Y2 Z3 Z4 X5 X11 Y12]
+ (-0.00876482757568875) [Y2 Z3 Z4 Y5 Y11 Y12]
+ (-0.00876482757568875) [X2 Z3 Z4 X5 X11 X12]
+ (-0.00876482757568875) [X2 Z3 Z4 Y5 Y11 X12]
+ (-0.00876482757568875) [Y3 X4 X10 Z11 Z12 Y13]
+ (-0.00876482757568875) [Y3 Y4 Y10 Z11 Z12 Y13]
+ (-0.00876482757568875) [X3 X4 X10 Z11 Z12 X13]
+ (-0.00876482757568875) [X3 Y4 Y10 Z11 Z12 X13]
+ (-0.008125251921381043) [Y0 Z1 Z2 Y3 X8 X9]
+ (-0.008125251921381043) [X0 Z1 Z2 X3 Y8 Y9]
+ (-0.007306759928832928) [Y4 X5 X7 Z8 Z9 Y10]
+ (-0.007306759928832928) [Y4 Y5 Y7 Z8 Z9 Y10]
+ (-0.007306759928832928) [X4 X5 X7 Z8 Z9 X10]
+ (-0.007306759928832928) [X4 Y5 Y7 Z8 Z9 X10]
+ (-0.005805188989826909) [Y2 Z3 Z4 Z5 Y6 Z8]
+ (-0.005805188989826909) [X2 Z3 Z4 Z5 X6 Z8]
+ (-0.005805188989826909) [Y3 Z4 Z5 Z6 Y7 Z9]
+ (-0.005805188989826909) [X3 Z4 Z5 Z6 X7 Z9]
+ (-0.005652620978017352) [Y0 X1 X3 Z4 Z5 Y6]
+ (-0.005652620978017352) [Y0 Y1 Y3 Z4 Z5 Y6]
+ (-0.005652620978017352) [X0 X1 X3 Z4 Z5 X6]
+ (-0.005652620978017352) [X0 Y1 Y3 Z4 Z5 X6]
+ (-0.005143391768825037) [Y2 Z3 Y4 Y5 Z6 Y7]
+ (-0.005143391768825037) [Y2 Z3 Y4 X5 Z6 X7]
+ (-0.005143391768825037) [X2 Z3 X4 Y5 Z6 Y7]
+ (-0.005143391768825037) [X2 Z3 X4 X5 Z6 X7]
+ (-0.0046849033881552204) [Y0 Z1 Z2 Y3 X6 X7]
+ (-0.0046849033881552204) [X0 Z1 Z2 X3 Y6 Y7]
+ (-0.004668620318776305) [Y1 X2 X7 Z8 Z9 Y10]
+ (-0.004668620318776305) [X1 Y2 Y7 Z8 Z9 X10]
+ (-0.004575007626639198) [Y0 Z1 Z2 Y3 X12 X13]
+ (-0.004575007626639198) [X0 Z1 Z2 X3 Y12 Y13]
+ (-0.004424855449441869) [Y0 Z1 Z2 Y3 X4 X5]
+ (-0.004424855449441869) [X0 Z1 Z2 X3 Y4 Y5]
+ (-0.004158797381840046) [Y3 Z4 Z5 X6 X12 Y13]
+ (-0.004158797381840046) [Y3 Z4 Z5 Y6 Y12 Y13]
+ (-0.004158797381840046) [X3 Z4 Z5 X6 X12 X13]
+ (-0.004158797381840046) [X3 Z4 Z5 Y6 Y12 X13]
+ (-0.003493790359890118) [Y2 Z3 Z4 Z5 Y6 Z13]
+ (-0.003493790359890118) [X2 Z3 Z4 Z5 X6 Z13]
+ (-0.003493790359890118) [Y3 Z4 Z5 Z6 Y7 Z12]
+ (-0.003493790359890118) [X3 Z4 Z5 Z6 X7 Z12]
+ (-0.002779026799025548) [Y1 Z2 Z3 Z4 Z5 Y7]
+ (-0.002779026799025548) [X1 Z2 Z3 Z4 Z5 X7]
+ (-0.0022939566113524814) [Y1 X2 X3 Z4 Z5 Y6]
+ (-0.0022939566113524814) [X1 Y2 Y3 Z4 Z5 X6]
+ (-0.001799219493663012) [Y0 Z1 Z2 Y3 X10 X11]
+ (-0.001799219493663012) [X0 Z1 Z2 X3 Y10 Y11]
+ (-0.0017278753941369612) [Y1 Z2 Z3 X4 X11 Y12]
+ (-0.0017278753941369612) [X1 Z2 Z3 Y4 Y11 X12]
+ (-0.0009298507967730257) [Y4 Z5 Y6 X10 Z11 X12]
+ (-0.0009298507967730257) [X4 Z5 X6 Y10 Z11 Y12]
+ (-0.0009298507967730257) [Y5 Z6 Y7 X11 Z12 X13]
+ (-0.0009298507967730257) [X5 Z6 X7 Y11 Z12 Y13]
+ (-0.0008533856254125543) [Y1 Z2 Z3 Y4 X5 X6]
+ (-0.0008533856254125543) [X1 Z2 Z3 X4 Y5 Y6]
+ (-0.0008145313270956612) [Y2 Z3 Z4 Z5 Y6 Z10]
+ (-0.0008145313270956612) [X2 Z3 Z4 Z5 X6 Z10]
+ (-0.0008145313270956612) [Y3 Z4 Z5 Z6 Y7 Z11]
+ (-0.0008145313270956612) [X3 Z4 Z5 Z6 X7 Z11]
+ (-7.735036880590125e-05) [Y0 X1 X7 Z8 Z9 Y10]
+ (-7.735036880590125e-05) [Y0 Y1 Y7 Z8 Z9 Y10]
+ (-7.735036880590125e-05) [X0 X1 X7 Z8 Z9 X10]
+ (-7.735036880590125e-05) [X0 Y1 Y7 Z8 Z9 X10]
+ (-8.774817863763433e-06) [Y4 Z5 Z6 Z7 Z8 Y10]
+ (-8.774817863763433e-06) [X4 Z5 Z6 Z7 Z8 X10]
+ (-8.774817863763433e-06) [Y5 Z6 Z7 Z9 Z10 Y11]
+ (-8.774817863763433e-06) [X5 Z6 Z7 Z9 Z10 X11]
+ (-7.518362215024336e-06) [Y4 Z5 Z7 Z8 Z9 Y10]
+ (-7.518362215024336e-06) [X4 Z5 Z7 Z8 Z9 X10]
+ (-7.518362215024336e-06) [Y5 Z6 Z8 Z9 Z10 Y11]
+ (-7.518362215024336e-06) [X5 Z6 Z8 Z9 Z10 X11]
+ (-7.444344675190199e-06) [Y4 Z5 Z6 Z7 Z9 Y10]
+ (-7.444344675190199e-06) [X4 Z5 Z6 Z7 Z9 X10]
+ (-7.444344675190199e-06) [Y5 Z6 Z7 Z8 Z10 Y11]
+ (-7.444344675190199e-06) [X5 Z6 Z7 Z8 Z10 X11]
+ (-6.524373847946506e-06) [Y6 Z7 Z8 Z9 Z10 Y12]
+ (-6.524373847946506e-06) [X6 Z7 Z8 Z9 Z10 X12]
+ (-6.524373847946506e-06) [Y7 Z8 Z9 Z11 Z12 Y13]
+ (-6.524373847946506e-06) [X7 Z8 Z9 Z11 Z12 X13]
+ (-6.290028432497119e-06) [Y4 Z5 Z6 Z8 Z9 Y10]
+ (-6.290028432497119e-06) [X4 Z5 Z6 Z8 Z9 X10]
+ (-6.290028432497119e-06) [Y5 Z7 Z8 Z9 Z10 Y11]
+ (-6.290028432497119e-06) [X5 Z7 Z8 Z9 Z10 X11]
+ (-5.974311712908896e-06) [Y4 Z5 Z6 X7 X10 Y11]
+ (-5.974311712908896e-06) [X4 Z5 Z6 Y7 Y10 X11]
+ (-5.2758831216445055e-06) [Y2 Z3 Z4 X5 X12 Y13]
+ (-5.2758831216445055e-06) [X2 Z3 Z4 Y5 Y12 X13]
+ (-4.643051068028934e-06) [Y2 Z3 Z4 Y5 X10 X11]
+ (-4.643051068028934e-06) [X2 Z3 Z4 X5 Y10 Y11]
+ (-4.556569217660564e-06) [Y4 Z5 Z6 Y7 X12 X13]
+ (-4.556569217660564e-06) [X4 Z5 Z6 X7 Y12 Y13]
+ (-4.253224225235523e-06) [Y4 Z6 Z7 Z8 Z9 Y10]
+ (-4.253224225235523e-06) [X4 Z6 Z7 Z8 Z9 X10]
+ (-3.7696594514975743e-06) [Y6 Z8 Z9 Z10 Z11 Y12]
+ (-3.7696594514975743e-06) [X6 Z8 Z9 Z10 Z11 X12]
+ (-3.694513294075345e-06) [Y4 Y5 X10 Z11 Z12 X13]
+ (-3.694513294075345e-06) [X4 X5 Y10 Z11 Z12 Y13]
+ (-3.610297130087252e-06) [Y6 Z7 Z9 Z10 Z11 Y12]
+ (-3.610297130087252e-06) [X6 Z7 Z9 Z10 Z11 X12]
+ (-3.610297130087252e-06) [Y7 Z8 Z10 Z11 Z12 Y13]
+ (-3.610297130087252e-06) [X7 Z8 Z10 Z11 Z12 X13]
+ (-3.3131454999498387e-06) [Y7 Z8 Z9 Y10 X11 X12]
+ (-3.3131454999498387e-06) [X7 Z8 Z9 X10 Y11 Y12]
+ (-3.2774831950337234e-06) [Y6 Z7 Z8 Z10 Z11 Y12]
+ (-3.2774831950337234e-06) [X6 Z7 Z8 Z10 Z11 X12]
+ (-3.2774831950337234e-06) [Y7 Z9 Z10 Z11 Z12 Y13]
+ (-3.2774831950337234e-06) [X7 Z9 Z10 Z11 Z12 X13]
+ (-3.2112283479966675e-06) [Y6 Z7 Z8 Z9 Z11 Y12]
+ (-3.2112283479966675e-06) [X6 Z7 Z8 Z9 Z11 X12]
+ (-3.2112283479966675e-06) [Y7 Z8 Z9 Z10 Z12 Y13]
+ (-3.2112283479966675e-06) [X7 Z8 Z9 Z10 Z12 X13]
+ (-3.1513463108547933e-06) [Y3 Y4 X7 Z8 Z9 X10]
+ (-3.1513463108547933e-06) [X3 X4 Y7 Z8 Z9 Y10]
+ (-3.0882507109545547e-06) [Y3 Z4 Z5 Y6 X11 X12]
+ (-3.0882507109545547e-06) [X3 Z4 Z5 X6 Y11 Y12]
+ (-2.1726691013405704e-06) [Y2 X3 X10 Z11 Z12 Y13]
+ (-2.1726691013405704e-06) [X2 Y3 Y10 Z11 Z12 X13]
+ (-1.4548424491035125e-06) [Y2 Z3 Z4 Y5 X6 X7]
+ (-1.4548424491035125e-06) [X2 Z3 Z4 X5 Y6 Y7]
+ (-1.3304731885732335e-06) [Y5 Z6 Z7 Y8 X9 X10]
+ (-1.3304731885732335e-06) [X5 Z6 Z7 X8 Y9 Y10]
+ (-1.2283337825272171e-06) [Y5 X6 X7 Z8 Z9 Y10]
+ (-1.2283337825272171e-06) [X5 Y6 Y7 Z8 Z9 X10]
+ (-1.0358477601754768e-06) [Y6 Y7 X10 Z11 Z12 X13]
+ (-1.0358477601754768e-06) [X6 X7 Y10 Z11 Z12 Y13]
+ (-7.956895372726861e-07) [Y2 Z3 Z4 Y5 X8 X9]
+ (-7.956895372726861e-07) [X2 Z3 Z4 X5 Y8 Y9]
+ (-6.733197741360703e-07) [Y0 Z1 Z2 Z3 Y4 Z10]
+ (-6.733197741360703e-07) [X0 Z1 Z2 Z3 X4 Z10]
+ (-6.733197741360703e-07) [Y1 Z2 Z3 Z4 Y5 Z11]
+ (-6.733197741360703e-07) [X1 Z2 Z3 Z4 X5 Z11]
+ (-6.628614201110622e-07) [Y8 X9 X10 Z11 Z12 Y13]
+ (-6.628614201110622e-07) [X8 Y9 Y10 Z11 Z12 X13]
+ (-6.556281913969781e-07) [Y0 Z1 Y2 X10 Z11 X12]
+ (-6.556281913969781e-07) [X0 Z1 X2 Y10 Z11 Y12]
+ (-6.556281913969781e-07) [Y1 Z2 Y3 X11 Z12 X13]
+ (-6.556281913969781e-07) [X1 Z2 X3 Y11 Z12 Y13]
+ (-6.418291573960156e-07) [Y0 Z1 Y2 Y10 Z11 Y12]
+ (-6.418291573960156e-07) [X0 Z1 X2 X10 Z11 X12]
+ (-6.418291573960156e-07) [Y1 Z2 Y3 Y11 Z12 Y13]
+ (-6.418291573960156e-07) [X1 Z2 X3 X11 Z12 X13]
+ (-5.927453081969475e-07) [Y0 Z1 Z2 Z3 Y4 Z11]
+ (-5.927453081969475e-07) [X0 Z1 Z2 Z3 X4 Z11]
+ (-5.927453081969475e-07) [Y1 Z2 Z3 Z4 Y5 Z10]
+ (-5.927453081969475e-07) [X1 Z2 Z3 Z4 X5 Z10]
+ (-5.627851911038957e-07) [Y0 X1 X10 Z11 Z12 Y13]
+ (-5.627851911038957e-07) [X0 Y1 Y10 Z11 Z12 X13]
+ (-5.287660624144587e-07) [Y0 Z1 Z2 X3 X11 Y12]
+ (-5.287660624144587e-07) [Y0 Z1 Z2 Y3 Y11 Y12]
+ (-5.287660624144587e-07) [X0 Z1 Z2 X3 X11 X12]
+ (-5.287660624144587e-07) [X0 Z1 Z2 Y3 Y11 X12]
+ (-5.287660624144587e-07) [Y1 X2 X10 Z11 Z12 Y13]
+ (-5.287660624144587e-07) [Y1 Y2 Y10 Z11 Z12 Y13]
+ (-5.287660624144587e-07) [X1 X2 X10 Z11 Z12 X13]
+ (-5.287660624144587e-07) [X1 Y2 Y10 Z11 Z12 X13]
+ (-4.838052750994922e-07) [Y4 Z5 Z6 Y7 X8 X9]
+ (-4.838052750994922e-07) [X4 Z5 Z6 X7 Y8 Y9]
+ (-3.5707613292081075e-07) [Y0 Y1 X2 Z3 Z4 X5]
+ (-3.5707613292081075e-07) [X0 X1 Y2 Z3 Z4 Y5]
+ (-3.328139350535286e-07) [Y7 X8 X9 Z10 Z11 Y12]
+ (-3.328139350535286e-07) [X7 Y8 Y9 Z10 Z11 X12]
+ (-3.0868265651063305e-07) [Y1 Z2 Z3 X4 X12 Y13]
+ (-3.0868265651063305e-07) [Y1 Z2 Z3 Y4 Y12 Y13]
+ (-3.0868265651063305e-07) [X1 Z2 Z3 X4 X12 X13]
+ (-3.0868265651063305e-07) [X1 Z2 Z3 Y4 Y12 X13]
+ (-2.4473231288638956e-07) [Y0 Y1 X4 Z5 Z6 X7]
+ (-2.4473231288638956e-07) [X0 X1 Y4 Z5 Z6 Y7]
+ (-2.3713289479465785e-07) [Y1 Z2 Z3 X4 X8 Y9]
+ (-2.3713289479465785e-07) [Y1 Z2 Z3 Y4 Y8 Y9]
+ (-2.3713289479465785e-07) [X1 Z2 Z3 X4 X8 X9]
+ (-2.3713289479465785e-07) [X1 Z2 Z3 Y4 Y8 X9]
+ (-2.1990516183536765e-07) [Y2 Y3 X4 Z5 Z6 X7]
+ (-2.1990516183536765e-07) [X2 X3 Y4 Z5 Z6 Y7]
+ (-1.933241277135696e-07) [Y0 Z1 Y2 Y3 Z4 Y5]
+ (-1.933241277135696e-07) [Y0 Z1 Y2 X3 Z4 X5]
+ (-1.933241277135696e-07) [X0 Z1 X2 Y3 Z4 Y5]
+ (-1.933241277135696e-07) [X0 Z1 X2 X3 Z4 X5]
+ (-1.839420915519878e-07) [Y1 Z2 Z3 X4 X6 Y7]
+ (-1.839420915519878e-07) [Y1 Z2 Z3 Y4 Y6 Y7]
+ (-1.839420915519878e-07) [X1 Z2 Z3 X4 X6 X7]
+ (-1.839420915519878e-07) [X1 Z2 Z3 Y4 Y6 X7]
+ (-1.55105391764265e-07) [Y0 Z1 Y2 Y4 Z5 Y6]
+ (-1.55105391764265e-07) [X0 Z1 X2 X4 Z5 X6]
+ (-1.55105391764265e-07) [Y1 Z2 Y3 Y5 Z6 Y7]
+ (-1.55105391764265e-07) [X1 Z2 X3 X5 Z6 X7]
+ (-1.3807781481130456e-07) [Y0 Z1 Y2 X4 Z5 X6]
+ (-1.3807781481130456e-07) [X0 Z1 X2 Y4 Z5 Y6]
+ (-1.3807781481130456e-07) [Y0 Z1 Y2 Y5 Z6 Y7]
+ (-1.3807781481130456e-07) [Y0 Z1 Y2 X5 Z6 X7]
+ (-1.3807781481130456e-07) [X0 Z1 X2 Y5 Z6 Y7]
+ (-1.3807781481130456e-07) [X0 Z1 X2 X5 Z6 X7]
+ (-1.3807781481130456e-07) [Y1 Z2 Y3 Y4 Z5 Y6]
+ (-1.3807781481130456e-07) [Y1 Z2 Y3 X4 Z5 X6]
+ (-1.3807781481130456e-07) [X1 Z2 X3 Y4 Z5 Y6]
+ (-1.3807781481130456e-07) [X1 Z2 X3 X4 Z5 X6]
+ (-1.3807781481130456e-07) [Y1 Z2 Y3 X5 Z6 X7]
+ (-1.3807781481130456e-07) [X1 Z2 X3 Y5 Z6 Y7]
+ (-1.2919694862202636e-07) [Y0 Z1 Z2 Z3 Y4 Z5]
+ (-1.2919694862202636e-07) [X0 Z1 Z2 Z3 X4 Z5]
+ (-1.1076325598165333e-07) [Y0 Z1 Y2 Y11 Z12 Y13]
+ (-1.1076325598165333e-07) [Y0 Z1 Y2 X11 Z12 X13]
+ (-1.1076325598165333e-07) [X0 Z1 X2 Y11 Z12 Y13]
+ (-1.1076325598165333e-07) [X0 Z1 X2 X11 Z12 X13]
+ (-1.1076325598165333e-07) [Y1 Z2 Y3 Y10 Z11 Y12]
+ (-1.1076325598165333e-07) [Y1 Z2 Y3 X10 Z11 X12]
+ (-1.1076325598165333e-07) [X1 Z2 X3 Y10 Z11 Y12]
+ (-1.1076325598165333e-07) [X1 Z2 X3 X10 Z11 X12]
+ (8.05744659391227e-08) [Y1 Z2 Z3 X4 X10 Y11]
+ (8.05744659391227e-08) [Y1 Z2 Z3 Y4 Y10 Y11]
+ (8.05744659391227e-08) [X1 Z2 Z3 X4 X10 X11]
+ (8.05744659391227e-08) [X1 Z2 Z3 Y4 Y10 X11]
+ (8.649310135610358e-08) [Y0 Z1 Z2 Z3 Y4 Z9]
+ (8.649310135610358e-08) [X0 Z1 Z2 Z3 X4 Z9]
+ (8.649310135610358e-08) [Y1 Z2 Z3 Z4 Y5 Z8]
+ (8.649310135610358e-08) [X1 Z2 Z3 Z4 X5 Z8]
+ (1.8394209155198774e-07) [Y0 Z1 Z2 Z3 Y4 Z6]
+ (1.8394209155198774e-07) [X0 Z1 Z2 Z3 X4 Z6]
+ (1.8394209155198774e-07) [Y1 Z2 Z3 Z4 Y5 Z7]
+ (1.8394209155198774e-07) [X1 Z2 Z3 Z4 X5 Z7]
+ (2.1990516183536765e-07) [Y2 X3 X4 Z5 Z6 Y7]
+ (2.1990516183536765e-07) [X2 Y3 Y4 Z5 Z6 X7]
+ (2.4473231288638956e-07) [Y0 X1 X4 Z5 Z6 Y7]
+ (2.4473231288638956e-07) [X0 Y1 Y4 Z5 Z6 X7]
+ (3.2362599615076146e-07) [Y0 Z1 Z2 Z3 Y4 Z8]
+ (3.2362599615076146e-07) [X0 Z1 Z2 Z3 X4 Z8]
+ (3.2362599615076146e-07) [Y1 Z2 Z3 Z4 Y5 Z9]
+ (3.2362599615076146e-07) [X1 Z2 Z3 Z4 X5 Z9]
+ (3.328139350535286e-07) [Y7 Y8 X9 Z10 Z11 X12]
+ (3.328139350535286e-07) [X7 X8 Y9 Z10 Z11 Y12]
+ (3.5707613292081075e-07) [Y0 X1 X2 Z3 Z4 Y5]
+ (3.5707613292081075e-07) [X0 Y1 Y2 Z3 Z4 X5]
+ (4.838052750994922e-07) [Y4 Z5 Z6 X7 X8 Y9]
+ (4.838052750994922e-07) [X4 Z5 Z6 Y7 Y8 X9]
+ (5.627851911038957e-07) [Y0 Y1 X10 Z11 Z12 X13]
+ (5.627851911038957e-07) [X0 X1 Y10 Z11 Z12 Y13]
+ (6.628614201110622e-07) [Y8 Y9 X10 Z11 Z12 X13]
+ (6.628614201110622e-07) [X8 X9 Y10 Z11 Z12 Y13]
+ (7.956895372726861e-07) [Y2 Z3 Z4 X5 X8 Y9]
+ (7.956895372726861e-07) [X2 Z3 Z4 Y5 Y8 X9]
+ (9.306536651166607e-07) [Y0 Z1 Z2 Z3 Y4 Z13]
+ (9.306536651166607e-07) [X0 Z1 Z2 Z3 X4 Z13]
+ (9.306536651166607e-07) [Y1 Z2 Z3 Z4 Y5 Z12]
+ (9.306536651166607e-07) [X1 Z2 Z3 Z4 X5 Z12]
+ (1.0358477601754768e-06) [Y6 X7 X10 Z11 Z12 Y13]
+ (1.0358477601754768e-06) [X6 Y7 Y10 Z11 Z12 X13]
+ (1.2283337825272171e-06) [Y5 Y6 X7 Z8 Z9 X10]
+ (1.2283337825272171e-06) [X5 X6 Y7 Z8 Z9 Y10]
+ (1.2393363216272936e-06) [Y0 Z1 Z2 Z3 Y4 Z12]
+ (1.2393363216272936e-06) [X0 Z1 Z2 Z3 X4 Z12]
+ (1.2393363216272936e-06) [Y1 Z2 Z3 Z4 Y5 Z13]
+ (1.2393363216272936e-06) [X1 Z2 Z3 Z4 X5 Z13]
+ (1.3304731885732335e-06) [Y5 Z6 Z7 X8 X9 Y10]
+ (1.3304731885732335e-06) [X5 Z6 Z7 Y8 Y9 X10]
+ (1.4548424491035125e-06) [Y2 Z3 Z4 X5 X6 Y7]
+ (1.4548424491035125e-06) [X2 Z3 Z4 Y5 Y6 X7]
+ (2.1726691013405704e-06) [Y2 Y3 X10 Z11 Z12 X13]
+ (2.1726691013405704e-06) [X2 X3 Y10 Z11 Z12 Y13]
+ (3.0882507109545547e-06) [Y3 Z4 Z5 X6 X11 Y12]
+ (3.0882507109545547e-06) [X3 Z4 Z5 Y6 Y11 X12]
+ (3.1174479461774806e-06) [Z0 Y1 Z2 Z3 Z4 Y5]
+ (3.1174479461774806e-06) [Z0 X1 Z2 Z3 Z4 X5]
+ (3.1513463108547933e-06) [Y3 X4 X7 Z8 Z9 Y10]
+ (3.1513463108547933e-06) [X3 Y4 Y7 Z8 Z9 X10]
+ (3.3131454999498387e-06) [Y7 Z8 Z9 X10 X11 Y12]
+ (3.3131454999498387e-06) [X7 Z8 Z9 Y10 Y11 X12]
+ (3.334331289091543e-06) [Y5 Z6 Z7 Z8 Z9 Y11]
+ (3.334331289091543e-06) [X5 Z6 Z7 Z8 Z9 X11]
+ (3.694513294075345e-06) [Y4 X5 X10 Z11 Z12 Y13]
+ (3.694513294075345e-06) [X4 Y5 Y10 Z11 Z12 X13]
+ (4.183932559084192e-06) [Y7 Z8 Z9 Z10 Z11 Y13]
+ (4.183932559084192e-06) [X7 Z8 Z9 Z10 Z11 X13]
+ (4.556569217660564e-06) [Y4 Z5 Z6 X7 X12 Y13]
+ (4.556569217660564e-06) [X4 Z5 Z6 Y7 Y12 X13]
+ (4.643051068028934e-06) [Y2 Z3 Z4 X5 X10 Y11]
+ (4.643051068028934e-06) [X2 Z3 Z4 Y5 Y10 X11]
+ (5.2758831216445055e-06) [Y2 Z3 Z4 Y5 X12 X13]
+ (5.2758831216445055e-06) [X2 Z3 Z4 X5 Y12 Y13]
+ (5.974311712908896e-06) [Y4 Z5 Z6 Y7 X10 X11]
+ (5.974311712908896e-06) [X4 Z5 Z6 X7 Y10 Y11]
+ (0.0002921986261110536) [Y6 Z7 Y8 Y9 Z10 Y11]
+ (0.0002921986261110536) [Y6 Z7 Y8 X9 Z10 X11]
+ (0.0002921986261110536) [X6 Z7 X8 Y9 Z10 Y11]
+ (0.0002921986261110536) [X6 Z7 X8 X9 Z10 X11]
+ (0.0004956762314916402) [Z2 Y3 Z4 Z5 Z6 Y7]
+ (0.0004956762314916402) [Z2 X3 Z4 Z5 Z6 X7]
+ (0.0006650070219499279) [Y2 Z3 Z4 Z5 Y6 Z12]
+ (0.0006650070219499279) [X2 Z3 Z4 Z5 X6 Z12]
+ (0.0006650070219499279) [Y3 Z4 Z5 Z6 Y7 Z13]
+ (0.0006650070219499279) [X3 Z4 Z5 Z6 X7 Z13]
+ (0.0008533856254125543) [Y1 Z2 Z3 X4 X5 Y6]
+ (0.0008533856254125543) [X1 Z2 Z3 Y4 Y5 X6]
+ (0.0016095313817213793) [Y0 Z1 Z2 Z3 Z4 Y6]
+ (0.0016095313817213793) [X0 Z1 Z2 Z3 Z4 X6]
+ (0.0016095313817213793) [Y1 Z2 Z3 Z5 Z6 Y7]
+ (0.0016095313817213793) [X1 Z2 Z3 Z5 Z6 X7]
+ (0.001667604181144066) [Y0 Z1 Z3 Z4 Z5 Y6]
+ (0.001667604181144066) [X0 Z1 Z3 Z4 Z5 X6]
+ (0.001667604181144066) [Y1 Z2 Z4 Z5 Z6 Y7]
+ (0.001667604181144066) [X1 Z2 Z4 Z5 Z6 X7]
+ (0.0017278753941369612) [Y1 Z2 Z3 Y4 X11 X12]
+ (0.0017278753941369612) [X1 Z2 Z3 X4 Y11 Y12]
+ (0.001799219493663012) [Y0 Z1 Z2 X3 X10 Y11]
+ (0.001799219493663012) [X0 Z1 Z2 Y3 Y10 X11]
+ (0.0022939566113524814) [Y1 Y2 X3 Z4 Z5 X6]
+ (0.0022939566113524814) [X1 X2 Y3 Z4 Z5 Y6]
+ (0.0024629170071339334) [Y0 Z1 Z2 Z3 Z5 Y6]
+ (0.0024629170071339334) [X0 Z1 Z2 Z3 Z5 X6]
+ (0.0024629170071339334) [Y1 Z2 Z3 Z4 Z6 Y7]
+ (0.0024629170071339334) [X1 Z2 Z3 Z4 Z6 X7]
+ (0.003961560792496547) [Y0 Z1 Z2 Z4 Z5 Y6]
+ (0.003961560792496547) [X0 Z1 Z2 Z4 Z5 X6]
+ (0.003961560792496547) [Y1 Z3 Z4 Z5 Z6 Y7]
+ (0.003961560792496547) [X1 Z3 Z4 Z5 Z6 X7]
+ (0.004424855449441869) [Y0 Z1 Z2 X3 X4 Y5]
+ (0.004424855449441869) [X0 Z1 Z2 Y3 Y4 X5]
+ (0.004575007626639198) [Y0 Z1 Z2 X3 X12 Y13]
+ (0.004575007626639198) [X0 Z1 Z2 Y3 Y12 X13]
+ (0.004668620318776305) [Y1 Y2 X7 Z8 Z9 X10]
+ (0.004668620318776305) [X1 X2 Y7 Z8 Z9 Y10]
+ (0.0046849033881552204) [Y0 Z1 Z2 X3 X6 Y7]
+ (0.0046849033881552204) [X0 Z1 Z2 Y3 Y6 X7]
+ (0.005324835234221703) [Y2 Z3 Y4 X10 Z11 X12]
+ (0.005324835234221703) [X2 Z3 X4 Y10 Z11 Y12]
+ (0.005324835234221703) [Y3 Z4 Y5 X11 Z12 X13]
+ (0.005324835234221703) [X3 Z4 X5 Y11 Z12 Y13]
+ (0.005368659358109554) [Y2 X3 X7 Z8 Z9 Y10]
+ (0.005368659358109554) [Y2 Y3 Y7 Z8 Z9 Y10]
+ (0.005368659358109554) [X2 X3 X7 Z8 Z9 X10]
+ (0.005368659358109554) [X2 Y3 Y7 Z8 Z9 X10]
+ (0.00796088072592155) [Y4 Z5 Y6 Y10 Z11 Y12]
+ (0.00796088072592155) [X4 Z5 X6 X10 Z11 X12]
+ (0.00796088072592155) [Y5 Z6 Y7 Y11 Z12 Y13]
+ (0.00796088072592155) [X5 Z6 X7 X11 Z12 X13]
+ (0.008125251921381043) [Y0 Z1 Z2 X3 X8 Y9]
+ (0.008125251921381043) [X0 Z1 Z2 Y3 Y8 X9]
+ (0.008890731522694576) [Y4 Z5 X6 X10 Z11 Y12]
+ (0.008890731522694576) [X4 Z5 Y6 Y10 Z11 X12]
+ (0.008890731522694576) [Y5 Z6 X7 X11 Z12 Y13]
+ (0.008890731522694576) [X5 Z6 Y7 Y11 Z12 X13]
+ (0.010263414868158514) [Y2 Z3 X4 X10 Z11 Y12]
+ (0.010263414868158514) [X2 Z3 Y4 Y10 Z11 X12]
+ (0.010263414868158514) [Y3 Z4 X5 X11 Z12 Y13]
+ (0.010263414868158514) [X3 Z4 Y5 Y11 Z12 X13]
+ (0.010540425907671435) [Y6 Z7 Z8 Z9 Y10 Z13]
+ (0.010540425907671435) [X6 Z7 Z8 Z9 X10 Z13]
+ (0.010540425907671435) [Y7 Z8 Z9 Z10 Y11 Z12]
+ (0.010540425907671435) [X7 Z8 Z9 Z10 X11 Z12]
+ (0.01096007494054259) [Z4 Y7 Z8 Z9 Z10 Y11]
+ (0.01096007494054259) [Z4 X7 Z8 Z9 Z10 X11]
+ (0.01096007494054259) [Z5 Y6 Z7 Z8 Z9 Y10]
+ (0.01096007494054259) [Z5 X6 Z7 Z8 Z9 X10]
+ (0.011307274008848067) [Y6 Z7 Z8 Z9 Y10 Z11]
+ (0.011307274008848067) [X6 Z7 Z8 Z9 X10 Z11]
+ (0.014411099430130896) [Y2 Z3 Z4 Z5 Y6 Z11]
+ (0.014411099430130896) [X2 Z3 Z4 Z5 X6 Z11]
+ (0.014411099430130896) [Y3 Z4 Z5 Z6 Y7 Z10]
+ (0.014411099430130896) [X3 Z4 Z5 Z6 X7 Z10]
+ (0.01522563075722656) [Y3 Z4 Z5 X6 X10 Y11]
+ (0.01522563075722656) [Y3 Z4 Z5 Y6 Y10 Y11]
+ (0.01522563075722656) [X3 Z4 Z5 X6 X10 X11]
+ (0.01522563075722656) [X3 Z4 Z5 Y6 Y10 X11]
+ (0.015588250102380219) [Y2 Z3 Y4 Y10 Z11 Y12]
+ (0.015588250102380219) [X2 Z3 X4 X10 Z11 X12]
+ (0.015588250102380219) [Y3 Z4 Y5 Y11 Z12 Y13]
+ (0.015588250102380219) [X3 Z4 X5 X11 Z12 X13]
+ (0.018266834869375515) [Z4 Y6 Z7 Z8 Z9 Y10]
+ (0.018266834869375515) [Z4 X6 Z7 Z8 Z9 X10]
+ (0.018266834869375515) [Z5 Y7 Z8 Z9 Z10 Y11]
+ (0.018266834869375515) [Z5 X7 Z8 Z9 Z10 X11]
+ (0.019020423173039914) [Z2 Y6 Z7 Z8 Z9 Y10]
+ (0.019020423173039914) [Z2 X6 Z7 Z8 Z9 X10]
+ (0.019020423173039914) [Z3 Y7 Z8 Z9 Z10 Y11]
+ (0.019020423173039914) [Z3 X7 Z8 Z9 Z10 X11]
+ (0.020175921723535477) [Y4 Z5 Z6 X7 X11 Y12]
+ (0.020175921723535477) [Y4 Z5 Z6 Y7 Y11 Y12]
+ (0.020175921723535477) [X4 Z5 Z6 X7 X11 X12]
+ (0.020175921723535477) [X4 Z5 Z6 Y7 Y11 X12]
+ (0.020175921723535477) [Y5 X6 X10 Z11 Z12 Y13]
+ (0.020175921723535477) [Y5 Y6 Y10 Z11 Z12 Y13]
+ (0.020175921723535477) [X5 X6 X10 Z11 Z12 X13]
+ (0.020175921723535477) [X5 Y6 Y10 Z11 Z12 X13]
+ (0.024353077678068963) [Y2 Z3 Y4 Y11 Z12 Y13]
+ (0.024353077678068963) [Y2 Z3 Y4 X11 Z12 X13]
+ (0.024353077678068963) [X2 Z3 X4 Y11 Z12 Y13]
+ (0.024353077678068963) [X2 Z3 X4 X11 Z12 X13]
+ (0.024353077678068963) [Y3 Z4 Y5 Y10 Z11 Y12]
+ (0.024353077678068963) [Y3 Z4 Y5 X10 Z11 X12]
+ (0.024353077678068963) [X3 Z4 X5 Y10 Z11 Y12]
+ (0.024353077678068963) [X3 Z4 X5 X10 Z11 X12]
+ (0.024389082531149464) [Z2 Y7 Z8 Z9 Z10 Y11]
+ (0.024389082531149464) [Z2 X7 Z8 Z9 Z10 X11]
+ (0.024389082531149464) [Z3 Y6 Z7 Z8 Z9 Y10]
+ (0.024389082531149464) [Z3 X6 Z7 Z8 Z9 X10]
+ (0.025104957138844468) [Y6 Z7 Z8 Z9 Y10 Z12]
+ (0.025104957138844468) [X6 Z7 Z8 Z9 X10 Z12]
+ (0.025104957138844468) [Y7 Z8 Z9 Z10 Y11 Z13]
+ (0.025104957138844468) [X7 Z8 Z9 Z10 X11 Z13]
+ (0.030787505389143932) [Z6 Y7 Z8 Z9 Z10 Y11]
+ (0.030787505389143932) [Z6 X7 Z8 Z9 Z10 X11]
+ (0.04587947078129796) [Y0 Z2 Z3 Z4 Z5 Y6]
+ (0.04587947078129796) [X0 Z2 Z3 Z4 Z5 X6]
+ (0.05600733087780754) [Z0 Y7 Z8 Z9 Z10 Y11]
+ (0.05600733087780754) [Z0 X7 Z8 Z9 Z10 X11]
+ (0.05600733087780754) [Z1 Y6 Z7 Z8 Z9 Y10]
+ (0.05600733087780754) [Z1 X6 Z7 Z8 Z9 X10]
+ (0.05608468124661344) [Z0 Y6 Z7 Z8 Z9 Y10]
+ (0.05608468124661344) [Z0 X6 Z7 Z8 Z9 X10]
+ (0.05608468124661344) [Z1 Y7 Z8 Z9 Z10 Y11]
+ (0.05608468124661344) [Z1 X7 Z8 Z9 Z10 X11]
+ (-6.631277927758647e-05) [Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-6.631277927758647e-05) [X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-6.631277927758641e-05) [Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-6.631277927758641e-05) [X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-2.5950860066313504e-05) [Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.5950860066313504e-05) [X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.595086006631349e-05) [Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.595086006631349e-05) [X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.04274327701378368) [Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.04274327701378368) [X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (0.04274327701378369) [Y0 Z1 Z2 Z3 Z4 Z5 Y6]
+ (0.04274327701378369) [X0 Z1 Z2 Z3 Z4 Z5 X6]
+ (-0.04764261217638309) [Y4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-0.04764261217638309) [X4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-0.04764261217638309) [Y5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-0.04764261217638309) [X5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-0.04171881383982175) [Y4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-0.04171881383982175) [X4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-0.04171881383982175) [Y5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-0.04171881383982175) [X5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-0.039564416322893425) [Y4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-0.039564416322893425) [X4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-0.039564416322893425) [Y5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.039564416322893425) [X5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03935916802205304) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (-0.03935916802205304) [X2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (-0.03935916802205304) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (-0.03935916802205304) [X3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (-0.03931805194719759) [Y4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.03931805194719759) [X4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.03931805194719759) [Y5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03931805194719759) [X5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03560837898831258) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.03560837898831258) [X2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.029903789512624818) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (-0.029903789512624818) [X2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (-0.029903789512624818) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (-0.029903789512624818) [X3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (-0.02873077955190549) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.02873077955190549) [X2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.02873077955190549) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.02873077955190549) [X3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.025637238296026772) [Y4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-0.025637238296026772) [X4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-0.025637238296026772) [Y5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-0.025637238296026772) [X5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-0.024755463292890953) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (-0.024755463292890953) [X2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (-0.024755463292890953) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (-0.024755463292890953) [X3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (-0.024282117354692843) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.024282117354692843) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.023145130929528933) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (-0.023145130929528933) [X5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (-0.02252844019601306) [Y4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.02252844019601306) [X4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.021433810721600943) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (-0.021433810721600943) [X2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (-0.021433810721600943) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (-0.021433810721600943) [X3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251565) [Y3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.019257505095251565) [X3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.01902824244384726) [Y2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (-0.01902824244384726) [X2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (-0.01888903030494291) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-0.01888903030494291) [X2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-0.01888903030494291) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.01888903030494291) [X3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.016024603689179608) [Y5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-0.016024603689179608) [X5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-0.015225630757226556) [Y2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (-0.015225630757226556) [X2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (-0.014603704729162089) [Y3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.014603704729162089) [X3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.014564531231173034) [Y6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.014564531231173034) [X6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.011756013419819245) [Y2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.011756013419819245) [X2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.011285190200840898) [Y4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (-0.011285190200840898) [X4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (-0.009841749246962581) [Y3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (-0.009841749246962581) [X3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (-0.009612634606847166) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-0.009612634606847166) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-0.009612634606847166) [Y5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-0.009612634606847166) [X5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-0.008469978791023878) [Y3 Z4 Z5 X6 X7 Z8 Z9 Y10]
+ (-0.008469978791023878) [X3 Z4 Z5 Y6 Y7 Z8 Z9 X10]
+ (-0.007306759928832927) [Y4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-0.007306759928832927) [X4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005923798336561342) [Y5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (-0.005923798336561342) [X5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (-0.005652620978017352) [Y0 Y1 X2 Z3 Z4 Z5 Z6 X7]
+ (-0.005652620978017352) [X0 X1 Y2 Z3 Z4 Z5 Z6 Y7]
+ (-0.005368659358109554) [Y2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005368659358109554) [X2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.004158797381840046) [Y2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.004158797381840046) [X2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.0033566705638328888) [Y1 Z2 Z3 Z4 Z5 X6 X8 Y9]
+ (-0.0033566705638328888) [Y1 Z2 Z3 Z4 Z5 Y6 Y8 Y9]
+ (-0.0033566705638328888) [X1 Z2 Z3 Z4 Z5 X6 X8 X9]
+ (-0.0033566705638328888) [X1 Z2 Z3 Z4 Z5 Y6 Y8 X9]
+ (-0.0032675138544235502) [Y1 Z2 Z3 Z4 Z5 X6 X12 Y13]
+ (-0.0032675138544235502) [Y1 Z2 Z3 Z4 Z5 Y6 Y12 Y13]
+ (-0.0032675138544235502) [X1 Z2 Z3 Z4 Z5 X6 X12 X13]
+ (-0.0032675138544235502) [X1 Z2 Z3 Z4 Z5 Y6 Y12 X13]
+ (-0.0027790267990255484) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7]
+ (-0.0027790267990255484) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7]
+ (-0.002686040977806607) [Y0 Z1 Z2 Z3 X4 X10 Z11 Y12]
+ (-0.002686040977806607) [X0 Z1 Z2 Z3 Y4 Y10 Z11 X12]
+ (-0.002686040977806607) [Y1 Z2 Z3 Z4 X5 X11 Z12 Y13]
+ (-0.002686040977806607) [X1 Z2 Z3 Z4 Y5 Y11 Z12 X13]
+ (-0.0022939566113524814) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7]
+ (-0.0022939566113524814) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7]
+ (-0.0022939566113524814) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7]
+ (-0.0022939566113524814) [X0 Z1 X2 X3 Z4 Z5 Z6 X7]
+ (-0.0009581655836696461) [Y0 Z1 Z2 Z3 Z4 X5 X11 Y12]
+ (-0.0009581655836696461) [Y0 Z1 Z2 Z3 Z4 Y5 Y11 Y12]
+ (-0.0009581655836696461) [X0 Z1 Z2 Z3 Z4 X5 X11 X12]
+ (-0.0009581655836696461) [X0 Z1 Z2 Z3 Z4 Y5 Y11 X12]
+ (-0.0009581655836696461) [Y1 Z2 Z3 X4 X10 Z11 Z12 Y13]
+ (-0.0009581655836696461) [Y1 Z2 Z3 Y4 Y10 Z11 Z12 Y13]
+ (-0.0009581655836696461) [X1 Z2 Z3 X4 X10 Z11 Z12 X13]
+ (-0.0009581655836696461) [X1 Z2 Z3 Y4 Y10 Z11 Z12 X13]
+ (-0.00024636437569583534) [Y5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.00024636437569583534) [X5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0001384017730354988) [Y1 Z2 Z3 Z4 Z5 X6 X10 Y11]
+ (-0.0001384017730354988) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Y11]
+ (-0.0001384017730354988) [X1 Z2 Z3 Z4 Z5 X6 X10 X11]
+ (-0.0001384017730354988) [X1 Z2 Z3 Z4 Z5 Y6 Y10 X11]
+ (-7.735036880590126e-05) [Y0 Y1 X6 Z7 Z8 Z9 Z10 X11]
+ (-7.735036880590126e-05) [X0 X1 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585304162493e-05) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585304162493e-05) [Z0 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.6103585304162493e-05) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.6103585304162493e-05) [Z1 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808793804462e-05) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.5316808793804462e-05) [Z0 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808793804462e-05) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5316808793804462e-05) [Z1 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-9.806102774275141e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-9.806102774275141e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-9.806102774275141e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-9.806102774275141e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-7.089799466912408e-06) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.089799466912408e-06) [Z2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.089799466912408e-06) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.089799466912408e-06) [Z3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-6.652209668514385e-06) [Z0 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.652209668514385e-06) [Z0 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-6.652209668514385e-06) [Z1 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.652209668514385e-06) [Z1 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.481851832969884e-06) [Z0 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.481851832969884e-06) [Z0 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.481851832969884e-06) [Z1 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.481851832969884e-06) [Z1 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-5.0714807359768075e-06) [Y5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-5.0714807359768075e-06) [Y5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-5.0714807359768075e-06) [X5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-5.0714807359768075e-06) [X5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-4.7346220382983335e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-4.7346220382983335e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-4.7346220382983335e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-4.7346220382983335e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-4.728843146793277e-06) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-4.728843146793277e-06) [Z2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-4.728843146793277e-06) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.728843146793277e-06) [Z3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.253224225235523e-06) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.253224225235523e-06) [Z4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.7696594514975743e-06) [Z6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.7696594514975743e-06) [Z6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.5443954289444674e-06) [Y2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-3.5443954289444674e-06) [Y2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-3.5443954289444674e-06) [X2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-3.5443954289444674e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-3.5443954289444674e-06) [Y3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-3.5443954289444674e-06) [Y3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-3.5443954289444674e-06) [X3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-3.5443954289444674e-06) [X3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-2.3609563201191312e-06) [Y2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-2.3609563201191312e-06) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-2.3609563201191312e-06) [X2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-2.3609563201191312e-06) [X2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-2.103215604392659e-06) [Z2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.103215604392659e-06) [Z2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.103215604392659e-06) [Z3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.103215604392659e-06) [Z3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.011122097863297e-06) [Z2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.011122097863297e-06) [Z2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.011122097863297e-06) [Z3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.011122097863297e-06) [Z3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.942946836465706e-06) [Z4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.942946836465706e-06) [Z4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.942946836465706e-06) [Z5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.942946836465706e-06) [Z5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.654117476798846e-06) [Z4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.654117476798846e-06) [Z4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.654117476798846e-06) [Z5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.654117476798846e-06) [Z5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.5224930675035926e-06) [Y2 Z3 Z4 X5 X7 Z8 Z9 Y10]
+ (-1.5224930675035926e-06) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Y10]
+ (-1.5224930675035926e-06) [X2 Z3 Z4 X5 X7 Z8 Z9 X10]
+ (-1.5224930675035926e-06) [X2 Z3 Z4 Y5 Y7 Z8 Z9 X10]
+ (-1.5224930675035926e-06) [Y3 X4 X6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930675035926e-06) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930675035926e-06) [X3 X4 X6 Z7 Z8 Z9 Z10 X11]
+ (-1.5224930675035926e-06) [X3 Y4 Y6 Z7 Z8 Z9 Z10 X11]
+ (-1.2283337825272171e-06) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (-1.2283337825272171e-06) [Y4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (-1.2283337825272171e-06) [X4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (-1.2283337825272171e-06) [X4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (-7.988770288666606e-07) [Y2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (-7.988770288666606e-07) [X2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (-7.988770288666606e-07) [Y3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (-7.988770288666606e-07) [X3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (-7.867765103580301e-07) [Y0 X1 X5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765103580301e-07) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765103580301e-07) [X0 X1 X5 Z6 Z7 Z8 Z9 X10]
+ (-7.867765103580301e-07) [X0 Y1 Y5 Z6 Z7 Z8 Z9 X10]
+ (-7.189990974509484e-07) [Y1 Y2 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.189990974509484e-07) [X1 X2 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-6.175246206481663e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X11 X12]
+ (-6.175246206481663e-07) [X1 Z2 Z3 Z4 Z5 X6 Y11 Y12]
+ (-5.47164774415228e-07) [Y0 Z1 Z2 Y3 X10 Z11 Z12 X13]
+ (-5.47164774415228e-07) [X0 Z1 Z2 X3 Y10 Z11 Z12 Y13]
+ (-4.5614471798991324e-07) [Y2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (-4.5614471798991324e-07) [X2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (-4.5614471798991324e-07) [Y3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (-4.5614471798991324e-07) [X3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (-4.523389677150416e-07) [Y1 Y2 X5 Z6 Z7 Z8 Z9 X10]
+ (-4.523389677150416e-07) [X1 X2 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-3.4273231087674735e-07) [Y2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (-3.4273231087674735e-07) [X2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (-3.4273231087674735e-07) [Y3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (-3.4273231087674735e-07) [X3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (-3.328139350535286e-07) [Y6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-3.328139350535286e-07) [Y6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-3.328139350535286e-07) [X6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-3.328139350535286e-07) [X6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-3.0868265651063305e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X12 X13]
+ (-3.0868265651063305e-07) [X0 Z1 Z2 Z3 Z4 X5 Y12 Y13]
+ (-2.8882935966686e-07) [Y4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8882935966686e-07) [Y4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8882935966686e-07) [X4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.8882935966686e-07) [X4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-2.3713289479465785e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X8 X9]
+ (-2.3713289479465785e-07) [X0 Z1 Z2 Z3 Z4 X5 Y8 Y9]
+ (-1.8394209155198777e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7]
+ (-1.8394209155198777e-07) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7]
+ (-8.05744659391227e-08) [Y0 Z1 Z2 Z3 Z4 X5 X10 Y11]
+ (-8.05744659391227e-08) [X0 Z1 Z2 Z3 Z4 Y5 Y10 X11]
+ (4.53717809545374e-08) [X2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.53717809545374e-08) [Y2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.53717809545374e-08) [X3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (4.53717809545374e-08) [Y3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (8.05744659391227e-08) [Y0 Z1 Z2 Z3 Z4 Y5 X10 X11]
+ (8.05744659391227e-08) [X0 Z1 Z2 Z3 Z4 X5 Y10 Y11]
+ (9.209350652936207e-08) [Y2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350652936207e-08) [Y2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350652936207e-08) [X2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (9.209350652936207e-08) [X2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.7035783554450037e-07) [Y0 X1 X7 Z8 Z9 Z10 Z11 Y12]
+ (1.7035783554450037e-07) [Y0 Y1 Y7 Z8 Z9 Z10 Z11 Y12]
+ (1.7035783554450037e-07) [X0 X1 X7 Z8 Z9 Z10 Z11 X12]
+ (1.7035783554450037e-07) [X0 Y1 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.8394209155198777e-07) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7]
+ (1.8394209155198777e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7]
+ (2.3713289479465785e-07) [Y0 Z1 Z2 Z3 Z4 X5 X8 Y9]
+ (2.3713289479465785e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y8 X9]
+ (3.0868265651063305e-07) [Y0 Z1 Z2 Z3 Z4 X5 X12 Y13]
+ (3.0868265651063305e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y12 X13]
+ (4.523389677150416e-07) [Y1 X2 X5 Z6 Z7 Z8 Z9 Y10]
+ (4.523389677150416e-07) [X1 Y2 Y5 Z6 Z7 Z8 Z9 X10]
+ (5.47164774415228e-07) [Y0 Z1 Z2 X3 X10 Z11 Z12 Y13]
+ (5.47164774415228e-07) [X0 Z1 Z2 Y3 Y10 Z11 Z12 X13]
+ (6.175246206481663e-07) [Y1 Z2 Z3 Z4 Z5 X6 X11 Y12]
+ (6.175246206481663e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y11 X12]
+ (7.189990974509484e-07) [Y1 X2 X7 Z8 Z9 Z10 Z11 Y12]
+ (7.189990974509484e-07) [X1 Y2 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.3304731885732335e-06) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (1.3304731885732335e-06) [Y4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (1.3304731885732335e-06) [X4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (1.3304731885732335e-06) [X4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (1.6288532433512003e-06) [Y2 Z3 X4 X6 Z7 Z8 Z9 Y10]
+ (1.6288532433512003e-06) [X2 Z3 Y4 Y6 Z7 Z8 Z9 X10]
+ (1.6288532433512003e-06) [Y3 Z4 X5 X7 Z8 Z9 Z10 Y11]
+ (1.6288532433512003e-06) [X3 Z4 Y5 Y7 Z8 Z9 Z10 X11]
+ (1.6893489512913601e-06) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (1.6893489512913601e-06) [X2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (1.6893489512913601e-06) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (1.6893489512913601e-06) [X3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (2.7455184000778077e-06) [Y2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (2.7455184000778077e-06) [Y2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (2.7455184000778077e-06) [X2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (2.7455184000778077e-06) [X2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (2.7455184000778077e-06) [Y3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (2.7455184000778077e-06) [Y3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (2.7455184000778077e-06) [X3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (2.7455184000778077e-06) [X3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (3.211842018794952e-06) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (3.211842018794952e-06) [Y2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (3.211842018794952e-06) [X2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (3.211842018794952e-06) [X2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (3.211842018794952e-06) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (3.211842018794952e-06) [Y3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (3.211842018794952e-06) [X3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (3.211842018794952e-06) [X3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (3.3131454999498387e-06) [Y6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (3.3131454999498387e-06) [Y6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (3.3131454999498387e-06) [X6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (3.3131454999498387e-06) [X6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (3.334331289091543e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (3.334331289091543e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (4.1839325590841925e-06) [Y6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (4.1839325590841925e-06) [X6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (7.735036880590126e-05) [Y0 X1 X6 Z7 Z8 Z9 Z10 Y11]
+ (7.735036880590126e-05) [X0 Y1 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.00024636437569583534) [Y5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.00024636437569583534) [X5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.0004458535128840824) [Y0 Z1 X2 X6 Z7 Z8 Z9 Y10]
+ (0.0004458535128840824) [X0 Z1 Y2 Y6 Z7 Z8 Z9 X10]
+ (0.0004458535128840824) [Y1 Z2 X3 X7 Z8 Z9 Z10 Y11]
+ (0.0004458535128840824) [X1 Z2 Y3 Y7 Z8 Z9 Z10 X11]
+ (0.0005940221543005475) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005475) [Y0 Z1 Y2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005475) [X0 Z1 X2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005475) [X0 Z1 X2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005475) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005475) [Y1 Z2 Y3 X6 Z7 Z8 Z9 X10]
+ (0.0005940221543005475) [X1 Z2 X3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005475) [X1 Z2 X3 X6 Z7 Z8 Z9 X10]
+ (0.0008533856254125542) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7]
+ (0.0008533856254125542) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7]
+ (0.0008533856254125542) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7]
+ (0.0008533856254125542) [X0 Z1 Z2 Z3 X4 X5 Z6 X7]
+ (0.0010435246534907623) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z13]
+ (0.0010435246534907623) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z13]
+ (0.0010435246534907623) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z12]
+ (0.0010435246534907623) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z12]
+ (0.0012803060973496736) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z9]
+ (0.0012803060973496736) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z9]
+ (0.0012803060973496736) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z8]
+ (0.0012803060973496736) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z8]
+ (0.0013038004788127023) [Y0 Z1 Z2 Z3 Y4 Y10 Z11 Y12]
+ (0.0013038004788127023) [X0 Z1 Z2 Z3 X4 X10 Z11 X12]
+ (0.0013038004788127023) [Y1 Z2 Z3 Z4 Y5 Y11 Z12 Y13]
+ (0.0013038004788127023) [X1 Z2 Z3 Z4 X5 X11 Z12 X13]
+ (0.002261966062482349) [Y0 Z1 Z2 Z3 Y4 Y11 Z12 Y13]
+ (0.002261966062482349) [Y0 Z1 Z2 Z3 Y4 X11 Z12 X13]
+ (0.002261966062482349) [X0 Z1 Z2 Z3 X4 Y11 Z12 Y13]
+ (0.002261966062482349) [X0 Z1 Z2 Z3 X4 X11 Z12 X13]
+ (0.002261966062482349) [Y1 Z2 Z3 Z4 Y5 Y10 Z11 Y12]
+ (0.002261966062482349) [Y1 Z2 Z3 Z4 Y5 X10 Z11 X12]
+ (0.002261966062482349) [X1 Z2 Z3 Z4 X5 Y10 Z11 Y12]
+ (0.002261966062482349) [X1 Z2 Z3 Z4 X5 X10 Z11 X12]
+ (0.003989841456619311) [Y0 Z1 Z2 Z3 Y4 X10 Z11 X12]
+ (0.003989841456619311) [X0 Z1 Z2 Z3 X4 Y10 Z11 Y12]
+ (0.003989841456619311) [Y1 Z2 Z3 Z4 Y5 X11 Z12 X13]
+ (0.003989841456619311) [X1 Z2 Z3 Z4 X5 Y11 Z12 Y13]
+ (0.004158797381840046) [Y2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.004158797381840046) [X2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.004311038507914312) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z12]
+ (0.004311038507914312) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z12]
+ (0.004311038507914312) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z13]
+ (0.004311038507914312) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z13]
+ (0.004636976661182562) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z8]
+ (0.004636976661182562) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z8]
+ (0.004636976661182562) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z9]
+ (0.004636976661182562) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z9]
+ (0.005114473831660387) [Y0 Z1 Z2 X3 X7 Z8 Z9 Y10]
+ (0.005114473831660387) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Y10]
+ (0.005114473831660387) [X0 Z1 Z2 X3 X7 Z8 Z9 X10]
+ (0.005114473831660387) [X0 Z1 Z2 Y3 Y7 Z8 Z9 X10]
+ (0.005114473831660387) [Y1 X2 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.005114473831660387) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.005114473831660387) [X1 X2 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005114473831660387) [X1 Y2 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.00524153538280386) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z11]
+ (0.00524153538280386) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z11]
+ (0.00524153538280386) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z10]
+ (0.00524153538280386) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z10]
+ (0.005262642473076852) [Y0 Z1 Y2 X6 Z7 Z8 Z9 X10]
+ (0.005262642473076852) [X0 Z1 X2 Y6 Z7 Z8 Z9 Y10]
+ (0.005262642473076852) [Y1 Z2 Y3 X7 Z8 Z9 Z10 X11]
+ (0.005262642473076852) [X1 Z2 X3 Y7 Z8 Z9 Z10 Y11]
+ (0.005368659358109554) [Y2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005368659358109554) [X2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.00537993715583936) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z10]
+ (0.00537993715583936) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z10]
+ (0.00537993715583936) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z11]
+ (0.00537993715583936) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z11]
+ (0.005652620978017352) [Y0 X1 X2 Z3 Z4 Z5 Z6 Y7]
+ (0.005652620978017352) [X0 Y1 Y2 Z3 Z4 Z5 Z6 X7]
+ (0.0057084959859609345) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Y10]
+ (0.0057084959859609345) [X0 Z1 X2 X6 Z7 Z8 Z9 X10]
+ (0.0057084959859609345) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Y11]
+ (0.0057084959859609345) [X1 Z2 X3 X7 Z8 Z9 Z10 X11]
+ (0.005923798336561342) [Y5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (0.005923798336561342) [X5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (0.007306759928832927) [Y4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.007306759928832927) [X4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.008469978791023878) [Y3 Z4 Z5 Y6 X7 Z8 Z9 X10]
+ (0.008469978791023878) [X3 Z4 Z5 X6 Y7 Z8 Z9 Y10]
+ (0.009841749246962581) [Y3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (0.009841749246962581) [X3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (0.011285190200840898) [Y4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (0.011285190200840898) [X4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (0.011756013419819245) [Y2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.011756013419819245) [X2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.014564531231173034) [Y6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.014564531231173034) [X6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.014603704729162089) [Y3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.014603704729162089) [X3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.015225630757226556) [Y2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (0.015225630757226556) [X2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (0.016024603689179608) [Y5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (0.016024603689179608) [X5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (0.01902824244384726) [Y2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (0.01902824244384726) [X2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (0.019257505095251565) [Y3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.019257505095251565) [X3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.04587947078129797) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.04587947078129797) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-0.36937089366156106) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.36937089366156106) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.36937089366156106) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.36937089366156106) [X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.2816425776702284) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.2816425776702284) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.28164257767022827) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.28164257767022827) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0906514420703647) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0906514420703647) [Z0 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0906514420703647) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0906514420703647) [Z1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.07635021950635001) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.07635021950635001) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.07635021950635001) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.07635021950635001) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214016) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.06752385099214016) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214016) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.06752385099214016) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03560837898831258) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.03560837898831258) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03490334337366181) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03490334337366181) [Z2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03490334337366181) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.03490334337366181) [Z3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.024591860883830006) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.024591860883830006) [Z2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.024591860883830006) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.024591860883830006) [Z3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.024282117354692843) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.024282117354692843) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.023145130929528933) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (-0.023145130929528933) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (-0.02252844019601306) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.02252844019601306) [Z4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.01953805031131469) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-0.01953805031131469) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-0.01953805031131469) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-0.01953805031131469) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-0.017091553155898796) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-0.017091553155898796) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-0.017091553155898796) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-0.017091553155898796) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-0.016024603689179608) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-0.016024603689179608) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-0.016024603689179608) [X4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-0.016024603689179608) [X4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-0.01031148248983181) [Y2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.01031148248983181) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.01031148248983181) [X2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.01031148248983181) [X2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.009841749246962581) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962581) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.009841749246962581) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962581) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209858) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209858) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209858) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008826368514209858) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008541996625454821) [Y2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454821) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454821) [X2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454821) [X2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454821) [Y3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454821) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454821) [X3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.008541996625454821) [X3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.008469978791023878) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (-0.008469978791023878) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (-0.008469978791023878) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (-0.008469978791023878) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (-0.004668620318776305) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.004668620318776305) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.003876470899336943) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.003876470899336943) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.0038040661717285438) [Y0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0038040661717285438) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0038040661717285438) [X0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0038040661717285438) [X0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0034841573002178904) [Y1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0034841573002178904) [X1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0033566705638328888) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.0033566705638328888) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.0032675138544235502) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.0032675138544235502) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.002141361223101612) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.002141361223101612) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.0017278753941369612) [Y0 Z1 Z2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (-0.0017278753941369612) [X0 Z1 Z2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (-0.0016407548553124189) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0016407548553124189) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0014528843214169414) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0014528843214169414) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0014528843214169414) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0014528843214169414) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0007870896771024471) [Y1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (-0.0007870896771024471) [X1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0005192743499487798) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 X10]
+ (-0.0005192743499487798) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Y10]
+ (-0.00019400857029756288) [Y1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.00019400857029756288) [X1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0001384017730354988) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (-0.0001384017730354988) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (-7.141625221158047e-05) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-7.141625221158047e-05) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-7.141625221158047e-05) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.141625221158047e-05) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-5.071480735976808e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-5.071480735976808e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-3.1513463108547933e-06) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-3.1513463108547933e-06) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-3.0882507109545547e-06) [Y2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-3.0882507109545547e-06) [X2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-2.988511706254481e-06) [Y3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.988511706254481e-06) [X3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8742990711295713e-06) [Y3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-2.8742990711295713e-06) [X3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-2.3609563201191317e-06) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-2.3609563201191317e-06) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.3002946561364335e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-1.3002946561364335e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-1.1468376506118896e-06) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.1468376506118896e-06) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.1468376506118896e-06) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.1468376506118896e-06) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.352332102086924e-07) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.352332102086924e-07) [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.352332102086924e-07) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.352332102086924e-07) [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.091637197953745e-07) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637197953745e-07) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637197953745e-07) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637197953745e-07) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637197953745e-07) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637197953745e-07) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637197953745e-07) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.091637197953745e-07) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.074305985005553e-07) [Y0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.074305985005553e-07) [X0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.074305985005553e-07) [Y1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.074305985005553e-07) [X1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.900128985315563e-07) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-7.900128985315563e-07) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.900128985315563e-07) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.900128985315563e-07) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.8677651035803e-07) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.8677651035803e-07) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.560692463957451e-07) [Y0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692463957451e-07) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692463957451e-07) [X0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692463957451e-07) [X0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692463957451e-07) [Y1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692463957451e-07) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692463957451e-07) [X1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.560692463957451e-07) [X1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-4.997018421601104e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-4.997018421601104e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-4.997018421601104e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-4.997018421601104e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-4.997018421601104e-07) [Y1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-4.997018421601104e-07) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-4.997018421601104e-07) [X1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-4.997018421601104e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-3.5682475208033294e-07) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.5682475208033294e-07) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.5682475208033294e-07) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.5682475208033294e-07) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393081651493e-07) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393081651493e-07) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393081651493e-07) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393081651493e-07) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393081651493e-07) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393081651493e-07) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.3767393081651493e-07) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393081651493e-07) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-2.8882935966686e-07) [Y4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.8882935966686e-07) [X4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.686381543657617e-07) [Y3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.686381543657617e-07) [X3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-1.7035783554450037e-07) [Y0 X1 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.7035783554450037e-07) [X0 Y1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-9.209350652936205e-08) [Y2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.209350652936205e-08) [X2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243127715e-08) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773243127715e-08) [Y0 Z1 Y2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243127715e-08) [X0 Z1 X2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773243127715e-08) [X0 Z1 X2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243127715e-08) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773243127715e-08) [Y1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.379773243127715e-08) [X1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773243127715e-08) [X1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9742253789760626e-08) [X0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9742253789760626e-08) [Y0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.9742253789760626e-08) [X1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.9742253789760626e-08) [Y1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0474716554032639e-08) [Y0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.0474716554032639e-08) [X0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.0474716554032639e-08) [Y1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.0474716554032639e-08) [X1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (9.209350652936205e-08) [Y2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (9.209350652936205e-08) [X2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0717282181753464e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (1.0717282181753464e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (1.0717282181753464e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (1.0717282181753464e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (1.200428749294834e-07) [X0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (1.200428749294834e-07) [Y0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (1.200428749294834e-07) [X1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (1.200428749294834e-07) [Y1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (1.7035783554450037e-07) [Y0 Y1 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.7035783554450037e-07) [X0 X1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.3120943049852687e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (2.3120943049852687e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (2.3120943049852687e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (2.3120943049852687e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (2.686381543657617e-07) [Y3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (2.686381543657617e-07) [X3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (2.8882935966686e-07) [Y4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.8882935966686e-07) [X4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.092250615734145e-07) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (4.092250615734145e-07) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (4.092250615734145e-07) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (4.092250615734145e-07) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (4.092250615734145e-07) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (4.092250615734145e-07) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (4.092250615734145e-07) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (4.092250615734145e-07) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (4.444597853940569e-07) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (4.444597853940569e-07) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (4.444597853940569e-07) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (4.444597853940569e-07) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (4.684915094836648e-07) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.684915094836648e-07) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.684915094836648e-07) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (4.684915094836648e-07) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (7.24697442465701e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (7.24697442465701e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (7.24697442465701e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (7.24697442465701e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (7.24697442465701e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (7.24697442465701e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (7.24697442465701e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (7.24697442465701e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (7.8677651035803e-07) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (7.8677651035803e-07) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (1.3002946561364335e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (1.3002946561364335e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (2.3609563201191317e-06) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (2.3609563201191317e-06) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (2.8742990711295713e-06) [Y3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (2.8742990711295713e-06) [X3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (2.8836765758208366e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (2.8836765758208366e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (2.947356011344744e-06) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.947356011344744e-06) [X2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.947356011344744e-06) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.947356011344744e-06) [X3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.988511706254481e-06) [Y3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.988511706254481e-06) [X3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (3.0882507109545547e-06) [Y2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (3.0882507109545547e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (3.1513463108547933e-06) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (3.1513463108547933e-06) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (3.846201670920642e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (3.846201670920642e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (3.846201670920642e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (3.846201670920642e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (5.071480735976808e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (5.071480735976808e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (5.105526721558913e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (5.105526721558913e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (5.105526721558913e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (5.105526721558913e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (5.146496327057076e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (5.146496327057076e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (5.146496327057076e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (5.146496327057076e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (5.159350501556531e-06) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (5.159350501556531e-06) [X2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (5.159350501556531e-06) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.159350501556531e-06) [X3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.427988655922292e-06) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.427988655922292e-06) [X2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.427988655922292e-06) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.427988655922292e-06) [X3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.935867717599225e-06) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.935867717599225e-06) [X2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.935867717599225e-06) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.935867717599225e-06) [X3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.253273347490027e-06) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (7.253273347490027e-06) [X2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (7.979825792688485e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (7.979825792688485e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (7.979825792688485e-06) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (7.979825792688485e-06) [X3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (4.2055484112183544e-05) [Y2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.2055484112183544e-05) [X2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.2055484112183544e-05) [Y3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.2055484112183544e-05) [X3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0001384017730354988) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (0.0001384017730354988) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (0.0001878705338954776) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0001878705338954776) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0001878705338954776) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0001878705338954776) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.00019400857029756288) [Y1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.00019400857029756288) [X1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.00024636437569583534) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00024636437569583534) [Y4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.00024636437569583534) [X4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00024636437569583534) [X4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0005192743499487798) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Y10]
+ (0.0005192743499487798) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 X10]
+ (0.0007156734248908666) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007156734248908666) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0007156734248908666) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007156734248908666) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024471) [Y1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007870896771024471) [X1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (0.0015324835230730097) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (0.0015324835230730097) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (0.0015324835230730097) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (0.0015324835230730097) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (0.0016407548553124189) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0016407548553124189) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0017278753941369612) [Y0 Z1 Z2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (0.0017278753941369612) [X0 Z1 Z2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (0.0024464971554158917) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (0.0024464971554158917) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (0.0024464971554158917) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (0.0024464971554158917) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (0.0032675138544235502) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.0032675138544235502) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.0033566705638328888) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.0033566705638328888) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.0034841573002178904) [Y1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0034841573002178904) [X1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.003876470899336943) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.003876470899336943) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.004668620318776305) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.004668620318776305) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.004767272188278079) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (0.004767272188278079) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (0.004767272188278079) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (0.004767272188278079) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (0.005286546538226859) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (0.005286546538226859) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (0.005286546538226859) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (0.005286546538226859) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (0.005408954422409953) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (0.005408954422409953) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (0.005408954422409953) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (0.005408954422409953) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (0.005923798336561342) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561342) [Y4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (0.005923798336561342) [X4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561342) [X4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (0.01071550846979674) [Y2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.01071550846979674) [X2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.01071550846979674) [Y3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01071550846979674) [X3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.010757563953908924) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.010757563953908924) [X2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.010757563953908924) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010757563953908924) [X3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.014603704729162089) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.014603704729162089) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.014603704729162089) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.014603704729162089) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.019299560579363745) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.019299560579363745) [Y2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.019299560579363745) [X2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.019299560579363745) [X2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.019299560579363745) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.019299560579363745) [Y3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.019299560579363745) [X3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.019299560579363745) [X3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.05859198873386175) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.05859198873386175) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (5.775950526708911e-05) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.775950526708911e-05) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.775950526708911e-05) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.775950526708911e-05) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.07165035181002702) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.07165035181002702) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.07165035181002706) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.07165035181002706) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.019257505095251565) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.019257505095251565) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.01031148248983181) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.01031148248983181) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008826368514209858) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209858) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0075974640297706295) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0075974640297706295) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0075974640297706295) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0075974640297706295) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311883) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311883) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311883) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311883) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311883) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311883) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311883) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311883) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0053480515826766365) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0053480515826766365) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0053480515826766365) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0053480515826766365) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0038040661717285438) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0038040661717285438) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0029841661681219334) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-0.0029841661681219334) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-0.0029841661681219334) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-0.0029841661681219334) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-0.002446497155415892) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (-0.002446497155415892) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (-0.0022494124470939917) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0022494124470939917) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0022494124470939917) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0022494124470939917) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.002141361223101612) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.002141361223101612) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.0018638942824587448) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0018638942824587448) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0018638942824587448) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0018638942824587448) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0018638942824587448) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0018638942824587448) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0018638942824587448) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0018638942824587448) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0016407548553124189) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0016407548553124189) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0016407548553124189) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0016407548553124189) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0012223378081538357) [Y0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538357) [Y0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538357) [X0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538357) [X0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538357) [Y1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538357) [Y1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538357) [X1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0012223378081538357) [X1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.001028329237856273) [Y0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.001028329237856273) [X0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.001028329237856273) [Y1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.001028329237856273) [X1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.1463061451989448e-05) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.1463061451989448e-05) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.8742990711295713e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-2.8742990711295713e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-2.8742990711295713e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-2.8742990711295713e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.3002946561364335e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-1.3002946561364335e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-1.3002946561364335e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-1.3002946561364335e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-1.044494129677276e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-1.044494129677276e-06) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-1.044494129677276e-06) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-1.044494129677276e-06) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-9.956079228815864e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-9.956079228815864e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-9.956079228815864e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.956079228815864e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.10551503599292e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-8.10551503599292e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-8.10551503599292e-07) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.10551503599292e-07) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.661347212097115e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-7.661347212097115e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-7.661347212097115e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-7.661347212097115e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-7.540341413035785e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-7.540341413035785e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-7.189990974509484e-07) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.189990974509484e-07) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.876621657223507e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-6.876621657223507e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-6.876621657223507e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-6.876621657223507e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-6.175246206481663e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-6.175246206481663e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-4.523389677150416e-07) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.523389677150416e-07) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.0767325314975833e-07) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-3.0767325314975833e-07) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.0767325314975833e-07) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.0767325314975833e-07) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.0134714585999975e-07) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.0134714585999975e-07) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.9045998837369747e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-2.9045998837369747e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-2.9045998837369747e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-2.9045998837369747e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-2.6667317543561424e-07) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.6667317543561424e-07) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.6667317543561424e-07) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.6667317543561424e-07) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.8505641928229443e-07) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (-1.8505641928229443e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309319548006e-07) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.6569309319548006e-07) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309319548006e-07) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.6569309319548006e-07) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.8505641928229443e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (1.8505641928229443e-07) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (2.686381543657617e-07) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.686381543657617e-07) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.686381543657617e-07) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.686381543657617e-07) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714585999975e-07) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (3.0134714585999975e-07) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.523389677150416e-07) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (4.523389677150416e-07) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (4.6704023905547976e-07) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.6704023905547976e-07) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.6704023905547976e-07) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (4.6704023905547976e-07) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (6.175246206481663e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (6.175246206481663e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (7.189990974509484e-07) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.189990974509484e-07) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.540341413035785e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (7.540341413035785e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (8.949476486851312e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (8.949476486851312e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (1.7924939575501513e-06) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.7924939575501513e-06) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.7924939575501513e-06) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.7924939575501513e-06) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.883676575820837e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (2.883676575820837e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (2.988511706254481e-06) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.988511706254481e-06) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.988511706254481e-06) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.988511706254481e-06) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.253273347490027e-06) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.253273347490027e-06) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.4017109734087476e-05) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.4017109734087476e-05) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.4017109734087476e-05) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.4017109734087476e-05) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.5809603691637625e-05) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.5809603691637625e-05) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.5809603691637625e-05) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.5809603691637625e-05) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0005192743499487798) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (0.0005192743499487798) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (0.0005192743499487798) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (0.0005192743499487798) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (0.0007870896771024471) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024471) [Y0 Z1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024471) [X0 Z1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024471) [X0 Z1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0011726348316441876) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0011726348316441876) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0011726348316441876) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0011726348316441876) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.001236647801924503) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (0.001236647801924503) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (0.001236647801924503) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (0.001236647801924503) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (0.00220096406950046) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.00220096406950046) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.00220096406950046) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.00220096406950046) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798023) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798023) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002394972639798023) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798023) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002394972639798023) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002394972639798023) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.002394972639798023) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002394972639798023) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.002446497155415892) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (0.002446497155415892) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (0.0038040661717285438) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0038040661717285438) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.003876470899336943) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.003876470899336943) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.003876470899336943) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.003876470899336943) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.004220813970046436) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (0.004220813970046436) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (0.004220813970046436) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (0.004220813970046436) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (0.008826368514209858) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.008826368514209858) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.01031148248983181) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01031148248983181) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.019257505095251565) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.019257505095251565) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.05859198873386175) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.05859198873386175) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.3987009014025203e-05) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.3987009014025203e-05) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.39870090140252e-05) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.39870090140252e-05) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0034841573002178904) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0034841573002178904) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.002984166168121933) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.002984166168121933) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.00019400857029756288) [Y0 Z1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.00019400857029756288) [X0 Z1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061451989448e-05) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061451989448e-05) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.7924939575501513e-06) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.7924939575501513e-06) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.540341413035785e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413035785e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-7.540341413035785e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413035785e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.8505641928229443e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.8505641928229443e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.8505641928229443e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.8505641928229443e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.013471458599997e-07) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.013471458599997e-07) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.013471458599997e-07) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.013471458599997e-07) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (8.949476486851312e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (8.949476486851312e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (1.7924939575501513e-06) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.7924939575501513e-06) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756288) [Y0 Z1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756288) [X0 Z1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002984166168121933) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.002984166168121933) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.0034841573002178904) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0034841573002178904) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
Expectation value of XYI =  0.022659767960222288
Expectation value of XIZ =  0.07715357869738898
[0.27361669 0.00898685 0.26297431 0.00732554 0.21720814 0.00116213
 0.22790267 0.00082366]
Expectation value of XYI =  0.022659767960222343
Expectation value of XIZ =  0.07715357869738915
[0.02265977 0.07715358]
[RY(-1.5707963267948966, wires=[0]), RX(1.5707963267948966, wires=[1])]
[PauliZ(wires=[0]) @ PauliZ(wires=[1]), PauliZ(wires=[0]) @ PauliZ(wires=[2])]
pennylane.qnodes.base.QuantumFunctionError: Only observables that are qubit-wise commuting
Pauli words can be returned on the same wire
Minimum number of QWC groupings found: 2
Group 0:
Y0 X2 X3
Y0 Y1 X2 X3
X2 X3
Group 1:
Z0 Z1 Z2
Z0 Z1 Z2 Z3
Z0
Z0 Z1
Term expectation values:
Group 0 expectation values: [-0.14012997  0.01555488  0.18967764]
Group 1 expectation values: [0.93755207 0.94996042 0.96302938 0.96118149]
<H> =  3.8768259168631207
3.8768259168631207
Number of Hamiltonian terms/required measurements: 2050
Number of required measurements after optimization: 523
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_measurement_optimize.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
+ (-0.04207897647782276) [I0]
+ (0.12293305056183798) [Z0 Z2]
+ (0.12293305056183798) [Z1 Z3]
+ (0.17627640804319591) [Z2 Z3]
   (-46.46390678868891) [I0]
+ (0.7829661725950217) [Z10]
+ (0.7829661725950217) [Z11]
+ (0.8084581961720493) [Z12]
+ (0.8084581961720494) [Z13]
+ (1.2034402289145643) [Z4]
+ (1.2034402289145643) [Z5]
+ (1.3096862988615423) [Z6]
+ (1.3096862988615423) [Z7]
+ (1.3693525634718182) [Z9]
+ (1.6538942226831659) [Z2]
+ (1.653894222683166) [Z3]
+ (12.41263074211177) [Z0]
+ (12.41263074211177) [Z1]
+ (-8.194261372377456e-06) [Y10 Y12]
+ (-8.194261372377456e-06) [X10 X12]
+ (-1.8540608580214287e-06) [Y5 Y7]
+ (-1.8540608580214287e-06) [X5 X7]
+ (-7.764994120273387e-07) [Y3 Y5]
+ (-7.764994120273387e-07) [X3 X5]
+ (-5.929765815476512e-07) [Y4 Y6]
+ (-5.929765815476512e-07) [X4 X6]
+ (1.6021167407100396e-06) [Y2 Y4]
+ (1.6021167407100396e-06) [X2 X4]
+ (7.954413176256564e-06) [Y11 Y13]
+ (7.954413176256564e-06) [X11 X13]
+ (0.003276971931231579) [Y1 Y3]
+ (0.003276971931231579) [X1 X3]
+ (0.10433064780651359) [Y0 Y2]
+ (0.10433064780651359) [X0 X2]
+ (0.1127038692033222) [Z10 Z12]
+ (0.1127038692033222) [Z11 Z13]
+ (0.11383573679388641) [Z4 Z12]
+ (0.11383573679388641) [Z5 Z13]
+ (0.11952438964682675) [Z6 Z10]
+ (0.11952438964682675) [Z7 Z11]
+ (0.1248999091723761) [Z4 Z10]
+ (0.1248999091723761) [Z5 Z11]
+ (0.12495807739503169) [Z2 Z4]
+ (0.12495807739503169) [Z3 Z5]
+ (0.12799502492468376) [Z2 Z10]
+ (0.12799502492468376) [Z3 Z11]
+ (0.1340171526196367) [Z6 Z12]
+ (0.1340171526196367) [Z7 Z13]
+ (0.13701191674040727) [Z4 Z6]
+ (0.13701191674040727) [Z5 Z7]
+ (0.13734953064261324) [Z6 Z11]
+ (0.13734953064261324) [Z7 Z10]
+ (0.13739104762683166) [Z2 Z6]
+ (0.13739104762683166) [Z3 Z7]
+ (0.13766872645852588) [Z8 Z10]
+ (0.13766872645852588) [Z9 Z11]
+ (0.14011289865354748) [Z2 Z12]
+ (0.14011289865354748) [Z3 Z13]
+ (0.14257997712485754) [Z4 Z11]
+ (0.14257997712485754) [Z5 Z10]
+ (0.14722943218766182) [Z8 Z11]
+ (0.14722943218766182) [Z9 Z10]
+ (0.14899430575065525) [Z4 Z7]
+ (0.14899430575065525) [Z5 Z6]
+ (0.14926355147388917) [Z10 Z11]
+ (0.14960702684445287) [Z4 Z8]
+ (0.14960702684445287) [Z5 Z9]
+ (0.14973486803496905) [Z8 Z12]
+ (0.14973486803496905) [Z9 Z13]
+ (0.15071408121008237) [Z2 Z8]
+ (0.15071408121008237) [Z3 Z9]
+ (0.15138327161428816) [Z6 Z13]
+ (0.15138327161428816) [Z7 Z12]
+ (0.1521504070886902) [Z4 Z13]
+ (0.1521504070886902) [Z5 Z12]
+ (0.15337968243314115) [Z2 Z11]
+ (0.15337968243314115) [Z3 Z10]
+ (0.15435748657223597) [Z12 Z13]
+ (0.15569010671752387) [Z2 Z13]
+ (0.15569010671752387) [Z3 Z12]
+ (0.15582269051553088) [Z8 Z13]
+ (0.15582269051553088) [Z9 Z12]
+ (0.1567639617643098) [Z4 Z9]
+ (0.1567639617643098) [Z5 Z8]
+ (0.15755314797985648) [Z4 Z5]
+ (0.1607976453483851) [Z2 Z5]
+ (0.1607976453483851) [Z3 Z4]
+ (0.16756653265461244) [Z6 Z8]
+ (0.16756653265461244) [Z7 Z9]
+ (0.16853486561579867) [Z2 Z7]
+ (0.16853486561579867) [Z3 Z6]
+ (0.18143991440303853) [Z6 Z9]
+ (0.18143991440303853) [Z7 Z8]
+ (0.1818908579075124) [Z2 Z3]
+ (0.1869082047691248) [Z2 Z9]
+ (0.1869082047691248) [Z3 Z8]
+ (0.19299723935364269) [Z0 Z10]
+ (0.19299723935364269) [Z1 Z11]
+ (0.19392534613270163) [Z6 Z7]
+ (0.19661770890342123) [Z0 Z4]
+ (0.19661770890342123) [Z1 Z5]
+ (0.199363545373608) [Z0 Z5]
+ (0.199363545373608) [Z1 Z4]
+ (0.200728664604418) [Z0 Z11]
+ (0.200728664604418) [Z1 Z10]
+ (0.21102659849791477) [Z0 Z12]
+ (0.21102659849791477) [Z1 Z13]
+ (0.21631037498631772) [Z0 Z13]
+ (0.21631037498631772) [Z1 Z12]
+ (0.2200397733437608) [Z8 Z9]
+ (0.23671080783830323) [Z0 Z2]
+ (0.23671080783830323) [Z1 Z3]
+ (0.24164663936017156) [Z0 Z6]
+ (0.24164663936017156) [Z1 Z7]
+ (0.2485348337131421) [Z0 Z7]
+ (0.2485348337131421) [Z1 Z6]
+ (0.2512944567459158) [Z0 Z3]
+ (0.2512944567459158) [Z1 Z2]
+ (1.1861763734860487) [Z0 Z1]
+ (-1.2260484989523135e-05) [Y4 Z5 Y6]
+ (-1.2260484989523135e-05) [X4 Z5 X6]
+ (-1.2260484989523135e-05) [Y5 Z6 Y7]
+ (-1.2260484989523135e-05) [X5 Z6 X7]
+ (-1.072231215823195e-05) [Y11 Z12 Y13]
+ (-1.072231215823195e-05) [X11 Z12 X13]
+ (-1.0722312158231943e-05) [Y10 Z11 Y12]
+ (-1.0722312158231943e-05) [X10 Z11 X12]
+ (-3.887051673775729e-06) [Y3 Z4 Y5]
+ (-3.887051673775729e-06) [X3 Z4 X5]
+ (-3.887051673775728e-06) [Y2 Z3 Y4]
+ (-3.887051673775728e-06) [X2 Z3 X4]
+ (0.1250703257977183) [Y0 Z1 Y2]
+ (0.1250703257977183) [X0 Z1 X2]
+ (0.12507032579771832) [Y1 Z2 Y3]
+ (0.12507032579771832) [X1 Z2 X3]
+ (-0.03831467029480382) [Y4 Y5 X12 X13]
+ (-0.03831467029480382) [X4 X5 Y12 Y13]
+ (-0.036194123559042446) [Y2 Y3 X8 X9]
+ (-0.036194123559042446) [X2 X3 Y8 Y9]
+ (-0.035839567953353385) [Y2 Y3 X4 X5]
+ (-0.035839567953353385) [X2 X3 Y4 Y5]
+ (-0.031143817988967006) [Y2 Y3 X6 X7]
+ (-0.031143817988967006) [X2 X3 Y6 Y7]
+ (-0.028685183716105782) [Y10 Y11 X12 X13]
+ (-0.028685183716105782) [X10 X11 Y12 Y13]
+ (-0.02599617759802117) [Y3 Z4 Z5 Y7]
+ (-0.02599617759802117) [X3 Z4 Z5 X7]
+ (-0.0253846575084574) [Y2 Y3 X10 X11]
+ (-0.0253846575084574) [X2 X3 Y10 Y11]
+ (-0.01902824244384724) [Y3 Y4 X11 X12]
+ (-0.01902824244384724) [X3 X4 Y11 Y12]
+ (-0.0178251409957865) [Y6 Y7 X10 X11]
+ (-0.0178251409957865) [X6 X7 Y10 Y11]
+ (-0.01768006795248143) [Y4 Y5 X10 X11]
+ (-0.01768006795248143) [X4 X5 Y10 Y11]
+ (-0.01736611899465143) [Y6 Y7 X12 X13]
+ (-0.01736611899465143) [X6 X7 Y12 Y13]
+ (-0.015577208063976404) [Y2 Y3 X12 X13]
+ (-0.015577208063976404) [X2 X3 Y12 Y13]
+ (-0.014583648907612557) [Y0 Y1 X2 X3]
+ (-0.014583648907612557) [X0 X1 Y2 Y3]
+ (-0.013873381748426101) [Y6 Y7 X8 X9]
+ (-0.013873381748426101) [X6 X7 Y8 Y9]
+ (-0.011982389010247967) [Y4 Y5 X6 X7]
+ (-0.011982389010247967) [X4 X5 Y6 Y7]
+ (-0.011285190200840884) [Y5 X6 X11 Y12]
+ (-0.011285190200840884) [X5 Y6 Y11 X12]
+ (-0.009560705729135982) [Y8 Y9 X10 X11]
+ (-0.009560705729135982) [X8 X9 Y10 Y11]
+ (-0.008125251921381011) [Y1 X2 X8 Y9]
+ (-0.008125251921381011) [Y1 Y2 Y8 Y9]
+ (-0.008125251921381011) [X1 X2 X8 X9]
+ (-0.008125251921381011) [X1 Y2 Y8 X9]
+ (-0.0077314252507753025) [Y0 Y1 X10 X11]
+ (-0.0077314252507753025) [X0 X1 Y10 Y11]
+ (-0.0071569349198569365) [Y4 Y5 X8 X9]
+ (-0.0071569349198569365) [X4 X5 Y8 Y9]
+ (-0.006888194352970569) [Y0 Y1 X6 X7]
+ (-0.006888194352970569) [X0 X1 Y6 Y7]
+ (-0.006509361201177233) [Y0 Y1 X8 X9]
+ (-0.006509361201177233) [X0 X1 Y8 Y9]
+ (-0.006087822480561848) [Y8 Y9 X12 X13]
+ (-0.006087822480561848) [X8 X9 Y12 Y13]
+ (-0.005283776488402953) [Y0 Y1 X12 X13]
+ (-0.005283776488402953) [X0 X1 Y12 Y13]
+ (-0.005143391768825136) [Y3 X4 X5 Y6]
+ (-0.005143391768825136) [X3 Y4 Y5 X6]
+ (-0.004684903388155178) [Y1 X2 X6 Y7]
+ (-0.004684903388155178) [Y1 Y2 Y6 Y7]
+ (-0.004684903388155178) [X1 X2 X6 X7]
+ (-0.004684903388155178) [X1 Y2 Y6 X7]
+ (-0.00457500762663919) [Y1 X2 X12 Y13]
+ (-0.00457500762663919) [Y1 Y2 Y12 Y13]
+ (-0.00457500762663919) [X1 X2 X12 X13]
+ (-0.00457500762663919) [X1 Y2 Y12 X13]
+ (-0.004424855449441846) [Y1 X2 X4 Y5]
+ (-0.004424855449441846) [Y1 Y2 Y4 Y5]
+ (-0.004424855449441846) [X1 X2 X4 X5]
+ (-0.004424855449441846) [X1 Y2 Y4 X5]
+ (-0.003479511890334384) [Y2 Z3 Z5 Y6]
+ (-0.003479511890334384) [X2 Z3 Z5 X6]
+ (-0.003479511890334384) [Y3 Z4 Z6 Y7]
+ (-0.003479511890334384) [X3 Z4 Z6 X7]
+ (-0.0027458364701868072) [Y0 Y1 X4 X5]
+ (-0.0027458364701868072) [X0 X1 Y4 Y5]
+ (-0.0017992194936630364) [Y1 X2 X10 Y11]
+ (-0.0017992194936630364) [Y1 Y2 Y10 Y11]
+ (-0.0017992194936630364) [X1 X2 X10 X11]
+ (-0.0017992194936630364) [X1 Y2 Y10 X11]
+ (-0.0002921986261110724) [Y7 Y8 X9 X10]
+ (-0.0002921986261110724) [X7 X8 Y9 Y10]
+ (-8.194261372377456e-06) [Z10 Y11 Z12 Y13]
+ (-8.194261372377456e-06) [Z10 X11 Z12 X13]
+ (-7.801707500595328e-06) [Y2 Z3 Y4 Z11]
+ (-7.801707500595328e-06) [X2 Z3 X4 Z11]
+ (-7.801707500595328e-06) [Y3 Z4 Y5 Z10]
+ (-7.801707500595328e-06) [X3 Z4 X5 Z10]
+ (-4.643051068536201e-06) [Y3 X4 X10 Y11]
+ (-4.643051068536201e-06) [Y3 Y4 Y10 Y11]
+ (-4.643051068536201e-06) [X3 X4 X10 X11]
+ (-4.643051068536201e-06) [X3 Y4 Y10 X11]
+ (-4.58885515570104e-06) [Y4 Z5 Y6 Z13]
+ (-4.58885515570104e-06) [X4 Z5 X6 Z13]
+ (-4.58885515570104e-06) [Y5 Z6 Y7 Z12]
+ (-4.58885515570104e-06) [X5 Z6 X7 Z12]
+ (-4.556569218164284e-06) [Y5 X6 X12 Y13]
+ (-4.556569218164284e-06) [Y5 Y6 Y12 Y13]
+ (-4.556569218164284e-06) [X5 X6 X12 X13]
+ (-4.556569218164284e-06) [X5 Y6 Y12 X13]
+ (-3.6945132946186404e-06) [Y4 X5 X11 Y12]
+ (-3.6945132946186404e-06) [Y4 Y5 Y11 Y12]
+ (-3.6945132946186404e-06) [X4 X5 X11 X12]
+ (-3.6945132946186404e-06) [X4 Y5 Y11 X12]
+ (-3.3440815565826798e-06) [Z0 Y5 Z6 Y7]
+ (-3.3440815565826798e-06) [Z0 X5 Z6 X7]
+ (-3.3440815565826798e-06) [Z1 Y4 Z5 Y6]
+ (-3.3440815565826798e-06) [Z1 X4 Z5 X6]
+ (-3.1586564320591257e-06) [Y2 Z3 Y4 Z10]
+ (-3.1586564320591257e-06) [X2 Z3 X4 Z10]
+ (-3.1586564320591257e-06) [Y3 Z4 Y5 Z11]
+ (-3.1586564320591257e-06) [X3 Z4 X5 Z11]
+ (-3.099349243695453e-06) [Z0 Y4 Z5 Y6]
+ (-3.099349243695453e-06) [Z0 X4 Z5 X6]
+ (-3.099349243695453e-06) [Z1 Y5 Z6 Y7]
+ (-3.099349243695453e-06) [Z1 X5 Z6 X7]
+ (-2.890967881813435e-06) [Z6 Y11 Z12 Y13]
+ (-2.890967881813435e-06) [Z6 X11 Z12 X13]
+ (-2.890967881813435e-06) [Z7 Y10 Z11 Y12]
+ (-2.890967881813435e-06) [Z7 X10 Z11 X12]
+ (-2.1776646051963157e-06) [Z0 Y10 Z11 Y12]
+ (-2.1776646051963157e-06) [Z0 X10 Z11 X12]
+ (-2.1776646051963157e-06) [Z1 Y11 Z12 Y13]
+ (-2.1776646051963157e-06) [Z1 X11 Z12 X13]
+ (-1.8818501832595167e-06) [Y4 Z5 Y6 Z9]
+ (-1.8818501832595167e-06) [X4 Z5 X6 Z9]
+ (-1.8818501832595167e-06) [Y5 Z6 Y7 Z8]
+ (-1.8818501832595167e-06) [X5 Z6 X7 Z8]
+ (-1.8551201216492506e-06) [Z6 Y10 Z11 Y12]
+ (-1.8551201216492506e-06) [Z6 X10 Z11 X12]
+ (-1.8551201216492506e-06) [Z7 Y11 Z12 Y13]
+ (-1.8551201216492506e-06) [Z7 X11 Z12 X13]
+ (-1.8540608580214285e-06) [Y4 Z5 Y6 Z7]
+ (-1.8540608580214285e-06) [X4 Z5 X6 Z7]
+ (-1.8163031699522794e-06) [Z4 Y11 Z12 Y13]
+ (-1.8163031699522794e-06) [Z4 X11 Z12 X13]
+ (-1.8163031699522794e-06) [Z5 Y10 Z11 Y12]
+ (-1.8163031699522794e-06) [Z5 X10 Z11 X12]
+ (-1.6923978286054116e-06) [Y4 Z5 Y6 Z10]
+ (-1.6923978286054116e-06) [X4 Z5 X6 Z10]
+ (-1.6923978286054116e-06) [Y5 Z6 Y7 Z11]
+ (-1.6923978286054116e-06) [X5 Z6 X7 Z11]
+ (-1.6148794140552558e-06) [Z0 Y11 Z12 Y13]
+ (-1.6148794140552558e-06) [Z0 X11 Z12 X13]
+ (-1.6148794140552558e-06) [Z1 Y10 Z11 Y12]
+ (-1.6148794140552558e-06) [Z1 X10 Z11 X12]
+ (-1.5973171979256088e-06) [Z8 Y10 Z11 Y12]
+ (-1.5973171979256088e-06) [Z8 X10 Z11 X12]
+ (-1.5973171979256088e-06) [Z9 Y11 Z12 Y13]
+ (-1.5973171979256088e-06) [Z9 X11 Z12 X13]
+ (-1.45484244909288e-06) [Y3 X4 X6 Y7]
+ (-1.45484244909288e-06) [Y3 Y4 Y6 Y7]
+ (-1.45484244909288e-06) [X3 X4 X6 X7]
+ (-1.45484244909288e-06) [X3 Y4 Y6 X7]
+ (-1.3980449081508429e-06) [Y4 Z5 Y6 Z8]
+ (-1.3980449081508429e-06) [X4 Z5 X6 Z8]
+ (-1.3980449081508429e-06) [Y5 Z6 Y7 Z9]
+ (-1.3980449081508429e-06) [X5 Z6 X7 Z9]
+ (-1.1954890099964784e-06) [Y2 Z3 Y4 Z7]
+ (-1.1954890099964784e-06) [X2 Z3 X4 Z7]
+ (-1.1954890099964784e-06) [Y3 Z4 Y5 Z6]
+ (-1.1954890099964784e-06) [X3 Z4 X5 Z6]
+ (-1.1908508083965414e-06) [Z0 Y3 Z4 Y5]
+ (-1.1908508083965414e-06) [Z0 X3 Z4 X5]
+ (-1.1908508083965414e-06) [Z1 Y2 Z3 Y4]
+ (-1.1908508083965414e-06) [Z1 X2 Z3 X4]
+ (-1.1708301370556437e-06) [Z2 Y5 Z6 Y7]
+ (-1.1708301370556437e-06) [Z2 X5 Z6 X7]
+ (-1.1708301370556437e-06) [Z3 Y4 Z5 Y6]
+ (-1.1708301370556437e-06) [Z3 X4 Z5 X6]
+ (-1.0632283424462652e-06) [Z2 Y10 Z11 Y12]
+ (-1.0632283424462652e-06) [Z2 X10 Z11 X12]
+ (-1.0632283424462652e-06) [Z3 Y11 Z12 Y13]
+ (-1.0632283424462652e-06) [Z3 X11 Z12 X13]
+ (-1.0358477601641843e-06) [Y6 X7 X11 Y12]
+ (-1.0358477601641843e-06) [Y6 Y7 Y11 Y12]
+ (-1.0358477601641843e-06) [X6 X7 X11 X12]
+ (-1.0358477601641843e-06) [X6 Y7 Y11 X12]
+ (-9.509249751751254e-07) [Z2 Y4 Z5 Y6]
+ (-9.509249751751254e-07) [Z2 X4 Z5 X6]
+ (-9.509249751751254e-07) [Z3 Y5 Z6 Y7]
+ (-9.509249751751254e-07) [Z3 X5 Z6 X7]
+ (-9.344557777532479e-07) [Z8 Y11 Z12 Y13]
+ (-9.344557777532479e-07) [Z8 X11 Z12 X13]
+ (-9.344557777532479e-07) [Z9 Y10 Z11 Y12]
+ (-9.344557777532479e-07) [Z9 X10 Z11 X12]
+ (-8.337746754786812e-07) [Z0 Y2 Z3 Y4]
+ (-8.337746754786812e-07) [Z0 X2 Z3 X4]
+ (-8.337746754786812e-07) [Z1 Y3 Z4 Y5]
+ (-8.337746754786812e-07) [Z1 X3 Z4 X5]
+ (-7.956895372896644e-07) [Y3 X4 X8 Y9]
+ (-7.956895372896644e-07) [Y3 Y4 Y8 Y9]
+ (-7.956895372896644e-07) [X3 X4 X8 X9]
+ (-7.956895372896644e-07) [X3 Y4 Y8 X9]
+ (-7.764994120273387e-07) [Y2 Z3 Y4 Z5]
+ (-7.764994120273387e-07) [X2 Z3 X4 Z5]
+ (-5.929765815476512e-07) [Z4 Y5 Z6 Y7]
+ (-5.929765815476512e-07) [Z4 X5 Z6 X7]
+ (-5.770052995420394e-07) [Y2 Z3 Y4 Z9]
+ (-5.770052995420394e-07) [X2 Z3 X4 Z9]
+ (-5.770052995420394e-07) [Y3 Z4 Y5 Z8]
+ (-5.770052995420394e-07) [X3 Z4 X5 Z8]
+ (-5.471647744782934e-07) [Y1 Y2 X11 X12]
+ (-5.471647744782934e-07) [X1 X2 Y11 Y12]
+ (-4.838052751086737e-07) [Y5 X6 X8 Y9]
+ (-4.838052751086737e-07) [Y5 Y6 Y8 Y9]
+ (-4.838052751086737e-07) [X5 X6 X8 X9]
+ (-4.838052751086737e-07) [X5 Y6 Y8 X9]
+ (-3.5707613291786027e-07) [Y0 X1 X3 Y4]
+ (-3.5707613291786027e-07) [Y0 Y1 Y3 Y4]
+ (-3.5707613291786027e-07) [X0 X1 X3 X4]
+ (-3.5707613291786027e-07) [X0 Y1 Y3 X4]
+ (-2.4473231288722685e-07) [Y0 X1 X5 Y6]
+ (-2.4473231288722685e-07) [Y0 Y1 Y5 Y6]
+ (-2.4473231288722685e-07) [X0 X1 X5 X6]
+ (-2.4473231288722685e-07) [X0 Y1 Y5 X6]
+ (-2.1990516188051842e-07) [Y2 X3 X5 Y6]
+ (-2.1990516188051842e-07) [Y2 Y3 Y5 Y6]
+ (-2.1990516188051842e-07) [X2 X3 X5 X6]
+ (-2.1990516188051842e-07) [X2 Y3 Y5 X6]
+ (-1.9332412771531168e-07) [Y1 X2 X3 Y4]
+ (-1.9332412771531168e-07) [X1 Y2 Y3 X4]
+ (-1.2919694865188438e-07) [Y1 Z2 Z3 Y5]
+ (-1.2919694865188438e-07) [X1 Z2 Z3 X5]
+ (1.7379332623595084e-07) [Y0 Z1 Z3 Y4]
+ (1.7379332623595084e-07) [X0 Z1 Z3 X4]
+ (1.7379332623595084e-07) [Y1 Z2 Z4 Y5]
+ (1.7379332623595084e-07) [X1 Z2 Z4 X5]
+ (1.9332412771531168e-07) [Y1 Y2 X3 X4]
+ (1.9332412771531168e-07) [X1 X2 Y3 Y4]
+ (2.1868423774762512e-07) [Y2 Z3 Y4 Z8]
+ (2.1868423774762512e-07) [X2 Z3 X4 Z8]
+ (2.1868423774762512e-07) [Y3 Z4 Y5 Z9]
+ (2.1868423774762512e-07) [X3 Z4 X5 Z9]
+ (2.5935343909640186e-07) [Y2 Z3 Y4 Z6]
+ (2.5935343909640186e-07) [X2 Z3 X4 Z6]
+ (2.5935343909640186e-07) [Y3 Z4 Y5 Z7]
+ (2.5935343909640186e-07) [X3 Z4 X5 Z7]
+ (3.606071867913903e-07) [Y0 Z1 Z2 Y4]
+ (3.606071867913903e-07) [X0 Z1 Z2 X4]
+ (3.606071867913903e-07) [Y1 Z3 Z4 Y5]
+ (3.606071867913903e-07) [X1 Z3 Z4 X5]
+ (5.471647744782934e-07) [Y1 X2 X11 Y12]
+ (5.471647744782934e-07) [X1 Y2 Y11 X12]
+ (5.627851911410602e-07) [Y0 X1 X11 Y12]
+ (5.627851911410602e-07) [Y0 Y1 Y11 Y12]
+ (5.627851911410602e-07) [X0 X1 X11 X12]
+ (5.627851911410602e-07) [X0 Y1 Y11 X12]
+ (6.628614201723609e-07) [Y8 X9 X11 Y12]
+ (6.628614201723609e-07) [Y8 Y9 Y11 Y12]
+ (6.628614201723609e-07) [X8 X9 X11 X12]
+ (6.628614201723609e-07) [X8 Y9 Y11 X12]
+ (1.1094407591077679e-06) [Z2 Y11 Z12 Y13]
+ (1.1094407591077679e-06) [Z2 X11 Z12 X13]
+ (1.1094407591077679e-06) [Z3 Y10 Z11 Y12]
+ (1.1094407591077679e-06) [Z3 X10 Z11 X12]
+ (1.6021167407100396e-06) [Z2 Y3 Z4 Y5]
+ (1.6021167407100396e-06) [Z2 X3 Z4 X5]
+ (1.8782101246663608e-06) [Z4 Y10 Z11 Y12]
+ (1.8782101246663608e-06) [Z4 X10 Z11 X12]
+ (1.8782101246663608e-06) [Z5 Y11 Z12 Y13]
+ (1.8782101246663608e-06) [Z5 X11 Z12 X13]
+ (2.1726691015540332e-06) [Y2 X3 X11 Y12]
+ (2.1726691015540332e-06) [Y2 Y3 Y11 Y12]
+ (2.1726691015540332e-06) [X2 X3 X11 X12]
+ (2.1726691015540332e-06) [X2 Y3 Y11 X12]
+ (3.117447946114733e-06) [Y0 Z2 Z3 Y4]
+ (3.117447946114733e-06) [X0 Z2 Z3 X4]
+ (3.5390541844604424e-06) [Y2 Z3 Y4 Z12]
+ (3.5390541844604424e-06) [X2 Z3 X4 Z12]
+ (3.5390541844604424e-06) [Y3 Z4 Y5 Z13]
+ (3.5390541844604424e-06) [X3 Z4 X5 Z13]
+ (4.281913884909852e-06) [Y4 Z5 Y6 Z11]
+ (4.281913884909852e-06) [X4 Z5 X6 Z11]
+ (4.281913884909852e-06) [Y5 Z6 Y7 Z10]
+ (4.281913884909852e-06) [X5 Z6 X7 Z10]
+ (5.27588312224402e-06) [Y3 X4 X12 Y13]
+ (5.27588312224402e-06) [Y3 Y4 Y12 Y13]
+ (5.27588312224402e-06) [X3 X4 X12 X13]
+ (5.27588312224402e-06) [X3 Y4 Y12 X13]
+ (5.974311713515264e-06) [Y5 X6 X10 Y11]
+ (5.974311713515264e-06) [Y5 Y6 Y10 Y11]
+ (5.974311713515264e-06) [X5 X6 X10 X11]
+ (5.974311713515264e-06) [X5 Y6 Y10 X11]
+ (7.954413176256564e-06) [Y10 Z11 Y12 Z13]
+ (7.954413176256564e-06) [X10 Z11 X12 Z13]
+ (8.814937306704463e-06) [Y2 Z3 Y4 Z13]
+ (8.814937306704463e-06) [X2 Z3 X4 Z13]
+ (8.814937306704463e-06) [Y3 Z4 Y5 Z12]
+ (8.814937306704463e-06) [X3 Z4 X5 Z12]
+ (0.0002921986261110724) [Y7 X8 X9 Y10]
+ (0.0002921986261110724) [X7 Y8 Y9 X10]
+ (0.0004956762314915796) [Y2 Z4 Z5 Y6]
+ (0.0004956762314915796) [X2 Z4 Z5 X6]
+ (0.0011059037691896418) [Y0 Z1 Y2 Z5]
+ (0.0011059037691896418) [X0 Z1 X2 Z5]
+ (0.0011059037691896418) [Y1 Z2 Y3 Z4]
+ (0.0011059037691896418) [X1 Z2 X3 Z4]
+ (0.0016638798784907524) [Y2 Z3 Z4 Y6]
+ (0.0016638798784907524) [X2 Z3 Z4 X6]
+ (0.0016638798784907524) [Y3 Z5 Z6 Y7]
+ (0.0016638798784907524) [X3 Z5 Z6 X7]
+ (0.0017560707018412195) [Y0 Z1 Y2 Z11]
+ (0.0017560707018412195) [X0 Z1 X2 Z11]
+ (0.0017560707018412195) [Y1 Z2 Y3 Z10]
+ (0.0017560707018412195) [X1 Z2 X3 Z10]
+ (0.002326230623158023) [Y0 Z1 Y2 Z13]
+ (0.002326230623158023) [X0 Z1 X2 Z13]
+ (0.002326230623158023) [Y1 Z2 Y3 Z12]
+ (0.002326230623158023) [X1 Z2 X3 Z12]
+ (0.0027458364701868072) [Y0 X1 X4 Y5]
+ (0.0027458364701868072) [X0 Y1 Y4 X5]
+ (0.0029297686747509913) [Y0 Z1 Y2 Z9]
+ (0.0029297686747509913) [X0 Z1 X2 Z9]
+ (0.0029297686747509913) [Y1 Z2 Y3 Z8]
+ (0.0029297686747509913) [X1 Z2 X3 Z8]
+ (0.0032769719312315784) [Y0 Z1 Y2 Z3]
+ (0.0032769719312315784) [X0 Z1 X2 Z3]
+ (0.0033476175306661237) [Y0 Z1 Y2 Z7]
+ (0.0033476175306661237) [X0 Z1 X2 Z7]
+ (0.0033476175306661237) [Y1 Z2 Y3 Z6]
+ (0.0033476175306661237) [X1 Z2 X3 Z6]
+ (0.0035552901955042556) [Y0 Z1 Y2 Z10]
+ (0.0035552901955042556) [X0 Z1 X2 Z10]
+ (0.0035552901955042556) [Y1 Z2 Y3 Z11]
+ (0.0035552901955042556) [X1 Z2 X3 Z11]
+ (0.005143391768825136) [Y3 Y4 X5 X6]
+ (0.005143391768825136) [X3 X4 Y5 Y6]
+ (0.005283776488402953) [Y0 X1 X12 Y13]
+ (0.005283776488402953) [X0 Y1 Y12 X13]
+ (0.005530759218631488) [Y0 Z1 Y2 Z4]
+ (0.005530759218631488) [X0 Z1 X2 Z4]
+ (0.005530759218631488) [Y1 Z2 Y3 Z5]
+ (0.005530759218631488) [X1 Z2 X3 Z5]
+ (0.006087822480561848) [Y8 X9 X12 Y13]
+ (0.006087822480561848) [X8 Y9 Y12 X13]
+ (0.006509361201177233) [Y0 X1 X8 Y9]
+ (0.006509361201177233) [X0 Y1 Y8 X9]
+ (0.006888194352970569) [Y0 X1 X6 Y7]
+ (0.006888194352970569) [X0 Y1 Y6 X7]
+ (0.006901238249797211) [Y0 Z1 Y2 Z12]
+ (0.006901238249797211) [X0 Z1 X2 Z12]
+ (0.006901238249797211) [Y1 Z2 Y3 Z13]
+ (0.006901238249797211) [X1 Z2 X3 Z13]
+ (0.0071569349198569365) [Y4 X5 X8 Y9]
+ (0.0071569349198569365) [X4 Y5 Y8 X9]
+ (0.0077314252507753025) [Y0 X1 X10 Y11]
+ (0.0077314252507753025) [X0 Y1 Y10 X11]
+ (0.008032520918821302) [Y0 Z1 Y2 Z6]
+ (0.008032520918821302) [X0 Z1 X2 Z6]
+ (0.008032520918821302) [Y1 Z2 Y3 Z7]
+ (0.008032520918821302) [X1 Z2 X3 Z7]
+ (0.009560705729135982) [Y8 X9 X10 Y11]
+ (0.009560705729135982) [X8 Y9 Y10 X11]
+ (0.011055020596132) [Y0 Z1 Y2 Z8]
+ (0.011055020596132) [X0 Z1 X2 Z8]
+ (0.011055020596132) [Y1 Z2 Y3 Z9]
+ (0.011055020596132) [X1 Z2 X3 Z9]
+ (0.011285190200840884) [Y5 Y6 X11 X12]
+ (0.011285190200840884) [X5 X6 Y11 Y12]
+ (0.0113072740088483) [Y7 Z8 Z9 Y11]
+ (0.0113072740088483) [X7 Z8 Z9 X11]
+ (0.011982389010247967) [Y4 X5 X6 Y7]
+ (0.011982389010247967) [X4 Y5 Y6 X7]
+ (0.013873381748426101) [Y6 X7 X8 Y9]
+ (0.013873381748426101) [X6 Y7 Y8 X9]
+ (0.014583648907612557) [Y0 X1 X2 Y3]
+ (0.014583648907612557) [X0 Y1 Y2 X3]
+ (0.015577208063976404) [Y2 X3 X12 Y13]
+ (0.015577208063976404) [X2 Y3 Y12 X13]
+ (0.01736611899465143) [Y6 X7 X12 Y13]
+ (0.01736611899465143) [X6 Y7 Y12 X13]
+ (0.01768006795248143) [Y4 X5 X10 Y11]
+ (0.01768006795248143) [X4 Y5 Y10 X11]
+ (0.0178251409957865) [Y6 X7 X10 Y11]
+ (0.0178251409957865) [X6 Y7 Y10 X11]
+ (0.01902824244384724) [Y3 X4 X11 Y12]
+ (0.01902824244384724) [X3 Y4 Y11 X12]
+ (0.0253846575084574) [Y2 X3 X10 Y11]
+ (0.0253846575084574) [X2 Y3 Y10 X11]
+ (0.028685183716105782) [Y10 X11 X12 Y13]
+ (0.028685183716105782) [X10 Y11 Y12 X13]
+ (0.029812424517345795) [Y6 Z7 Z8 Y10]
+ (0.029812424517345795) [X6 Z7 Z8 X10]
+ (0.029812424517345795) [Y7 Z9 Z10 Y11]
+ (0.029812424517345795) [X7 Z9 Z10 X11]
+ (0.03010462314345687) [Y6 Z7 Z9 Y10]
+ (0.03010462314345687) [X6 Z7 Z9 X10]
+ (0.03010462314345687) [Y7 Z8 Z10 Y11]
+ (0.03010462314345687) [X7 Z8 Z10 X11]
+ (0.030787505389143904) [Y6 Z8 Z9 Y10]
+ (0.030787505389143904) [X6 Z8 Z9 X10]
+ (0.031143817988967006) [Y2 X3 X6 Y7]
+ (0.031143817988967006) [X2 Y3 Y6 X7]
+ (0.035839567953353385) [Y2 X3 X4 Y5]
+ (0.035839567953353385) [X2 Y3 Y4 X5]
+ (0.036194123559042446) [Y2 X3 X8 Y9]
+ (0.036194123559042446) [X2 Y3 Y8 X9]
+ (0.03831467029480382) [Y4 X5 X12 Y13]
+ (0.03831467029480382) [X4 Y5 Y12 X13]
+ (0.10433064780651359) [Z0 Y1 Z2 Y3]
+ (0.10433064780651359) [Z0 X1 Z2 X3]
+ (-0.12133276911042422) [Y3 Z4 Z5 Z6 Y7]
+ (-0.12133276911042422) [X3 Z4 Z5 Z6 X7]
+ (-0.1213327691104242) [Y2 Z3 Z4 Z5 Y6]
+ (-0.1213327691104242) [X2 Z3 Z4 Z5 X6]
+ (3.202076879236079e-06) [Y0 Z1 Z2 Z3 Y4]
+ (3.202076879236079e-06) [X0 Z1 Z2 Z3 X4]
+ (3.202076879236079e-06) [Y1 Z2 Z3 Z4 Y5]
+ (3.202076879236079e-06) [X1 Z2 Z3 Z4 X5]
+ (0.22848106564918877) [Y7 Z8 Z9 Z10 Y11]
+ (0.22848106564918877) [X7 Z8 Z9 Z10 X11]
+ (0.2284810656491888) [Y6 Z7 Z8 Z9 Y10]
+ (0.2284810656491888) [X6 Z7 Z8 Z9 X10]
+ (-0.032767657823290615) [Z0 Y3 Z4 Z5 Z6 Y7]
+ (-0.032767657823290615) [Z0 X3 Z4 Z5 Z6 X7]
+ (-0.032767657823290615) [Z1 Y2 Z3 Z4 Z5 Y6]
+ (-0.032767657823290615) [Z1 X2 Z3 Z4 Z5 X6]
+ (-0.027115036845273263) [Z0 Y2 Z3 Z4 Z5 Y6]
+ (-0.027115036845273263) [Z0 X2 Z3 Z4 Z5 X6]
+ (-0.027115036845273263) [Z1 Y3 Z4 Z5 Z6 Y7]
+ (-0.027115036845273263) [Z1 X3 Z4 Z5 Z6 X7]
+ (-0.02599617759802117) [Y2 Z3 Z4 Z5 Y6 Z7]
+ (-0.02599617759802117) [X2 Z3 Z4 Z5 X6 Z7]
+ (-0.01756120240964622) [Y2 Z3 Z4 Z5 Y6 Z9]
+ (-0.01756120240964622) [X2 Z3 Z4 Z5 X6 Z9]
+ (-0.01756120240964622) [Y3 Z4 Z5 Z6 Y7 Z8]
+ (-0.01756120240964622) [X3 Z4 Z5 Z6 X7 Z8]
+ (-0.014564531231172996) [Y7 Z8 Z9 X10 X12 Y13]
+ (-0.014564531231172996) [Y7 Z8 Z9 Y10 Y12 Y13]
+ (-0.014564531231172996) [X7 Z8 Z9 X10 X12 X13]
+ (-0.014564531231172996) [X7 Z8 Z9 Y10 Y12 X13]
+ (-0.012215040997613936) [Y4 Z5 Y6 Y11 Z12 Y13]
+ (-0.012215040997613936) [Y4 Z5 Y6 X11 Z12 X13]
+ (-0.012215040997613936) [X4 Z5 X6 Y11 Z12 Y13]
+ (-0.012215040997613936) [X4 Z5 X6 X11 Z12 X13]
+ (-0.012215040997613936) [Y5 Z6 Y7 Y10 Z11 Y12]
+ (-0.012215040997613936) [Y5 Z6 Y7 X10 Z11 X12]
+ (-0.012215040997613936) [X5 Z6 X7 Y10 Z11 Y12]
+ (-0.012215040997613936) [X5 Z6 X7 X10 Z11 X12]
+ (-0.011756013419819269) [Y3 Z4 Z5 X6 X8 Y9]
+ (-0.011756013419819269) [Y3 Z4 Z5 Y6 Y8 Y9]
+ (-0.011756013419819269) [X3 Z4 Z5 X6 X8 X9]
+ (-0.011756013419819269) [X3 Z4 Z5 Y6 Y8 X9]
+ (-0.008764827575688776) [Y2 Z3 Z4 X5 X11 Y12]
+ (-0.008764827575688776) [Y2 Z3 Z4 Y5 Y11 Y12]
+ (-0.008764827575688776) [X2 Z3 Z4 X5 X11 X12]
+ (-0.008764827575688776) [X2 Z3 Z4 Y5 Y11 X12]
+ (-0.008764827575688776) [Y3 X4 X10 Z11 Z12 Y13]
+ (-0.008764827575688776) [Y3 Y4 Y10 Z11 Z12 Y13]
+ (-0.008764827575688776) [X3 X4 X10 Z11 Z12 X13]
+ (-0.008764827575688776) [X3 Y4 Y10 Z11 Z12 X13]
+ (-0.008125251921381011) [Y0 Z1 Z2 Y3 X8 X9]
+ (-0.008125251921381011) [X0 Z1 Z2 X3 Y8 Y9]
+ (-0.00730675992883296) [Y4 X5 X7 Z8 Z9 Y10]
+ (-0.00730675992883296) [Y4 Y5 Y7 Z8 Z9 Y10]
+ (-0.00730675992883296) [X4 X5 X7 Z8 Z9 X10]
+ (-0.00730675992883296) [X4 Y5 Y7 Z8 Z9 X10]
+ (-0.005805188989826953) [Y2 Z3 Z4 Z5 Y6 Z8]
+ (-0.005805188989826953) [X2 Z3 Z4 Z5 X6 Z8]
+ (-0.005805188989826953) [Y3 Z4 Z5 Z6 Y7 Z9]
+ (-0.005805188989826953) [X3 Z4 Z5 Z6 X7 Z9]
+ (-0.005652620978017355) [Y0 X1 X3 Z4 Z5 Y6]
+ (-0.005652620978017355) [Y0 Y1 Y3 Z4 Z5 Y6]
+ (-0.005652620978017355) [X0 X1 X3 Z4 Z5 X6]
+ (-0.005652620978017355) [X0 Y1 Y3 Z4 Z5 X6]
+ (-0.005143391768825136) [Y2 Z3 Y4 Y5 Z6 Y7]
+ (-0.005143391768825136) [Y2 Z3 Y4 X5 Z6 X7]
+ (-0.005143391768825136) [X2 Z3 X4 Y5 Z6 Y7]
+ (-0.005143391768825136) [X2 Z3 X4 X5 Z6 X7]
+ (-0.004684903388155178) [Y0 Z1 Z2 Y3 X6 X7]
+ (-0.004684903388155178) [X0 Z1 Z2 X3 Y6 Y7]
+ (-0.0046686203187762945) [Y1 X2 X7 Z8 Z9 Y10]
+ (-0.0046686203187762945) [X1 Y2 Y7 Z8 Z9 X10]
+ (-0.004575007626639189) [Y0 Z1 Z2 Y3 X12 X13]
+ (-0.004575007626639189) [X0 Z1 Z2 X3 Y12 Y13]
+ (-0.004424855449441846) [Y0 Z1 Z2 Y3 X4 X5]
+ (-0.004424855449441846) [X0 Z1 Z2 X3 Y4 Y5]
+ (-0.004158797381840007) [Y3 Z4 Z5 X6 X12 Y13]
+ (-0.004158797381840007) [Y3 Z4 Z5 Y6 Y12 Y13]
+ (-0.004158797381840007) [X3 Z4 Z5 X6 X12 X13]
+ (-0.004158797381840007) [X3 Z4 Z5 Y6 Y12 X13]
+ (-0.0034937903598901607) [Y2 Z3 Z4 Z5 Y6 Z13]
+ (-0.0034937903598901607) [X2 Z3 Z4 Z5 X6 Z13]
+ (-0.0034937903598901607) [Y3 Z4 Z5 Z6 Y7 Z12]
+ (-0.0034937903598901607) [X3 Z4 Z5 Z6 X7 Z12]
+ (-0.0027790267990255497) [Y1 Z2 Z3 Z4 Z5 Y7]
+ (-0.0027790267990255497) [X1 Z2 Z3 Z4 Z5 X7]
+ (-0.00229395661135245) [Y1 X2 X3 Z4 Z5 Y6]
+ (-0.00229395661135245) [X1 Y2 Y3 Z4 Z5 X6]
+ (-0.0017992194936630364) [Y0 Z1 Z2 Y3 X10 X11]
+ (-0.0017992194936630364) [X0 Z1 Z2 X3 Y10 Y11]
+ (-0.0017278753941369557) [Y1 Z2 Z3 X4 X11 Y12]
+ (-0.0017278753941369557) [X1 Z2 Z3 Y4 Y11 X12]
+ (-0.0009298507967730487) [Y4 Z5 Y6 X10 Z11 X12]
+ (-0.0009298507967730487) [X4 Z5 X6 Y10 Z11 Y12]
+ (-0.0009298507967730487) [Y5 Z6 Y7 X11 Z12 X13]
+ (-0.0009298507967730487) [X5 Z6 X7 Y11 Z12 Y13]
+ (-0.00085338562541255) [Y1 Z2 Z3 Y4 X5 X6]
+ (-0.00085338562541255) [X1 Z2 Z3 X4 Y5 Y6]
+ (-0.0008145313270957522) [Y2 Z3 Z4 Z5 Y6 Z10]
+ (-0.0008145313270957522) [X2 Z3 Z4 Z5 X6 Z10]
+ (-0.0008145313270957522) [Y3 Z4 Z5 Z6 Y7 Z11]
+ (-0.0008145313270957522) [X3 Z4 Z5 Z6 X7 Z11]
+ (-7.735036880591836e-05) [Y0 X1 X7 Z8 Z9 Y10]
+ (-7.735036880591836e-05) [Y0 Y1 Y7 Z8 Z9 Y10]
+ (-7.735036880591836e-05) [X0 X1 X7 Z8 Z9 X10]
+ (-7.735036880591836e-05) [X0 Y1 Y7 Z8 Z9 X10]
+ (-8.77481786475405e-06) [Y4 Z5 Z6 Z7 Z8 Y10]
+ (-8.77481786475405e-06) [X4 Z5 Z6 Z7 Z8 X10]
+ (-8.77481786475405e-06) [Y5 Z6 Z7 Z9 Z10 Y11]
+ (-8.77481786475405e-06) [X5 Z6 Z7 Z9 Z10 X11]
+ (-7.518362215838818e-06) [Y4 Z5 Z7 Z8 Z9 Y10]
+ (-7.518362215838818e-06) [X4 Z5 Z7 Z8 Z9 X10]
+ (-7.518362215838818e-06) [Y5 Z6 Z8 Z9 Z10 Y11]
+ (-7.518362215838818e-06) [X5 Z6 Z8 Z9 Z10 X11]
+ (-7.44434467604891e-06) [Y4 Z5 Z6 Z7 Z9 Y10]
+ (-7.44434467604891e-06) [X4 Z5 Z6 Z7 Z9 X10]
+ (-7.44434467604891e-06) [Y5 Z6 Z7 Z8 Z10 Y11]
+ (-7.44434467604891e-06) [X5 Z6 Z7 Z8 Z10 X11]
+ (-6.524373848623125e-06) [Y6 Z7 Z8 Z9 Z10 Y12]
+ (-6.524373848623125e-06) [X6 Z7 Z8 Z9 Z10 X12]
+ (-6.524373848623125e-06) [Y7 Z8 Z9 Z11 Z12 Y13]
+ (-6.524373848623125e-06) [X7 Z8 Z9 Z11 Z12 X13]
+ (-6.290028433335309e-06) [Y4 Z5 Z6 Z8 Z9 Y10]
+ (-6.290028433335309e-06) [X4 Z5 Z6 Z8 Z9 X10]
+ (-6.290028433335309e-06) [Y5 Z7 Z8 Z9 Z10 Y11]
+ (-6.290028433335309e-06) [X5 Z7 Z8 Z9 Z10 X11]
+ (-5.974311713515263e-06) [Y4 Z5 Z6 X7 X10 Y11]
+ (-5.974311713515263e-06) [X4 Z5 Z6 Y7 Y10 X11]
+ (-5.27588312224402e-06) [Y2 Z3 Z4 X5 X12 Y13]
+ (-5.27588312224402e-06) [X2 Z3 Z4 Y5 Y12 X13]
+ (-4.643051068536201e-06) [Y2 Z3 Z4 Y5 X10 X11]
+ (-4.643051068536201e-06) [X2 Z3 Z4 X5 Y10 Y11]
+ (-4.556569218164285e-06) [Y4 Z5 Z6 Y7 X12 X13]
+ (-4.556569218164285e-06) [X4 Z5 Z6 X7 Y12 Y13]
+ (-4.253224225607854e-06) [Y4 Z6 Z7 Z8 Z9 Y10]
+ (-4.253224225607854e-06) [X4 Z6 Z7 Z8 Z9 X10]
+ (-3.769659452014876e-06) [Y6 Z8 Z9 Z10 Z11 Y12]
+ (-3.769659452014876e-06) [X6 Z8 Z9 Z10 Z11 X12]
+ (-3.6945132946186404e-06) [Y4 Y5 X10 Z11 Z12 X13]
+ (-3.6945132946186404e-06) [X4 X5 Y10 Z11 Z12 Y13]
+ (-3.610297130605181e-06) [Y6 Z7 Z9 Z10 Z11 Y12]
+ (-3.610297130605181e-06) [X6 Z7 Z9 Z10 Z11 X12]
+ (-3.610297130605181e-06) [Y7 Z8 Z10 Z11 Z12 Y13]
+ (-3.610297130605181e-06) [X7 Z8 Z10 Z11 Z12 X13]
+ (-3.3131455001772933e-06) [Y7 Z8 Z9 Y10 X11 X12]
+ (-3.3131455001772933e-06) [X7 Z8 Z9 X10 Y11 Y12]
+ (-3.2774831955372456e-06) [Y6 Z7 Z8 Z10 Z11 Y12]
+ (-3.2774831955372456e-06) [X6 Z7 Z8 Z10 Z11 X12]
+ (-3.2774831955372456e-06) [Y7 Z9 Z10 Z11 Z12 Y13]
+ (-3.2774831955372456e-06) [X7 Z9 Z10 Z11 Z12 X13]
+ (-3.2112283484458313e-06) [Y6 Z7 Z8 Z9 Z11 Y12]
+ (-3.2112283484458313e-06) [X6 Z7 Z8 Z9 Z11 X12]
+ (-3.2112283484458313e-06) [Y7 Z8 Z9 Z10 Z12 Y13]
+ (-3.2112283484458313e-06) [X7 Z8 Z9 Z10 Z12 X13]
+ (-3.151346311181914e-06) [Y3 Y4 X7 Z8 Z9 X10]
+ (-3.151346311181914e-06) [X3 X4 Y7 Z8 Z9 Y10]
+ (-3.088250711376335e-06) [Y3 Z4 Z5 Y6 X11 X12]
+ (-3.088250711376335e-06) [X3 Z4 Z5 X6 Y11 Y12]
+ (-2.1726691015540332e-06) [Y2 X3 X10 Z11 Z12 Y13]
+ (-2.1726691015540332e-06) [X2 Y3 Y10 Z11 Z12 X13]
+ (-1.4548424490928803e-06) [Y2 Z3 Z4 Y5 X6 X7]
+ (-1.4548424490928803e-06) [X2 Z3 Z4 X5 Y6 Y7]
+ (-1.3304731887051392e-06) [Y5 Z6 Z7 Y8 X9 X10]
+ (-1.3304731887051392e-06) [X5 Z6 Z7 X8 Y9 Y10]
+ (-1.2283337825035089e-06) [Y5 X6 X7 Z8 Z9 Y10]
+ (-1.2283337825035089e-06) [X5 Y6 Y7 Z8 Z9 X10]
+ (-1.0358477601641843e-06) [Y6 Y7 X10 Z11 Z12 X13]
+ (-1.0358477601641843e-06) [X6 X7 Y10 Z11 Z12 Y13]
+ (-7.956895372896644e-07) [Y2 Z3 Z4 Y5 X8 X9]
+ (-7.956895372896644e-07) [X2 Z3 Z4 X5 Y8 Y9]
+ (-6.73319774252823e-07) [Y0 Z1 Z2 Z3 Y4 Z10]
+ (-6.73319774252823e-07) [X0 Z1 Z2 Z3 X4 Z10]
+ (-6.73319774252823e-07) [Y1 Z2 Z3 Z4 Y5 Z11]
+ (-6.73319774252823e-07) [X1 Z2 Z3 Z4 X5 Z11]
+ (-6.628614201723609e-07) [Y8 X9 X10 Z11 Z12 Y13]
+ (-6.628614201723609e-07) [X8 Y9 Y10 Z11 Z12 X13]
+ (-6.55628191469531e-07) [Y0 Z1 Y2 X10 Z11 X12]
+ (-6.55628191469531e-07) [X0 Z1 X2 Y10 Z11 Y12]
+ (-6.55628191469531e-07) [Y1 Z2 Y3 X11 Z12 X13]
+ (-6.55628191469531e-07) [X1 Z2 X3 Y11 Z12 Y13]
+ (-6.41829157469734e-07) [Y0 Z1 Y2 Y10 Z11 Y12]
+ (-6.41829157469734e-07) [X0 Z1 X2 X10 Z11 X12]
+ (-6.41829157469734e-07) [Y1 Z2 Y3 Y11 Z12 Y13]
+ (-6.41829157469734e-07) [X1 Z2 X3 X11 Z12 X13]
+ (-5.927453082977421e-07) [Y0 Z1 Z2 Z3 Y4 Z11]
+ (-5.927453082977421e-07) [X0 Z1 Z2 Z3 X4 Z11]
+ (-5.927453082977421e-07) [Y1 Z2 Z3 Z4 Y5 Z10]
+ (-5.927453082977421e-07) [X1 Z2 Z3 Z4 X5 Z10]
+ (-5.627851911410602e-07) [Y0 X1 X10 Z11 Z12 Y13]
+ (-5.627851911410602e-07) [X0 Y1 Y10 Z11 Z12 X13]
+ (-5.287660624780792e-07) [Y0 Z1 Z2 X3 X11 Y12]
+ (-5.287660624780792e-07) [Y0 Z1 Z2 Y3 Y11 Y12]
+ (-5.287660624780792e-07) [X0 Z1 Z2 X3 X11 X12]
+ (-5.287660624780792e-07) [X0 Z1 Z2 Y3 Y11 X12]
+ (-5.287660624780792e-07) [Y1 X2 X10 Z11 Z12 Y13]
+ (-5.287660624780792e-07) [Y1 Y2 Y10 Z11 Z12 Y13]
+ (-5.287660624780792e-07) [X1 X2 X10 Z11 Z12 X13]
+ (-5.287660624780792e-07) [X1 Y2 Y10 Z11 Z12 X13]
+ (-4.838052751086737e-07) [Y4 Z5 Z6 Y7 X8 X9]
+ (-4.838052751086737e-07) [X4 Z5 Z6 X7 Y8 Y9]
+ (-3.5707613291786027e-07) [Y0 Y1 X2 Z3 Z4 X5]
+ (-3.5707613291786027e-07) [X0 X1 Y2 Z3 Z4 Y5]
+ (-3.3281393506793533e-07) [Y7 X8 X9 Z10 Z11 Y12]
+ (-3.3281393506793533e-07) [X7 Y8 Y9 Z10 Z11 X12]
+ (-3.086826565134335e-07) [Y1 Z2 Z3 X4 X12 Y13]
+ (-3.086826565134335e-07) [Y1 Z2 Z3 Y4 Y12 Y13]
+ (-3.086826565134335e-07) [X1 Z2 Z3 X4 X12 X13]
+ (-3.086826565134335e-07) [X1 Z2 Z3 Y4 Y12 X13]
+ (-2.4473231288722685e-07) [Y0 Y1 X4 Z5 Z6 X7]
+ (-2.4473231288722685e-07) [X0 X1 Y4 Z5 Z6 Y7]
+ (-2.3713289480052117e-07) [Y1 Z2 Z3 X4 X8 Y9]
+ (-2.3713289480052117e-07) [Y1 Z2 Z3 Y4 Y8 Y9]
+ (-2.3713289480052117e-07) [X1 Z2 Z3 X4 X8 X9]
+ (-2.3713289480052117e-07) [X1 Z2 Z3 Y4 Y8 X9]
+ (-2.1990516188051842e-07) [Y2 Y3 X4 Z5 Z6 X7]
+ (-2.1990516188051842e-07) [X2 X3 Y4 Z5 Z6 Y7]
+ (-1.9332412771531168e-07) [Y0 Z1 Y2 Y3 Z4 Y5]
+ (-1.9332412771531168e-07) [Y0 Z1 Y2 X3 Z4 X5]
+ (-1.9332412771531168e-07) [X0 Z1 X2 Y3 Z4 Y5]
+ (-1.9332412771531168e-07) [X0 Z1 X2 X3 Z4 X5]
+ (-1.8394209155352706e-07) [Y1 Z2 Z3 X4 X6 Y7]
+ (-1.8394209155352706e-07) [Y1 Z2 Z3 Y4 Y6 Y7]
+ (-1.8394209155352706e-07) [X1 Z2 Z3 X4 X6 X7]
+ (-1.8394209155352706e-07) [X1 Z2 Z3 Y4 Y6 X7]
+ (-1.5510539176942295e-07) [Y0 Z1 Y2 Y4 Z5 Y6]
+ (-1.5510539176942295e-07) [X0 Z1 X2 X4 Z5 X6]
+ (-1.5510539176942295e-07) [Y1 Z2 Y3 Y5 Z6 Y7]
+ (-1.5510539176942295e-07) [X1 Z2 X3 X5 Z6 X7]
+ (-1.3807781481130466e-07) [Y0 Z1 Y2 X4 Z5 X6]
+ (-1.3807781481130466e-07) [X0 Z1 X2 Y4 Z5 Y6]
+ (-1.3807781481130466e-07) [Y0 Z1 Y2 Y5 Z6 Y7]
+ (-1.3807781481130466e-07) [Y0 Z1 Y2 X5 Z6 X7]
+ (-1.3807781481130466e-07) [X0 Z1 X2 Y5 Z6 Y7]
+ (-1.3807781481130466e-07) [X0 Z1 X2 X5 Z6 X7]
+ (-1.3807781481130466e-07) [Y1 Z2 Y3 Y4 Z5 Y6]
+ (-1.3807781481130466e-07) [Y1 Z2 Y3 X4 Z5 X6]
+ (-1.3807781481130466e-07) [X1 Z2 X3 Y4 Z5 Y6]
+ (-1.3807781481130466e-07) [X1 Z2 X3 X4 Z5 X6]
+ (-1.3807781481130466e-07) [Y1 Z2 Y3 X5 Z6 X7]
+ (-1.3807781481130466e-07) [X1 Z2 X3 Y5 Z6 Y7]
+ (-1.2919694865188438e-07) [Y0 Z1 Z2 Z3 Y4 Z5]
+ (-1.2919694865188438e-07) [X0 Z1 Z2 Z3 X4 Z5]
+ (-1.1076325599144622e-07) [Y0 Z1 Y2 Y11 Z12 Y13]
+ (-1.1076325599144622e-07) [Y0 Z1 Y2 X11 Z12 X13]
+ (-1.1076325599144622e-07) [X0 Z1 X2 Y11 Z12 Y13]
+ (-1.1076325599144622e-07) [X0 Z1 X2 X11 Z12 X13]
+ (-1.1076325599144622e-07) [Y1 Z2 Y3 Y10 Z11 Y12]
+ (-1.1076325599144622e-07) [Y1 Z2 Y3 X10 Z11 X12]
+ (-1.1076325599144622e-07) [X1 Z2 X3 Y10 Z11 Y12]
+ (-1.1076325599144622e-07) [X1 Z2 X3 X10 Z11 X12]
+ (8.057446595508074e-08) [Y1 Z2 Z3 X4 X10 Y11]
+ (8.057446595508074e-08) [Y1 Z2 Z3 Y4 Y10 Y11]
+ (8.057446595508074e-08) [X1 Z2 Z3 X4 X10 X11]
+ (8.057446595508074e-08) [X1 Z2 Z3 Y4 Y10 X11]
+ (8.649310133022204e-08) [Y0 Z1 Z2 Z3 Y4 Z9]
+ (8.649310133022204e-08) [X0 Z1 Z2 Z3 X4 Z9]
+ (8.649310133022204e-08) [Y1 Z2 Z3 Z4 Y5 Z8]
+ (8.649310133022204e-08) [X1 Z2 Z3 Z4 X5 Z8]
+ (1.839420915535271e-07) [Y0 Z1 Z2 Z3 Y4 Z6]
+ (1.839420915535271e-07) [X0 Z1 Z2 Z3 X4 Z6]
+ (1.839420915535271e-07) [Y1 Z2 Z3 Z4 Y5 Z7]
+ (1.839420915535271e-07) [X1 Z2 Z3 Z4 X5 Z7]
+ (2.1990516188051842e-07) [Y2 X3 X4 Z5 Z6 Y7]
+ (2.1990516188051842e-07) [X2 Y3 Y4 Z5 Z6 X7]
+ (2.4473231288722685e-07) [Y0 X1 X4 Z5 Z6 Y7]
+ (2.4473231288722685e-07) [X0 Y1 Y4 Z5 Z6 X7]
+ (3.236259961307432e-07) [Y0 Z1 Z2 Z3 Y4 Z8]
+ (3.236259961307432e-07) [X0 Z1 Z2 Z3 X4 Z8]
+ (3.236259961307432e-07) [Y1 Z2 Z3 Z4 Y5 Z9]
+ (3.236259961307432e-07) [X1 Z2 Z3 Z4 X5 Z9]
+ (3.3281393506793533e-07) [Y7 Y8 X9 Z10 Z11 X12]
+ (3.3281393506793533e-07) [X7 X8 Y9 Z10 Z11 Y12]
+ (3.5707613291786027e-07) [Y0 X1 X2 Z3 Z4 Y5]
+ (3.5707613291786027e-07) [X0 Y1 Y2 Z3 Z4 X5]
+ (4.838052751086737e-07) [Y4 Z5 Z6 X7 X8 Y9]
+ (4.838052751086737e-07) [X4 Z5 Z6 Y7 Y8 X9]
+ (5.627851911410602e-07) [Y0 Y1 X10 Z11 Z12 X13]
+ (5.627851911410602e-07) [X0 X1 Y10 Z11 Z12 Y13]
+ (6.628614201723609e-07) [Y8 Y9 X10 Z11 Z12 X13]
+ (6.628614201723609e-07) [X8 X9 Y10 Z11 Z12 Y13]
+ (7.956895372896644e-07) [Y2 Z3 Z4 X5 X8 Y9]
+ (7.956895372896644e-07) [X2 Z3 Z4 Y5 Y8 X9]
+ (9.306536651887498e-07) [Y0 Z1 Z2 Z3 Y4 Z13]
+ (9.306536651887498e-07) [X0 Z1 Z2 Z3 X4 Z13]
+ (9.306536651887498e-07) [Y1 Z2 Z3 Z4 Y5 Z12]
+ (9.306536651887498e-07) [X1 Z2 Z3 Z4 X5 Z12]
+ (1.0358477601641843e-06) [Y6 X7 X10 Z11 Z12 Y13]
+ (1.0358477601641843e-06) [X6 Y7 Y10 Z11 Z12 X13]
+ (1.2283337825035089e-06) [Y5 Y6 X7 Z8 Z9 X10]
+ (1.2283337825035089e-06) [X5 X6 Y7 Z8 Z9 Y10]
+ (1.2393363217021834e-06) [Y0 Z1 Z2 Z3 Y4 Z12]
+ (1.2393363217021834e-06) [X0 Z1 Z2 Z3 X4 Z12]
+ (1.2393363217021834e-06) [Y1 Z2 Z3 Z4 Y5 Z13]
+ (1.2393363217021834e-06) [X1 Z2 Z3 Z4 X5 Z13]
+ (1.3304731887051392e-06) [Y5 Z6 Z7 X8 X9 Y10]
+ (1.3304731887051392e-06) [X5 Z6 Z7 Y8 Y9 X10]
+ (1.4548424490928803e-06) [Y2 Z3 Z4 X5 X6 Y7]
+ (1.4548424490928803e-06) [X2 Z3 Z4 Y5 Y6 X7]
+ (2.1726691015540332e-06) [Y2 Y3 X10 Z11 Z12 X13]
+ (2.1726691015540332e-06) [X2 X3 Y10 Z11 Z12 Y13]
+ (3.088250711376335e-06) [Y3 Z4 Z5 X6 X11 Y12]
+ (3.088250711376335e-06) [X3 Z4 Z5 Y6 Y11 X12]
+ (3.117447946114733e-06) [Z0 Y1 Z2 Z3 Z4 Y5]
+ (3.117447946114733e-06) [Z0 X1 Z2 Z3 Z4 X5]
+ (3.151346311181914e-06) [Y3 X4 X7 Z8 Z9 Y10]
+ (3.151346311181914e-06) [X3 Y4 Y7 Z8 Z9 X10]
+ (3.3131455001772933e-06) [Y7 Z8 Z9 X10 X11 Y12]
+ (3.3131455001772933e-06) [X7 Z8 Z9 Y10 Y11 X12]
+ (3.3343312893992163e-06) [Y5 Z6 Z7 Z8 Z9 Y11]
+ (3.3343312893992163e-06) [X5 Z6 Z7 Z8 Z9 X11]
+ (3.6945132946186404e-06) [Y4 X5 X10 Z11 Z12 Y13]
+ (3.6945132946186404e-06) [X4 Y5 Y10 Z11 Z12 X13]
+ (4.18393255944849e-06) [Y7 Z8 Z9 Z10 Z11 Y13]
+ (4.18393255944849e-06) [X7 Z8 Z9 Z10 Z11 X13]
+ (4.556569218164285e-06) [Y4 Z5 Z6 X7 X12 Y13]
+ (4.556569218164285e-06) [X4 Z5 Z6 Y7 Y12 X13]
+ (4.643051068536201e-06) [Y2 Z3 Z4 X5 X10 Y11]
+ (4.643051068536201e-06) [X2 Z3 Z4 Y5 Y10 X11]
+ (5.27588312224402e-06) [Y2 Z3 Z4 Y5 X12 X13]
+ (5.27588312224402e-06) [X2 Z3 Z4 X5 Y12 Y13]
+ (5.974311713515263e-06) [Y4 Z5 Z6 Y7 X10 X11]
+ (5.974311713515263e-06) [X4 Z5 Z6 X7 Y10 Y11]
+ (0.0002921986261110724) [Y6 Z7 Y8 Y9 Z10 Y11]
+ (0.0002921986261110724) [Y6 Z7 Y8 X9 Z10 X11]
+ (0.0002921986261110724) [X6 Z7 X8 Y9 Z10 Y11]
+ (0.0002921986261110724) [X6 Z7 X8 X9 Z10 X11]
+ (0.0004956762314915796) [Z2 Y3 Z4 Z5 Z6 Y7]
+ (0.0004956762314915796) [Z2 X3 Z4 Z5 Z6 X7]
+ (0.0006650070219498466) [Y2 Z3 Z4 Z5 Y6 Z12]
+ (0.0006650070219498466) [X2 Z3 Z4 Z5 X6 Z12]
+ (0.0006650070219498466) [Y3 Z4 Z5 Z6 Y7 Z13]
+ (0.0006650070219498466) [X3 Z4 Z5 Z6 X7 Z13]
+ (0.00085338562541255) [Y1 Z2 Z3 X4 X5 Y6]
+ (0.00085338562541255) [X1 Z2 Z3 Y4 Y5 X6]
+ (0.0016095313817213691) [Y0 Z1 Z2 Z3 Z4 Y6]
+ (0.0016095313817213691) [X0 Z1 Z2 Z3 Z4 X6]
+ (0.0016095313817213691) [Y1 Z2 Z3 Z5 Z6 Y7]
+ (0.0016095313817213691) [X1 Z2 Z3 Z5 Z6 X7]
+ (0.001667604181144043) [Y0 Z1 Z3 Z4 Z5 Y6]
+ (0.001667604181144043) [X0 Z1 Z3 Z4 Z5 X6]
+ (0.001667604181144043) [Y1 Z2 Z4 Z5 Z6 Y7]
+ (0.001667604181144043) [X1 Z2 Z4 Z5 Z6 X7]
+ (0.0017278753941369557) [Y1 Z2 Z3 Y4 X11 X12]
+ (0.0017278753941369557) [X1 Z2 Z3 X4 Y11 Y12]
+ (0.0017992194936630364) [Y0 Z1 Z2 X3 X10 Y11]
+ (0.0017992194936630364) [X0 Z1 Z2 Y3 Y10 X11]
+ (0.00229395661135245) [Y1 Y2 X3 Z4 Z5 X6]
+ (0.00229395661135245) [X1 X2 Y3 Z4 Z5 Y6]
+ (0.002462917007133919) [Y0 Z1 Z2 Z3 Z5 Y6]
+ (0.002462917007133919) [X0 Z1 Z2 Z3 Z5 X6]
+ (0.002462917007133919) [Y1 Z2 Z3 Z4 Z6 Y7]
+ (0.002462917007133919) [X1 Z2 Z3 Z4 Z6 X7]
+ (0.003961560792496493) [Y0 Z1 Z2 Z4 Z5 Y6]
+ (0.003961560792496493) [X0 Z1 Z2 Z4 Z5 X6]
+ (0.003961560792496493) [Y1 Z3 Z4 Z5 Z6 Y7]
+ (0.003961560792496493) [X1 Z3 Z4 Z5 Z6 X7]
+ (0.004424855449441846) [Y0 Z1 Z2 X3 X4 Y5]
+ (0.004424855449441846) [X0 Z1 Z2 Y3 Y4 X5]
+ (0.004575007626639189) [Y0 Z1 Z2 X3 X12 Y13]
+ (0.004575007626639189) [X0 Z1 Z2 Y3 Y12 X13]
+ (0.0046686203187762945) [Y1 Y2 X7 Z8 Z9 X10]
+ (0.0046686203187762945) [X1 X2 Y7 Z8 Z9 Y10]
+ (0.004684903388155178) [Y0 Z1 Z2 X3 X6 Y7]
+ (0.004684903388155178) [X0 Z1 Z2 Y3 Y6 X7]
+ (0.00532483523422167) [Y2 Z3 Y4 X10 Z11 X12]
+ (0.00532483523422167) [X2 Z3 X4 Y10 Z11 Y12]
+ (0.00532483523422167) [Y3 Z4 Y5 X11 Z12 X13]
+ (0.00532483523422167) [X3 Z4 X5 Y11 Z12 Y13]
+ (0.005368659358109488) [Y2 X3 X7 Z8 Z9 Y10]
+ (0.005368659358109488) [Y2 Y3 Y7 Z8 Z9 Y10]
+ (0.005368659358109488) [X2 X3 X7 Z8 Z9 X10]
+ (0.005368659358109488) [X2 Y3 Y7 Z8 Z9 X10]
+ (0.007960880725921578) [Y4 Z5 Y6 Y10 Z11 Y12]
+ (0.007960880725921578) [X4 Z5 X6 X10 Z11 X12]
+ (0.007960880725921578) [Y5 Z6 Y7 Y11 Z12 Y13]
+ (0.007960880725921578) [X5 Z6 X7 X11 Z12 X13]
+ (0.008125251921381011) [Y0 Z1 Z2 X3 X8 Y9]
+ (0.008125251921381011) [X0 Z1 Z2 Y3 Y8 X9]
+ (0.008890731522694626) [Y4 Z5 X6 X10 Z11 Y12]
+ (0.008890731522694626) [X4 Z5 Y6 Y10 Z11 X12]
+ (0.008890731522694626) [Y5 Z6 X7 X11 Z12 Y13]
+ (0.008890731522694626) [X5 Z6 Y7 Y11 Z12 X13]
+ (0.010263414868158467) [Y2 Z3 X4 X10 Z11 Y12]
+ (0.010263414868158467) [X2 Z3 Y4 Y10 Z11 X12]
+ (0.010263414868158467) [Y3 Z4 X5 X11 Z12 Y13]
+ (0.010263414868158467) [X3 Z4 Y5 Y11 Z12 X13]
+ (0.010540425907671548) [Y6 Z7 Z8 Z9 Y10 Z13]
+ (0.010540425907671548) [X6 Z7 Z8 Z9 X10 Z13]
+ (0.010540425907671548) [Y7 Z8 Z9 Z10 Y11 Z12]
+ (0.010540425907671548) [X7 Z8 Z9 Z10 X11 Z12]
+ (0.010960074940542578) [Z4 Y7 Z8 Z9 Z10 Y11]
+ (0.010960074940542578) [Z4 X7 Z8 Z9 Z10 X11]
+ (0.010960074940542578) [Z5 Y6 Z7 Z8 Z9 Y10]
+ (0.010960074940542578) [Z5 X6 Z7 Z8 Z9 X10]
+ (0.0113072740088483) [Y6 Z7 Z8 Z9 Y10 Z11]
+ (0.0113072740088483) [X6 Z7 Z8 Z9 X10 Z11]
+ (0.014411099430130811) [Y2 Z3 Z4 Z5 Y6 Z11]
+ (0.014411099430130811) [X2 Z3 Z4 Z5 X6 Z11]
+ (0.014411099430130811) [Y3 Z4 Z5 Z6 Y7 Z10]
+ (0.014411099430130811) [X3 Z4 Z5 Z6 X7 Z10]
+ (0.015225630757226563) [Y3 Z4 Z5 X6 X10 Y11]
+ (0.015225630757226563) [Y3 Z4 Z5 Y6 Y10 Y11]
+ (0.015225630757226563) [X3 Z4 Z5 X6 X10 X11]
+ (0.015225630757226563) [X3 Z4 Z5 Y6 Y10 X11]
+ (0.015588250102380137) [Y2 Z3 Y4 Y10 Z11 Y12]
+ (0.015588250102380137) [X2 Z3 X4 X10 Z11 X12]
+ (0.015588250102380137) [Y3 Z4 Y5 Y11 Z12 Y13]
+ (0.015588250102380137) [X3 Z4 X5 X11 Z12 X13]
+ (0.018266834869375536) [Z4 Y6 Z7 Z8 Z9 Y10]
+ (0.018266834869375536) [Z4 X6 Z7 Z8 Z9 X10]
+ (0.018266834869375536) [Z5 Y7 Z8 Z9 Z10 Y11]
+ (0.018266834869375536) [Z5 X7 Z8 Z9 Z10 X11]
+ (0.019020423173039917) [Z2 Y6 Z7 Z8 Z9 Y10]
+ (0.019020423173039917) [Z2 X6 Z7 Z8 Z9 X10]
+ (0.019020423173039917) [Z3 Y7 Z8 Z9 Z10 Y11]
+ (0.019020423173039917) [Z3 X7 Z8 Z9 Z10 X11]
+ (0.020175921723535512) [Y4 Z5 Z6 X7 X11 Y12]
+ (0.020175921723535512) [Y4 Z5 Z6 Y7 Y11 Y12]
+ (0.020175921723535512) [X4 Z5 Z6 X7 X11 X12]
+ (0.020175921723535512) [X4 Z5 Z6 Y7 Y11 X12]
+ (0.020175921723535512) [Y5 X6 X10 Z11 Z12 Y13]
+ (0.020175921723535512) [Y5 Y6 Y10 Z11 Z12 Y13]
+ (0.020175921723535512) [X5 X6 X10 Z11 Z12 X13]
+ (0.020175921723535512) [X5 Y6 Y10 Z11 Z12 X13]
+ (0.024353077678068914) [Y2 Z3 Y4 Y11 Z12 Y13]
+ (0.024353077678068914) [Y2 Z3 Y4 X11 Z12 X13]
+ (0.024353077678068914) [X2 Z3 X4 Y11 Z12 Y13]
+ (0.024353077678068914) [X2 Z3 X4 X11 Z12 X13]
+ (0.024353077678068914) [Y3 Z4 Y5 Y10 Z11 Y12]
+ (0.024353077678068914) [Y3 Z4 Y5 X10 Z11 X12]
+ (0.024353077678068914) [X3 Z4 X5 Y10 Z11 Y12]
+ (0.024353077678068914) [X3 Z4 X5 X10 Z11 X12]
+ (0.02438908253114941) [Z2 Y7 Z8 Z9 Z10 Y11]
+ (0.02438908253114941) [Z2 X7 Z8 Z9 Z10 X11]
+ (0.02438908253114941) [Z3 Y6 Z7 Z8 Z9 Y10]
+ (0.02438908253114941) [Z3 X6 Z7 Z8 Z9 X10]
+ (0.025104957138844544) [Y6 Z7 Z8 Z9 Y10 Z12]
+ (0.025104957138844544) [X6 Z7 Z8 Z9 X10 Z12]
+ (0.025104957138844544) [Y7 Z8 Z9 Z10 Y11 Z13]
+ (0.025104957138844544) [X7 Z8 Z9 Z10 X11 Z13]
+ (0.030787505389143904) [Z6 Y7 Z8 Z9 Z10 Y11]
+ (0.030787505389143904) [Z6 X7 Z8 Z9 Z10 X11]
+ (0.04587947078129813) [Y0 Z2 Z3 Z4 Z5 Y6]
+ (0.04587947078129813) [X0 Z2 Z3 Z4 Z5 X6]
+ (0.056007330877807626) [Z0 Y7 Z8 Z9 Z10 Y11]
+ (0.056007330877807626) [Z0 X7 Z8 Z9 Z10 X11]
+ (0.056007330877807626) [Z1 Y6 Z7 Z8 Z9 Y10]
+ (0.056007330877807626) [Z1 X6 Z7 Z8 Z9 X10]
+ (0.05608468124661353) [Z0 Y6 Z7 Z8 Z9 Y10]
+ (0.05608468124661353) [Z0 X6 Z7 Z8 Z9 X10]
+ (0.05608468124661353) [Z1 Y7 Z8 Z9 Z10 Y11]
+ (0.05608468124661353) [Z1 X7 Z8 Z9 Z10 X11]
+ (-6.631277928564243e-05) [Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-6.631277928564243e-05) [X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-6.631277928564239e-05) [Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-6.631277928564239e-05) [X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-2.595086006973784e-05) [Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.595086006973784e-05) [X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.595086006973784e-05) [Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.595086006973784e-05) [X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.042743277013782936) [Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.042743277013782936) [X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (0.04274327701378295) [Y0 Z1 Z2 Z3 Z4 Z5 Y6]
+ (0.04274327701378295) [X0 Z1 Z2 Z3 Z4 Z5 X6]
+ (-0.04764261217638305) [Y4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-0.04764261217638305) [X4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-0.04764261217638305) [Y5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-0.04764261217638305) [X5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-0.041718813839821706) [Y4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-0.041718813839821706) [X4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-0.041718813839821706) [Y5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-0.041718813839821706) [X5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-0.03956441632289323) [Y4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-0.03956441632289323) [X4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-0.03956441632289323) [Y5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03956441632289323) [X5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03935916802205308) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (-0.03935916802205308) [X2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (-0.03935916802205308) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (-0.03935916802205308) [X3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (-0.03931805194719748) [Y4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.03931805194719748) [X4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.03931805194719748) [Y5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03931805194719748) [X5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03560837898831243) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.03560837898831243) [X2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.029903789512624845) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (-0.029903789512624845) [X2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (-0.029903789512624845) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (-0.029903789512624845) [X3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (-0.0287307795519055) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0287307795519055) [X2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0287307795519055) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0287307795519055) [X3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.025637238296026817) [Y4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-0.025637238296026817) [X4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-0.025637238296026817) [Y5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-0.025637238296026817) [X5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-0.024755463292890977) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (-0.024755463292890977) [X2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (-0.024755463292890977) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (-0.024755463292890977) [X3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (-0.024282117354693183) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.024282117354693183) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.023145130929529013) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (-0.023145130929529013) [X5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (-0.022528440196012956) [Y4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.022528440196012956) [X4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.02143381072160086) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (-0.02143381072160086) [X2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (-0.02143381072160086) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (-0.02143381072160086) [X3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251606) [Y3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.019257505095251606) [X3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.01902824244384724) [Y2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (-0.01902824244384724) [X2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (-0.018889030304942944) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-0.018889030304942944) [X2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-0.018889030304942944) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.018889030304942944) [X3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.016024603689179403) [Y5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-0.016024603689179403) [X5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-0.015225630757226563) [Y2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (-0.015225630757226563) [X2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (-0.014603704729162108) [Y3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.014603704729162108) [X3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.014564531231172998) [Y6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.014564531231172998) [X6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.011756013419819269) [Y2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.011756013419819269) [X2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.011285190200840884) [Y4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (-0.011285190200840884) [X4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (-0.009841749246962553) [Y3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (-0.009841749246962553) [X3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (-0.009612634606847416) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-0.009612634606847416) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-0.009612634606847416) [Y5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-0.009612634606847416) [X5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-0.008469978791023987) [Y3 Z4 Z5 X6 X7 Z8 Z9 Y10]
+ (-0.008469978791023987) [X3 Z4 Z5 Y6 Y7 Z8 Z9 X10]
+ (-0.007306759928832958) [Y4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-0.007306759928832958) [X4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005923798336561337) [Y5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (-0.005923798336561337) [X5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (-0.005652620978017355) [Y0 Y1 X2 Z3 Z4 Z5 Z6 X7]
+ (-0.005652620978017355) [X0 X1 Y2 Z3 Z4 Z5 Z6 Y7]
+ (-0.005368659358109487) [Y2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005368659358109487) [X2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.004158797381840007) [Y2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.004158797381840007) [X2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.003356670563832899) [Y1 Z2 Z3 Z4 Z5 X6 X8 Y9]
+ (-0.003356670563832899) [Y1 Z2 Z3 Z4 Z5 Y6 Y8 Y9]
+ (-0.003356670563832899) [X1 Z2 Z3 Z4 Z5 X6 X8 X9]
+ (-0.003356670563832899) [X1 Z2 Z3 Z4 Z5 Y6 Y8 X9]
+ (-0.003267513854423554) [Y1 Z2 Z3 Z4 Z5 X6 X12 Y13]
+ (-0.003267513854423554) [Y1 Z2 Z3 Z4 Z5 Y6 Y12 Y13]
+ (-0.003267513854423554) [X1 Z2 Z3 Z4 Z5 X6 X12 X13]
+ (-0.003267513854423554) [X1 Z2 Z3 Z4 Z5 Y6 Y12 X13]
+ (-0.0027790267990255497) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7]
+ (-0.0027790267990255497) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7]
+ (-0.0026860409778066145) [Y0 Z1 Z2 Z3 X4 X10 Z11 Y12]
+ (-0.0026860409778066145) [X0 Z1 Z2 Z3 Y4 Y10 Z11 X12]
+ (-0.0026860409778066145) [Y1 Z2 Z3 Z4 X5 X11 Z12 Y13]
+ (-0.0026860409778066145) [X1 Z2 Z3 Z4 Y5 Y11 Z12 X13]
+ (-0.00229395661135245) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7]
+ (-0.00229395661135245) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7]
+ (-0.00229395661135245) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7]
+ (-0.00229395661135245) [X0 Z1 X2 X3 Z4 Z5 Z6 X7]
+ (-0.0009581655836696586) [Y0 Z1 Z2 Z3 Z4 X5 X11 Y12]
+ (-0.0009581655836696586) [Y0 Z1 Z2 Z3 Z4 Y5 Y11 Y12]
+ (-0.0009581655836696586) [X0 Z1 Z2 Z3 Z4 X5 X11 X12]
+ (-0.0009581655836696586) [X0 Z1 Z2 Z3 Z4 Y5 Y11 X12]
+ (-0.0009581655836696586) [Y1 Z2 Z3 X4 X10 Z11 Z12 Y13]
+ (-0.0009581655836696586) [Y1 Z2 Z3 Y4 Y10 Z11 Z12 Y13]
+ (-0.0009581655836696586) [X1 Z2 Z3 X4 X10 Z11 Z12 X13]
+ (-0.0009581655836696586) [X1 Z2 Z3 Y4 Y10 Z11 Z12 X13]
+ (-0.0002463643756957541) [Y5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.0002463643756957541) [X5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.00013840177303550704) [Y1 Z2 Z3 Z4 Z5 X6 X10 Y11]
+ (-0.00013840177303550704) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Y11]
+ (-0.00013840177303550704) [X1 Z2 Z3 Z4 Z5 X6 X10 X11]
+ (-0.00013840177303550704) [X1 Z2 Z3 Z4 Z5 Y6 Y10 X11]
+ (-7.735036880591836e-05) [Y0 Y1 X6 Z7 Z8 Z9 Z10 X11]
+ (-7.735036880591836e-05) [X0 X1 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585306045918e-05) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585306045918e-05) [Z0 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.6103585306045918e-05) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.6103585306045918e-05) [Z1 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808795612183e-05) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.5316808795612183e-05) [Z0 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808795612183e-05) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5316808795612183e-05) [Z1 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-9.806102775304608e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-9.806102775304608e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-9.806102775304608e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-9.806102775304608e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-7.089799467701546e-06) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.089799467701546e-06) [Z2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.089799467701546e-06) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.089799467701546e-06) [Z3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-6.652209669520341e-06) [Z0 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.652209669520341e-06) [Z0 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-6.652209669520341e-06) [Z1 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.652209669520341e-06) [Z1 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.481851833976335e-06) [Z0 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.481851833976335e-06) [Z0 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.481851833976335e-06) [Z1 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.481851833976335e-06) [Z1 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-5.07148073646035e-06) [Y5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-5.07148073646035e-06) [Y5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-5.07148073646035e-06) [X5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-5.07148073646035e-06) [X5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-4.73462203884426e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-4.73462203884426e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-4.73462203884426e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-4.73462203884426e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-4.728843147303917e-06) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-4.728843147303917e-06) [Z2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-4.728843147303917e-06) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.728843147303917e-06) [Z3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.253224225607854e-06) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.253224225607854e-06) [Z4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.769659452014876e-06) [Z6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.769659452014876e-06) [Z6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.5443954293722953e-06) [Y2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-3.5443954293722953e-06) [Y2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-3.5443954293722953e-06) [X2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-3.5443954293722953e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-3.5443954293722953e-06) [Y3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-3.5443954293722953e-06) [Y3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-3.5443954293722953e-06) [X3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-3.5443954293722953e-06) [X3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-2.3609563203976293e-06) [Y2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-2.3609563203976293e-06) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-2.3609563203976293e-06) [X2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-2.3609563203976293e-06) [X2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-2.1032156046981257e-06) [Z2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.1032156046981257e-06) [Z2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.1032156046981257e-06) [Z3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.1032156046981257e-06) [Z3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.0111220982076108e-06) [Z2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.0111220982076108e-06) [Z2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.0111220982076108e-06) [Z3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.0111220982076108e-06) [Z3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9429468367456792e-06) [Z4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.9429468367456792e-06) [Z4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.9429468367456792e-06) [Z5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.9429468367456792e-06) [Z5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.6541174771455422e-06) [Z4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.6541174771455422e-06) [Z4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.6541174771455422e-06) [Z5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.6541174771455422e-06) [Z5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.5224930676280565e-06) [Y2 Z3 Z4 X5 X7 Z8 Z9 Y10]
+ (-1.5224930676280565e-06) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Y10]
+ (-1.5224930676280565e-06) [X2 Z3 Z4 X5 X7 Z8 Z9 X10]
+ (-1.5224930676280565e-06) [X2 Z3 Z4 Y5 Y7 Z8 Z9 X10]
+ (-1.5224930676280565e-06) [Y3 X4 X6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930676280565e-06) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930676280565e-06) [X3 X4 X6 Z7 Z8 Z9 Z10 X11]
+ (-1.5224930676280565e-06) [X3 Y4 Y6 Z7 Z8 Z9 Z10 X11]
+ (-1.2283337825035089e-06) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (-1.2283337825035089e-06) [Y4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (-1.2283337825035089e-06) [X4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (-1.2283337825035089e-06) [X4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (-7.988770288665981e-07) [Y2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (-7.988770288665981e-07) [X2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (-7.988770288665981e-07) [Y3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (-7.988770288665981e-07) [X3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (-7.867765104337353e-07) [Y0 X1 X5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765104337353e-07) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765104337353e-07) [X0 X1 X5 Z6 Z7 Z8 Z9 X10]
+ (-7.867765104337353e-07) [X0 Y1 Y5 Z6 Z7 Z8 Z9 X10]
+ (-7.189990975396648e-07) [Y1 Y2 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.189990975396648e-07) [X1 X2 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-6.175246207195268e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X11 X12]
+ (-6.175246207195268e-07) [X1 Z2 Z3 Z4 Z5 X6 Y11 Y12]
+ (-5.471647744782934e-07) [Y0 Z1 Z2 Y3 X10 Z11 Z12 X13]
+ (-5.471647744782934e-07) [X0 Z1 Z2 X3 Y10 Z11 Z12 Y13]
+ (-4.561447179959603e-07) [Y2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (-4.561447179959603e-07) [X2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (-4.561447179959603e-07) [Y3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (-4.561447179959603e-07) [X3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (-4.5233896779621997e-07) [Y1 Y2 X5 Z6 Z7 Z8 Z9 X10]
+ (-4.5233896779621997e-07) [X1 X2 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-3.4273231087063786e-07) [Y2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (-3.4273231087063786e-07) [X2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (-3.4273231087063786e-07) [Y3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (-3.4273231087063786e-07) [X3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (-3.3281393506793533e-07) [Y6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-3.3281393506793533e-07) [Y6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-3.3281393506793533e-07) [X6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-3.3281393506793533e-07) [X6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-3.0868265651343345e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X12 X13]
+ (-3.0868265651343345e-07) [X0 Z1 Z2 Z3 Z4 X5 Y12 Y13]
+ (-2.8882935960013696e-07) [Y4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8882935960013696e-07) [Y4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8882935960013696e-07) [X4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.8882935960013696e-07) [X4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-2.3713289480052117e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X8 X9]
+ (-2.3713289480052117e-07) [X0 Z1 Z2 Z3 Z4 X5 Y8 Y9]
+ (-1.8394209155352712e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7]
+ (-1.8394209155352712e-07) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7]
+ (-8.057446595508074e-08) [Y0 Z1 Z2 Z3 Z4 X5 X10 Y11]
+ (-8.057446595508074e-08) [X0 Z1 Z2 Z3 Z4 Y5 Y10 X11]
+ (4.537178095793308e-08) [X2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.537178095793308e-08) [Y2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.537178095793308e-08) [X3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (4.537178095793308e-08) [Y3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (8.057446595508074e-08) [Y0 Z1 Z2 Z3 Z4 Y5 X10 X11]
+ (8.057446595508074e-08) [X0 Z1 Z2 Z3 Z4 X5 Y10 Y11]
+ (9.209350649051473e-08) [Y2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350649051473e-08) [Y2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350649051473e-08) [X2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (9.209350649051473e-08) [X2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.7035783554400588e-07) [Y0 X1 X7 Z8 Z9 Z10 Z11 Y12]
+ (1.7035783554400588e-07) [Y0 Y1 Y7 Z8 Z9 Z10 Z11 Y12]
+ (1.7035783554400588e-07) [X0 X1 X7 Z8 Z9 Z10 Z11 X12]
+ (1.7035783554400588e-07) [X0 Y1 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.8394209155352712e-07) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7]
+ (1.8394209155352712e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7]
+ (2.3713289480052117e-07) [Y0 Z1 Z2 Z3 Z4 X5 X8 Y9]
+ (2.3713289480052117e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y8 X9]
+ (3.0868265651343345e-07) [Y0 Z1 Z2 Z3 Z4 X5 X12 Y13]
+ (3.0868265651343345e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y12 X13]
+ (4.5233896779621997e-07) [Y1 X2 X5 Z6 Z7 Z8 Z9 Y10]
+ (4.5233896779621997e-07) [X1 Y2 Y5 Z6 Z7 Z8 Z9 X10]
+ (5.471647744782934e-07) [Y0 Z1 Z2 X3 X10 Z11 Z12 Y13]
+ (5.471647744782934e-07) [X0 Z1 Z2 Y3 Y10 Z11 Z12 X13]
+ (6.175246207195268e-07) [Y1 Z2 Z3 Z4 Z5 X6 X11 Y12]
+ (6.175246207195268e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y11 X12]
+ (7.189990975396648e-07) [Y1 X2 X7 Z8 Z9 Z10 Z11 Y12]
+ (7.189990975396648e-07) [X1 Y2 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.3304731887051392e-06) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (1.3304731887051392e-06) [Y4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (1.3304731887051392e-06) [X4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (1.3304731887051392e-06) [X4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (1.6288532435538576e-06) [Y2 Z3 X4 X6 Z7 Z8 Z9 Y10]
+ (1.6288532435538576e-06) [X2 Z3 Y4 Y6 Z7 Z8 Z9 X10]
+ (1.6288532435538576e-06) [Y3 Z4 X5 X7 Z8 Z9 Z10 Y11]
+ (1.6288532435538576e-06) [X3 Z4 Y5 Y7 Z8 Z9 Z10 X11]
+ (1.6893489514973196e-06) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (1.6893489514973196e-06) [X2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (1.6893489514973196e-06) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (1.6893489514973196e-06) [X3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (2.7455184005056965e-06) [Y2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (2.7455184005056965e-06) [Y2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (2.7455184005056965e-06) [X2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (2.7455184005056965e-06) [X2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (2.7455184005056965e-06) [Y3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (2.7455184005056965e-06) [Y3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (2.7455184005056965e-06) [X3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (2.7455184005056965e-06) [X3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (3.211842019125376e-06) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (3.211842019125376e-06) [Y2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (3.211842019125376e-06) [X2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (3.211842019125376e-06) [X2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (3.211842019125376e-06) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (3.211842019125376e-06) [Y3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (3.211842019125376e-06) [X3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (3.211842019125376e-06) [X3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (3.3131455001772937e-06) [Y6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (3.3131455001772937e-06) [Y6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (3.3131455001772937e-06) [X6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (3.3131455001772937e-06) [X6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (3.3343312893992163e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (3.3343312893992163e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (4.1839325594484895e-06) [Y6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (4.1839325594484895e-06) [X6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (7.735036880591836e-05) [Y0 X1 X6 Z7 Z8 Z9 Z10 Y11]
+ (7.735036880591836e-05) [X0 Y1 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.0002463643756957541) [Y5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.0002463643756957541) [X5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.00044585351288408456) [Y0 Z1 X2 X6 Z7 Z8 Z9 Y10]
+ (0.00044585351288408456) [X0 Z1 Y2 Y6 Z7 Z8 Z9 X10]
+ (0.00044585351288408456) [Y1 Z2 X3 X7 Z8 Z9 Z10 Y11]
+ (0.00044585351288408456) [X1 Z2 Y3 Y7 Z8 Z9 Z10 X11]
+ (0.0005940221543005324) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005324) [Y0 Z1 Y2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005324) [X0 Z1 X2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005324) [X0 Z1 X2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005324) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005324) [Y1 Z2 Y3 X6 Z7 Z8 Z9 X10]
+ (0.0005940221543005324) [X1 Z2 X3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005324) [X1 Z2 X3 X6 Z7 Z8 Z9 X10]
+ (0.00085338562541255) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7]
+ (0.00085338562541255) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7]
+ (0.00085338562541255) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7]
+ (0.00085338562541255) [X0 Z1 Z2 Z3 X4 X5 Z6 X7]
+ (0.0010435246534907501) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z13]
+ (0.0010435246534907501) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z13]
+ (0.0010435246534907501) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z12]
+ (0.0010435246534907501) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z12]
+ (0.001280306097349659) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z9]
+ (0.001280306097349659) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z9]
+ (0.001280306097349659) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z8]
+ (0.001280306097349659) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z8]
+ (0.00130380047881269) [Y0 Z1 Z2 Z3 Y4 Y10 Z11 Y12]
+ (0.00130380047881269) [X0 Z1 Z2 Z3 X4 X10 Z11 X12]
+ (0.00130380047881269) [Y1 Z2 Z3 Z4 Y5 Y11 Z12 Y13]
+ (0.00130380047881269) [X1 Z2 Z3 Z4 X5 X11 Z12 X13]
+ (0.002261966062482348) [Y0 Z1 Z2 Z3 Y4 Y11 Z12 Y13]
+ (0.002261966062482348) [Y0 Z1 Z2 Z3 Y4 X11 Z12 X13]
+ (0.002261966062482348) [X0 Z1 Z2 Z3 X4 Y11 Z12 Y13]
+ (0.002261966062482348) [X0 Z1 Z2 Z3 X4 X11 Z12 X13]
+ (0.002261966062482348) [Y1 Z2 Z3 Z4 Y5 Y10 Z11 Y12]
+ (0.002261966062482348) [Y1 Z2 Z3 Z4 Y5 X10 Z11 X12]
+ (0.002261966062482348) [X1 Z2 Z3 Z4 X5 Y10 Z11 Y12]
+ (0.002261966062482348) [X1 Z2 Z3 Z4 X5 X10 Z11 X12]
+ (0.003989841456619305) [Y0 Z1 Z2 Z3 Y4 X10 Z11 X12]
+ (0.003989841456619305) [X0 Z1 Z2 Z3 X4 Y10 Z11 Y12]
+ (0.003989841456619305) [Y1 Z2 Z3 Z4 Y5 X11 Z12 X13]
+ (0.003989841456619305) [X1 Z2 Z3 Z4 X5 Y11 Z12 Y13]
+ (0.004158797381840007) [Y2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.004158797381840007) [X2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.004311038507914304) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z12]
+ (0.004311038507914304) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z12]
+ (0.004311038507914304) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z13]
+ (0.004311038507914304) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z13]
+ (0.004636976661182558) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z8]
+ (0.004636976661182558) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z8]
+ (0.004636976661182558) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z9]
+ (0.004636976661182558) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z9]
+ (0.005114473831660379) [Y0 Z1 Z2 X3 X7 Z8 Z9 Y10]
+ (0.005114473831660379) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Y10]
+ (0.005114473831660379) [X0 Z1 Z2 X3 X7 Z8 Z9 X10]
+ (0.005114473831660379) [X0 Z1 Z2 Y3 Y7 Z8 Z9 X10]
+ (0.005114473831660379) [Y1 X2 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.005114473831660379) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.005114473831660379) [X1 X2 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005114473831660379) [X1 Y2 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.005241535382803874) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z11]
+ (0.005241535382803874) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z11]
+ (0.005241535382803874) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z10]
+ (0.005241535382803874) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z10]
+ (0.005262642473076827) [Y0 Z1 Y2 X6 Z7 Z8 Z9 X10]
+ (0.005262642473076827) [X0 Z1 X2 Y6 Z7 Z8 Z9 Y10]
+ (0.005262642473076827) [Y1 Z2 Y3 X7 Z8 Z9 Z10 X11]
+ (0.005262642473076827) [X1 Z2 X3 Y7 Z8 Z9 Z10 Y11]
+ (0.005368659358109487) [Y2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005368659358109487) [X2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.00537993715583938) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z10]
+ (0.00537993715583938) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z10]
+ (0.00537993715583938) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z11]
+ (0.00537993715583938) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z11]
+ (0.005652620978017355) [Y0 X1 X2 Z3 Z4 Z5 Z6 Y7]
+ (0.005652620978017355) [X0 Y1 Y2 Z3 Z4 Z5 Z6 X7]
+ (0.005708495985960912) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Y10]
+ (0.005708495985960912) [X0 Z1 X2 X6 Z7 Z8 Z9 X10]
+ (0.005708495985960912) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Y11]
+ (0.005708495985960912) [X1 Z2 X3 X7 Z8 Z9 Z10 X11]
+ (0.005923798336561337) [Y5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (0.005923798336561337) [X5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (0.007306759928832958) [Y4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.007306759928832958) [X4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.008469978791023987) [Y3 Z4 Z5 Y6 X7 Z8 Z9 X10]
+ (0.008469978791023987) [X3 Z4 Z5 X6 Y7 Z8 Z9 Y10]
+ (0.009841749246962553) [Y3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (0.009841749246962553) [X3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (0.011285190200840884) [Y4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (0.011285190200840884) [X4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (0.011756013419819269) [Y2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.011756013419819269) [X2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.014564531231172998) [Y6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.014564531231172998) [X6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.014603704729162108) [Y3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.014603704729162108) [X3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.015225630757226563) [Y2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (0.015225630757226563) [X2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (0.016024603689179403) [Y5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (0.016024603689179403) [X5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (0.01902824244384724) [Y2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (0.01902824244384724) [X2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (0.019257505095251606) [Y3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.019257505095251606) [X3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.04587947078129812) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.04587947078129812) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-0.3693708936615621) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.3693708936615621) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.3693708936615621) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.3693708936615621) [X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.2816425776702303) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.2816425776702303) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.28164257767023027) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.28164257767023027) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.09065144207036466) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.09065144207036466) [Z0 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.09065144207036466) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.09065144207036466) [Z1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.07635021950635006) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.07635021950635006) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.07635021950635006) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.07635021950635006) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214024) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.06752385099214024) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214024) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.06752385099214024) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03560837898831243) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.03560837898831243) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03490334337366158) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03490334337366158) [Z2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03490334337366158) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.03490334337366158) [Z3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.024591860883829874) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.024591860883829874) [Z2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.024591860883829874) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.024591860883829874) [Z3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.02428211735469318) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.02428211735469318) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.023145130929529016) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (-0.023145130929529016) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (-0.022528440196012956) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.022528440196012956) [Z4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.019538050311314756) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-0.019538050311314756) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-0.019538050311314756) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-0.019538050311314756) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-0.017091553155898862) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-0.017091553155898862) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-0.017091553155898862) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-0.017091553155898862) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-0.016024603689179403) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-0.016024603689179403) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-0.016024603689179403) [X4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-0.016024603689179403) [X4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-0.0103114824898317) [Y2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0103114824898317) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0103114824898317) [X2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0103114824898317) [X2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.009841749246962553) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962553) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.009841749246962553) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962553) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209816) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209816) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209816) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008826368514209816) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008541996625454852) [Y2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454852) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454852) [X2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454852) [X2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454852) [Y3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454852) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454852) [X3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.008541996625454852) [X3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.008469978791023987) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (-0.008469978791023987) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (-0.008469978791023987) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (-0.008469978791023987) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (-0.0046686203187762945) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0046686203187762945) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.003876470899336951) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.003876470899336951) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.0038040661717285355) [Y0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0038040661717285355) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0038040661717285355) [X0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0038040661717285355) [X0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.003484157300217873) [Y1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.003484157300217873) [X1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.003356670563832899) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.003356670563832899) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.0032675138544235537) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.0032675138544235537) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.0021413612231016093) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.0021413612231016093) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.0017278753941369557) [Y0 Z1 Z2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (-0.0017278753941369557) [X0 Z1 Z2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (-0.0016407548553123961) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0016407548553123961) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0014528843214169133) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0014528843214169133) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0014528843214169133) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0014528843214169133) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0007870896771024497) [Y1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (-0.0007870896771024497) [X1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-0.00051927434994876) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 X10]
+ (-0.00051927434994876) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Y10]
+ (-0.00019400857029756386) [Y1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.00019400857029756386) [X1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.00013840177303550704) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (-0.00013840177303550704) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (-7.141625221156935e-05) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-7.141625221156935e-05) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-7.141625221156935e-05) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.141625221156935e-05) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-5.071480736460349e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-5.071480736460349e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-3.151346311181914e-06) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-3.151346311181914e-06) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-3.088250711376335e-06) [Y2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-3.088250711376335e-06) [X2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-2.9885117063276855e-06) [Y3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.9885117063276855e-06) [X3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8742990714313594e-06) [Y3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-2.8742990714313594e-06) [X3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-2.3609563203976293e-06) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-2.3609563203976293e-06) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.3002946561855302e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-1.3002946561855302e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-1.146837650769208e-06) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.146837650769208e-06) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.146837650769208e-06) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.146837650769208e-06) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.352332103130832e-07) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.352332103130832e-07) [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.352332103130832e-07) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.352332103130832e-07) [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.091637199162288e-07) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637199162288e-07) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637199162288e-07) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637199162288e-07) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637199162288e-07) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637199162288e-07) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637199162288e-07) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.091637199162288e-07) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.074305985982285e-07) [Y0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.074305985982285e-07) [X0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.074305985982285e-07) [Y1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.074305985982285e-07) [X1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.900128986491991e-07) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-7.900128986491991e-07) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.900128986491991e-07) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.900128986491991e-07) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.867765104337353e-07) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.867765104337353e-07) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.560692464925925e-07) [Y0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692464925925e-07) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692464925925e-07) [X0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692464925925e-07) [X0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692464925925e-07) [Y1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692464925925e-07) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692464925925e-07) [X1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.560692464925925e-07) [X1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-4.997018422241951e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-4.997018422241951e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-4.997018422241951e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-4.997018422241951e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-4.997018422241951e-07) [Y1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-4.997018422241951e-07) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-4.997018422241951e-07) [X1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-4.997018422241951e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-3.568247521200088e-07) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.568247521200088e-07) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.568247521200088e-07) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.568247521200088e-07) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393085297927e-07) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393085297927e-07) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393085297927e-07) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393085297927e-07) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393085297927e-07) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393085297927e-07) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.3767393085297927e-07) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393085297927e-07) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-2.8882935960013696e-07) [Y4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.8882935960013696e-07) [X4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.6863815454407206e-07) [Y3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.6863815454407206e-07) [X3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-1.7035783554400588e-07) [Y0 X1 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.7035783554400588e-07) [X0 Y1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-9.209350649051473e-08) [Y2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.209350649051473e-08) [X2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243952706e-08) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773243952706e-08) [Y0 Z1 Y2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243952706e-08) [X0 Z1 X2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773243952706e-08) [X0 Z1 X2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243952706e-08) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773243952706e-08) [Y1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.379773243952706e-08) [X1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773243952706e-08) [X1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.97422537932605e-08) [X0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.97422537932605e-08) [Y0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.97422537932605e-08) [X1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.97422537932605e-08) [Y1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.047471655548407e-08) [Y0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.047471655548407e-08) [X0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.047471655548407e-08) [Y1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.047471655548407e-08) [X1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (9.209350649051473e-08) [Y2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (9.209350649051473e-08) [X2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0717282183524565e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (1.0717282183524565e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (1.0717282183524565e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (1.0717282183524565e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (1.2004287494174931e-07) [X0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (1.2004287494174931e-07) [Y0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (1.2004287494174931e-07) [X1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (1.2004287494174931e-07) [Y1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (1.7035783554400588e-07) [Y0 Y1 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.7035783554400588e-07) [X0 X1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.3120943052410326e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (2.3120943052410326e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (2.3120943052410326e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (2.3120943052410326e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (2.6863815454407206e-07) [Y3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (2.6863815454407206e-07) [X3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (2.8882935960013696e-07) [Y4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.8882935960013696e-07) [X4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.0922506161007574e-07) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (4.0922506161007574e-07) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (4.0922506161007574e-07) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (4.0922506161007574e-07) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (4.0922506161007574e-07) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (4.0922506161007574e-07) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (4.0922506161007574e-07) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (4.0922506161007574e-07) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (4.444597854170835e-07) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (4.444597854170835e-07) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (4.444597854170835e-07) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (4.444597854170835e-07) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (4.684915095240983e-07) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.684915095240983e-07) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.684915095240983e-07) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (4.684915095240983e-07) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (7.246974425547725e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (7.246974425547725e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (7.246974425547725e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (7.246974425547725e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (7.246974425547725e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (7.246974425547725e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (7.246974425547725e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (7.246974425547725e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (7.867765104337353e-07) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (7.867765104337353e-07) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (1.3002946561855302e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (1.3002946561855302e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (2.3609563203976293e-06) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (2.3609563203976293e-06) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (2.8742990714313594e-06) [Y3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (2.8742990714313594e-06) [X3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (2.883676576186841e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (2.883676576186841e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (2.9473560118077536e-06) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.9473560118077536e-06) [X2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.9473560118077536e-06) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.9473560118077536e-06) [X3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.9885117063276855e-06) [Y3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.9885117063276855e-06) [X3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (3.088250711376335e-06) [Y2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (3.088250711376335e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (3.151346311181914e-06) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (3.151346311181914e-06) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (3.846201671405414e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (3.846201671405414e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (3.846201671405414e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (3.846201671405414e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (5.071480736460349e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (5.071480736460349e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (5.10552672213943e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (5.10552672213943e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (5.10552672213943e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (5.10552672213943e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (5.146496327590944e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (5.146496327590944e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (5.146496327590944e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (5.146496327590944e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (5.159350502067726e-06) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (5.159350502067726e-06) [X2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (5.159350502067726e-06) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.159350502067726e-06) [X3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.427988656611797e-06) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.427988656611797e-06) [X2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.427988656611797e-06) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.427988656611797e-06) [X3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.935867718135439e-06) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.935867718135439e-06) [X2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.935867718135439e-06) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.935867718135439e-06) [X3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.253273348276761e-06) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (7.253273348276761e-06) [X2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (7.979825793570788e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (7.979825793570788e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (7.979825793570788e-06) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (7.979825793570788e-06) [X3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (4.205548411219612e-05) [Y2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.205548411219612e-05) [X2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.205548411219612e-05) [Y3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.205548411219612e-05) [X3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00013840177303550704) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (0.00013840177303550704) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (0.00018787053389548346) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.00018787053389548346) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.00018787053389548346) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.00018787053389548346) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.00019400857029756386) [Y1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.00019400857029756386) [X1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.0002463643756957541) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0002463643756957541) [Y4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0002463643756957541) [X4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0002463643756957541) [X4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.00051927434994876) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Y10]
+ (0.00051927434994876) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 X10]
+ (0.0007156734248908804) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007156734248908804) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0007156734248908804) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007156734248908804) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024497) [Y1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007870896771024497) [X1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (0.0015324835230730235) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (0.0015324835230730235) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (0.0015324835230730235) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (0.0015324835230730235) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (0.0016407548553123961) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0016407548553123961) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0017278753941369557) [Y0 Z1 Z2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (0.0017278753941369557) [X0 Z1 Z2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (0.0024464971554158934) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (0.0024464971554158934) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (0.0024464971554158934) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (0.0024464971554158934) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (0.0032675138544235537) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.0032675138544235537) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.003356670563832899) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.003356670563832899) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.003484157300217873) [Y1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.003484157300217873) [X1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.003876470899336951) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.003876470899336951) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.0046686203187762945) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.0046686203187762945) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.00476727218827811) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (0.00476727218827811) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (0.00476727218827811) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (0.00476727218827811) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (0.00528654653822687) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (0.00528654653822687) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (0.00528654653822687) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (0.00528654653822687) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (0.005408954422409974) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (0.005408954422409974) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (0.005408954422409974) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (0.005408954422409974) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (0.005923798336561337) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561337) [Y4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (0.005923798336561337) [X4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561337) [X4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (0.010715508469796756) [Y2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.010715508469796756) [X2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.010715508469796756) [Y3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010715508469796756) [X3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.01075756395390895) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.01075756395390895) [X2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.01075756395390895) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01075756395390895) [X3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.014603704729162106) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.014603704729162106) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.014603704729162106) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.014603704729162106) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.0192995605793638) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0192995605793638) [Y2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0192995605793638) [X2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0192995605793638) [X2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0192995605793638) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0192995605793638) [Y3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0192995605793638) [X3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0192995605793638) [X3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.05859198873386186) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.05859198873386186) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (5.775950527419276e-05) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.775950527419276e-05) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.7759505274192766e-05) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.7759505274192766e-05) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.07165035181002564) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.07165035181002564) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.07165035181002569) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.07165035181002569) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251606) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.019257505095251606) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0103114824898317) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0103114824898317) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008826368514209815) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209815) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.007597464029770571) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.007597464029770571) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.007597464029770571) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.007597464029770571) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311859) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311859) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311859) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311859) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311859) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311859) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311859) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311859) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005348051582676586) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005348051582676586) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005348051582676586) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005348051582676586) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0038040661717285355) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0038040661717285355) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0029841661681219264) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-0.0029841661681219264) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-0.0029841661681219264) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-0.0029841661681219264) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-0.0024464971554158934) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (-0.0024464971554158934) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (-0.002249412447093986) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.002249412447093986) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.002249412447093986) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.002249412447093986) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0021413612231016093) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.0021413612231016093) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.0018638942824587127) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0018638942824587127) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0018638942824587127) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0018638942824587127) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0018638942824587127) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0018638942824587127) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0018638942824587127) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0018638942824587127) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0016407548553123963) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0016407548553123963) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0016407548553123963) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0016407548553123963) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0012223378081538375) [Y0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538375) [Y0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538375) [X0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538375) [X0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538375) [Y1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538375) [Y1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538375) [X1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0012223378081538375) [X1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0010283292378562737) [Y0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0010283292378562737) [X0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0010283292378562737) [Y1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0010283292378562737) [X1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.1463061453105732e-05) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.1463061453105732e-05) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.8742990714313594e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-2.8742990714313594e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-2.8742990714313594e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-2.8742990714313594e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.3002946561855302e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-1.3002946561855302e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-1.3002946561855302e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-1.3002946561855302e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-1.044494129803213e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-1.044494129803213e-06) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-1.044494129803213e-06) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-1.044494129803213e-06) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-9.956079229963318e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-9.956079229963318e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-9.956079229963318e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.956079229963318e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.105515037107031e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-8.105515037107031e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-8.105515037107031e-07) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.105515037107031e-07) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.661347213075151e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-7.661347213075151e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-7.661347213075151e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-7.661347213075151e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-7.540341413795041e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-7.540341413795041e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-7.189990975396648e-07) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.189990975396648e-07) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.87662165824938e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-6.87662165824938e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-6.87662165824938e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-6.87662165824938e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-6.175246207195268e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-6.175246207195268e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-4.5233896779621997e-07) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.5233896779621997e-07) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.0767325319605975e-07) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-3.0767325319605975e-07) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.0767325319605975e-07) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.0767325319605975e-07) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.0134714589582575e-07) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.0134714589582575e-07) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.904599884237089e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-2.904599884237089e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-2.904599884237089e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-2.904599884237089e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-2.6667317547745063e-07) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.6667317547745063e-07) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.6667317547745063e-07) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.6667317547745063e-07) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.850564192856286e-07) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (-1.850564192856286e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309318024651e-07) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.6569309318024651e-07) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309318024651e-07) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.6569309318024651e-07) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.850564192856286e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (1.850564192856286e-07) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (2.6863815454407206e-07) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.6863815454407206e-07) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.6863815454407206e-07) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.6863815454407206e-07) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714589582575e-07) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (3.0134714589582575e-07) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.5233896779621997e-07) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (4.5233896779621997e-07) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (4.670402390760723e-07) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.670402390760723e-07) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.670402390760723e-07) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (4.670402390760723e-07) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (6.175246207195268e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (6.175246207195268e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (7.189990975396648e-07) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.189990975396648e-07) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.540341413795041e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (7.540341413795041e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (8.949476487543671e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (8.949476487543671e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (1.792493957717231e-06) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.792493957717231e-06) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.792493957717231e-06) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.792493957717231e-06) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.883676576186841e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (2.883676576186841e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (2.9885117063276855e-06) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.9885117063276855e-06) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.9885117063276855e-06) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.9885117063276855e-06) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.253273348276761e-06) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.253273348276761e-06) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.401710973553535e-05) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.401710973553535e-05) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.401710973553535e-05) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.401710973553535e-05) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.580960369325258e-05) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.580960369325258e-05) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.580960369325258e-05) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.580960369325258e-05) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.00051927434994876) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (0.00051927434994876) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (0.00051927434994876) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (0.00051927434994876) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (0.0007870896771024496) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024496) [Y0 Z1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024496) [X0 Z1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024496) [X0 Z1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0011726348316441894) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0011726348316441894) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0011726348316441894) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0011726348316441894) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0012366478019245244) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (0.0012366478019245244) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (0.0012366478019245244) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (0.0012366478019245244) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (0.002200964069500463) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.002200964069500463) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002200964069500463) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002200964069500463) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0023949726397980266) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0023949726397980266) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0023949726397980266) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0023949726397980266) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0023949726397980266) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0023949726397980266) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0023949726397980266) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0023949726397980266) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0024464971554158934) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (0.0024464971554158934) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (0.0038040661717285355) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0038040661717285355) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.003876470899336951) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.003876470899336951) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.003876470899336951) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.003876470899336951) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.004220813970046451) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (0.004220813970046451) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (0.004220813970046451) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (0.004220813970046451) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (0.008826368514209815) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.008826368514209815) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0103114824898317) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0103114824898317) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.019257505095251606) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.019257505095251606) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.05859198873386186) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.05859198873386186) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.398700901491165e-05) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.398700901491165e-05) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.398700901491165e-05) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.398700901491165e-05) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.003484157300217873) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.003484157300217873) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0029841661681219256) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.0029841661681219256) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.00019400857029756386) [Y0 Z1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.00019400857029756386) [X0 Z1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061453105734e-05) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061453105734e-05) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.792493957717231e-06) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.792493957717231e-06) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.540341413795041e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413795041e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-7.540341413795041e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413795041e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.850564192856286e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.850564192856286e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.850564192856286e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.850564192856286e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714589582575e-07) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.0134714589582575e-07) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714589582575e-07) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.0134714589582575e-07) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (8.94947648754367e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (8.94947648754367e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (1.792493957717231e-06) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.792493957717231e-06) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756386) [Y0 Z1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756386) [X0 Z1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0029841661681219256) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.0029841661681219256) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.003484157300217873) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.003484157300217873) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
/home/runner/work/qml/qml/demonstrations/tutorial_measurement_optimize.py:401: UserWarning: The init module will be deprecated soon, since templates can now provide a method that returns the shape of parameter tensors.
Expectation value of XYI =  0.022659767960222288
Expectation value of XIZ =  0.07715357869738898
[0.27361669 0.00898685 0.26297431 0.00732554 0.21720814 0.00116213
 0.22790267 0.00082366]
Expectation value of XYI =  0.022659767960222343
Expectation value of XIZ =  0.07715357869738915
[0.02265977 0.07715358]
[RY(-1.5707963267948966, wires=[0]), RX(1.5707963267948966, wires=[1])]
[PauliZ(wires=[0]) @ PauliZ(wires=[1]), PauliZ(wires=[0]) @ PauliZ(wires=[2])]
pennylane.qnodes.base.QuantumFunctionError: Only observables that are qubit-wise commuting
Pauli words can be returned on the same wire
Minimum number of QWC groupings found: 2
Group 0:
Y0 X2 X3
Y0 Y1 X2 X3
X2 X3
Group 1:
Z0 Z1 Z2
Z0 Z1 Z2 Z3
Z0
Z0 Z1
/home/runner/work/qml/qml/demonstrations/tutorial_measurement_optimize.py:738: UserWarning: The init module will be deprecated soon, since templates can now provide a method that returns the shape of parameter tensors.
Term expectation values:
Group 0 expectation values: [-0.14012997  0.01555488  0.18967764]
Group 1 expectation values: [0.93755207 0.94996042 0.96302938 0.96118149]
<H> =  3.8768259168631207
3.8768259168631207
 </code>
 </pre>
 </details>

---

## 10. tutorial_general_parshift.html <a name="demo9"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_general_parshift.html):

```
For 2 qubits the spectrum is [-2.0, -1.0, 0.0, 1.0, 2.0].
For 4 qubits the spectrum is [-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0].
For 5 qubits the spectrum is [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0].
Second-order finite difference:    [ 0.26814   1.696854 -2.055918 -7.236953]
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_general_parshift.html):

```
For 2 qubits the spectrum is [-2.0, -1.0, 0, 1.0, 2.0].
For 4 qubits the spectrum is [-4.0, -3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0].
For 5 qubits the spectrum is [-5.0, -4.0, -3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0, 5.0].
Second-order finite difference:    [ 0.26814   1.696853 -2.055918 -7.236953]
```

---

## 11. tutorial_vqe_parallel.html <a name="demo10"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_vqe_parallel.html):

```
Speed up: 2.95
Evaluation time: 335.20 s
Evaluation time: 113.68 s
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_vqe_parallel.html):

```
Speed up: 2.96
Evaluation time: 278.62 s
Evaluation time: 94.13 s
```

---

## 12. tutorial_noisy_circuits.html <a name="demo11"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_noisy_circuits.html):

```
Step: 5    Cost: 0.07733960999999957
Step: 10    Cost: 0.0773396099969988
Step: 15    Cost: 0.07733959171203489
Step: 20    Cost: 0.07722827121891838
Step: 25    Cost: 0.0017923029380396919
Step: 30    Cost: 3.0199179590479204e-07
Step: 34    Cost: 5.228404765345524e-10
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_noisy_circuits.html):

```
Step: 5    Cost: 0.07733960999999988
Step: 10    Cost: 0.07733960999863909
Step: 15    Cost: 0.07733960170319246
Step: 20    Cost: 0.07728907281668594
Step: 25    Cost: 0.006192562764640602
Step: 30    Cost: 6.427645677603198e-07
Step: 34    Cost: 1.1072988376257744e-09
```

---

## 13. tutorial_quantum_chemistry.html <a name="demo12"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_quantum_chemistry.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
(-46.463906788688995+0j) [] +
(-0.014583648907612668+0j) [X0 X1 Y2 Y3] +
(-3.5707613292007076e-07+0j) [X0 X1 Y2 Z3 Z4 Y5] +
(-0.005652620978017386+0j) [X0 X1 Y2 Z3 Z4 Z5 Z6 Y7] +
(-0.008826368514209853+0j) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.7924939576262682e-06+0j) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-3.5707613292007076e-07+0j) [X0 X1 X3 X4] +
(-0.005652620978017386+0j) [X0 X1 X3 Z4 Z5 X6] +
(-0.008826368514209853+0j) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.7924939576262682e-06+0j) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.002745836470186808+0j) [X0 X1 Y4 Y5] +
(-2.447323128849657e-07+0j) [X0 X1 Y4 Z5 Z6 Y7] +
(-7.867765104004244e-07+0j) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.003804066171728541+0j) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.447323128849657e-07+0j) [X0 X1 X5 X6] +
(-7.867765104004244e-07+0j) [X0 X1 X5 Z6 Z7 Z8 Z9 X10] +
(-0.0038040661717285403+0j) [X0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.006888194352970585+0j) [X0 X1 Y6 Y7] +
(-7.735036880592201e-05+0j) [X0 X1 Y6 Z7 Z8 Z9 Z10 Y11] +
(1.7035783554117184e-07+0j) [X0 X1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.735036880592202e-05+0j) [X0 X1 X7 Z8 Z9 X10] +
(1.7035783554117184e-07+0j) [X0 X1 X7 Z8 Z9 Z10 Z11 X12] +
(-0.006509361201177241+0j) [X0 X1 Y8 Y9] +
(-0.007731425250775302+0j) [X0 X1 Y10 Y11] +
(5.627851911146693e-07+0j) [X0 X1 Y10 Z11 Z12 Y13] +
(5.627851911146693e-07+0j) [X0 X1 X11 X12] +
(-0.005283776488402964+0j) [X0 X1 Y12 Y13] +
(0.014583648907612668+0j) [X0 Y1 Y2 X3] +
(3.5707613292007076e-07+0j) [X0 Y1 Y2 Z3 Z4 X5] +
(0.005652620978017386+0j) [X0 Y1 Y2 Z3 Z4 Z5 Z6 X7] +
(0.008826368514209853+0j) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-1.7924939576262682e-06+0j) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.5707613292007076e-07+0j) [X0 Y1 Y3 X4] +
(-0.005652620978017386+0j) [X0 Y1 Y3 Z4 Z5 X6] +
(-0.008826368514209853+0j) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.7924939576262682e-06+0j) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.002745836470186808+0j) [X0 Y1 Y4 X5] +
(2.447323128849657e-07+0j) [X0 Y1 Y4 Z5 Z6 X7] +
(7.867765104004244e-07+0j) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.003804066171728541+0j) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.447323128849657e-07+0j) [X0 Y1 Y5 X6] +
(-7.867765104004244e-07+0j) [X0 Y1 Y5 Z6 Z7 Z8 Z9 X10] +
(-0.0038040661717285403+0j) [X0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.006888194352970585+0j) [X0 Y1 Y6 X7] +
(7.735036880592201e-05+0j) [X0 Y1 Y6 Z7 Z8 Z9 Z10 X11] +
(-1.7035783554117184e-07+0j) [X0 Y1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-7.735036880592202e-05+0j) [X0 Y1 Y7 Z8 Z9 X10] +
(1.7035783554117184e-07+0j) [X0 Y1 Y7 Z8 Z9 Z10 Z11 X12] +
(0.006509361201177241+0j) [X0 Y1 Y8 X9] +
(0.007731425250775302+0j) [X0 Y1 Y10 X11] +
(-5.627851911146693e-07+0j) [X0 Y1 Y10 Z11 Z12 X13] +
(5.627851911146693e-07+0j) [X0 Y1 Y11 X12] +
(0.005283776488402964+0j) [X0 Y1 Y12 X13] +
(0.12507032579772073+0j) [X0 Z1 X2] +
(-1.9332412772469333e-07+0j) [X0 Z1 X2 X3 Z4 X5] +
(-0.0022939566113524784+0j) [X0 Z1 X2 X3 Z4 Z5 Z6 X7] +
(-0.0016407548553124033+0j) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(3.0134714587025076e-07+0j) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.9332412772469333e-07+0j) [X0 Z1 X2 Y3 Z4 Y5] +
(-0.0022939566113524784+0j) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7] +
(-0.0016407548553124033+0j) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(3.0134714587025076e-07+0j) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0032769719312316084+0j) [X0 Z1 X2 Z3] +
(-1.5510539176302515e-07+0j) [X0 Z1 X2 X4 Z5 X6] +
(-1.146837650692886e-06+0j) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.007597464029770604+0j) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.3807781481235694e-07+0j) [X0 Z1 X2 Y4 Z5 Y6] +
(-7.900128985929648e-07+0j) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.005348051582676607+0j) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.005530759218631505+0j) [X0 Z1 X2 Z4] +
(-1.3807781481235694e-07+0j) [X0 Z1 X2 X5 Z6 X7] +
(-3.376739308354988e-07+0j) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0018638942824587273+0j) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.3807781481235694e-07+0j) [X0 Z1 X2 Y5 Z6 Y7] +
(-3.376739308354988e-07+0j) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0018638942824587273+0j) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.001105903769189652+0j) [X0 Z1 X2 Z5] +
(0.005708495985960928+0j) [X0 Z1 X2 X6 Z7 Z8 Z9 X10] +
(-8.352332102629944e-07+0j) [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 X12] +
1.974225379294662e-08j [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.005262642473076847+0j) [X0 Z1 X2 Y6 Z7 Z8 Z9 Y10] +
(-8.074305985528383e-07+0j) [X0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.008032520918821342+0j) [X0 Z1 X2 Z6] +
(0.0005940221543005357+0j) [X0 Z1 X2 X7 Z8 Z9 Z10 X11] +
(-8.379773244429492e-08+0j) [X0 Z1 X2 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005940221543005357+0j) [X0 Z1 X2 Y7 Z8 Z9 Z10 Y11] +
(-8.379773244429492e-08+0j) [X0 Z1 X2 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0033476175306661627+0j) [X0 Z1 X2 Z7] +
(0.011055020596132045+0j) [X0 Z1 X2 Z8] +
(0.0029297686747510143+0j) [X0 Z1 X2 Z9] +
(-6.418291574346671e-07+0j) [X0 Z1 X2 X10 Z11 X12] +
(-6.556281914387427e-07+0j) [X0 Z1 X2 Y10 Z11 Y12] +
(0.0035552901955042474+0j) [X0 Z1 X2 Z10] +
(-1.1076325599262786e-07+0j) [X0 Z1 X2 X11 Z12 X13] +
(-1.1076325599262786e-07+0j) [X0 Z1 X2 Y11 Z12 Y13] +
(0.0017560707018412097+0j) [X0 Z1 X2 Z11] +
(0.006901238249797265+0j) [X0 Z1 X2 Z12] +
(0.002326230623158061+0j) [X0 Z1 X2 Z13] +
(-3.56824752099921e-07+0j) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0022494124470939982+0j) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.0474716555442856e-08+0j) [X0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0004458535128840802+0j) [X0 Z1 Y2 Y6 Z7 Z8 Z9 X10] +
(-1.9742253792414605e-08+0j) [X0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004424855449441853+0j) [X0 Z1 Z2 X3 Y4 Y5] +
(-4.523389677574658e-07+0j) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0034841573002178804+0j) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-8.091637198573868e-07+0j) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 X10] +
(-0.005733569747311878+0j) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004684903388155179+0j) [X0 Z1 Z2 X3 Y6 Y7] +
(0.004668620318776312+0j) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Y11] +
(-7.189990974897915e-07+0j) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005114473831660392+0j) [X0 Z1 Z2 X3 X7 Z8 Z9 X10] +
(-7.560692464374515e-07+0j) [X0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 X12] +
(-0.008125251921381029+0j) [X0 Z1 Z2 X3 Y8 Y9] +
(-0.0017992194936630379+0j) [X0 Z1 Z2 X3 Y10 Y11] +
(-5.471647744464549e-07+0j) [X0 Z1 Z2 X3 Y10 Z11 Z12 Y13] +
(-5.287660624416994e-07+0j) [X0 Z1 Z2 X3 X11 X12] +
(-0.004575007626639204+0j) [X0 Z1 Z2 X3 Y12 Y13] +
(0.004424855449441853+0j) [X0 Z1 Z2 Y3 Y4 X5] +
(4.523389677574658e-07+0j) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.0034841573002178804+0j) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.091637198573868e-07+0j) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 X10] +
(-0.005733569747311878+0j) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.004684903388155179+0j) [X0 Z1 Z2 Y3 Y6 X7] +
(-0.004668620318776312+0j) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 X11] +
(7.189990974897915e-07+0j) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005114473831660392+0j) [X0 Z1 Z2 Y3 Y7 Z8 Z9 X10] +
(-7.560692464374515e-07+0j) [X0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 X12] +
(0.008125251921381029+0j) [X0 Z1 Z2 Y3 Y8 X9] +
(0.0017992194936630379+0j) [X0 Z1 Z2 Y3 Y10 X11] +
(5.471647744464549e-07+0j) [X0 Z1 Z2 Y3 Y10 Z11 Z12 X13] +
(-5.287660624416994e-07+0j) [X0 Z1 Z2 Y3 Y11 X12] +
(0.004575007626639204+0j) [X0 Z1 Z2 Y3 Y12 X13] +
(3.2020768792953243e-06+0j) [X0 Z1 Z2 Z3 X4] +
(0.0008533856254125544+0j) [X0 Z1 Z2 Z3 X4 X5 Z6 X7] +
(0.0007870896771024452+0j) [X0 Z1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.0008533856254125544+0j) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7] +
(0.0007870896771024452+0j) [X0 Z1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.2919694865072288e-07+0j) [X0 Z1 Z2 Z3 X4 Z5] +
(4.4445978540484825e-07+0j) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 X10] +
(0.001172634831644189+0j) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.684915095066112e-07+0j) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Y10] +
(0.0022009640695004715+0j) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.8394209155510707e-07+0j) [X0 Z1 Z2 Z3 X4 Z6] +
(4.092250615890948e-07+0j) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 X11] +
(0.0023949726397980314+0j) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.092250615890948e-07+0j) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Y11] +
(0.0023949726397980314+0j) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(3.2362599614613936e-07+0j) [X0 Z1 Z2 Z3 X4 Z8] +
(8.649310134165053e-08+0j) [X0 Z1 Z2 Z3 X4 Z9] +
(0.0013038004788126954+0j) [X0 Z1 Z2 Z3 X4 X10 Z11 X12] +
(0.003989841456619305+0j) [X0 Z1 Z2 Z3 X4 Y10 Z11 Y12] +
(-6.733197741916719e-07+0j) [X0 Z1 Z2 Z3 X4 Z10] +
(0.002261966062482346+0j) [X0 Z1 Z2 Z3 X4 X11 Z12 X13] +
(0.002261966062482346+0j) [X0 Z1 Z2 Z3 X4 Y11 Z12 Y13] +
(-5.927453082499351e-07+0j) [X0 Z1 Z2 Z3 X4 Z11] +
(1.2393363216556851e-06+0j) [X0 Z1 Z2 Z3 X4 Z12] +
(9.306536651426536e-07+0j) [X0 Z1 Z2 Z3 X4 Z13] +
(-0.0010283292378562828+0j) [X0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.0026860409778066093+0j) [X0 Z1 Z2 Z3 Y4 Y10 Z11 X12] +
(-1.839420915551071e-07+0j) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7] +
(-0.00019400857029755968+0j) [X0 Z1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0012223378081538422+0j) [X0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12] +
(-2.371328948044889e-07+0j) [X0 Z1 Z2 Z3 Z4 X5 Y8 Y9] +
(8.057446594173692e-08+0j) [X0 Z1 Z2 Z3 Z4 X5 Y10 Y11] +
(0.001727875394136959+0j) [X0 Z1 Z2 Z3 Z4 X5 Y10 Z11 Z12 Y13] +
(-0.0009581655836696496+0j) [X0 Z1 Z2 Z3 Z4 X5 X11 X12] +
(-3.086826565130316e-07+0j) [X0 Z1 Z2 Z3 Z4 X5 Y12 Y13] +
(1.839420915551071e-07+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7] +
(0.00019400857029755968+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0012223378081538422+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12] +
(2.371328948044889e-07+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y8 X9] +
(-8.057446594173692e-08+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y10 X11] +
(-0.001727875394136959+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y10 Z11 Z12 X13] +
(-0.0009581655836696496+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y11 X12] +
(3.086826565130316e-07+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y12 X13] +
(0.04274327701378339+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6] +
(0.0005192743499487552+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11] +
(-1.850564192799201e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005192743499487552+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11] +
(-1.850564192799201e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0027790267990255475+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7] +
(0.0046369766611825845+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z8] +
(0.0012803060973496758+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z9] +
(2.312094305081157e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 X12] +
(1.0717282182668988e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y10 Z11 Y12] +
(0.005379937155839389+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z10] +
(7.246974425021575e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X11 Z12 X13] +
(7.246974425021575e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y11 Z12 Y13] +
(0.005241535382803878+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z11] +
(0.004311038507914334+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z12] +
(0.0010435246534907644+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z13] +
(1.2004287493415056e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 X12] +
(-0.003356670563832909+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y8 Y9] +
(-0.00013840177303551043+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Y11] +
(-6.175246206754677e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13] +
(-4.997018421879928e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 X12] +
(-0.003267513854423569+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y12 Y13] +
(0.003356670563832909+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y8 X9] +
(0.00013840177303551043+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 X11] +
(6.175246206754677e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13] +
(-4.997018421879928e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 X12] +
(0.003267513854423569+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y12 X13] +
(0.0038764708993369477+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11] +
(-7.540341413326895e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(0.0038764708993369477+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11] +
(-7.540341413326895e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(0.07165035181002641+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0021413612231016292+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11] +
(0.004220813970046447+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12] +
(0.0012366478019245112+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13] +
(-0.0029841661681219364+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(0.0029841661681219364+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(-1.3987009014562066e-05+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(8.949476487105949e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(-6.876621657651154e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12] +
(-7.66134721251706e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12] +
(0.0015324835230730114+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 X10] +
(-2.9045998838999507e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12] +
(0.005408954422409959+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 X10] +
(-1.0444941297226846e-06+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12] +
(0.004767272188278111+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 X10] +
(-8.105515036434764e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12] +
(0.0052865465382268655+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 X10] +
(-9.956079229233966e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0016095313817213813+0j) [X0 Z1 Z2 Z3 Z4 X6] +
(-7.141625221158963e-05+0j) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 X10] +
(-2.666731754666927e-07+0j) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0024629170071339365+0j) [X0 Z1 Z2 Z3 Z5 X6] +
(0.0007156734248908555+0j) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 X10] +
(-3.076732531808918e-07+0j) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(3.606071868096661e-07+0j) [X0 Z1 Z2 X4] +
(0.00396156079249654+0j) [X0 Z1 Z2 Z4 Z5 X6] +
(0.00018787053389545741+0j) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.6569309321397216e-07+0j) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.7379332624498545e-07+0j) [X0 Z1 Z3 X4] +
(0.001667604181144062+0j) [X0 Z1 Z3 Z4 Z5 X6] +
(-0.001452884321416946+0j) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(4.67040239084223e-07+0j) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.10433064780651402+0j) [X0 X2] +
(3.117447946180392e-06+0j) [X0 Z2 Z3 X4] +
(0.04587947078129832+0j) [X0 Z2 Z3 Z4 Z5 X6] +
(0.058591988733861844+0j) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-1.1463061452437355e-05+0j) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.014583648907612668+0j) [Y0 X1 X2 Y3] +
(3.5707613292007076e-07+0j) [Y0 X1 X2 Z3 Z4 Y5] +
(0.005652620978017386+0j) [Y0 X1 X2 Z3 Z4 Z5 Z6 Y7] +
(0.008826368514209853+0j) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.7924939576262682e-06+0j) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-3.5707613292007076e-07+0j) [Y0 X1 X3 Y4] +
(-0.005652620978017386+0j) [Y0 X1 X3 Z4 Z5 Y6] +
(-0.008826368514209853+0j) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.7924939576262682e-06+0j) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.002745836470186808+0j) [Y0 X1 X4 Y5] +
(2.447323128849657e-07+0j) [Y0 X1 X4 Z5 Z6 Y7] +
(7.867765104004244e-07+0j) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.003804066171728541+0j) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.447323128849657e-07+0j) [Y0 X1 X5 Y6] +
(-7.867765104004244e-07+0j) [Y0 X1 X5 Z6 Z7 Z8 Z9 Y10] +
(-0.0038040661717285403+0j) [Y0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.006888194352970585+0j) [Y0 X1 X6 Y7] +
(7.735036880592201e-05+0j) [Y0 X1 X6 Z7 Z8 Z9 Z10 Y11] +
(-1.7035783554117184e-07+0j) [Y0 X1 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.735036880592202e-05+0j) [Y0 X1 X7 Z8 Z9 Y10] +
(1.7035783554117184e-07+0j) [Y0 X1 X7 Z8 Z9 Z10 Z11 Y12] +
(0.006509361201177241+0j) [Y0 X1 X8 Y9] +
(0.007731425250775302+0j) [Y0 X1 X10 Y11] +
(-5.627851911146693e-07+0j) [Y0 X1 X10 Z11 Z12 Y13] +
(5.627851911146693e-07+0j) [Y0 X1 X11 Y12] +
(0.005283776488402964+0j) [Y0 X1 X12 Y13] +
(-0.014583648907612668+0j) [Y0 Y1 X2 X3] +
(-3.5707613292007076e-07+0j) [Y0 Y1 X2 Z3 Z4 X5] +
(-0.005652620978017386+0j) [Y0 Y1 X2 Z3 Z4 Z5 Z6 X7] +
(-0.008826368514209853+0j) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.7924939576262682e-06+0j) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.5707613292007076e-07+0j) [Y0 Y1 Y3 Y4] +
(-0.005652620978017386+0j) [Y0 Y1 Y3 Z4 Z5 Y6] +
(-0.008826368514209853+0j) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.7924939576262682e-06+0j) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.002745836470186808+0j) [Y0 Y1 X4 X5] +
(-2.447323128849657e-07+0j) [Y0 Y1 X4 Z5 Z6 X7] +
(-7.867765104004244e-07+0j) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.003804066171728541+0j) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.447323128849657e-07+0j) [Y0 Y1 Y5 Y6] +
(-7.867765104004244e-07+0j) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.0038040661717285403+0j) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.006888194352970585+0j) [Y0 Y1 X6 X7] +
(-7.735036880592201e-05+0j) [Y0 Y1 X6 Z7 Z8 Z9 Z10 X11] +
(1.7035783554117184e-07+0j) [Y0 Y1 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-7.735036880592202e-05+0j) [Y0 Y1 Y7 Z8 Z9 Y10] +
(1.7035783554117184e-07+0j) [Y0 Y1 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.006509361201177241+0j) [Y0 Y1 X8 X9] +
(-0.007731425250775302+0j) [Y0 Y1 X10 X11] +
(5.627851911146693e-07+0j) [Y0 Y1 X10 Z11 Z12 X13] +
(5.627851911146693e-07+0j) [Y0 Y1 Y11 Y12] +
(-0.005283776488402964+0j) [Y0 Y1 X12 X13] +
(-3.56824752099921e-07+0j) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0022494124470939982+0j) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0004458535128840802+0j) [Y0 Z1 X2 X6 Z7 Z8 Z9 Y10] +
(-1.9742253792414605e-08+0j) [Y0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.0474716555442856e-08+0j) [Y0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.12507032579772073+0j) [Y0 Z1 Y2] +
(-1.9332412772469333e-07+0j) [Y0 Z1 Y2 X3 Z4 X5] +
(-0.0022939566113524784+0j) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7] +
(-0.0016407548553124033+0j) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(3.0134714587025076e-07+0j) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.9332412772469333e-07+0j) [Y0 Z1 Y2 Y3 Z4 Y5] +
(-0.0022939566113524784+0j) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7] +
(-0.0016407548553124033+0j) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(3.0134714587025076e-07+0j) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0032769719312316084+0j) [Y0 Z1 Y2 Z3] +
(-1.3807781481235694e-07+0j) [Y0 Z1 Y2 X4 Z5 X6] +
(-7.900128985929648e-07+0j) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.005348051582676607+0j) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.5510539176302515e-07+0j) [Y0 Z1 Y2 Y4 Z5 Y6] +
(-1.146837650692886e-06+0j) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.007597464029770604+0j) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.005530759218631505+0j) [Y0 Z1 Y2 Z4] +
(-1.3807781481235694e-07+0j) [Y0 Z1 Y2 X5 Z6 X7] +
(-3.376739308354988e-07+0j) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0018638942824587273+0j) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.3807781481235694e-07+0j) [Y0 Z1 Y2 Y5 Z6 Y7] +
(-3.376739308354988e-07+0j) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0018638942824587273+0j) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.001105903769189652+0j) [Y0 Z1 Y2 Z5] +
(0.005262642473076847+0j) [Y0 Z1 Y2 X6 Z7 Z8 Z9 X10] +
(-8.074305985528383e-07+0j) [Y0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.005708495985960928+0j) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Y10] +
-1.974225379294662e-08j [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(-8.352332102629944e-07+0j) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.008032520918821342+0j) [Y0 Z1 Y2 Z6] +
(0.0005940221543005357+0j) [Y0 Z1 Y2 X7 Z8 Z9 Z10 X11] +
(-8.379773244429492e-08+0j) [Y0 Z1 Y2 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005940221543005357+0j) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Y11] +
(-8.379773244429492e-08+0j) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0033476175306661627+0j) [Y0 Z1 Y2 Z7] +
(0.011055020596132045+0j) [Y0 Z1 Y2 Z8] +
(0.0029297686747510143+0j) [Y0 Z1 Y2 Z9] +
(-6.556281914387427e-07+0j) [Y0 Z1 Y2 X10 Z11 X12] +
(-6.418291574346671e-07+0j) [Y0 Z1 Y2 Y10 Z11 Y12] +
(0.0035552901955042474+0j) [Y0 Z1 Y2 Z10] +
(-1.1076325599262786e-07+0j) [Y0 Z1 Y2 X11 Z12 X13] +
(-1.1076325599262786e-07+0j) [Y0 Z1 Y2 Y11 Z12 Y13] +
(0.0017560707018412097+0j) [Y0 Z1 Y2 Z11] +
(0.006901238249797265+0j) [Y0 Z1 Y2 Z12] +
(0.002326230623158061+0j) [Y0 Z1 Y2 Z13] +
(0.004424855449441853+0j) [Y0 Z1 Z2 X3 X4 Y5] +
(4.523389677574658e-07+0j) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.0034841573002178804+0j) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-8.091637198573868e-07+0j) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Y10] +
(-0.005733569747311878+0j) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.004684903388155179+0j) [Y0 Z1 Z2 X3 X6 Y7] +
(-0.004668620318776312+0j) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Y11] +
(7.189990974897915e-07+0j) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005114473831660392+0j) [Y0 Z1 Z2 X3 X7 Z8 Z9 Y10] +
(-7.560692464374515e-07+0j) [Y0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 Y12] +
(0.008125251921381029+0j) [Y0 Z1 Z2 X3 X8 Y9] +
(0.0017992194936630379+0j) [Y0 Z1 Z2 X3 X10 Y11] +
(5.471647744464549e-07+0j) [Y0 Z1 Z2 X3 X10 Z11 Z12 Y13] +
(-5.287660624416994e-07+0j) [Y0 Z1 Z2 X3 X11 Y12] +
(0.004575007626639204+0j) [Y0 Z1 Z2 X3 X12 Y13] +
(-0.004424855449441853+0j) [Y0 Z1 Z2 Y3 X4 X5] +
(-4.523389677574658e-07+0j) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0034841573002178804+0j) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.091637198573868e-07+0j) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.005733569747311878+0j) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004684903388155179+0j) [Y0 Z1 Z2 Y3 X6 X7] +
(0.004668620318776312+0j) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 X11] +
(-7.189990974897915e-07+0j) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005114473831660392+0j) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Y10] +
(-7.560692464374515e-07+0j) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.008125251921381029+0j) [Y0 Z1 Z2 Y3 X8 X9] +
(-0.0017992194936630379+0j) [Y0 Z1 Z2 Y3 X10 X11] +
(-5.471647744464549e-07+0j) [Y0 Z1 Z2 Y3 X10 Z11 Z12 X13] +
(-5.287660624416994e-07+0j) [Y0 Z1 Z2 Y3 Y11 Y12] +
(-0.004575007626639204+0j) [Y0 Z1 Z2 Y3 X12 X13] +
(-0.0010283292378562828+0j) [Y0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.0026860409778066093+0j) [Y0 Z1 Z2 Z3 X4 X10 Z11 Y12] +
(3.2020768792953243e-06+0j) [Y0 Z1 Z2 Z3 Y4] +
(0.0008533856254125544+0j) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7] +
(0.0007870896771024452+0j) [Y0 Z1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.0008533856254125544+0j) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7] +
(0.0007870896771024452+0j) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.2919694865072288e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z5] +
(4.684915095066112e-07+0j) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 X10] +
(0.0022009640695004715+0j) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.4445978540484825e-07+0j) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Y10] +
(0.001172634831644189+0j) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.8394209155510707e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z6] +
(4.092250615890948e-07+0j) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 X11] +
(0.0023949726397980314+0j) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.092250615890948e-07+0j) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Y11] +
(0.0023949726397980314+0j) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(3.2362599614613936e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z8] +
(8.649310134165053e-08+0j) [Y0 Z1 Z2 Z3 Y4 Z9] +
(0.003989841456619305+0j) [Y0 Z1 Z2 Z3 Y4 X10 Z11 X12] +
(0.0013038004788126954+0j) [Y0 Z1 Z2 Z3 Y4 Y10 Z11 Y12] +
(-6.733197741916719e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z10] +
(0.002261966062482346+0j) [Y0 Z1 Z2 Z3 Y4 X11 Z12 X13] +
(0.002261966062482346+0j) [Y0 Z1 Z2 Z3 Y4 Y11 Z12 Y13] +
(-5.927453082499351e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z11] +
(1.2393363216556851e-06+0j) [Y0 Z1 Z2 Z3 Y4 Z12] +
(9.306536651426536e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z13] +
(1.839420915551071e-07+0j) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7] +
(0.00019400857029755968+0j) [Y0 Z1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0012223378081538422+0j) [Y0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12] +
(2.371328948044889e-07+0j) [Y0 Z1 Z2 Z3 Z4 X5 X8 Y9] +
(-8.057446594173692e-08+0j) [Y0 Z1 Z2 Z3 Z4 X5 X10 Y11] +
(-0.001727875394136959+0j) [Y0 Z1 Z2 Z3 Z4 X5 X10 Z11 Z12 Y13] +
(-0.0009581655836696496+0j) [Y0 Z1 Z2 Z3 Z4 X5 X11 Y12] +
(3.086826565130316e-07+0j) [Y0 Z1 Z2 Z3 Z4 X5 X12 Y13] +
(-1.839420915551071e-07+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7] +
(-0.00019400857029755968+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0012223378081538422+0j) [Y0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12] +
(-2.371328948044889e-07+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X8 X9] +
(8.057446594173692e-08+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X10 X11] +
(0.001727875394136959+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X10 Z11 Z12 X13] +
(-0.0009581655836696496+0j) [Y0 Z1 Z2 Z3 Z4 Y5 Y11 Y12] +
(-3.086826565130316e-07+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X12 X13] +
(1.2004287493415056e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 Y12] +
(0.04274327701378339+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6] +
(0.0005192743499487552+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11] +
(-1.850564192799201e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005192743499487552+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11] +
(-1.850564192799201e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0027790267990255475+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7] +
(0.0046369766611825845+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z8] +
(0.0012803060973496758+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z9] +
(1.0717282182668988e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X10 Z11 X12] +
(2.312094305081157e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Y12] +
(0.005379937155839389+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z10] +
(7.246974425021575e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X11 Z12 X13] +
(7.246974425021575e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y11 Z12 Y13] +
(0.005241535382803878+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z11] +
(0.004311038507914334+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z12] +
(0.0010435246534907644+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z13] +
(0.003356670563832909+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X8 Y9] +
(0.00013840177303551043+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Y11] +
(6.175246206754677e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13] +
(-4.997018421879928e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 Y12] +
(0.003267513854423569+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X12 Y13] +
(-0.003356670563832909+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X8 X9] +
(-0.00013840177303551043+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 X11] +
(-6.175246206754677e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13] +
(-4.997018421879928e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Y12] +
(-0.003267513854423569+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X12 X13] +
(0.0038764708993369477+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11] +
(-7.540341413326895e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(0.0038764708993369477+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11] +
(-7.540341413326895e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(0.07165035181002641+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0021413612231016292+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11] +
(0.004220813970046447+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12] +
(0.0012366478019245112+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13] +
(0.0029841661681219364+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(-0.0029841661681219364+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(-1.3987009014562066e-05+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(8.949476487105949e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(-6.876621657651154e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12] +
(-7.66134721251706e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12] +
(0.0015324835230730114+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Y10] +
(-2.9045998838999507e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12] +
(0.005408954422409959+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Y10] +
(-1.0444941297226846e-06+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12] +
(0.004767272188278111+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Y10] +
(-8.105515036434764e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12] +
(0.0052865465382268655+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Y10] +
(-9.956079229233966e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0016095313817213813+0j) [Y0 Z1 Z2 Z3 Z4 Y6] +
(-7.141625221158963e-05+0j) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Y10] +
(-2.666731754666927e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0024629170071339365+0j) [Y0 Z1 Z2 Z3 Z5 Y6] +
(0.0007156734248908555+0j) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Y10] +
(-3.076732531808918e-07+0j) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(3.606071868096661e-07+0j) [Y0 Z1 Z2 Y4] +
(0.00396156079249654+0j) [Y0 Z1 Z2 Z4 Z5 Y6] +
(0.00018787053389545741+0j) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.6569309321397216e-07+0j) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.7379332624498545e-07+0j) [Y0 Z1 Z3 Y4] +
(0.001667604181144062+0j) [Y0 Z1 Z3 Z4 Z5 Y6] +
(-0.001452884321416946+0j) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(4.67040239084223e-07+0j) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.10433064780651402+0j) [Y0 Y2] +
(3.117447946180392e-06+0j) [Y0 Z2 Z3 Y4] +
(0.04587947078129832+0j) [Y0 Z2 Z3 Z4 Z5 Y6] +
(0.058591988733861844+0j) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-1.1463061452437355e-05+0j) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(12.412630742111773+0j) [Z0] +
(0.104330647806514+0j) [Z0 X1 Z2 X3] +
(3.117447946180392e-06+0j) [Z0 X1 Z2 Z3 Z4 X5] +
(0.04587947078129832+0j) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7] +
(0.058591988733861844+0j) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-1.1463061452437354e-05+0j) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.104330647806514+0j) [Z0 Y1 Z2 Y3] +
(3.117447946180392e-06+0j) [Z0 Y1 Z2 Z3 Z4 Y5] +
(0.04587947078129832+0j) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7] +
(0.058591988733861844+0j) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.1463061452437354e-05+0j) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.1861763734860502+0j) [Z0 Z1] +
(-8.337746755089204e-07+0j) [Z0 X2 Z3 X4] +
(-0.027115036845273298+0j) [Z0 X2 Z3 Z4 Z5 X6] +
(-0.06752385099214026+0j) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.4017109734795515e-05+0j) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-8.337746755089204e-07+0j) [Z0 Y2 Z3 Y4] +
(-0.027115036845273298+0j) [Z0 Y2 Z3 Z4 Z5 Y6] +
(-0.06752385099214026+0j) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.4017109734795515e-05+0j) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.236710807838304+0j) [Z0 Z2] +
(-1.1908508084289912e-06+0j) [Z0 X3 Z4 X5] +
(-0.032767657823290684+0j) [Z0 X3 Z4 Z5 Z6 X7] +
(-0.07635021950635011+0j) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.5809603692421784e-05+0j) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.1908508084289912e-06+0j) [Z0 Y3 Z4 Y5] +
(-0.032767657823290684+0j) [Z0 Y3 Z4 Z5 Z6 Y7] +
(-0.07635021950635011+0j) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.5809603692421784e-05+0j) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.25129445674591666+0j) [Z0 Z3] +
(-3.0993492435801796e-06+0j) [Z0 X4 Z5 X6] +
(-1.5316808794776046e-05+0j) [Z0 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.08684737589863614+0j) [Z0 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-3.0993492435801796e-06+0j) [Z0 Y4 Z5 Y6] +
(-1.5316808794776046e-05+0j) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.08684737589863614+0j) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.1966177089034213+0j) [Z0 Z4] +
(-3.3440815564651455e-06+0j) [Z0 X5 Z6 X7] +
(-1.6103585305176472e-05+0j) [Z0 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.09065144207036467+0j) [Z0 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.3440815564651455e-06+0j) [Z0 Y5 Z6 Y7] +
(-1.6103585305176472e-05+0j) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.09065144207036467+0j) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.19936354537360812+0j) [Z0 Z5] +
(0.0560846812466135+0j) [Z0 X6 Z7 Z8 Z9 X10] +
(-6.652209669039851e-06+0j) [Z0 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0560846812466135+0j) [Z0 Y6 Z7 Z8 Z9 Y10] +
(-6.652209669039851e-06+0j) [Z0 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.24164663936017183+0j) [Z0 Z6] +
(0.05600733087780757+0j) [Z0 X7 Z8 Z9 Z10 X11] +
(-6.4818518334986794e-06+0j) [Z0 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.05600733087780757+0j) [Z0 Y7 Z8 Z9 Z10 Y11] +
(-6.4818518334986794e-06+0j) [Z0 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.24853483371314244+0j) [Z0 Z7] +
(0.27232518306605674+0j) [Z0 Z8] +
(0.278834544267234+0j) [Z0 Z9] +
(-2.1776646050149986e-06+0j) [Z0 X10 Z11 X12] +
(-2.1776646050149986e-06+0j) [Z0 Y10 Z11 Y12] +
(0.19299723935364266+0j) [Z0 Z10] +
(-1.6148794139003297e-06+0j) [Z0 X11 Z12 X13] +
(-1.6148794139003297e-06+0j) [Z0 Y11 Z12 Y13] +
(0.20072866460441796+0j) [Z0 Z11] +
(0.2110265984979152+0j) [Z0 Z12] +
(0.21631037498631817+0j) [Z0 Z13] +
(1.9332412772469333e-07+0j) [X1 X2 Y3 Y4] +
(0.0022939566113524784+0j) [X1 X2 Y3 Z4 Z5 Y6] +
(0.0016407548553124035+0j) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-3.0134714587025076e-07+0j) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004424855449441853+0j) [X1 X2 X4 X5] +
(-8.091637198573868e-07+0j) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.005733569747311878+0j) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-4.523389677574658e-07+0j) [X1 X2 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.0034841573002178804+0j) [X1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004684903388155179+0j) [X1 X2 X6 X7] +
(0.005114473831660392+0j) [X1 X2 X6 Z7 Z8 Z9 Z10 X11] +
(-7.560692464374515e-07+0j) [X1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.004668620318776312+0j) [X1 X2 Y7 Z8 Z9 Y10] +
(-7.189990974897915e-07+0j) [X1 X2 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.008125251921381029+0j) [X1 X2 X8 X9] +
(-0.0017992194936630379+0j) [X1 X2 X10 X11] +
(-5.287660624416994e-07+0j) [X1 X2 X10 Z11 Z12 X13] +
(-5.471647744464549e-07+0j) [X1 X2 Y11 Y12] +
(-0.004575007626639204+0j) [X1 X2 X12 X13] +
(-1.9332412772469333e-07+0j) [X1 Y2 Y3 X4] +
(-0.0022939566113524784+0j) [X1 Y2 Y3 Z4 Z5 X6] +
(-0.0016407548553124035+0j) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(3.0134714587025076e-07+0j) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004424855449441853+0j) [X1 Y2 Y4 X5] +
(-8.091637198573868e-07+0j) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.005733569747311878+0j) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.523389677574658e-07+0j) [X1 Y2 Y5 Z6 Z7 Z8 Z9 X10] +
(0.0034841573002178804+0j) [X1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004684903388155179+0j) [X1 Y2 Y6 X7] +
(0.005114473831660392+0j) [X1 Y2 Y6 Z7 Z8 Z9 Z10 X11] +
(-7.560692464374515e-07+0j) [X1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.004668620318776312+0j) [X1 Y2 Y7 Z8 Z9 X10] +
(7.189990974897915e-07+0j) [X1 Y2 Y7 Z8 Z9 Z10 Z11 X12] +
(-0.008125251921381029+0j) [X1 Y2 Y8 X9] +
(-0.0017992194936630379+0j) [X1 Y2 Y10 X11] +
(-5.287660624416994e-07+0j) [X1 Y2 Y10 Z11 Z12 X13] +
(5.471647744464549e-07+0j) [X1 Y2 Y11 X12] +
(-0.004575007626639204+0j) [X1 Y2 Y12 X13] +
(0.12507032579772076+0j) [X1 Z2 X3] +
(-1.3807781481235694e-07+0j) [X1 Z2 X3 X4 Z5 X6] +
(-3.376739308354988e-07+0j) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0018638942824587273+0j) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.3807781481235694e-07+0j) [X1 Z2 X3 Y4 Z5 Y6] +
(-3.376739308354988e-07+0j) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0018638942824587273+0j) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.001105903769189652+0j) [X1 Z2 X3 Z4] +
(-1.5510539176302515e-07+0j) [X1 Z2 X3 X5 Z6 X7] +
(-1.146837650692886e-06+0j) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.007597464029770604+0j) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.3807781481235694e-07+0j) [X1 Z2 X3 Y5 Z6 Y7] +
(-7.900128985929648e-07+0j) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.005348051582676607+0j) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005530759218631505+0j) [X1 Z2 X3 Z5] +
(0.0005940221543005357+0j) [X1 Z2 X3 X6 Z7 Z8 Z9 X10] +
(-8.379773244429492e-08+0j) [X1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0005940221543005357+0j) [X1 Z2 X3 Y6 Z7 Z8 Z9 Y10] +
(-8.379773244429492e-08+0j) [X1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0033476175306661627+0j) [X1 Z2 X3 Z6] +
(0.005708495985960928+0j) [X1 Z2 X3 X7 Z8 Z9 Z10 X11] +
(-8.352332102629944e-07+0j) [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 X13] +
1.974225379294662e-08j [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005262642473076847+0j) [X1 Z2 X3 Y7 Z8 Z9 Z10 Y11] +
(-8.074305985528383e-07+0j) [X1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.008032520918821342+0j) [X1 Z2 X3 Z7] +
(0.0029297686747510143+0j) [X1 Z2 X3 Z8] +
(0.011055020596132045+0j) [X1 Z2 X3 Z9] +
(-1.1076325599262786e-07+0j) [X1 Z2 X3 X10 Z11 X12] +
(-1.1076325599262786e-07+0j) [X1 Z2 X3 Y10 Z11 Y12] +
(0.0017560707018412097+0j) [X1 Z2 X3 Z10] +
(-6.418291574346671e-07+0j) [X1 Z2 X3 X11 Z12 X13] +
(-6.556281914387427e-07+0j) [X1 Z2 X3 Y11 Z12 Y13] +
(0.0035552901955042474+0j) [X1 Z2 X3 Z11] +
(0.002326230623158061+0j) [X1 Z2 X3 Z12] +
(0.006901238249797265+0j) [X1 Z2 X3 Z13] +
(-3.56824752099921e-07+0j) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0022494124470939982+0j) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.0474716555442856e-08+0j) [X1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0004458535128840802+0j) [X1 Z2 Y3 Y7 Z8 Z9 Z10 X11] +
(-1.9742253792414605e-08+0j) [X1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0008533856254125546+0j) [X1 Z2 Z3 X4 Y5 Y6] +
(-0.0007870896771024452+0j) [X1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Y10] +
(-1.839420915551071e-07+0j) [X1 Z2 Z3 X4 X6 X7] +
(-0.0012223378081538422+0j) [X1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.00019400857029755968+0j) [X1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Y12] +
(-2.371328948044889e-07+0j) [X1 Z2 Z3 X4 X8 X9] +
(8.057446594173692e-08+0j) [X1 Z2 Z3 X4 X10 X11] +
(-0.0009581655836696496+0j) [X1 Z2 Z3 X4 X10 Z11 Z12 X13] +
(0.001727875394136959+0j) [X1 Z2 Z3 X4 Y11 Y12] +
(-3.086826565130316e-07+0j) [X1 Z2 Z3 X4 X12 X13] +
(0.0008533856254125546+0j) [X1 Z2 Z3 Y4 Y5 X6] +
(0.0007870896771024452+0j) [X1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 X10] +
(-1.839420915551071e-07+0j) [X1 Z2 Z3 Y4 Y6 X7] +
(-0.0012223378081538422+0j) [X1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.00019400857029755968+0j) [X1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 X12] +
(-2.371328948044889e-07+0j) [X1 Z2 Z3 Y4 Y8 X9] +
(8.057446594173692e-08+0j) [X1 Z2 Z3 Y4 Y10 X11] +
(-0.0009581655836696496+0j) [X1 Z2 Z3 Y4 Y10 Z11 Z12 X13] +
(-0.001727875394136959+0j) [X1 Z2 Z3 Y4 Y11 X12] +
(-3.086826565130316e-07+0j) [X1 Z2 Z3 Y4 Y12 X13] +
(3.2020768792953234e-06+0j) [X1 Z2 Z3 Z4 X5] +
(4.092250615890948e-07+0j) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 X10] +
(0.0023949726397980314+0j) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.092250615890948e-07+0j) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Y10] +
(0.0023949726397980314+0j) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(4.4445978540484825e-07+0j) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 X11] +
(0.001172634831644189+0j) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.684915095066112e-07+0j) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Y11] +
(0.0022009640695004715+0j) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.8394209155510707e-07+0j) [X1 Z2 Z3 Z4 X5 Z7] +
(8.649310134165053e-08+0j) [X1 Z2 Z3 Z4 X5 Z8] +
(3.2362599614613936e-07+0j) [X1 Z2 Z3 Z4 X5 Z9] +
(0.002261966062482346+0j) [X1 Z2 Z3 Z4 X5 X10 Z11 X12] +
(0.002261966062482346+0j) [X1 Z2 Z3 Z4 X5 Y10 Z11 Y12] +
(-5.927453082499351e-07+0j) [X1 Z2 Z3 Z4 X5 Z10] +
(0.0013038004788126954+0j) [X1 Z2 Z3 Z4 X5 X11 Z12 X13] +
(0.003989841456619305+0j) [X1 Z2 Z3 Z4 X5 Y11 Z12 Y13] +
(-6.733197741916719e-07+0j) [X1 Z2 Z3 Z4 X5 Z11] +
(9.306536651426536e-07+0j) [X1 Z2 Z3 Z4 X5 Z12] +
(1.2393363216556851e-06+0j) [X1 Z2 Z3 Z4 X5 Z13] +
(-0.0010283292378562828+0j) [X1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0026860409778066093+0j) [X1 Z2 Z3 Z4 Y5 Y11 Z12 X13] +
(-0.0005192743499487552+0j) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Y10] +
(1.850564192799201e-07+0j) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.003356670563832909+0j) [X1 Z2 Z3 Z4 Z5 X6 X8 X9] +
(-0.00013840177303551043+0j) [X1 Z2 Z3 Z4 Z5 X6 X10 X11] +
(-4.997018421879928e-07+0j) [X1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 X13] +
(-6.175246206754677e-07+0j) [X1 Z2 Z3 Z4 Z5 X6 Y11 Y12] +
(-0.003267513854423569+0j) [X1 Z2 Z3 Z4 Z5 X6 X12 X13] +
(0.0005192743499487552+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 X10] +
(-1.850564192799201e-07+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12] +
(-0.003356670563832909+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y8 X9] +
(-0.00013840177303551043+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y10 X11] +
(-4.997018421879928e-07+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 X13] +
(6.175246206754677e-07+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y11 X12] +
(-0.003267513854423569+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y12 X13] +
(0.04274327701378337+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7] +
(0.0012803060973496758+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z8] +
(0.0046369766611825845+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z9] +
(7.246974425021575e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 X12] +
(7.246974425021575e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Y12] +
(0.005241535382803878+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z10] +
(2.312094305081157e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 X13] +
(1.0717282182668988e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y11 Z12 Y13] +
(0.005379937155839389+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z11] +
(0.0010435246534907644+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z12] +
(0.004311038507914334+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z13] +
(1.2004287493415056e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 X13] +
(-0.003876470899336948+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Y10] +
(7.540341413326895e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12] +
(0.003876470899336948+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 X10] +
(-7.540341413326895e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12] +
(-0.002984166168121936+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13] +
(-0.002984166168121936+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13] +
(0.07165035181002644+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.0012366478019245112+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12] +
(0.004220813970046447+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13] +
(-1.3987009014562063e-05+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(8.949476487105949e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13] +
(-7.66134721251706e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13] +
(-0.0021413612231016292+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X11] +
(-6.876621657651154e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13] +
(0.005408954422409959+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 X11] +
(-1.0444941297226846e-06+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13] +
(0.0015324835230730114+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 X11] +
(-2.9045998838999507e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13] +
(0.0052865465382268655+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 X11] +
(-9.956079229233966e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0027790267990255475+0j) [X1 Z2 Z3 Z4 Z5 X7] +
(0.004767272188278111+0j) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 X11] +
(-8.105515036434764e-07+0j) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0024629170071339365+0j) [X1 Z2 Z3 Z4 Z6 X7] +
(0.0007156734248908555+0j) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 X11] +
(-3.076732531808918e-07+0j) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2919694865072288e-07+0j) [X1 Z2 Z3 X5] +
(0.0016095313817213813+0j) [X1 Z2 Z3 Z5 Z6 X7] +
(-7.141625221158963e-05+0j) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-2.666731754666927e-07+0j) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.7379332624498545e-07+0j) [X1 Z2 Z4 X5] +
(0.001667604181144062+0j) [X1 Z2 Z4 Z5 Z6 X7] +
(-0.001452884321416946+0j) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(4.67040239084223e-07+0j) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0032769719312316084+0j) [X1 X3] +
(3.606071868096661e-07+0j) [X1 Z3 Z4 X5] +
(0.00396156079249654+0j) [X1 Z3 Z4 Z5 Z6 X7] +
(0.00018787053389545741+0j) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.6569309321397216e-07+0j) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.9332412772469333e-07+0j) [Y1 X2 X3 Y4] +
(-0.0022939566113524784+0j) [Y1 X2 X3 Z4 Z5 Y6] +
(-0.0016407548553124035+0j) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(3.0134714587025076e-07+0j) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004424855449441853+0j) [Y1 X2 X4 Y5] +
(-8.091637198573868e-07+0j) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.005733569747311878+0j) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(4.523389677574658e-07+0j) [Y1 X2 X5 Z6 Z7 Z8 Z9 Y10] +
(0.0034841573002178804+0j) [Y1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004684903388155179+0j) [Y1 X2 X6 Y7] +
(0.005114473831660392+0j) [Y1 X2 X6 Z7 Z8 Z9 Z10 Y11] +
(-7.560692464374515e-07+0j) [Y1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.004668620318776312+0j) [Y1 X2 X7 Z8 Z9 Y10] +
(7.189990974897915e-07+0j) [Y1 X2 X7 Z8 Z9 Z10 Z11 Y12] +
(-0.008125251921381029+0j) [Y1 X2 X8 Y9] +
(-0.0017992194936630379+0j) [Y1 X2 X10 Y11] +
(-5.287660624416994e-07+0j) [Y1 X2 X10 Z11 Z12 Y13] +
(5.471647744464549e-07+0j) [Y1 X2 X11 Y12] +
(-0.004575007626639204+0j) [Y1 X2 X12 Y13] +
(1.9332412772469333e-07+0j) [Y1 Y2 X3 X4] +
(0.0022939566113524784+0j) [Y1 Y2 X3 Z4 Z5 X6] +
(0.0016407548553124035+0j) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-3.0134714587025076e-07+0j) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004424855449441853+0j) [Y1 Y2 Y4 Y5] +
(-8.091637198573868e-07+0j) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.005733569747311878+0j) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-4.523389677574658e-07+0j) [Y1 Y2 X5 Z6 Z7 Z8 Z9 X10] +
(-0.0034841573002178804+0j) [Y1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004684903388155179+0j) [Y1 Y2 Y6 Y7] +
(0.005114473831660392+0j) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Y11] +
(-7.560692464374515e-07+0j) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.004668620318776312+0j) [Y1 Y2 X7 Z8 Z9 X10] +
(-7.189990974897915e-07+0j) [Y1 Y2 X7 Z8 Z9 Z10 Z11 X12] +
(-0.008125251921381029+0j) [Y1 Y2 Y8 Y9] +
(-0.0017992194936630379+0j) [Y1 Y2 Y10 Y11] +
(-5.287660624416994e-07+0j) [Y1 Y2 Y10 Z11 Z12 Y13] +
(-5.471647744464549e-07+0j) [Y1 Y2 X11 X12] +
(-0.004575007626639204+0j) [Y1 Y2 Y12 Y13] +
(-3.56824752099921e-07+0j) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0022494124470939982+0j) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0004458535128840802+0j) [Y1 Z2 X3 X7 Z8 Z9 Z10 Y11] +
(-1.9742253792414605e-08+0j) [Y1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.0474716555442856e-08+0j) [Y1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.12507032579772076+0j) [Y1 Z2 Y3] +
(-1.3807781481235694e-07+0j) [Y1 Z2 Y3 X4 Z5 X6] +
(-3.376739308354988e-07+0j) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0018638942824587273+0j) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.3807781481235694e-07+0j) [Y1 Z2 Y3 Y4 Z5 Y6] +
(-3.376739308354988e-07+0j) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0018638942824587273+0j) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.001105903769189652+0j) [Y1 Z2 Y3 Z4] +
(-1.3807781481235694e-07+0j) [Y1 Z2 Y3 X5 Z6 X7] +
(-7.900128985929648e-07+0j) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.005348051582676607+0j) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.5510539176302515e-07+0j) [Y1 Z2 Y3 Y5 Z6 Y7] +
(-1.146837650692886e-06+0j) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.007597464029770604+0j) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005530759218631505+0j) [Y1 Z2 Y3 Z5] +
(0.0005940221543005357+0j) [Y1 Z2 Y3 X6 Z7 Z8 Z9 X10] +
(-8.379773244429492e-08+0j) [Y1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0005940221543005357+0j) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Y10] +
(-8.379773244429492e-08+0j) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0033476175306661627+0j) [Y1 Z2 Y3 Z6] +
(0.005262642473076847+0j) [Y1 Z2 Y3 X7 Z8 Z9 Z10 X11] +
(-8.074305985528383e-07+0j) [Y1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005708495985960928+0j) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Y11] +
-1.974225379294662e-08j [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.352332102629944e-07+0j) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.008032520918821342+0j) [Y1 Z2 Y3 Z7] +
(0.0029297686747510143+0j) [Y1 Z2 Y3 Z8] +
(0.011055020596132045+0j) [Y1 Z2 Y3 Z9] +
(-1.1076325599262786e-07+0j) [Y1 Z2 Y3 X10 Z11 X12] +
(-1.1076325599262786e-07+0j) [Y1 Z2 Y3 Y10 Z11 Y12] +
(0.0017560707018412097+0j) [Y1 Z2 Y3 Z10] +
(-6.556281914387427e-07+0j) [Y1 Z2 Y3 X11 Z12 X13] +
(-6.418291574346671e-07+0j) [Y1 Z2 Y3 Y11 Z12 Y13] +
(0.0035552901955042474+0j) [Y1 Z2 Y3 Z11] +
(0.002326230623158061+0j) [Y1 Z2 Y3 Z12] +
(0.006901238249797265+0j) [Y1 Z2 Y3 Z13] +
(0.0008533856254125546+0j) [Y1 Z2 Z3 X4 X5 Y6] +
(0.0007870896771024452+0j) [Y1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Y10] +
(-1.839420915551071e-07+0j) [Y1 Z2 Z3 X4 X6 Y7] +
(-0.0012223378081538422+0j) [Y1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.00019400857029755968+0j) [Y1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Y12] +
(-2.371328948044889e-07+0j) [Y1 Z2 Z3 X4 X8 Y9] +
(8.057446594173692e-08+0j) [Y1 Z2 Z3 X4 X10 Y11] +
(-0.0009581655836696496+0j) [Y1 Z2 Z3 X4 X10 Z11 Z12 Y13] +
(-0.001727875394136959+0j) [Y1 Z2 Z3 X4 X11 Y12] +
(-3.086826565130316e-07+0j) [Y1 Z2 Z3 X4 X12 Y13] +
(-0.0008533856254125546+0j) [Y1 Z2 Z3 Y4 X5 X6] +
(-0.0007870896771024452+0j) [Y1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 X10] +
(-1.839420915551071e-07+0j) [Y1 Z2 Z3 Y4 Y6 Y7] +
(-0.0012223378081538422+0j) [Y1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.00019400857029755968+0j) [Y1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 X12] +
(-2.371328948044889e-07+0j) [Y1 Z2 Z3 Y4 Y8 Y9] +
(8.057446594173692e-08+0j) [Y1 Z2 Z3 Y4 Y10 Y11] +
(-0.0009581655836696496+0j) [Y1 Z2 Z3 Y4 Y10 Z11 Z12 Y13] +
(0.001727875394136959+0j) [Y1 Z2 Z3 Y4 X11 X12] +
(-3.086826565130316e-07+0j) [Y1 Z2 Z3 Y4 Y12 Y13] +
(-0.0010283292378562828+0j) [Y1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0026860409778066093+0j) [Y1 Z2 Z3 Z4 X5 X11 Z12 Y13] +
(3.2020768792953234e-06+0j) [Y1 Z2 Z3 Z4 Y5] +
(4.092250615890948e-07+0j) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 X10] +
(0.0023949726397980314+0j) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.092250615890948e-07+0j) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Y10] +
(0.0023949726397980314+0j) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(4.684915095066112e-07+0j) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 X11] +
(0.0022009640695004715+0j) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.4445978540484825e-07+0j) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Y11] +
(0.001172634831644189+0j) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.8394209155510707e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z7] +
(8.649310134165053e-08+0j) [Y1 Z2 Z3 Z4 Y5 Z8] +
(3.2362599614613936e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z9] +
(0.002261966062482346+0j) [Y1 Z2 Z3 Z4 Y5 X10 Z11 X12] +
(0.002261966062482346+0j) [Y1 Z2 Z3 Z4 Y5 Y10 Z11 Y12] +
(-5.927453082499351e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z10] +
(0.003989841456619305+0j) [Y1 Z2 Z3 Z4 Y5 X11 Z12 X13] +
(0.0013038004788126954+0j) [Y1 Z2 Z3 Z4 Y5 Y11 Z12 Y13] +
(-6.733197741916719e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z11] +
(9.306536651426536e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z12] +
(1.2393363216556851e-06+0j) [Y1 Z2 Z3 Z4 Y5 Z13] +
(0.0005192743499487552+0j) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Y10] +
(-1.850564192799201e-07+0j) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12] +
(-0.003356670563832909+0j) [Y1 Z2 Z3 Z4 Z5 X6 X8 Y9] +
(-0.00013840177303551043+0j) [Y1 Z2 Z3 Z4 Z5 X6 X10 Y11] +
(-4.997018421879928e-07+0j) [Y1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 Y13] +
(6.175246206754677e-07+0j) [Y1 Z2 Z3 Z4 Z5 X6 X11 Y12] +
(-0.003267513854423569+0j) [Y1 Z2 Z3 Z4 Z5 X6 X12 Y13] +
(-0.0005192743499487552+0j) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 X10] +
(1.850564192799201e-07+0j) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12] +
(-0.003356670563832909+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y8 Y9] +
(-0.00013840177303551043+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Y11] +
(-4.997018421879928e-07+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 Y13] +
(-6.175246206754677e-07+0j) [Y1 Z2 Z3 Z4 Z5 Y6 X11 X12] +
(-0.003267513854423569+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y12 Y13] +
(1.2004287493415056e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 Y13] +
(0.04274327701378337+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7] +
(0.0012803060973496758+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z8] +
(0.0046369766611825845+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z9] +
(7.246974425021575e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 X12] +
(7.246974425021575e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Y12] +
(0.005241535382803878+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z10] +
(1.0717282182668988e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X11 Z12 X13] +
(2.312094305081157e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 Y13] +
(0.005379937155839389+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z11] +
(0.0010435246534907644+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z12] +
(0.004311038507914334+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z13] +
(0.003876470899336948+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Y10] +
(-7.540341413326895e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12] +
(-0.003876470899336948+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 X10] +
(7.540341413326895e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12] +
(-0.002984166168121936+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13] +
(-0.002984166168121936+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13] +
(0.07165035181002644+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.0012366478019245112+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12] +
(0.004220813970046447+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13] +
(-1.3987009014562063e-05+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(8.949476487105949e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13] +
(-7.66134721251706e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13] +
(-0.0021413612231016292+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y11] +
(-6.876621657651154e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13] +
(0.005408954422409959+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Y11] +
(-1.0444941297226846e-06+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13] +
(0.0015324835230730114+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Y11] +
(-2.9045998838999507e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13] +
(0.0052865465382268655+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Y11] +
(-9.956079229233966e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0027790267990255475+0j) [Y1 Z2 Z3 Z4 Z5 Y7] +
(0.004767272188278111+0j) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Y11] +
(-8.105515036434764e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0024629170071339365+0j) [Y1 Z2 Z3 Z4 Z6 Y7] +
(0.0007156734248908555+0j) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Y11] +
(-3.076732531808918e-07+0j) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.2919694865072288e-07+0j) [Y1 Z2 Z3 Y5] +
(0.0016095313817213813+0j) [Y1 Z2 Z3 Z5 Z6 Y7] +
(-7.141625221158963e-05+0j) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-2.666731754666927e-07+0j) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.7379332624498545e-07+0j) [Y1 Z2 Z4 Y5] +
(0.001667604181144062+0j) [Y1 Z2 Z4 Z5 Z6 Y7] +
(-0.001452884321416946+0j) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(4.67040239084223e-07+0j) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0032769719312316084+0j) [Y1 Y3] +
(3.606071868096661e-07+0j) [Y1 Z3 Z4 Y5] +
(0.00396156079249654+0j) [Y1 Z3 Z4 Z5 Z6 Y7] +
(0.00018787053389545741+0j) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.6569309321397216e-07+0j) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(12.412630742111773+0j) [Z1] +
(-1.1908508084289912e-06+0j) [Z1 X2 Z3 X4] +
(-0.032767657823290684+0j) [Z1 X2 Z3 Z4 Z5 X6] +
(-0.07635021950635011+0j) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.5809603692421784e-05+0j) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.1908508084289912e-06+0j) [Z1 Y2 Z3 Y4] +
(-0.032767657823290684+0j) [Z1 Y2 Z3 Z4 Z5 Y6] +
(-0.07635021950635011+0j) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.5809603692421784e-05+0j) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.25129445674591666+0j) [Z1 Z2] +
(-8.337746755089204e-07+0j) [Z1 X3 Z4 X5] +
(-0.027115036845273298+0j) [Z1 X3 Z4 Z5 Z6 X7] +
(-0.06752385099214026+0j) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.4017109734795515e-05+0j) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.337746755089204e-07+0j) [Z1 Y3 Z4 Y5] +
(-0.027115036845273298+0j) [Z1 Y3 Z4 Z5 Z6 Y7] +
(-0.06752385099214026+0j) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.4017109734795515e-05+0j) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.236710807838304+0j) [Z1 Z3] +
(-3.3440815564651455e-06+0j) [Z1 X4 Z5 X6] +
(-1.6103585305176472e-05+0j) [Z1 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.09065144207036467+0j) [Z1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-3.3440815564651455e-06+0j) [Z1 Y4 Z5 Y6] +
(-1.6103585305176472e-05+0j) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.09065144207036467+0j) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.19936354537360812+0j) [Z1 Z4] +
(-3.0993492435801796e-06+0j) [Z1 X5 Z6 X7] +
(-1.5316808794776046e-05+0j) [Z1 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.08684737589863614+0j) [Z1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.0993492435801796e-06+0j) [Z1 Y5 Z6 Y7] +
(-1.5316808794776046e-05+0j) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.08684737589863614+0j) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.1966177089034213+0j) [Z1 Z5] +
(0.05600733087780757+0j) [Z1 X6 Z7 Z8 Z9 X10] +
(-6.4818518334986794e-06+0j) [Z1 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.05600733087780757+0j) [Z1 Y6 Z7 Z8 Z9 Y10] +
(-6.4818518334986794e-06+0j) [Z1 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.24853483371314244+0j) [Z1 Z6] +
(0.0560846812466135+0j) [Z1 X7 Z8 Z9 Z10 X11] +
(-6.652209669039851e-06+0j) [Z1 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0560846812466135+0j) [Z1 Y7 Z8 Z9 Z10 Y11] +
(-6.652209669039851e-06+0j) [Z1 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.24164663936017183+0j) [Z1 Z7] +
(0.278834544267234+0j) [Z1 Z8] +
(0.27232518306605674+0j) [Z1 Z9] +
(-1.6148794139003297e-06+0j) [Z1 X10 Z11 X12] +
(-1.6148794139003297e-06+0j) [Z1 Y10 Z11 Y12] +
(0.20072866460441796+0j) [Z1 Z10] +
(-2.1776646050149986e-06+0j) [Z1 X11 Z12 X13] +
(-2.1776646050149986e-06+0j) [Z1 Y11 Z12 Y13] +
(0.19299723935364266+0j) [Z1 Z11] +
(0.21631037498631817+0j) [Z1 Z12] +
(0.2110265984979152+0j) [Z1 Z13] +
(-0.035839567953353475+0j) [X2 X3 Y4 Y5] +
(-2.199051618636281e-07+0j) [X2 X3 Y4 Z5 Z6 Y7] +
(-2.3609563203048072e-06+0j) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.010311482489831734+0j) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.1990516186362813e-07+0j) [X2 X3 X5 X6] +
(-2.3609563203048072e-06+0j) [X2 X3 X5 Z6 Z7 Z8 Z9 X10] +
(-0.010311482489831734+0j) [X2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.031143817988967034+0j) [X2 X3 Y6 Y7] +
(0.005368659358109488+0j) [X2 X3 Y6 Z7 Z8 Z9 Z10 Y11] +
(9.209350655392001e-08+0j) [X2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005368659358109488+0j) [X2 X3 X7 Z8 Z9 X10] +
(9.209350655392001e-08+0j) [X2 X3 X7 Z8 Z9 Z10 Z11 X12] +
(-0.03619412355904255+0j) [X2 X3 Y8 Y9] +
(-0.025384657508457455+0j) [X2 X3 Y10 Y11] +
(2.172669101465766e-06+0j) [X2 X3 Y10 Z11 Z12 Y13] +
(2.172669101465766e-06+0j) [X2 X3 X11 X12] +
(-0.015577208063976446+0j) [X2 X3 Y12 Y13] +
(0.035839567953353475+0j) [X2 Y3 Y4 X5] +
(2.199051618636281e-07+0j) [X2 Y3 Y4 Z5 Z6 X7] +
(2.3609563203048072e-06+0j) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.010311482489831734+0j) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.1990516186362813e-07+0j) [X2 Y3 Y5 X6] +
(-2.3609563203048072e-06+0j) [X2 Y3 Y5 Z6 Z7 Z8 Z9 X10] +
(-0.010311482489831734+0j) [X2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.031143817988967034+0j) [X2 Y3 Y6 X7] +
(-0.005368659358109488+0j) [X2 Y3 Y6 Z7 Z8 Z9 Z10 X11] +
(-9.209350655392001e-08+0j) [X2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005368659358109488+0j) [X2 Y3 Y7 Z8 Z9 X10] +
(9.209350655392001e-08+0j) [X2 Y3 Y7 Z8 Z9 Z10 Z11 X12] +
(0.03619412355904255+0j) [X2 Y3 Y8 X9] +
(0.025384657508457455+0j) [X2 Y3 Y10 X11] +
(-2.172669101465766e-06+0j) [X2 Y3 Y10 Z11 Z12 X13] +
(2.172669101465766e-06+0j) [X2 Y3 Y11 X12] +
(0.015577208063976446+0j) [X2 Y3 Y12 X13] +
(-3.887051674060869e-06+0j) [X2 Z3 X4] +
(-0.005143391768825121+0j) [X2 Z3 X4 X5 Z6 X7] +
(-0.009841749246962633+0j) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(2.9885117062334056e-06+0j) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.005143391768825121+0j) [X2 Z3 X4 Y5 Z6 Y7] +
(-0.009841749246962633+0j) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(2.9885117062334056e-06+0j) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.764994120952451e-07+0j) [X2 Z3 X4 Z5] +
(1.689348951397978e-06+0j) [X2 Z3 X4 X6 Z7 Z8 Z9 X10] +
(0.010757563953908969+0j) [X2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.5371780954305395e-08+0j) [X2 Z3 X4 Y6 Z7 Z8 Z9 Y10] +
(4.2055484112204795e-05+0j) [X2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(2.5935343910426286e-07+0j) [X2 Z3 X4 Z6] +
(3.211842018916505e-06+0j) [X2 Z3 X4 X7 Z8 Z9 Z10 X11] +
(0.019299560579363842+0j) [X2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(3.211842018916505e-06+0j) [X2 Z3 X4 Y7 Z8 Z9 Z10 Y11] +
(0.019299560579363842+0j) [X2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.1954890099743e-06+0j) [X2 Z3 X4 Z7] +
(2.1868423775235842e-07+0j) [X2 Z3 X4 Z8] +
(-5.770052995564484e-07+0j) [X2 Z3 X4 Z9] +
(0.015588250102380189+0j) [X2 Z3 X4 X10 Z11 X12] +
(0.005324835234221696+0j) [X2 Z3 X4 Y10 Z11 Y12] +
(-3.158656431863782e-06+0j) [X2 Z3 X4 Z10] +
(0.024353077678068973+0j) [X2 Z3 X4 X11 Z12 X13] +
(0.024353077678068973+0j) [X2 Z3 X4 Y11 Z12 Y13] +
(-7.801707500142726e-06+0j) [X2 Z3 X4 Z11] +
(3.5390541842417923e-06+0j) [X2 Z3 X4 Z12] +
(8.814937306165704e-06+0j) [X2 Z3 X4 Z13] +
(1.6288532434574125e-06+0j) [X2 Z3 Y4 Y6 Z7 Z8 Z9 X10] +
(0.010715508469796764+0j) [X2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.010263414868158495+0j) [X2 Z3 Y4 Y10 Z11 X12] +
(-1.4548424490785627e-06+0j) [X2 Z3 Z4 X5 Y6 Y7] +
(-3.1513463109759394e-06+0j) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Y11] +
(-0.019257505095251634+0j) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.5224930675185264e-06+0j) [X2 Z3 Z4 X5 X7 Z8 Z9 X10] +
(-0.008541996625454868+0j) [X2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12] +
(-7.956895373088069e-07+0j) [X2 Z3 Z4 X5 Y8 Y9] +
(-4.643051068278944e-06+0j) [X2 Z3 Z4 X5 Y10 Y11] +
(-0.01902824244384728+0j) [X2 Z3 Z4 X5 Y10 Z11 Z12 Y13] +
(-0.008764827575688786+0j) [X2 Z3 Z4 X5 X11 X12] +
(5.275883121923911e-06+0j) [X2 Z3 Z4 X5 Y12 Y13] +
(1.4548424490785627e-06+0j) [X2 Z3 Z4 Y5 Y6 X7] +
(3.1513463109759394e-06+0j) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 X11] +
(0.019257505095251634+0j) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.5224930675185264e-06+0j) [X2 Z3 Z4 Y5 Y7 Z8 Z9 X10] +
(-0.008541996625454868+0j) [X2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12] +
(7.956895373088069e-07+0j) [X2 Z3 Z4 Y5 Y8 X9] +
(4.643051068278944e-06+0j) [X2 Z3 Z4 Y5 Y10 X11] +
(0.01902824244384728+0j) [X2 Z3 Z4 Y5 Y10 Z11 Z12 X13] +
(-0.008764827575688786+0j) [X2 Z3 Z4 Y5 Y11 X12] +
(-5.275883121923911e-06+0j) [X2 Z3 Z4 Y5 Y12 X13] +
(-0.12133276911042468+0j) [X2 Z3 Z4 Z5 X6] +
(-0.008469978791024027+0j) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11] +
(2.686381544961821e-07+0j) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.008469978791024027+0j) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11] +
(2.686381544961821e-07+0j) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.02599617759802128+0j) [X2 Z3 Z4 Z5 X6 Z7] +
(-0.005805188989826954+0j) [X2 Z3 Z4 Z5 X6 Z8] +
(-0.01756120240964626+0j) [X2 Z3 Z4 Z5 X6 Z9] +
(-7.988770288600311e-07+0j) [X2 Z3 Z4 Z5 X6 X10 Z11 X12] +
(-3.4273231086759956e-07+0j) [X2 Z3 Z4 Z5 X6 Y10 Z11 Y12] +
(-0.0008145313270957405+0j) [X2 Z3 Z4 Z5 X6 Z10] +
(2.7455184003115176e-06+0j) [X2 Z3 Z4 Z5 X6 X11 Z12 X13] +
(2.7455184003115176e-06+0j) [X2 Z3 Z4 Z5 X6 Y11 Z12 Y13] +
(0.014411099430130818+0j) [X2 Z3 Z4 Z5 X6 Z11] +
(0.0006650070219498333+0j) [X2 Z3 Z4 Z5 X6 Z12] +
(-0.0034937903598902063+0j) [X2 Z3 Z4 Z5 X6 Z13] +
(-4.5614471799243157e-07+0j) [X2 Z3 Z4 Z5 Y6 Y10 Z11 X12] +
(-0.011756013419819304+0j) [X2 Z3 Z4 Z5 Z6 X7 Y8 Y9] +
(0.015225630757226558+0j) [X2 Z3 Z4 Z5 Z6 X7 Y10 Y11] +
(-3.088250711179117e-06+0j) [X2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13] +
(-3.544395429171549e-06+0j) [X2 Z3 Z4 Z5 Z6 X7 X11 X12] +
(-0.00415879738184004+0j) [X2 Z3 Z4 Z5 Z6 X7 Y12 Y13] +
(0.011756013419819304+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y8 X9] +
(-0.015225630757226558+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y10 X11] +
(3.088250711179117e-06+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13] +
(-3.544395429171549e-06+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y11 X12] +
(0.00415879738184004+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y12 X13] +
(0.014603704729162097+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11] +
(-2.874299071254574e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(0.014603704729162097+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11] +
(-2.874299071254574e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(-0.2816425776702295+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-1.300294656101864e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13] +
(-1.300294656101864e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13] +
(-0.024282117354693045+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11] +
(-0.019538050311314756+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12] +
(-0.01709155315589884+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13] +
(0.002446497155415913+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(-0.002446497155415913+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(5.775950527045218e-05+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(2.883676575980342e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(5.146496327265053e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12] +
(3.84620167116319e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12] +
(-0.03935916802205306+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 X10] +
(7.979825793106215e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12] +
(-0.024755463292890967+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z9 X10] +
(5.105526721851641e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12] +
(-0.021433810721600825+0j) [X2 Z3 Z4 Z5 Z6 Z8 Z9 X10] +
(5.15935050178204e-06+0j) [X2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12] +
(-0.029903789512624852+0j) [X2 Z3 Z4 Z5 Z7 Z8 Z9 X10] +
(5.4279886562782206e-06+0j) [X2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12] +
(0.001663879878490749+0j) [X2 Z3 Z4 X6] +
(-0.018889030304942857+0j) [X2 Z3 Z4 Z6 Z7 Z8 Z9 X10] +
(2.947356011539224e-06+0j) [X2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.003479511890334372+0j) [X2 Z3 Z5 X6] +
(-0.02873077955190549+0j) [X2 Z3 Z5 Z6 Z7 Z8 Z9 X10] +
(5.9358677177726295e-06+0j) [X2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.6021167407515033e-06+0j) [X2 X4] +
(0.0004956762314916141+0j) [X2 Z4 Z5 X6] +
(-0.03560837898831254+0j) [X2 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(7.25327334787924e-06+0j) [X2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.035839567953353475+0j) [Y2 X3 X4 Y5] +
(2.199051618636281e-07+0j) [Y2 X3 X4 Z5 Z6 Y7] +
(2.3609563203048072e-06+0j) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.010311482489831734+0j) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.1990516186362813e-07+0j) [Y2 X3 X5 Y6] +
(-2.3609563203048072e-06+0j) [Y2 X3 X5 Z6 Z7 Z8 Z9 Y10] +
(-0.010311482489831734+0j) [Y2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.031143817988967034+0j) [Y2 X3 X6 Y7] +
(-0.005368659358109488+0j) [Y2 X3 X6 Z7 Z8 Z9 Z10 Y11] +
(-9.209350655392001e-08+0j) [Y2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005368659358109488+0j) [Y2 X3 X7 Z8 Z9 Y10] +
(9.209350655392001e-08+0j) [Y2 X3 X7 Z8 Z9 Z10 Z11 Y12] +
(0.03619412355904255+0j) [Y2 X3 X8 Y9] +
(0.025384657508457455+0j) [Y2 X3 X10 Y11] +
(-2.172669101465766e-06+0j) [Y2 X3 X10 Z11 Z12 Y13] +
(2.172669101465766e-06+0j) [Y2 X3 X11 Y12] +
(0.015577208063976446+0j) [Y2 X3 X12 Y13] +
(-0.035839567953353475+0j) [Y2 Y3 X4 X5] +
(-2.199051618636281e-07+0j) [Y2 Y3 X4 Z5 Z6 X7] +
(-2.3609563203048072e-06+0j) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.010311482489831734+0j) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.1990516186362813e-07+0j) [Y2 Y3 Y5 Y6] +
(-2.3609563203048072e-06+0j) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.010311482489831734+0j) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.031143817988967034+0j) [Y2 Y3 X6 X7] +
(0.005368659358109488+0j) [Y2 Y3 X6 Z7 Z8 Z9 Z10 X11] +
(9.209350655392001e-08+0j) [Y2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005368659358109488+0j) [Y2 Y3 Y7 Z8 Z9 Y10] +
(9.209350655392001e-08+0j) [Y2 Y3 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.03619412355904255+0j) [Y2 Y3 X8 X9] +
(-0.025384657508457455+0j) [Y2 Y3 X10 X11] +
(2.172669101465766e-06+0j) [Y2 Y3 X10 Z11 Z12 X13] +
(2.172669101465766e-06+0j) [Y2 Y3 Y11 Y12] +
(-0.015577208063976446+0j) [Y2 Y3 X12 X13] +
(1.6288532434574125e-06+0j) [Y2 Z3 X4 X6 Z7 Z8 Z9 Y10] +
(0.010715508469796764+0j) [Y2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.010263414868158495+0j) [Y2 Z3 X4 X10 Z11 Y12] +
(-3.887051674060869e-06+0j) [Y2 Z3 Y4] +
(-0.005143391768825121+0j) [Y2 Z3 Y4 X5 Z6 X7] +
(-0.009841749246962633+0j) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(2.9885117062334056e-06+0j) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.005143391768825121+0j) [Y2 Z3 Y4 Y5 Z6 Y7] +
(-0.009841749246962633+0j) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(2.9885117062334056e-06+0j) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.764994120952451e-07+0j) [Y2 Z3 Y4 Z5] +
(4.5371780954305395e-08+0j) [Y2 Z3 Y4 X6 Z7 Z8 Z9 X10] +
(4.2055484112204795e-05+0j) [Y2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.689348951397978e-06+0j) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Y10] +
(0.010757563953908969+0j) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(2.5935343910426286e-07+0j) [Y2 Z3 Y4 Z6] +
(3.211842018916505e-06+0j) [Y2 Z3 Y4 X7 Z8 Z9 Z10 X11] +
(0.019299560579363842+0j) [Y2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(3.211842018916505e-06+0j) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Y11] +
(0.019299560579363842+0j) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.1954890099743e-06+0j) [Y2 Z3 Y4 Z7] +
(2.1868423775235842e-07+0j) [Y2 Z3 Y4 Z8] +
(-5.770052995564484e-07+0j) [Y2 Z3 Y4 Z9] +
(0.005324835234221696+0j) [Y2 Z3 Y4 X10 Z11 X12] +
(0.015588250102380189+0j) [Y2 Z3 Y4 Y10 Z11 Y12] +
(-3.158656431863782e-06+0j) [Y2 Z3 Y4 Z10] +
(0.024353077678068973+0j) [Y2 Z3 Y4 X11 Z12 X13] +
(0.024353077678068973+0j) [Y2 Z3 Y4 Y11 Z12 Y13] +
(-7.801707500142726e-06+0j) [Y2 Z3 Y4 Z11] +
(3.5390541842417923e-06+0j) [Y2 Z3 Y4 Z12] +
(8.814937306165704e-06+0j) [Y2 Z3 Y4 Z13] +
(1.4548424490785627e-06+0j) [Y2 Z3 Z4 X5 X6 Y7] +
(3.1513463109759394e-06+0j) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Y11] +
(0.019257505095251634+0j) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.5224930675185264e-06+0j) [Y2 Z3 Z4 X5 X7 Z8 Z9 Y10] +
(-0.008541996625454868+0j) [Y2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12] +
(7.956895373088069e-07+0j) [Y2 Z3 Z4 X5 X8 Y9] +
(4.643051068278944e-06+0j) [Y2 Z3 Z4 X5 X10 Y11] +
(0.01902824244384728+0j) [Y2 Z3 Z4 X5 X10 Z11 Z12 Y13] +
(-0.008764827575688786+0j) [Y2 Z3 Z4 X5 X11 Y12] +
(-5.275883121923911e-06+0j) [Y2 Z3 Z4 X5 X12 Y13] +
(-1.4548424490785627e-06+0j) [Y2 Z3 Z4 Y5 X6 X7] +
(-3.1513463109759394e-06+0j) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 X11] +
(-0.019257505095251634+0j) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.5224930675185264e-06+0j) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Y10] +
(-0.008541996625454868+0j) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12] +
(-7.956895373088069e-07+0j) [Y2 Z3 Z4 Y5 X8 X9] +
(-4.643051068278944e-06+0j) [Y2 Z3 Z4 Y5 X10 X11] +
(-0.01902824244384728+0j) [Y2 Z3 Z4 Y5 X10 Z11 Z12 X13] +
(-0.008764827575688786+0j) [Y2 Z3 Z4 Y5 Y11 Y12] +
(5.275883121923911e-06+0j) [Y2 Z3 Z4 Y5 X12 X13] +
(-4.5614471799243157e-07+0j) [Y2 Z3 Z4 Z5 X6 X10 Z11 Y12] +
(-0.12133276911042468+0j) [Y2 Z3 Z4 Z5 Y6] +
(-0.008469978791024027+0j) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11] +
(2.686381544961821e-07+0j) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.008469978791024027+0j) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11] +
(2.686381544961821e-07+0j) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.02599617759802128+0j) [Y2 Z3 Z4 Z5 Y6 Z7] +
(-0.005805188989826954+0j) [Y2 Z3 Z4 Z5 Y6 Z8] +
(-0.01756120240964626+0j) [Y2 Z3 Z4 Z5 Y6 Z9] +
(-3.4273231086759956e-07+0j) [Y2 Z3 Z4 Z5 Y6 X10 Z11 X12] +
(-7.988770288600311e-07+0j) [Y2 Z3 Z4 Z5 Y6 Y10 Z11 Y12] +
(-0.0008145313270957405+0j) [Y2 Z3 Z4 Z5 Y6 Z10] +
(2.7455184003115176e-06+0j) [Y2 Z3 Z4 Z5 Y6 X11 Z12 X13] +
(2.7455184003115176e-06+0j) [Y2 Z3 Z4 Z5 Y6 Y11 Z12 Y13] +
(0.014411099430130818+0j) [Y2 Z3 Z4 Z5 Y6 Z11] +
(0.0006650070219498333+0j) [Y2 Z3 Z4 Z5 Y6 Z12] +
(-0.0034937903598902063+0j) [Y2 Z3 Z4 Z5 Y6 Z13] +
(0.011756013419819304+0j) [Y2 Z3 Z4 Z5 Z6 X7 X8 Y9] +
(-0.015225630757226558+0j) [Y2 Z3 Z4 Z5 Z6 X7 X10 Y11] +
(3.088250711179117e-06+0j) [Y2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13] +
(-3.544395429171549e-06+0j) [Y2 Z3 Z4 Z5 Z6 X7 X11 Y12] +
(0.00415879738184004+0j) [Y2 Z3 Z4 Z5 Z6 X7 X12 Y13] +
(-0.011756013419819304+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X8 X9] +
(0.015225630757226558+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X10 X11] +
(-3.088250711179117e-06+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13] +
(-3.544395429171549e-06+0j) [Y2 Z3 Z4 Z5 Z6 Y7 Y11 Y12] +
(-0.00415879738184004+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X12 X13] +
(0.014603704729162097+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11] +
(-2.874299071254574e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(0.014603704729162097+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11] +
(-2.874299071254574e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(-0.2816425776702295+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-1.300294656101864e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13] +
(-1.300294656101864e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13] +
(-0.024282117354693045+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11] +
(-0.019538050311314756+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12] +
(-0.01709155315589884+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13] +
(-0.002446497155415913+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(0.002446497155415913+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(5.775950527045218e-05+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(2.883676575980342e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(5.146496327265053e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12] +
(3.84620167116319e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12] +
(-0.03935916802205306+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Y10] +
(7.979825793106215e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12] +
(-0.024755463292890967+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Y10] +
(5.105526721851641e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12] +
(-0.021433810721600825+0j) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Y10] +
(5.15935050178204e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12] +
(-0.029903789512624852+0j) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Y10] +
(5.4279886562782206e-06+0j) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.001663879878490749+0j) [Y2 Z3 Z4 Y6] +
(-0.018889030304942857+0j) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Y10] +
(2.947356011539224e-06+0j) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.003479511890334372+0j) [Y2 Z3 Z5 Y6] +
(-0.02873077955190549+0j) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Y10] +
(5.9358677177726295e-06+0j) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.6021167407515033e-06+0j) [Y2 Y4] +
(0.0004956762314916141+0j) [Y2 Z4 Z5 Y6] +
(-0.03560837898831254+0j) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(7.25327334787924e-06+0j) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.6538942226831717+0j) [Z2] +
(1.6021167407515033e-06+0j) [Z2 X3 Z4 X5] +
(0.0004956762314916141+0j) [Z2 X3 Z4 Z5 Z6 X7] +
(-0.03560837898831254+0j) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(7.25327334787924e-06+0j) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.6021167407515033e-06+0j) [Z2 Y3 Z4 Y5] +
(0.0004956762314916141+0j) [Z2 Y3 Z4 Z5 Z6 Y7] +
(-0.03560837898831254+0j) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(7.25327334787924e-06+0j) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.18189085790751347+0j) [Z2 Z3] +
(-9.509249751234378e-07+0j) [Z2 X4 Z5 X6] +
(-4.7288431470776664e-06+0j) [Z2 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0245918608838299+0j) [Z2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-9.509249751234378e-07+0j) [Z2 Y4 Z5 Y6] +
(-4.7288431470776664e-06+0j) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0245918608838299+0j) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.12495807739503206+0j) [Z2 Z4] +
(-1.170830136987066e-06+0j) [Z2 X5 Z6 X7] +
(-7.089799467382474e-06+0j) [Z2 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.03490334337366163+0j) [Z2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.170830136987066e-06+0j) [Z2 Y5 Z6 Y7] +
(-7.089799467382474e-06+0j) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.03490334337366163+0j) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.16079764534838553+0j) [Z2 Z5] +
(0.019020423173039917+0j) [Z2 X6 Z7 Z8 Z9 X10] +
(-2.103215604517678e-06+0j) [Z2 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.019020423173039917+0j) [Z2 Y6 Z7 Z8 Z9 Y10] +
(-2.103215604517678e-06+0j) [Z2 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.1373910476268321+0j) [Z2 Z6] +
(0.0243890825311494+0j) [Z2 X7 Z8 Z9 Z10 X11] +
(-2.011122097963758e-06+0j) [Z2 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0243890825311494+0j) [Z2 Y7 Z8 Z9 Z10 Y11] +
(-2.011122097963758e-06+0j) [Z2 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.16853486561579914+0j) [Z2 Z7] +
(0.15071408121008276+0j) [Z2 Z8] +
(0.1869082047691253+0j) [Z2 Z9] +
(-1.0632283422925685e-06+0j) [Z2 X10 Z11 X12] +
(-1.0632283422925685e-06+0j) [Z2 Y10 Z11 Y12] +
(0.12799502492468418+0j) [Z2 Z10] +
(1.1094407591731973e-06+0j) [Z2 X11 Z12 X13] +
(1.1094407591731973e-06+0j) [Z2 Y11 Z12 Y13] +
(0.15337968243314165+0j) [Z2 Z11] +
(0.1401128986535481+0j) [Z2 Z12] +
(0.15569010671752453+0j) [Z2 Z13] +
(0.005143391768825121+0j) [X3 X4 Y5 Y6] +
(0.009841749246962633+0j) [X3 X4 Y5 Z6 Z7 Z8 Z9 Y10] +
(-2.9885117062334056e-06+0j) [X3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.4548424490785627e-06+0j) [X3 X4 X6 X7] +
(-1.5224930675185264e-06+0j) [X3 X4 X6 Z7 Z8 Z9 Z10 X11] +
(-0.008541996625454868+0j) [X3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.1513463109759394e-06+0j) [X3 X4 Y7 Z8 Z9 Y10] +
(-0.019257505095251634+0j) [X3 X4 Y7 Z8 Z9 Z10 Z11 Y12] +
(-7.956895373088069e-07+0j) [X3 X4 X8 X9] +
(-4.6430510682789445e-06+0j) [X3 X4 X10 X11] +
(-0.008764827575688786+0j) [X3 X4 X10 Z11 Z12 X13] +
(-0.01902824244384728+0j) [X3 X4 Y11 Y12] +
(5.275883121923911e-06+0j) [X3 X4 X12 X13] +
(-0.005143391768825121+0j) [X3 Y4 Y5 X6] +
(-0.009841749246962633+0j) [X3 Y4 Y5 Z6 Z7 Z8 Z9 X10] +
(2.9885117062334056e-06+0j) [X3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.4548424490785627e-06+0j) [X3 Y4 Y6 X7] +
(-1.5224930675185264e-06+0j) [X3 Y4 Y6 Z7 Z8 Z9 Z10 X11] +
(-0.008541996625454868+0j) [X3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(3.1513463109759394e-06+0j) [X3 Y4 Y7 Z8 Z9 X10] +
(0.019257505095251634+0j) [X3 Y4 Y7 Z8 Z9 Z10 Z11 X12] +
(-7.956895373088069e-07+0j) [X3 Y4 Y8 X9] +
(-4.6430510682789445e-06+0j) [X3 Y4 Y10 X11] +
(-0.008764827575688786+0j) [X3 Y4 Y10 Z11 Z12 X13] +
(0.01902824244384728+0j) [X3 Y4 Y11 X12] +
(5.275883121923911e-06+0j) [X3 Y4 Y12 X13] +
(-3.887051674060871e-06+0j) [X3 Z4 X5] +
(3.211842018916505e-06+0j) [X3 Z4 X5 X6 Z7 Z8 Z9 X10] +
(0.019299560579363842+0j) [X3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(3.211842018916505e-06+0j) [X3 Z4 X5 Y6 Z7 Z8 Z9 Y10] +
(0.019299560579363842+0j) [X3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.1954890099743e-06+0j) [X3 Z4 X5 Z6] +
(1.689348951397978e-06+0j) [X3 Z4 X5 X7 Z8 Z9 Z10 X11] +
(0.010757563953908969+0j) [X3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.5371780954305395e-08+0j) [X3 Z4 X5 Y7 Z8 Z9 Z10 Y11] +
(4.2055484112204795e-05+0j) [X3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(2.5935343910426286e-07+0j) [X3 Z4 X5 Z7] +
(-5.770052995564484e-07+0j) [X3 Z4 X5 Z8] +
(2.1868423775235842e-07+0j) [X3 Z4 X5 Z9] +
(0.024353077678068973+0j) [X3 Z4 X5 X10 Z11 X12] +
(0.024353077678068973+0j) [X3 Z4 X5 Y10 Z11 Y12] +
(-7.801707500142726e-06+0j) [X3 Z4 X5 Z10] +
(0.015588250102380189+0j) [X3 Z4 X5 X11 Z12 X13] +
(0.005324835234221696+0j) [X3 Z4 X5 Y11 Z12 Y13] +
(-3.158656431863782e-06+0j) [X3 Z4 X5 Z11] +
(8.814937306165704e-06+0j) [X3 Z4 X5 Z12] +
(3.5390541842417923e-06+0j) [X3 Z4 X5 Z13] +
(1.6288532434574125e-06+0j) [X3 Z4 Y5 Y7 Z8 Z9 Z10 X11] +
(0.010715508469796764+0j) [X3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.010263414868158495+0j) [X3 Z4 Y5 Y11 Z12 X13] +
(0.008469978791024027+0j) [X3 Z4 Z5 X6 Y7 Z8 Z9 Y10] +
(-2.686381544961821e-07+0j) [X3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.011756013419819302+0j) [X3 Z4 Z5 X6 X8 X9] +
(0.015225630757226558+0j) [X3 Z4 Z5 X6 X10 X11] +
(-3.544395429171549e-06+0j) [X3 Z4 Z5 X6 X10 Z11 Z12 X13] +
(-3.088250711179117e-06+0j) [X3 Z4 Z5 X6 Y11 Y12] +
(-0.00415879738184004+0j) [X3 Z4 Z5 X6 X12 X13] +
(-0.008469978791024027+0j) [X3 Z4 Z5 Y6 Y7 Z8 Z9 X10] +
(2.686381544961821e-07+0j) [X3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12] +
(-0.011756013419819302+0j) [X3 Z4 Z5 Y6 Y8 X9] +
(0.015225630757226558+0j) [X3 Z4 Z5 Y6 Y10 X11] +
(-3.544395429171549e-06+0j) [X3 Z4 Z5 Y6 Y10 Z11 Z12 X13] +
(3.088250711179117e-06+0j) [X3 Z4 Z5 Y6 Y11 X12] +
(-0.00415879738184004+0j) [X3 Z4 Z5 Y6 Y12 X13] +
(-0.12133276911042469+0j) [X3 Z4 Z5 Z6 X7] +
(-0.01756120240964626+0j) [X3 Z4 Z5 Z6 X7 Z8] +
(-0.005805188989826954+0j) [X3 Z4 Z5 Z6 X7 Z9] +
(2.7455184003115176e-06+0j) [X3 Z4 Z5 Z6 X7 X10 Z11 X12] +
(2.7455184003115176e-06+0j) [X3 Z4 Z5 Z6 X7 Y10 Z11 Y12] +
(0.014411099430130818+0j) [X3 Z4 Z5 Z6 X7 Z10] +
(-7.988770288600311e-07+0j) [X3 Z4 Z5 Z6 X7 X11 Z12 X13] +
(-3.4273231086759956e-07+0j) [X3 Z4 Z5 Z6 X7 Y11 Z12 Y13] +
(-0.0008145313270957405+0j) [X3 Z4 Z5 Z6 X7 Z11] +
(-0.0034937903598902063+0j) [X3 Z4 Z5 Z6 X7 Z12] +
(0.0006650070219498333+0j) [X3 Z4 Z5 Z6 X7 Z13] +
(-4.5614471799243157e-07+0j) [X3 Z4 Z5 Z6 Y7 Y11 Z12 X13] +
(-0.014603704729162094+0j) [X3 Z4 Z5 Z6 Z7 X8 Y9 Y10] +
(2.874299071254574e-06+0j) [X3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12] +
(0.014603704729162094+0j) [X3 Z4 Z5 Z6 Z7 Y8 Y9 X10] +
(-2.874299071254574e-06+0j) [X3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12] +
(1.300294656101864e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Y12] +
(0.002446497155415914+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13] +
(-1.300294656101864e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 X12] +
(0.002446497155415914+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13] +
(-0.2816425776702294+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.01709155315589884+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12] +
(-0.019538050311314756+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13] +
(5.775950527045216e-05+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(2.8836765759803414e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13] +
(3.84620167116319e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13] +
(-0.024282117354693045+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X11] +
(5.146496327265053e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13] +
(-0.024755463292890967+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z10 X11] +
(5.105526721851641e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13] +
(-0.03935916802205306+0j) [X3 Z4 Z5 Z6 Z7 Z9 Z10 X11] +
(7.979825793106215e-06+0j) [X3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13] +
(-0.029903789512624852+0j) [X3 Z4 Z5 Z6 Z8 Z9 Z10 X11] +
(5.4279886562782206e-06+0j) [X3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.025996177598021277+0j) [X3 Z4 Z5 X7] +
(-0.021433810721600825+0j) [X3 Z4 Z5 Z7 Z8 Z9 Z10 X11] +
(5.15935050178204e-06+0j) [X3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.003479511890334372+0j) [X3 Z4 Z6 X7] +
(-0.02873077955190549+0j) [X3 Z4 Z6 Z7 Z8 Z9 Z10 X11] +
(5.9358677177726295e-06+0j) [X3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-7.764994120952451e-07+0j) [X3 X5] +
(0.001663879878490749+0j) [X3 Z5 Z6 X7] +
(-0.018889030304942857+0j) [X3 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(2.947356011539224e-06+0j) [X3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.005143391768825121+0j) [Y3 X4 X5 Y6] +
(-0.009841749246962633+0j) [Y3 X4 X5 Z6 Z7 Z8 Z9 Y10] +
(2.9885117062334056e-06+0j) [Y3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.4548424490785627e-06+0j) [Y3 X4 X6 Y7] +
(-1.5224930675185264e-06+0j) [Y3 X4 X6 Z7 Z8 Z9 Z10 Y11] +
(-0.008541996625454868+0j) [Y3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(3.1513463109759394e-06+0j) [Y3 X4 X7 Z8 Z9 Y10] +
(0.019257505095251634+0j) [Y3 X4 X7 Z8 Z9 Z10 Z11 Y12] +
(-7.956895373088069e-07+0j) [Y3 X4 X8 Y9] +
(-4.6430510682789445e-06+0j) [Y3 X4 X10 Y11] +
(-0.008764827575688786+0j) [Y3 X4 X10 Z11 Z12 Y13] +
(0.01902824244384728+0j) [Y3 X4 X11 Y12] +
(5.275883121923911e-06+0j) [Y3 X4 X12 Y13] +
(0.005143391768825121+0j) [Y3 Y4 X5 X6] +
(0.009841749246962633+0j) [Y3 Y4 X5 Z6 Z7 Z8 Z9 X10] +
(-2.9885117062334056e-06+0j) [Y3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.4548424490785627e-06+0j) [Y3 Y4 Y6 Y7] +
(-1.5224930675185264e-06+0j) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Y11] +
(-0.008541996625454868+0j) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-3.1513463109759394e-06+0j) [Y3 Y4 X7 Z8 Z9 X10] +
(-0.019257505095251634+0j) [Y3 Y4 X7 Z8 Z9 Z10 Z11 X12] +
(-7.956895373088069e-07+0j) [Y3 Y4 Y8 Y9] +
(-4.6430510682789445e-06+0j) [Y3 Y4 Y10 Y11] +
(-0.008764827575688786+0j) [Y3 Y4 Y10 Z11 Z12 Y13] +
(-0.01902824244384728+0j) [Y3 Y4 X11 X12] +
(5.275883121923911e-06+0j) [Y3 Y4 Y12 Y13] +
(1.6288532434574125e-06+0j) [Y3 Z4 X5 X7 Z8 Z9 Z10 Y11] +
(0.010715508469796764+0j) [Y3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.010263414868158495+0j) [Y3 Z4 X5 X11 Z12 Y13] +
(-3.887051674060871e-06+0j) [Y3 Z4 Y5] +
(3.211842018916505e-06+0j) [Y3 Z4 Y5 X6 Z7 Z8 Z9 X10] +
(0.019299560579363842+0j) [Y3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(3.211842018916505e-06+0j) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Y10] +
(0.019299560579363842+0j) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.1954890099743e-06+0j) [Y3 Z4 Y5 Z6] +
(4.5371780954305395e-08+0j) [Y3 Z4 Y5 X7 Z8 Z9 Z10 X11] +
(4.2055484112204795e-05+0j) [Y3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.689348951397978e-06+0j) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Y11] +
(0.010757563953908969+0j) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(2.5935343910426286e-07+0j) [Y3 Z4 Y5 Z7] +
(-5.770052995564484e-07+0j) [Y3 Z4 Y5 Z8] +
(2.1868423775235842e-07+0j) [Y3 Z4 Y5 Z9] +
(0.024353077678068973+0j) [Y3 Z4 Y5 X10 Z11 X12] +
(0.024353077678068973+0j) [Y3 Z4 Y5 Y10 Z11 Y12] +
(-7.801707500142726e-06+0j) [Y3 Z4 Y5 Z10] +
(0.005324835234221696+0j) [Y3 Z4 Y5 X11 Z12 X13] +
(0.015588250102380189+0j) [Y3 Z4 Y5 Y11 Z12 Y13] +
(-3.158656431863782e-06+0j) [Y3 Z4 Y5 Z11] +
(8.814937306165704e-06+0j) [Y3 Z4 Y5 Z12] +
(3.5390541842417923e-06+0j) [Y3 Z4 Y5 Z13] +
(-0.008469978791024027+0j) [Y3 Z4 Z5 X6 X7 Z8 Z9 Y10] +
(2.686381544961821e-07+0j) [Y3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12] +
(-0.011756013419819302+0j) [Y3 Z4 Z5 X6 X8 Y9] +
(0.015225630757226558+0j) [Y3 Z4 Z5 X6 X10 Y11] +
(-3.544395429171549e-06+0j) [Y3 Z4 Z5 X6 X10 Z11 Z12 Y13] +
(3.088250711179117e-06+0j) [Y3 Z4 Z5 X6 X11 Y12] +
(-0.00415879738184004+0j) [Y3 Z4 Z5 X6 X12 Y13] +
(0.008469978791024027+0j) [Y3 Z4 Z5 Y6 X7 Z8 Z9 X10] +
(-2.686381544961821e-07+0j) [Y3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12] +
(-0.011756013419819302+0j) [Y3 Z4 Z5 Y6 Y8 Y9] +
(0.015225630757226558+0j) [Y3 Z4 Z5 Y6 Y10 Y11] +
(-3.544395429171549e-06+0j) [Y3 Z4 Z5 Y6 Y10 Z11 Z12 Y13] +
(-3.088250711179117e-06+0j) [Y3 Z4 Z5 Y6 X11 X12] +
(-0.00415879738184004+0j) [Y3 Z4 Z5 Y6 Y12 Y13] +
(-4.5614471799243157e-07+0j) [Y3 Z4 Z5 Z6 X7 X11 Z12 Y13] +
(-0.12133276911042469+0j) [Y3 Z4 Z5 Z6 Y7] +
(-0.01756120240964626+0j) [Y3 Z4 Z5 Z6 Y7 Z8] +
(-0.005805188989826954+0j) [Y3 Z4 Z5 Z6 Y7 Z9] +
(2.7455184003115176e-06+0j) [Y3 Z4 Z5 Z6 Y7 X10 Z11 X12] +
(2.7455184003115176e-06+0j) [Y3 Z4 Z5 Z6 Y7 Y10 Z11 Y12] +
(0.014411099430130818+0j) [Y3 Z4 Z5 Z6 Y7 Z10] +
(-3.4273231086759956e-07+0j) [Y3 Z4 Z5 Z6 Y7 X11 Z12 X13] +
(-7.988770288600311e-07+0j) [Y3 Z4 Z5 Z6 Y7 Y11 Z12 Y13] +
(-0.0008145313270957405+0j) [Y3 Z4 Z5 Z6 Y7 Z11] +
(-0.0034937903598902063+0j) [Y3 Z4 Z5 Z6 Y7 Z12] +
(0.0006650070219498333+0j) [Y3 Z4 Z5 Z6 Y7 Z13] +
(0.014603704729162094+0j) [Y3 Z4 Z5 Z6 Z7 X8 X9 Y10] +
(-2.874299071254574e-06+0j) [Y3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12] +
(-0.014603704729162094+0j) [Y3 Z4 Z5 Z6 Z7 Y8 X9 X10] +
(2.874299071254574e-06+0j) [Y3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12] +
(-1.300294656101864e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Y12] +
(0.002446497155415914+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13] +
(1.300294656101864e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 X12] +
(0.002446497155415914+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13] +
(-0.2816425776702294+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.01709155315589884+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12] +
(-0.019538050311314756+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13] +
(5.775950527045216e-05+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(2.8836765759803414e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13] +
(3.84620167116319e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13] +
(-0.024282117354693045+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y11] +
(5.146496327265053e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13] +
(-0.024755463292890967+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Y11] +
(5.105526721851641e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13] +
(-0.03935916802205306+0j) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Y11] +
(7.979825793106215e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13] +
(-0.029903789512624852+0j) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Y11] +
(5.4279886562782206e-06+0j) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.025996177598021277+0j) [Y3 Z4 Z5 Y7] +
(-0.021433810721600825+0j) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Y11] +
(5.15935050178204e-06+0j) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.003479511890334372+0j) [Y3 Z4 Z6 Y7] +
(-0.02873077955190549+0j) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Y11] +
(5.9358677177726295e-06+0j) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.764994120952451e-07+0j) [Y3 Y5] +
(0.001663879878490749+0j) [Y3 Z5 Z6 Y7] +
(-0.018889030304942857+0j) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(2.947356011539224e-06+0j) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.6538942226831719+0j) [Z3] +
(-1.170830136987066e-06+0j) [Z3 X4 Z5 X6] +
(-7.089799467382474e-06+0j) [Z3 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.03490334337366163+0j) [Z3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.170830136987066e-06+0j) [Z3 Y4 Z5 Y6] +
(-7.089799467382474e-06+0j) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.03490334337366163+0j) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.16079764534838553+0j) [Z3 Z4] +
(-9.509249751234378e-07+0j) [Z3 X5 Z6 X7] +
(-4.7288431470776664e-06+0j) [Z3 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0245918608838299+0j) [Z3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-9.509249751234378e-07+0j) [Z3 Y5 Z6 Y7] +
(-4.7288431470776664e-06+0j) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0245918608838299+0j) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.12495807739503206+0j) [Z3 Z5] +
(0.0243890825311494+0j) [Z3 X6 Z7 Z8 Z9 X10] +
(-2.011122097963758e-06+0j) [Z3 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0243890825311494+0j) [Z3 Y6 Z7 Z8 Z9 Y10] +
(-2.011122097963758e-06+0j) [Z3 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.16853486561579914+0j) [Z3 Z6] +
(0.019020423173039917+0j) [Z3 X7 Z8 Z9 Z10 X11] +
(-2.103215604517678e-06+0j) [Z3 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.019020423173039917+0j) [Z3 Y7 Z8 Z9 Z10 Y11] +
(-2.103215604517678e-06+0j) [Z3 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.1373910476268321+0j) [Z3 Z7] +
(0.1869082047691253+0j) [Z3 Z8] +
(0.15071408121008276+0j) [Z3 Z9] +
(1.1094407591731973e-06+0j) [Z3 X10 Z11 X12] +
(1.1094407591731973e-06+0j) [Z3 Y10 Z11 Y12] +
(0.15337968243314165+0j) [Z3 Z10] +
(-1.0632283422925685e-06+0j) [Z3 X11 Z12 X13] +
(-1.0632283422925685e-06+0j) [Z3 Y11 Z12 Y13] +
(0.12799502492468418+0j) [Z3 Z11] +
(0.15569010671752453+0j) [Z3 Z12] +
(0.1401128986535481+0j) [Z3 Z13] +
(-0.011982389010247965+0j) [X4 X5 Y6 Y7] +
(-0.0073067599288329805+0j) [X4 X5 Y6 Z7 Z8 Z9 Z10 Y11] +
(-2.888293596663979e-07+0j) [X4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0073067599288329805+0j) [X4 X5 X7 Z8 Z9 X10] +
(-2.888293596663979e-07+0j) [X4 X5 X7 Z8 Z9 Z10 Z11 X12] +
(-0.007156934919856932+0j) [X4 X5 Y8 Y9] +
(-0.017680067952481514+0j) [X4 X5 Y10 Y11] +
(-3.6945132944478417e-06+0j) [X4 X5 Y10 Z11 Z12 Y13] +
(-3.6945132944478412e-06+0j) [X4 X5 X11 X12] +
(-0.03831467029480385+0j) [X4 X5 Y12 Y13] +
(0.011982389010247965+0j) [X4 Y5 Y6 X7] +
(0.0073067599288329805+0j) [X4 Y5 Y6 Z7 Z8 Z9 Z10 X11] +
(2.888293596663979e-07+0j) [X4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0073067599288329805+0j) [X4 Y5 Y7 Z8 Z9 X10] +
(-2.888293596663979e-07+0j) [X4 Y5 Y7 Z8 Z9 Z10 Z11 X12] +
(0.007156934919856932+0j) [X4 Y5 Y8 X9] +
(0.017680067952481514+0j) [X4 Y5 Y10 X11] +
(3.6945132944478417e-06+0j) [X4 Y5 Y10 Z11 Z12 X13] +
(-3.6945132944478412e-06+0j) [X4 Y5 Y11 X12] +
(0.03831467029480385+0j) [X4 Y5 Y12 X13] +
(-1.226048498862685e-05+0j) [X4 Z5 X6] +
(-1.2283337824864386e-06+0j) [X4 Z5 X6 X7 Z8 Z9 Z10 X11] +
(0.0002463643756957808+0j) [X4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2283337824864386e-06+0j) [X4 Z5 X6 Y7 Z8 Z9 Z10 Y11] +
(0.0002463643756957808+0j) [X4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.854060857961665e-06+0j) [X4 Z5 X6 Z7] +
(-1.3980449080718772e-06+0j) [X4 Z5 X6 Z8] +
(-1.8818501831812504e-06+0j) [X4 Z5 X6 Z9] +
(0.007960880725921576+0j) [X4 Z5 X6 X10 Z11 X12] +
(-0.00092985079677302+0j) [X4 Z5 X6 Y10 Z11 Y12] +
(-1.6923978284805413e-06+0j) [X4 Z5 X6 Z10] +
(-0.012215040997613943+0j) [X4 Z5 X6 X11 Z12 X13] +
(-0.012215040997613943+0j) [X4 Z5 X6 Y11 Z12 Y13] +
(4.28191388472345e-06+0j) [X4 Z5 X6 Z11] +
(-4.5888551554080525e-06+0j) [X4 Z5 X6 Z13] +
(0.008890731522694598+0j) [X4 Z5 Y6 Y10 Z11 X12] +
(-4.838052751093733e-07+0j) [X4 Z5 Z6 X7 Y8 Y9] +
(5.974311713203992e-06+0j) [X4 Z5 Z6 X7 Y10 Y11] +
(0.011285190200840924+0j) [X4 Z5 Z6 X7 Y10 Z11 Z12 Y13] +
(0.020175921723535526+0j) [X4 Z5 Z6 X7 X11 X12] +
(-4.556569217877665e-06+0j) [X4 Z5 Z6 X7 Y12 Y13] +
(4.838052751093733e-07+0j) [X4 Z5 Z6 Y7 Y8 X9] +
(-5.974311713203992e-06+0j) [X4 Z5 Z6 Y7 Y10 X11] +
(-0.011285190200840924+0j) [X4 Z5 Z6 Y7 Y10 Z11 Z12 X13] +
(0.020175921723535526+0j) [X4 Z5 Z6 Y7 Y11 X12] +
(4.556569217877665e-06+0j) [X4 Z5 Z6 Y7 Y12 X13] +
(1.3304731886557553e-06+0j) [X4 Z5 Z6 Z7 X8 X9 Z10 X11] +
(0.005923798336561341+0j) [X4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(1.3304731886557553e-06+0j) [X4 Z5 Z6 Z7 X8 Y9 Z10 Y11] +
(0.005923798336561341+0j) [X4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(-6.631277928206737e-05+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.016024603689179504+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13] +
(-0.016024603689179504+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13] +
(3.3343312891723575e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z11] +
(-4.734622038553502e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z12] +
(-9.806102774699615e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z13] +
(-5.071480736146113e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(5.071480736146113e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(-0.36937089366156145+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.023145130929529002+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(-0.00961263460684733+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X12] +
(-0.025637238296026835+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z11 X12] +
(-8.774817864304719e-06+0j) [X4 Z5 Z6 Z7 Z8 X10] +
(-0.04764261217638301+0j) [X4 Z5 Z6 Z7 Z8 Z10 Z11 X12] +
(-7.444344675648964e-06+0j) [X4 Z5 Z6 Z7 Z9 X10] +
(-0.04171881383982167+0j) [X4 Z5 Z6 Z7 Z9 Z10 Z11 X12] +
(-6.290028432954373e-06+0j) [X4 Z5 Z6 Z8 Z9 X10] +
(-0.03956441632289326+0j) [X4 Z5 Z6 Z8 Z9 Z10 Z11 X12] +
(-7.518362215440813e-06+0j) [X4 Z5 Z7 Z8 Z9 X10] +
(-0.03931805194719748+0j) [X4 Z5 Z7 Z8 Z9 Z10 Z11 X12] +
(-5.929765814637604e-07+0j) [X4 X6] +
(-4.253224225342125e-06+0j) [X4 Z6 Z7 Z8 Z9 X10] +
(-0.022528440196012883+0j) [X4 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.011982389010247965+0j) [Y4 X5 X6 Y7] +
(0.0073067599288329805+0j) [Y4 X5 X6 Z7 Z8 Z9 Z10 Y11] +
(2.888293596663979e-07+0j) [Y4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0073067599288329805+0j) [Y4 X5 X7 Z8 Z9 Y10] +
(-2.888293596663979e-07+0j) [Y4 X5 X7 Z8 Z9 Z10 Z11 Y12] +
(0.007156934919856932+0j) [Y4 X5 X8 Y9] +
(0.017680067952481514+0j) [Y4 X5 X10 Y11] +
(3.6945132944478417e-06+0j) [Y4 X5 X10 Z11 Z12 Y13] +
(-3.6945132944478412e-06+0j) [Y4 X5 X11 Y12] +
(0.03831467029480385+0j) [Y4 X5 X12 Y13] +
(-0.011982389010247965+0j) [Y4 Y5 X6 X7] +
(-0.0073067599288329805+0j) [Y4 Y5 X6 Z7 Z8 Z9 Z10 X11] +
(-2.888293596663979e-07+0j) [Y4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0073067599288329805+0j) [Y4 Y5 Y7 Z8 Z9 Y10] +
(-2.888293596663979e-07+0j) [Y4 Y5 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.007156934919856932+0j) [Y4 Y5 X8 X9] +
(-0.017680067952481514+0j) [Y4 Y5 X10 X11] +
(-3.6945132944478417e-06+0j) [Y4 Y5 X10 Z11 Z12 X13] +
(-3.6945132944478412e-06+0j) [Y4 Y5 Y11 Y12] +
(-0.03831467029480385+0j) [Y4 Y5 X12 X13] +
(0.008890731522694598+0j) [Y4 Z5 X6 X10 Z11 Y12] +
(-1.226048498862685e-05+0j) [Y4 Z5 Y6] +
(-1.2283337824864386e-06+0j) [Y4 Z5 Y6 X7 Z8 Z9 Z10 X11] +
(0.0002463643756957808+0j) [Y4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2283337824864386e-06+0j) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Y11] +
(0.0002463643756957808+0j) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.854060857961665e-06+0j) [Y4 Z5 Y6 Z7] +
(-1.3980449080718772e-06+0j) [Y4 Z5 Y6 Z8] +
(-1.8818501831812504e-06+0j) [Y4 Z5 Y6 Z9] +
(-0.00092985079677302+0j) [Y4 Z5 Y6 X10 Z11 X12] +
(0.007960880725921576+0j) [Y4 Z5 Y6 Y10 Z11 Y12] +
(-1.6923978284805413e-06+0j) [Y4 Z5 Y6 Z10] +
(-0.012215040997613943+0j) [Y4 Z5 Y6 X11 Z12 X13] +
(-0.012215040997613943+0j) [Y4 Z5 Y6 Y11 Z12 Y13] +
(4.28191388472345e-06+0j) [Y4 Z5 Y6 Z11] +
(-4.5888551554080525e-06+0j) [Y4 Z5 Y6 Z13] +
(4.838052751093733e-07+0j) [Y4 Z5 Z6 X7 X8 Y9] +
(-5.974311713203992e-06+0j) [Y4 Z5 Z6 X7 X10 Y11] +
(-0.011285190200840924+0j) [Y4 Z5 Z6 X7 X10 Z11 Z12 Y13] +
(0.020175921723535526+0j) [Y4 Z5 Z6 X7 X11 Y12] +
(4.556569217877665e-06+0j) [Y4 Z5 Z6 X7 X12 Y13] +
(-4.838052751093733e-07+0j) [Y4 Z5 Z6 Y7 X8 X9] +
(5.974311713203992e-06+0j) [Y4 Z5 Z6 Y7 X10 X11] +
(0.011285190200840924+0j) [Y4 Z5 Z6 Y7 X10 Z11 Z12 X13] +
(0.020175921723535526+0j) [Y4 Z5 Z6 Y7 Y11 Y12] +
(-4.556569217877665e-06+0j) [Y4 Z5 Z6 Y7 X12 X13] +
(1.3304731886557553e-06+0j) [Y4 Z5 Z6 Z7 Y8 X9 Z10 X11] +
(0.005923798336561341+0j) [Y4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(1.3304731886557553e-06+0j) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Y11] +
(0.005923798336561341+0j) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(-6.631277928206737e-05+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.016024603689179504+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13] +
(-0.016024603689179504+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13] +
(3.3343312891723575e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z11] +
(-4.734622038553502e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z12] +
(-9.806102774699615e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z13] +
(5.071480736146113e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(-5.071480736146113e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(-0.36937089366156145+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.023145130929529002+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(-0.00961263460684733+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y12] +
(-0.025637238296026835+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z11 Y12] +
(-8.774817864304719e-06+0j) [Y4 Z5 Z6 Z7 Z8 Y10] +
(-0.04764261217638301+0j) [Y4 Z5 Z6 Z7 Z8 Z10 Z11 Y12] +
(-7.444344675648964e-06+0j) [Y4 Z5 Z6 Z7 Z9 Y10] +
(-0.04171881383982167+0j) [Y4 Z5 Z6 Z7 Z9 Z10 Z11 Y12] +
(-6.290028432954373e-06+0j) [Y4 Z5 Z6 Z8 Z9 Y10] +
(-0.03956441632289326+0j) [Y4 Z5 Z6 Z8 Z9 Z10 Z11 Y12] +
(-7.518362215440813e-06+0j) [Y4 Z5 Z7 Z8 Z9 Y10] +
(-0.03931805194719748+0j) [Y4 Z5 Z7 Z8 Z9 Z10 Z11 Y12] +
(-5.929765814637604e-07+0j) [Y4 Y6] +
(-4.253224225342125e-06+0j) [Y4 Z6 Z7 Z8 Z9 Y10] +
(-0.022528440196012883+0j) [Y4 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-5.929765814637604e-07+0j) [Z4 X5 Z6 X7] +
(-4.253224225342125e-06+0j) [Z4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.022528440196012883+0j) [Z4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-5.929765814637604e-07+0j) [Z4 Y5 Z6 Y7] +
(-4.253224225342125e-06+0j) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.022528440196012883+0j) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.15755314797985662+0j) [Z4 Z5] +
(0.018266834869375487+0j) [Z4 X6 Z7 Z8 Z9 X10] +
(-1.654117477047395e-06+0j) [Z4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.018266834869375487+0j) [Z4 Y6 Z7 Z8 Z9 Y10] +
(-1.654117477047395e-06+0j) [Z4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.13701191674040736+0j) [Z4 Z6] +
(0.010960074940542505+0j) [Z4 X7 Z8 Z9 Z10 X11] +
(-1.942946836713793e-06+0j) [Z4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.010960074940542505+0j) [Z4 Y7 Z8 Z9 Z10 Y11] +
(-1.942946836713793e-06+0j) [Z4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.14899430575065534+0j) [Z4 Z7] +
(1.8782101245023854e-06+0j) [Z4 X10 Z11 X12] +
(1.8782101245023854e-06+0j) [Z4 Y10 Z11 Y12] +
(0.12489990917237609+0j) [Z4 Z10] +
(-1.8163031699454557e-06+0j) [Z4 X11 Z12 X13] +
(-1.8163031699454557e-06+0j) [Z4 Y11 Z12 Y13] +
(1.2283337824864386e-06+0j) [X5 X6 Y7 Z8 Z9 Y10] +
(-0.0002463643756957808+0j) [X5 X6 Y7 Z8 Z9 Z10 Z11 Y12] +
(-4.838052751093733e-07+0j) [X5 X6 X8 X9] +
(5.974311713203993e-06+0j) [X5 X6 X10 X11] +
(0.020175921723535526+0j) [X5 X6 X10 Z11 Z12 X13] +
(0.011285190200840924+0j) [X5 X6 Y11 Y12] +
(-4.556569217877664e-06+0j) [X5 X6 X12 X13] +
(-1.2283337824864386e-06+0j) [X5 Y6 Y7 Z8 Z9 X10] +
(0.0002463643756957808+0j) [X5 Y6 Y7 Z8 Z9 Z10 Z11 X12] +
(-4.838052751093733e-07+0j) [X5 Y6 Y8 X9] +
(5.974311713203993e-06+0j) [X5 Y6 Y10 X11] +
(0.020175921723535526+0j) [X5 Y6 Y10 Z11 Z12 X13] +
(-0.011285190200840924+0j) [X5 Y6 Y11 X12] +
(-4.556569217877664e-06+0j) [X5 Y6 Y12 X13] +
(-1.2260484988626848e-05+0j) [X5 Z6 X7] +
(-1.8818501831812504e-06+0j) [X5 Z6 X7 Z8] +
(-1.3980449080718772e-06+0j) [X5 Z6 X7 Z9] +
(-0.012215040997613943+0j) [X5 Z6 X7 X10 Z11 X12] +
(-0.012215040997613943+0j) [X5 Z6 X7 Y10 Z11 Y12] +
(4.28191388472345e-06+0j) [X5 Z6 X7 Z10] +
(0.007960880725921576+0j) [X5 Z6 X7 X11 Z12 X13] +
(-0.00092985079677302+0j) [X5 Z6 X7 Y11 Z12 Y13] +
(-1.6923978284805413e-06+0j) [X5 Z6 X7 Z11] +
(-4.5888551554080525e-06+0j) [X5 Z6 X7 Z12] +
(0.008890731522694598+0j) [X5 Z6 Y7 Y11 Z12 X13] +
(-1.3304731886557553e-06+0j) [X5 Z6 Z7 X8 Y9 Y10] +
(-0.005923798336561341+0j) [X5 Z6 Z7 X8 Y9 Z10 Z11 Y12] +
(1.3304731886557553e-06+0j) [X5 Z6 Z7 Y8 Y9 X10] +
(0.005923798336561341+0j) [X5 Z6 Z7 Y8 Y9 Z10 Z11 X12] +
(0.016024603689179504+0j) [X5 Z6 Z7 Z8 Z9 X10 Y11 Y12] +
(-5.071480736146114e-06+0j) [X5 Z6 Z7 Z8 Z9 X10 X12 X13] +
(-0.016024603689179504+0j) [X5 Z6 Z7 Z8 Z9 Y10 Y11 X12] +
(-5.071480736146114e-06+0j) [X5 Z6 Z7 Z8 Z9 Y10 Y12 X13] +
(-6.631277928206738e-05+0j) [X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-9.806102774699615e-06+0j) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z12] +
(-4.734622038553502e-06+0j) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z13] +
(-0.36937089366156145+0j) [X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.023145130929529002+0j) [X5 Z6 Z7 Z8 Z9 Z10 Z11 X13] +
(-0.025637238296026835+0j) [X5 Z6 Z7 Z8 Z9 Z10 Z12 X13] +
(3.3343312891723575e-06+0j) [X5 Z6 Z7 Z8 Z9 X11] +
(-0.00961263460684733+0j) [X5 Z6 Z7 Z8 Z9 Z11 Z12 X13] +
(-7.444344675648964e-06+0j) [X5 Z6 Z7 Z8 Z10 X11] +
(-0.04171881383982167+0j) [X5 Z6 Z7 Z8 Z10 Z11 Z12 X13] +
(-8.774817864304719e-06+0j) [X5 Z6 Z7 Z9 Z10 X11] +
(-0.04764261217638301+0j) [X5 Z6 Z7 Z9 Z10 Z11 Z12 X13] +
(-7.518362215440813e-06+0j) [X5 Z6 Z8 Z9 Z10 X11] +
(-0.03931805194719748+0j) [X5 Z6 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.854060857961665e-06+0j) [X5 X7] +
(-6.290028432954373e-06+0j) [X5 Z7 Z8 Z9 Z10 X11] +
(-0.03956441632289326+0j) [X5 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2283337824864386e-06+0j) [Y5 X6 X7 Z8 Z9 Y10] +
(0.0002463643756957808+0j) [Y5 X6 X7 Z8 Z9 Z10 Z11 Y12] +
(-4.838052751093733e-07+0j) [Y5 X6 X8 Y9] +
(5.974311713203993e-06+0j) [Y5 X6 X10 Y11] +
(0.020175921723535526+0j) [Y5 X6 X10 Z11 Z12 Y13] +
(-0.011285190200840924+0j) [Y5 X6 X11 Y12] +
(-4.556569217877664e-06+0j) [Y5 X6 X12 Y13] +
(1.2283337824864386e-06+0j) [Y5 Y6 X7 Z8 Z9 X10] +
(-0.0002463643756957808+0j) [Y5 Y6 X7 Z8 Z9 Z10 Z11 X12] +
(-4.838052751093733e-07+0j) [Y5 Y6 Y8 Y9] +
(5.974311713203993e-06+0j) [Y5 Y6 Y10 Y11] +
(0.020175921723535526+0j) [Y5 Y6 Y10 Z11 Z12 Y13] +
(0.011285190200840924+0j) [Y5 Y6 X11 X12] +
(-4.556569217877664e-06+0j) [Y5 Y6 Y12 Y13] +
(0.008890731522694598+0j) [Y5 Z6 X7 X11 Z12 Y13] +
(-1.2260484988626848e-05+0j) [Y5 Z6 Y7] +
(-1.8818501831812504e-06+0j) [Y5 Z6 Y7 Z8] +
(-1.3980449080718772e-06+0j) [Y5 Z6 Y7 Z9] +
(-0.012215040997613943+0j) [Y5 Z6 Y7 X10 Z11 X12] +
(-0.012215040997613943+0j) [Y5 Z6 Y7 Y10 Z11 Y12] +
(4.28191388472345e-06+0j) [Y5 Z6 Y7 Z10] +
(-0.00092985079677302+0j) [Y5 Z6 Y7 X11 Z12 X13] +
(0.007960880725921576+0j) [Y5 Z6 Y7 Y11 Z12 Y13] +
(-1.6923978284805413e-06+0j) [Y5 Z6 Y7 Z11] +
(-4.5888551554080525e-06+0j) [Y5 Z6 Y7 Z12] +
(1.3304731886557553e-06+0j) [Y5 Z6 Z7 X8 X9 Y10] +
(0.005923798336561341+0j) [Y5 Z6 Z7 X8 X9 Z10 Z11 Y12] +
(-1.3304731886557553e-06+0j) [Y5 Z6 Z7 Y8 X9 X10] +
(-0.005923798336561341+0j) [Y5 Z6 Z7 Y8 X9 Z10 Z11 X12] +
(-0.016024603689179504+0j) [Y5 Z6 Z7 Z8 Z9 X10 X11 Y12] +
(-5.071480736146114e-06+0j) [Y5 Z6 Z7 Z8 Z9 X10 X12 Y13] +
(0.016024603689179504+0j) [Y5 Z6 Z7 Z8 Z9 Y10 X11 X12] +
(-5.071480736146114e-06+0j) [Y5 Z6 Z7 Z8 Z9 Y10 Y12 Y13] +
(-6.631277928206738e-05+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-9.806102774699615e-06+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z12] +
(-4.734622038553502e-06+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z13] +
(-0.36937089366156145+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.023145130929529002+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y13] +
(-0.025637238296026835+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Z12 Y13] +
(3.3343312891723575e-06+0j) [Y5 Z6 Z7 Z8 Z9 Y11] +
(-0.00961263460684733+0j) [Y5 Z6 Z7 Z8 Z9 Z11 Z12 Y13] +
(-7.444344675648964e-06+0j) [Y5 Z6 Z7 Z8 Z10 Y11] +
(-0.04171881383982167+0j) [Y5 Z6 Z7 Z8 Z10 Z11 Z12 Y13] +
(-8.774817864304719e-06+0j) [Y5 Z6 Z7 Z9 Z10 Y11] +
(-0.04764261217638301+0j) [Y5 Z6 Z7 Z9 Z10 Z11 Z12 Y13] +
(-7.518362215440813e-06+0j) [Y5 Z6 Z8 Z9 Z10 Y11] +
(-0.03931805194719748+0j) [Y5 Z6 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.854060857961665e-06+0j) [Y5 Y7] +
(-6.290028432954373e-06+0j) [Y5 Z7 Z8 Z9 Z10 Y11] +
(-0.03956441632289326+0j) [Y5 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.010960074940542505+0j) [Z5 X6 Z7 Z8 Z9 X10] +
(-1.942946836713793e-06+0j) [Z5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.010960074940542505+0j) [Z5 Y6 Z7 Z8 Z9 Y10] +
(-1.942946836713793e-06+0j) [Z5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.14899430575065534+0j) [Z5 Z6] +
(0.018266834869375487+0j) [Z5 X7 Z8 Z9 Z10 X11] +
(-1.654117477047395e-06+0j) [Z5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.018266834869375487+0j) [Z5 Y7 Z8 Z9 Z10 Y11] +
(-1.654117477047395e-06+0j) [Z5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.13701191674040736+0j) [Z5 Z7] +
(-1.8163031699454557e-06+0j) [Z5 X10 Z11 X12] +
(-1.8163031699454557e-06+0j) [Z5 Y10 Z11 Y12] +
(1.8782101245023854e-06+0j) [Z5 X11 Z12 X13] +
(1.8782101245023854e-06+0j) [Z5 Y11 Z12 Y13] +
(0.12489990917237609+0j) [Z5 Z11] +
(-0.013873381748426132+0j) [X6 X7 Y8 Y9] +
(-0.017825140995786474+0j) [X6 X7 Y10 Y11] +
(-1.0358477601314118e-06+0j) [X6 X7 Y10 Z11 Z12 Y13] +
(-1.0358477601314118e-06+0j) [X6 X7 X11 X12] +
(-0.017366118994651458+0j) [X6 X7 Y12 Y13] +
(0.013873381748426132+0j) [X6 Y7 Y8 X9] +
(0.017825140995786474+0j) [X6 Y7 Y10 X11] +
(1.0358477601314118e-06+0j) [X6 Y7 Y10 Z11 Z12 X13] +
(-1.0358477601314118e-06+0j) [X6 Y7 Y11 X12] +
(0.017366118994651458+0j) [X6 Y7 Y12 X13] +
(0.00029219862611107837+0j) [X6 Z7 X8 X9 Z10 X11] +
(-3.32813935048787e-07+0j) [X6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(0.00029219862611107837+0j) [X6 Z7 X8 Y9 Z10 Y11] +
(-3.32813935048787e-07+0j) [X6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(0.22848106564918866+0j) [X6 Z7 Z8 Z9 X10] +
(3.313145500000725e-06+0j) [X6 Z7 Z8 Z9 X10 X11 Z12 X13] +
(3.313145500000725e-06+0j) [X6 Z7 Z8 Z9 X10 Y11 Z12 Y13] +
(0.011307274008848183+0j) [X6 Z7 Z8 Z9 X10 Z11] +
(0.025104957138844523+0j) [X6 Z7 Z8 Z9 X10 Z12] +
(0.010540425907671505+0j) [X6 Z7 Z8 Z9 X10 Z13] +
(-0.014564531231173017+0j) [X6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(0.014564531231173017+0j) [X6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(-2.5950860068297554e-05+0j) [X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.183932559184028e-06+0j) [X6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(-6.52437384824461e-06+0j) [X6 Z7 Z8 Z9 Z10 X12] +
(-3.2112283482438847e-06+0j) [X6 Z7 Z8 Z9 Z11 X12] +
(0.02981242451734572+0j) [X6 Z7 Z8 X10] +
(-3.2774831953051145e-06+0j) [X6 Z7 Z8 Z10 Z11 X12] +
(0.0301046231434568+0j) [X6 Z7 Z9 X10] +
(-3.6102971303539017e-06+0j) [X6 Z7 Z9 Z10 Z11 X12] +
(0.030787505389143894+0j) [X6 Z8 Z9 X10] +
(-3.7696594517650334e-06+0j) [X6 Z8 Z9 Z10 Z11 X12] +
(0.013873381748426132+0j) [Y6 X7 X8 Y9] +
(0.017825140995786474+0j) [Y6 X7 X10 Y11] +
(1.0358477601314118e-06+0j) [Y6 X7 X10 Z11 Z12 Y13] +
(-1.0358477601314118e-06+0j) [Y6 X7 X11 Y12] +
(0.017366118994651458+0j) [Y6 X7 X12 Y13] +
(-0.013873381748426132+0j) [Y6 Y7 X8 X9] +
(-0.017825140995786474+0j) [Y6 Y7 X10 X11] +
(-1.0358477601314118e-06+0j) [Y6 Y7 X10 Z11 Z12 X13] +
(-1.0358477601314118e-06+0j) [Y6 Y7 Y11 Y12] +
(-0.017366118994651458+0j) [Y6 Y7 X12 X13] +
(0.00029219862611107837+0j) [Y6 Z7 Y8 X9 Z10 X11] +
(-3.32813935048787e-07+0j) [Y6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(0.00029219862611107837+0j) [Y6 Z7 Y8 Y9 Z10 Y11] +
(-3.32813935048787e-07+0j) [Y6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(0.22848106564918866+0j) [Y6 Z7 Z8 Z9 Y10] +
(3.313145500000725e-06+0j) [Y6 Z7 Z8 Z9 Y10 X11 Z12 X13] +
(3.313145500000725e-06+0j) [Y6 Z7 Z8 Z9 Y10 Y11 Z12 Y13] +
(0.011307274008848183+0j) [Y6 Z7 Z8 Z9 Y10 Z11] +
(0.025104957138844523+0j) [Y6 Z7 Z8 Z9 Y10 Z12] +
(0.010540425907671505+0j) [Y6 Z7 Z8 Z9 Y10 Z13] +
(0.014564531231173017+0j) [Y6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(-0.014564531231173017+0j) [Y6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(-2.5950860068297554e-05+0j) [Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(4.183932559184028e-06+0j) [Y6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(-6.52437384824461e-06+0j) [Y6 Z7 Z8 Z9 Z10 Y12] +
(-3.2112283482438847e-06+0j) [Y6 Z7 Z8 Z9 Z11 Y12] +
(0.02981242451734572+0j) [Y6 Z7 Z8 Y10] +
(-3.2774831953051145e-06+0j) [Y6 Z7 Z8 Z10 Z11 Y12] +
(0.0301046231434568+0j) [Y6 Z7 Z9 Y10] +
(-3.6102971303539017e-06+0j) [Y6 Z7 Z9 Z10 Z11 Y12] +
(0.030787505389143894+0j) [Y6 Z8 Z9 Y10] +
(-3.7696594517650334e-06+0j) [Y6 Z8 Z9 Z10 Z11 Y12] +
(1.3096862988615428+0j) [Z6] +
(0.030787505389143894+0j) [Z6 X7 Z8 Z9 Z10 X11] +
(-3.7696594517650334e-06+0j) [Z6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.030787505389143894+0j) [Z6 Y7 Z8 Z9 Z10 Y11] +
(-3.7696594517650334e-06+0j) [Z6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.19392534613270188+0j) [Z6 Z7] +
(0.16756653265461252+0j) [Z6 Z8] +
(0.18143991440303867+0j) [Z6 Z9] +
(-1.8551201215214253e-06+0j) [Z6 X10 Z11 X12] +
(-1.8551201215214253e-06+0j) [Z6 Y10 Z11 Y12] +
(0.11952438964682682+0j) [Z6 Z10] +
(-2.890967881652837e-06+0j) [Z6 X11 Z12 X13] +
(-2.890967881652837e-06+0j) [Z6 Y11 Z12 Y13] +
(0.1373495306426133+0j) [Z6 Z11] +
(0.13401715261963698+0j) [Z6 Z12] +
(0.15138327161428844+0j) [Z6 Z13] +
(-0.00029219862611107837+0j) [X7 X8 Y9 Y10] +
(3.3281393504878704e-07+0j) [X7 X8 Y9 Z10 Z11 Y12] +
(0.00029219862611107837+0j) [X7 Y8 Y9 X10] +
(-3.3281393504878704e-07+0j) [X7 Y8 Y9 Z10 Z11 X12] +
(-3.313145500000725e-06+0j) [X7 Z8 Z9 X10 Y11 Y12] +
(-0.014564531231173017+0j) [X7 Z8 Z9 X10 X12 X13] +
(3.313145500000725e-06+0j) [X7 Z8 Z9 Y10 Y11 X12] +
(-0.014564531231173017+0j) [X7 Z8 Z9 Y10 Y12 X13] +
(0.2284810656491886+0j) [X7 Z8 Z9 Z10 X11] +
(0.010540425907671505+0j) [X7 Z8 Z9 Z10 X11 Z12] +
(0.025104957138844523+0j) [X7 Z8 Z9 Z10 X11 Z13] +
(-2.595086006829755e-05+0j) [X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.183932559184028e-06+0j) [X7 Z8 Z9 Z10 Z11 X13] +
(-3.2112283482438847e-06+0j) [X7 Z8 Z9 Z10 Z12 X13] +
(0.011307274008848185+0j) [X7 Z8 Z9 X11] +
(-6.52437384824461e-06+0j) [X7 Z8 Z9 Z11 Z12 X13] +
(0.0301046231434568+0j) [X7 Z8 Z10 X11] +
(-3.6102971303539017e-06+0j) [X7 Z8 Z10 Z11 Z12 X13] +
(0.02981242451734572+0j) [X7 Z9 Z10 X11] +
(-3.2774831953051145e-06+0j) [X7 Z9 Z10 Z11 Z12 X13] +
(0.00029219862611107837+0j) [Y7 X8 X9 Y10] +
(-3.3281393504878704e-07+0j) [Y7 X8 X9 Z10 Z11 Y12] +
(-0.00029219862611107837+0j) [Y7 Y8 X9 X10] +
(3.3281393504878704e-07+0j) [Y7 Y8 X9 Z10 Z11 X12] +
(3.313145500000725e-06+0j) [Y7 Z8 Z9 X10 X11 Y12] +
(-0.014564531231173017+0j) [Y7 Z8 Z9 X10 X12 Y13] +
(-3.313145500000725e-06+0j) [Y7 Z8 Z9 Y10 X11 X12] +
(-0.014564531231173017+0j) [Y7 Z8 Z9 Y10 Y12 Y13] +
(0.2284810656491886+0j) [Y7 Z8 Z9 Z10 Y11] +
(0.010540425907671505+0j) [Y7 Z8 Z9 Z10 Y11 Z12] +
(0.025104957138844523+0j) [Y7 Z8 Z9 Z10 Y11 Z13] +
(-2.595086006829755e-05+0j) [Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(4.183932559184028e-06+0j) [Y7 Z8 Z9 Z10 Z11 Y13] +
(-3.2112283482438847e-06+0j) [Y7 Z8 Z9 Z10 Z12 Y13] +
(0.011307274008848185+0j) [Y7 Z8 Z9 Y11] +
(-6.52437384824461e-06+0j) [Y7 Z8 Z9 Z11 Z12 Y13] +
(0.0301046231434568+0j) [Y7 Z8 Z10 Y11] +
(-3.6102971303539017e-06+0j) [Y7 Z8 Z10 Z11 Z12 Y13] +
(0.02981242451734572+0j) [Y7 Z9 Z10 Y11] +
(-3.2774831953051145e-06+0j) [Y7 Z9 Z10 Z11 Z12 Y13] +
(1.3096862988615419+0j) [Z7] +
(0.18143991440303867+0j) [Z7 Z8] +
(0.16756653265461252+0j) [Z7 Z9] +
(-2.890967881652837e-06+0j) [Z7 X10 Z11 X12] +
(-2.890967881652837e-06+0j) [Z7 Y10 Z11 Y12] +
(0.1373495306426133+0j) [Z7 Z10] +
(-1.8551201215214253e-06+0j) [Z7 X11 Z12 X13] +
(-1.8551201215214253e-06+0j) [Z7 Y11 Z12 Y13] +
(0.11952438964682682+0j) [Z7 Z11] +
(0.15138327161428844+0j) [Z7 Z12] +
(0.13401715261963698+0j) [Z7 Z13] +
(-0.009560705729135956+0j) [X8 X9 Y10 Y11] +
(6.628614201272325e-07+0j) [X8 X9 Y10 Z11 Z12 Y13] +
(6.628614201272327e-07+0j) [X8 X9 X11 X12] +
(0.009560705729135956+0j) [X8 Y9 Y10 X11] +
(-6.628614201272325e-07+0j) [X8 Y9 Y10 Z11 Z12 X13] +
(6.628614201272327e-07+0j) [X8 Y9 Y11 X12] +
(0.009560705729135956+0j) [Y8 X9 X10 Y11] +
(-6.628614201272325e-07+0j) [Y8 X9 X10 Z11 Z12 Y13] +
(6.628614201272327e-07+0j) [Y8 X9 X11 Y12] +
(-0.009560705729135956+0j) [Y8 Y9 X10 X11] +
(6.628614201272325e-07+0j) [Y8 Y9 X10 Z11 Z12 X13] +
(6.628614201272327e-07+0j) [Y8 Y9 Y11 Y12] +
(1.369352563471818+0j) [Z8] +
(-1.5973171977984636e-06+0j) [Z8 X10 Z11 X12] +
(-1.5973171977984636e-06+0j) [Z8 Y10 Z11 Y12] +
(0.13766872645852588+0j) [Z8 Z10] +
(-9.344557776712309e-07+0j) [Z8 X11 Z12 X13] +
(-9.344557776712309e-07+0j) [Z8 Y11 Z12 Y13] +
(0.14722943218766185+0j) [Z8 Z11] +
(0.14973486803496927+0j) [Z8 Z12] +
(0.1558226905155311+0j) [Z8 Z13] +
(1.369352563471818+0j) [Z9] +
(-9.344557776712309e-07+0j) [Z9 X10 Z11 X12] +
(-9.344557776712309e-07+0j) [Z9 Y10 Z11 Y12] +
(0.14722943218766185+0j) [Z9 Z10] +
(-1.5973171977984636e-06+0j) [Z9 X11 Z12 X13] +
(-1.5973171977984636e-06+0j) [Z9 Y11 Z12 Y13] +
(0.13766872645852588+0j) [Z9 Z11] +
(0.1558226905155311+0j) [Z9 Z12] +
(0.14973486803496927+0j) [Z9 Z13] +
(-0.028685183716105848+0j) [X10 X11 Y12 Y13] +
(0.028685183716105848+0j) [X10 Y11 Y12 X13] +
(-1.0722312157964374e-05+0j) [X10 Z11 X12] +
(7.95441317573004e-06+0j) [X10 Z11 X12 Z13] +
(-8.194261371892223e-06+0j) [X10 X12] +
(0.028685183716105848+0j) [Y10 X11 X12 Y13] +
(-0.028685183716105848+0j) [Y10 Y11 X12 X13] +
(-1.0722312157964374e-05+0j) [Y10 Z11 Y12] +
(7.95441317573004e-06+0j) [Y10 Z11 Y12 Z13] +
(-8.194261371892223e-06+0j) [Y10 Y12] +
(0.7829661725950211+0j) [Z10] +
(-8.194261371892223e-06+0j) [Z10 X11 Z12 X13] +
(-8.194261371892223e-06+0j) [Z10 Y11 Z12 Y13] +
(0.14926355147388912+0j) [Z10 Z11] +
(0.11270386920332232+0j) [Z10 Z12] +
(0.14138905291942816+0j) [Z10 Z13] +
(-1.0722312157964372e-05+0j) [X11 Z12 X13] +
(7.95441317573004e-06+0j) [X11 X13] +
(-1.0722312157964372e-05+0j) [Y11 Z12 Y13] +
(7.95441317573004e-06+0j) [Y11 Y13] +
(0.7829661725950212+0j) [Z11] +
(0.14138905291942816+0j) [Z11 Z12] +
(0.11270386920332232+0j) [Z11 Z13] +
(0.8084581961720487+0j) [Z12] +
(0.15435748657223633+0j) [Z12 Z13] +
(0.8084581961720488+0j) [Z13]
  (-46.46390678868893) [I0]
+ (0.7829661725950202) [Z10]
+ (0.7829661725950205) [Z11]
+ (0.808458196172048) [Z12]
+ (0.8084581961720483) [Z13]
+ (1.2034402289145636) [Z4]
+ (1.2034402289145636) [Z5]
+ (1.3096862988615436) [Z6]
+ (1.3693525634718198) [Z8]
+ (1.3693525634718198) [Z9]
+ (1.6538942226831725) [Z3]
+ (1.6538942226831728) [Z2]
+ (12.412630742111773) [Z0]
+ (12.412630742111773) [Z1]
+ (-8.194261372090515e-06) [Y10 Y12]
+ (-8.194261372090515e-06) [X10 X12]
+ (-1.8540608579559588e-06) [Y5 Y7]
+ (-1.8540608579559588e-06) [X5 X7]
+ (-7.764994118298485e-07) [Y3 Y5]
+ (-7.764994118298485e-07) [X3 X5]
+ (-5.929765815988198e-07) [Y4 Y6]
+ (-5.929765815988198e-07) [X4 X6]
+ (1.602116740551119e-06) [Y2 Y4]
+ (1.602116740551119e-06) [X2 X4]
+ (7.954413176158045e-06) [Y11 Y13]
+ (7.954413176158045e-06) [X11 X13]
+ (0.00327697193123167) [Y1 Y3]
+ (0.00327697193123167) [X1 X3]
+ (0.10433064780651399) [Y0 Y2]
+ (0.10433064780651399) [X0 X2]
+ (0.11270386920332205) [Z10 Z12]
+ (0.11270386920332205) [Z11 Z13]
+ (0.11383573679388644) [Z4 Z12]
+ (0.11383573679388644) [Z5 Z13]
+ (0.11952438964682664) [Z6 Z10]
+ (0.11952438964682664) [Z7 Z11]
+ (0.12489990917237591) [Z4 Z10]
+ (0.12489990917237591) [Z5 Z11]
+ (0.12495807739503195) [Z2 Z4]
+ (0.12495807739503195) [Z3 Z5]
+ (0.12799502492468398) [Z2 Z10]
+ (0.12799502492468398) [Z3 Z11]
+ (0.13401715261963681) [Z6 Z12]
+ (0.13401715261963681) [Z7 Z13]
+ (0.13701191674040727) [Z4 Z6]
+ (0.13701191674040727) [Z5 Z7]
+ (0.13734953064261313) [Z6 Z11]
+ (0.13734953064261313) [Z7 Z10]
+ (0.13739104762683205) [Z2 Z6]
+ (0.13739104762683205) [Z3 Z7]
+ (0.1376687264585258) [Z8 Z10]
+ (0.1376687264585258) [Z9 Z11]
+ (0.14011289865354787) [Z2 Z12]
+ (0.14011289865354787) [Z3 Z13]
+ (0.141389052919428) [Z10 Z13]
+ (0.141389052919428) [Z11 Z12]
+ (0.14257997712485737) [Z4 Z11]
+ (0.14257997712485737) [Z5 Z10]
+ (0.1472294321876617) [Z8 Z11]
+ (0.1472294321876617) [Z9 Z10]
+ (0.14899430575065523) [Z4 Z7]
+ (0.14899430575065523) [Z5 Z6]
+ (0.149263551473889) [Z10 Z11]
+ (0.14960702684445287) [Z4 Z8]
+ (0.14960702684445287) [Z5 Z9]
+ (0.1497348680349691) [Z8 Z12]
+ (0.1497348680349691) [Z9 Z13]
+ (0.15071408121008273) [Z2 Z8]
+ (0.15071408121008273) [Z3 Z9]
+ (0.15138327161428816) [Z6 Z13]
+ (0.15138327161428816) [Z7 Z12]
+ (0.15215040708869026) [Z4 Z13]
+ (0.15215040708869026) [Z5 Z12]
+ (0.15337968243314135) [Z2 Z11]
+ (0.15337968243314135) [Z3 Z10]
+ (0.1543574865722361) [Z12 Z13]
+ (0.15569010671752428) [Z2 Z13]
+ (0.15569010671752428) [Z3 Z12]
+ (0.15582269051553096) [Z8 Z13]
+ (0.15582269051553096) [Z9 Z12]
+ (0.1567639617643098) [Z4 Z9]
+ (0.1567639617643098) [Z5 Z8]
+ (0.15755314797985637) [Z4 Z5]
+ (0.1607976453483853) [Z2 Z5]
+ (0.1607976453483853) [Z3 Z4]
+ (0.16756653265461255) [Z6 Z8]
+ (0.16756653265461255) [Z7 Z9]
+ (0.16853486561579917) [Z2 Z7]
+ (0.16853486561579917) [Z3 Z6]
+ (0.1814399144030386) [Z6 Z9]
+ (0.1814399144030386) [Z7 Z8]
+ (0.1818908579075133) [Z2 Z3]
+ (0.18690820476912537) [Z2 Z9]
+ (0.18690820476912537) [Z3 Z8]
+ (0.19299723935364235) [Z0 Z10]
+ (0.19299723935364235) [Z1 Z11]
+ (0.1939253461327016) [Z6 Z7]
+ (0.19661770890342126) [Z0 Z4]
+ (0.19661770890342126) [Z1 Z5]
+ (0.19936354537360806) [Z0 Z5]
+ (0.19936354537360806) [Z1 Z4]
+ (0.20072866460441763) [Z0 Z11]
+ (0.20072866460441763) [Z1 Z10]
+ (0.21102659849791483) [Z0 Z12]
+ (0.21102659849791483) [Z1 Z13]
+ (0.21631037498631778) [Z0 Z13]
+ (0.21631037498631778) [Z1 Z12]
+ (0.23671080783830403) [Z0 Z2]
+ (0.23671080783830403) [Z1 Z3]
+ (0.2416466393601717) [Z0 Z6]
+ (0.2416466393601717) [Z1 Z7]
+ (0.24853483371314228) [Z0 Z7]
+ (0.24853483371314228) [Z1 Z6]
+ (0.25129445674591666) [Z0 Z3]
+ (0.25129445674591666) [Z1 Z2]
+ (0.2723251830660568) [Z0 Z8]
+ (0.2723251830660568) [Z1 Z9]
+ (1.1861763734860493) [Z0 Z1]
+ (-1.2260484988966326e-05) [Y4 Z5 Y6]
+ (-1.2260484988966326e-05) [X4 Z5 X6]
+ (-1.226048498896632e-05) [Y5 Z6 Y7]
+ (-1.226048498896632e-05) [X5 Z6 X7]
+ (-1.072231215755235e-05) [Y10 Z11 Y12]
+ (-1.072231215755235e-05) [X10 Z11 X12]
+ (-1.072231215755235e-05) [Y11 Z12 Y13]
+ (-1.072231215755235e-05) [X11 Z12 X13]
+ (-3.887051672969897e-06) [Y2 Z3 Y4]
+ (-3.887051672969897e-06) [X2 Z3 X4]
+ (-3.887051672969897e-06) [Y3 Z4 Y5]
+ (-3.887051672969897e-06) [X3 Z4 X5]
+ (0.1250703257977192) [Y1 Z2 Y3]
+ (0.1250703257977192) [X1 Z2 X3]
+ (0.1250703257977193) [Y0 Z1 Y2]
+ (0.1250703257977193) [X0 Z1 X2]
+ (-0.03831467029480382) [Y4 Y5 X12 X13]
+ (-0.03831467029480382) [X4 X5 Y12 Y13]
+ (-0.03619412355904262) [Y2 Y3 X8 X9]
+ (-0.03619412355904262) [X2 X3 Y8 Y9]
+ (-0.035839567953353364) [Y2 Y3 X4 X5]
+ (-0.035839567953353364) [X2 X3 Y4 Y5]
+ (-0.031143817988967096) [Y2 Y3 X6 X7]
+ (-0.031143817988967096) [X2 X3 Y6 Y7]
+ (-0.028685183716105924) [Y10 Y11 X12 X13]
+ (-0.028685183716105924) [X10 X11 Y12 Y13]
+ (-0.0259961775980211) [Y3 Z4 Z5 Y7]
+ (-0.0259961775980211) [X3 Z4 Z5 X7]
+ (-0.025384657508457368) [Y2 Y3 X10 X11]
+ (-0.025384657508457368) [X2 X3 Y10 Y11]
+ (-0.019028242443847224) [Y3 Y4 X11 X12]
+ (-0.019028242443847224) [X3 X4 Y11 Y12]
+ (-0.0178251409957865) [Y6 Y7 X10 X11]
+ (-0.0178251409957865) [X6 X7 Y10 Y11]
+ (-0.01768006795248148) [Y4 Y5 X10 X11]
+ (-0.01768006795248148) [X4 X5 Y10 Y11]
+ (-0.01736611899465137) [Y6 Y7 X12 X13]
+ (-0.01736611899465137) [X6 X7 Y12 Y13]
+ (-0.01557720806397642) [Y2 Y3 X12 X13]
+ (-0.01557720806397642) [X2 X3 Y12 Y13]
+ (-0.014583648907612653) [Y0 Y1 X2 X3]
+ (-0.014583648907612653) [X0 X1 Y2 Y3]
+ (-0.013873381748426075) [Y6 Y7 X8 X9]
+ (-0.013873381748426075) [X6 X7 Y8 Y9]
+ (-0.011982389010247944) [Y4 Y5 X6 X7]
+ (-0.011982389010247944) [X4 X5 Y6 Y7]
+ (-0.011285190200840914) [Y5 X6 X11 Y12]
+ (-0.011285190200840914) [X5 Y6 Y11 X12]
+ (-0.009560705729135933) [Y8 Y9 X10 X11]
+ (-0.009560705729135933) [X8 X9 Y10 Y11]
+ (-0.00812525192138102) [Y1 X2 X8 Y9]
+ (-0.00812525192138102) [Y1 Y2 Y8 Y9]
+ (-0.00812525192138102) [X1 X2 X8 X9]
+ (-0.00812525192138102) [X1 Y2 Y8 X9]
+ (-0.00773142525077527) [Y0 Y1 X10 X11]
+ (-0.00773142525077527) [X0 X1 Y10 Y11]
+ (-0.007156934919856943) [Y4 Y5 X8 X9]
+ (-0.007156934919856943) [X4 X5 Y8 Y9]
+ (-0.006888194352970542) [Y0 Y1 X6 X7]
+ (-0.006888194352970542) [X0 X1 Y6 Y7]
+ (-0.006509361201177231) [Y0 Y1 X8 X9]
+ (-0.006509361201177231) [X0 X1 Y8 Y9]
+ (-0.006087822480561847) [Y8 Y9 X12 X13]
+ (-0.006087822480561847) [X8 X9 Y12 Y13]
+ (-0.005283776488402946) [Y0 Y1 X12 X13]
+ (-0.005283776488402946) [X0 X1 Y12 Y13]
+ (-0.005143391768825111) [Y3 X4 X5 Y6]
+ (-0.005143391768825111) [X3 Y4 Y5 X6]
+ (-0.0045750076266391935) [Y1 X2 X12 Y13]
+ (-0.0045750076266391935) [Y1 Y2 Y12 Y13]
+ (-0.0045750076266391935) [X1 X2 X12 X13]
+ (-0.0045750076266391935) [X1 Y2 Y12 X13]
+ (-0.004424855449441847) [Y1 X2 X4 Y5]
+ (-0.004424855449441847) [Y1 Y2 Y4 Y5]
+ (-0.004424855449441847) [X1 X2 X4 X5]
+ (-0.004424855449441847) [X1 Y2 Y4 X5]
+ (-0.0034795118903343247) [Y2 Z3 Z5 Y6]
+ (-0.0034795118903343247) [X2 Z3 Z5 X6]
+ (-0.0034795118903343247) [Y3 Z4 Z6 Y7]
+ (-0.0034795118903343247) [X3 Z4 Z6 X7]
+ (-0.002745836470186808) [Y0 Y1 X4 X5]
+ (-0.002745836470186808) [X0 X1 Y4 Y5]
+ (-0.0017992194936630203) [Y1 X2 X10 Y11]
+ (-0.0017992194936630203) [Y1 Y2 Y10 Y11]
+ (-0.0017992194936630203) [X1 X2 X10 X11]
+ (-0.0017992194936630203) [X1 Y2 Y10 X11]
+ (-0.0002921986261110375) [Y7 Y8 X9 X10]
+ (-0.0002921986261110375) [X7 X8 Y9 Y10]
+ (-8.194261372090515e-06) [Z10 Y11 Z12 Y13]
+ (-8.194261372090515e-06) [Z10 X11 Z12 X13]
+ (-7.801707500395613e-06) [Y2 Z3 Y4 Z11]
+ (-7.801707500395613e-06) [X2 Z3 X4 Z11]
+ (-7.801707500395613e-06) [Y3 Z4 Y5 Z10]
+ (-7.801707500395613e-06) [X3 Z4 X5 Z10]
+ (-4.643051068408111e-06) [Y3 X4 X10 Y11]
+ (-4.643051068408111e-06) [Y3 Y4 Y10 Y11]
+ (-4.643051068408111e-06) [X3 X4 X10 X11]
+ (-4.643051068408111e-06) [X3 Y4 Y10 X11]
+ (-4.58885515562754e-06) [Y4 Z5 Y6 Z13]
+ (-4.58885515562754e-06) [X4 Z5 X6 Z13]
+ (-4.58885515562754e-06) [Y5 Z6 Y7 Z12]
+ (-4.58885515562754e-06) [X5 Z6 X7 Z12]
+ (-4.556569218064378e-06) [Y5 X6 X12 Y13]
+ (-4.556569218064378e-06) [Y5 Y6 Y12 Y13]
+ (-4.556569218064378e-06) [X5 X6 X12 X13]
+ (-4.556569218064378e-06) [X5 Y6 Y12 X13]
+ (-3.6945132943944286e-06) [Y4 X5 X11 Y12]
+ (-3.6945132943944286e-06) [Y4 Y5 Y11 Y12]
+ (-3.6945132943944286e-06) [X4 X5 X11 X12]
+ (-3.6945132943944286e-06) [X4 Y5 Y11 X12]
+ (-3.3440815564797043e-06) [Z0 Y5 Z6 Y7]
+ (-3.3440815564797043e-06) [Z0 X5 Z6 X7]
+ (-3.3440815564797043e-06) [Z1 Y4 Z5 Y6]
+ (-3.3440815564797043e-06) [Z1 X4 Z5 X6]
+ (-3.158656431987501e-06) [Y2 Z3 Y4 Z10]
+ (-3.158656431987501e-06) [X2 Z3 X4 Z10]
+ (-3.158656431987501e-06) [Y3 Z4 Y5 Z11]
+ (-3.158656431987501e-06) [X3 Z4 X5 Z11]
+ (-3.099349243605057e-06) [Z0 Y4 Z5 Y6]
+ (-3.099349243605057e-06) [Z0 X4 Z5 X6]
+ (-3.099349243605057e-06) [Z1 Y5 Z6 Y7]
+ (-3.099349243605057e-06) [Z1 X5 Z6 X7]
+ (-2.8909678816434246e-06) [Z6 Y11 Z12 Y13]
+ (-2.8909678816434246e-06) [Z6 X11 Z12 X13]
+ (-2.8909678816434246e-06) [Z7 Y10 Z11 Y12]
+ (-2.8909678816434246e-06) [Z7 X10 Z11 X12]
+ (-2.1776646050208024e-06) [Z0 Y10 Z11 Y12]
+ (-2.1776646050208024e-06) [Z0 X10 Z11 X12]
+ (-2.1776646050208024e-06) [Z1 Y11 Z12 Y13]
+ (-2.1776646050208024e-06) [Z1 X11 Z12 X13]
+ (-1.881850183207424e-06) [Y4 Z5 Y6 Z9]
+ (-1.881850183207424e-06) [X4 Z5 X6 Z9]
+ (-1.881850183207424e-06) [Y5 Z6 Y7 Z8]
+ (-1.881850183207424e-06) [X5 Z6 X7 Z8]
+ (-1.8551201214889371e-06) [Z6 Y10 Z11 Y12]
+ (-1.8551201214889371e-06) [Z6 X10 Z11 X12]
+ (-1.8551201214889371e-06) [Z7 Y11 Z12 Y13]
+ (-1.8551201214889371e-06) [Z7 X11 Z12 X13]
+ (-1.8540608579559586e-06) [Y4 Z5 Y6 Z7]
+ (-1.8540608579559586e-06) [X4 Z5 X6 Z7]
+ (-1.8163031696729518e-06) [Z4 Y11 Z12 Y13]
+ (-1.8163031696729518e-06) [Z4 X11 Z12 X13]
+ (-1.8163031696729518e-06) [Z5 Y10 Z11 Y12]
+ (-1.8163031696729518e-06) [Z5 X10 Z11 X12]
+ (-1.692397828562498e-06) [Y4 Z5 Y6 Z10]
+ (-1.692397828562498e-06) [X4 Z5 X6 Z10]
+ (-1.692397828562498e-06) [Y5 Z6 Y7 Z11]
+ (-1.692397828562498e-06) [X5 Z6 X7 Z11]
+ (-1.6148794138922206e-06) [Z0 Y11 Z12 Y13]
+ (-1.6148794138922206e-06) [Z0 X11 Z12 X13]
+ (-1.6148794138922206e-06) [Z1 Y10 Z11 Y12]
+ (-1.6148794138922206e-06) [Z1 X10 Z11 X12]
+ (-1.5973171977904807e-06) [Z8 Y10 Z11 Y12]
+ (-1.5973171977904807e-06) [Z8 X10 Z11 X12]
+ (-1.5973171977904807e-06) [Z9 Y11 Z12 Y13]
+ (-1.5973171977904807e-06) [Z9 X11 Z12 X13]
+ (-1.4548424490437363e-06) [Y3 X4 X6 Y7]
+ (-1.4548424490437363e-06) [Y3 Y4 Y6 Y7]
+ (-1.4548424490437363e-06) [X3 X4 X6 X7]
+ (-1.4548424490437363e-06) [X3 Y4 Y6 X7]
+ (-1.3980449081275986e-06) [Y4 Z5 Y6 Z8]
+ (-1.3980449081275986e-06) [X4 Z5 X6 Z8]
+ (-1.3980449081275986e-06) [Y5 Z6 Y7 Z9]
+ (-1.3980449081275986e-06) [X5 Z6 X7 Z9]
+ (-1.1954890099593231e-06) [Y2 Z3 Y4 Z7]
+ (-1.1954890099593231e-06) [X2 Z3 X4 Z7]
+ (-1.1954890099593231e-06) [Y3 Z4 Y5 Z6]
+ (-1.1954890099593231e-06) [X3 Z4 X5 Z6]
+ (-1.190850808332077e-06) [Z0 Y3 Z4 Y5]
+ (-1.190850808332077e-06) [Z0 X3 Z4 X5]
+ (-1.190850808332077e-06) [Z1 Y2 Z3 Y4]
+ (-1.190850808332077e-06) [Z1 X2 Z3 X4]
+ (-1.1708301370149171e-06) [Z2 Y5 Z6 Y7]
+ (-1.1708301370149171e-06) [Z2 X5 Z6 X7]
+ (-1.1708301370149171e-06) [Z3 Y4 Z5 Y6]
+ (-1.1708301370149171e-06) [Z3 X4 Z5 X6]
+ (-1.0632283423560371e-06) [Z2 Y10 Z11 Y12]
+ (-1.0632283423560371e-06) [Z2 X10 Z11 X12]
+ (-1.0632283423560371e-06) [Z3 Y11 Z12 Y13]
+ (-1.0632283423560371e-06) [Z3 X11 Z12 X13]
+ (-1.0358477601544873e-06) [Y6 X7 X11 Y12]
+ (-1.0358477601544873e-06) [Y6 Y7 Y11 Y12]
+ (-1.0358477601544873e-06) [X6 X7 X11 X12]
+ (-1.0358477601544873e-06) [X6 Y7 Y11 X12]
+ (-9.509249751760923e-07) [Z2 Y4 Z5 Y6]
+ (-9.509249751760923e-07) [Z2 X4 Z5 X6]
+ (-9.509249751760923e-07) [Z3 Y5 Z6 Y7]
+ (-9.509249751760923e-07) [Z3 X5 Z6 X7]
+ (-9.34455777637781e-07) [Z8 Y11 Z12 Y13]
+ (-9.34455777637781e-07) [Z8 X11 Z12 X13]
+ (-9.34455777637781e-07) [Z9 Y10 Z11 Y12]
+ (-9.34455777637781e-07) [Z9 X10 Z11 X12]
+ (-8.337746754359375e-07) [Z0 Y2 Z3 Y4]
+ (-8.337746754359375e-07) [Z0 X2 Z3 X4]
+ (-8.337746754359375e-07) [Z1 Y3 Z4 Y5]
+ (-8.337746754359375e-07) [Z1 X3 Z4 X5]
+ (-7.956895372271295e-07) [Y3 X4 X8 Y9]
+ (-7.956895372271295e-07) [Y3 Y4 Y8 Y9]
+ (-7.956895372271295e-07) [X3 X4 X8 X9]
+ (-7.956895372271295e-07) [X3 Y4 Y8 X9]
+ (-7.764994118298486e-07) [Y2 Z3 Y4 Z5]
+ (-7.764994118298486e-07) [X2 Z3 X4 Z5]
+ (-5.929765815988197e-07) [Z4 Y5 Z6 Y7]
+ (-5.929765815988197e-07) [Z4 X5 Z6 X7]
+ (-5.770052995050483e-07) [Y2 Z3 Y4 Z9]
+ (-5.770052995050483e-07) [X2 Z3 X4 Z9]
+ (-5.770052995050483e-07) [Y3 Z4 Y5 Z8]
+ (-5.770052995050483e-07) [X3 Z4 X5 Z8]
+ (-5.471647744551827e-07) [Y1 Y2 X11 X12]
+ (-5.471647744551827e-07) [X1 X2 Y11 Y12]
+ (-4.838052750798253e-07) [Y5 X6 X8 Y9]
+ (-4.838052750798253e-07) [Y5 Y6 Y8 Y9]
+ (-4.838052750798253e-07) [X5 X6 X8 X9]
+ (-4.838052750798253e-07) [X5 Y6 Y8 X9]
+ (-3.5707613289613943e-07) [Y0 X1 X3 Y4]
+ (-3.5707613289613943e-07) [Y0 Y1 Y3 Y4]
+ (-3.5707613289613943e-07) [X0 X1 X3 X4]
+ (-3.5707613289613943e-07) [X0 Y1 Y3 X4]
+ (-2.447323128746472e-07) [Y0 X1 X5 Y6]
+ (-2.447323128746472e-07) [Y0 Y1 Y5 Y6]
+ (-2.447323128746472e-07) [X0 X1 X5 X6]
+ (-2.447323128746472e-07) [X0 Y1 Y5 X6]
+ (-2.199051618388247e-07) [Y2 X3 X5 Y6]
+ (-2.199051618388247e-07) [Y2 Y3 Y5 Y6]
+ (-2.199051618388247e-07) [X2 X3 X5 X6]
+ (-2.199051618388247e-07) [X2 Y3 Y5 X6]
+ (-1.933241277033319e-07) [Y1 X2 X3 Y4]
+ (-1.933241277033319e-07) [X1 Y2 Y3 X4]
+ (-1.2919694861896926e-07) [Y1 Z2 Z3 Y5]
+ (-1.2919694861896926e-07) [X1 Z2 Z3 X5]
+ (1.7379332623180265e-07) [Y0 Z1 Z3 Y4]
+ (1.7379332623180265e-07) [X0 Z1 Z3 X4]
+ (1.7379332623180265e-07) [Y1 Z2 Z4 Y5]
+ (1.7379332623180265e-07) [X1 Z2 Z4 X5]
+ (1.933241277033319e-07) [Y1 Y2 X3 X4]
+ (1.933241277033319e-07) [X1 X2 Y3 Y4]
+ (2.186842377220812e-07) [Y2 Z3 Y4 Z8]
+ (2.186842377220812e-07) [X2 Z3 X4 Z8]
+ (2.186842377220812e-07) [Y3 Z4 Y5 Z9]
+ (2.186842377220812e-07) [X3 Z4 X5 Z9]
+ (2.5935343908441306e-07) [Y2 Z3 Y4 Z6]
+ (2.5935343908441306e-07) [X2 Z3 X4 Z6]
+ (2.5935343908441306e-07) [Y3 Z4 Y5 Z7]
+ (2.5935343908441306e-07) [X3 Z4 X5 Z7]
+ (3.606071867779064e-07) [Y0 Z1 Z2 Y4]
+ (3.606071867779064e-07) [X0 Z1 Z2 X4]
+ (3.606071867779064e-07) [Y1 Z3 Z4 Y5]
+ (3.606071867779064e-07) [X1 Z3 Z4 X5]
+ (5.471647744551827e-07) [Y1 X2 X11 Y12]
+ (5.471647744551827e-07) [X1 Y2 Y11 X12]
+ (5.627851911285821e-07) [Y0 X1 X11 Y12]
+ (5.627851911285821e-07) [Y0 Y1 Y11 Y12]
+ (5.627851911285821e-07) [X0 X1 X11 X12]
+ (5.627851911285821e-07) [X0 Y1 Y11 X12]
+ (6.628614201526998e-07) [Y8 X9 X11 Y12]
+ (6.628614201526998e-07) [Y8 Y9 Y11 Y12]
+ (6.628614201526998e-07) [X8 X9 X11 X12]
+ (6.628614201526998e-07) [X8 Y9 Y11 X12]
+ (1.1094407590740744e-06) [Z2 Y11 Z12 Y13]
+ (1.1094407590740744e-06) [Z2 X11 Z12 X13]
+ (1.1094407590740744e-06) [Z3 Y10 Z11 Y12]
+ (1.1094407590740744e-06) [Z3 X10 Z11 X12]
+ (1.602116740551119e-06) [Z2 Y3 Z4 Y5]
+ (1.602116740551119e-06) [Z2 X3 Z4 X5]
+ (1.878210124721477e-06) [Z4 Y10 Z11 Y12]
+ (1.878210124721477e-06) [Z4 X10 Z11 X12]
+ (1.878210124721477e-06) [Z5 Y11 Z12 Y13]
+ (1.878210124721477e-06) [Z5 X11 Z12 X13]
+ (2.172669101430111e-06) [Y2 X3 X11 Y12]
+ (2.172669101430111e-06) [Y2 Y3 Y11 Y12]
+ (2.172669101430111e-06) [X2 X3 X11 X12]
+ (2.172669101430111e-06) [X2 Y3 Y11 X12]
+ (3.1174479459494263e-06) [Y0 Z2 Z3 Y4]
+ (3.1174479459494263e-06) [X0 Z2 Z3 X4]
+ (3.5390541844703815e-06) [Y2 Z3 Y4 Z12]
+ (3.5390541844703815e-06) [X2 Z3 X4 Z12]
+ (3.5390541844703815e-06) [Y3 Z4 Y5 Z13]
+ (3.5390541844703815e-06) [X3 Z4 X5 Z13]
+ (4.281913884760978e-06) [Y4 Z5 Y6 Z11]
+ (4.281913884760978e-06) [X4 Z5 X6 Z11]
+ (4.281913884760978e-06) [Y5 Z6 Y7 Z10]
+ (4.281913884760978e-06) [X5 Z6 X7 Z10]
+ (5.275883122027672e-06) [Y3 X4 X12 Y13]
+ (5.275883122027672e-06) [Y3 Y4 Y12 Y13]
+ (5.275883122027672e-06) [X3 X4 X12 X13]
+ (5.275883122027672e-06) [X3 Y4 Y12 X13]
+ (5.974311713323477e-06) [Y5 X6 X10 Y11]
+ (5.974311713323477e-06) [Y5 Y6 Y10 Y11]
+ (5.974311713323477e-06) [X5 X6 X10 X11]
+ (5.974311713323477e-06) [X5 Y6 Y10 X11]
+ (7.954413176158045e-06) [Y10 Z11 Y12 Z13]
+ (7.954413176158045e-06) [X10 Z11 X12 Z13]
+ (8.814937306498053e-06) [Y2 Z3 Y4 Z13]
+ (8.814937306498053e-06) [X2 Z3 X4 Z13]
+ (8.814937306498053e-06) [Y3 Z4 Y5 Z12]
+ (8.814937306498053e-06) [X3 Z4 X5 Z12]
+ (0.0002921986261110375) [Y7 X8 X9 Y10]
+ (0.0002921986261110375) [X7 Y8 Y9 X10]
+ (0.0004956762314916223) [Y2 Z4 Z5 Y6]
+ (0.0004956762314916223) [X2 Z4 Z5 X6]
+ (0.0011059037691896964) [Y0 Z1 Y2 Z5]
+ (0.0011059037691896964) [X0 Z1 X2 Z5]
+ (0.0011059037691896964) [Y1 Z2 Y3 Z4]
+ (0.0011059037691896964) [X1 Z2 X3 Z4]
+ (0.0016638798784907862) [Y2 Z3 Z4 Y6]
+ (0.0016638798784907862) [X2 Z3 Z4 X6]
+ (0.0016638798784907862) [Y3 Z5 Z6 Y7]
+ (0.0016638798784907862) [X3 Z5 Z6 X7]
+ (0.0017560707018412444) [Y0 Z1 Y2 Z11]
+ (0.0017560707018412444) [X0 Z1 X2 Z11]
+ (0.0017560707018412444) [Y1 Z2 Y3 Z10]
+ (0.0017560707018412444) [X1 Z2 X3 Z10]
+ (0.002326230623158084) [Y0 Z1 Y2 Z13]
+ (0.002326230623158084) [X0 Z1 X2 Z13]
+ (0.002326230623158084) [Y1 Z2 Y3 Z12]
+ (0.002326230623158084) [X1 Z2 X3 Z12]
+ (0.002745836470186808) [Y0 X1 X4 Y5]
+ (0.002745836470186808) [X0 Y1 Y4 X5]
+ (0.002929768674751062) [Y0 Z1 Y2 Z9]
+ (0.002929768674751062) [X0 Z1 X2 Z9]
+ (0.002929768674751062) [Y1 Z2 Y3 Z8]
+ (0.002929768674751062) [X1 Z2 X3 Z8]
+ (0.00327697193123167) [Y0 Z1 Y2 Z3]
+ (0.00327697193123167) [X0 Z1 X2 Z3]
+ (0.0033476175306661844) [Y0 Z1 Y2 Z7]
+ (0.0033476175306661844) [X0 Z1 X2 Z7]
+ (0.0033476175306661844) [Y1 Z2 Y3 Z6]
+ (0.0033476175306661844) [X1 Z2 X3 Z6]
+ (0.0035552901955042647) [Y0 Z1 Y2 Z10]
+ (0.0035552901955042647) [X0 Z1 X2 Z10]
+ (0.0035552901955042647) [Y1 Z2 Y3 Z11]
+ (0.0035552901955042647) [X1 Z2 X3 Z11]
+ (0.005143391768825111) [Y3 Y4 X5 X6]
+ (0.005143391768825111) [X3 X4 Y5 Y6]
+ (0.005283776488402946) [Y0 X1 X12 Y13]
+ (0.005283776488402946) [X0 Y1 Y12 X13]
+ (0.005530759218631542) [Y0 Z1 Y2 Z4]
+ (0.005530759218631542) [X0 Z1 X2 Z4]
+ (0.005530759218631542) [Y1 Z2 Y3 Z5]
+ (0.005530759218631542) [X1 Z2 X3 Z5]
+ (0.006087822480561847) [Y8 X9 X12 Y13]
+ (0.006087822480561847) [X8 Y9 Y12 X13]
+ (0.006509361201177231) [Y0 X1 X8 Y9]
+ (0.006509361201177231) [X0 Y1 Y8 X9]
+ (0.006888194352970542) [Y0 X1 X6 Y7]
+ (0.006888194352970542) [X0 Y1 Y6 X7]
+ (0.006901238249797278) [Y0 Z1 Y2 Z12]
+ (0.006901238249797278) [X0 Z1 X2 Z12]
+ (0.006901238249797278) [Y1 Z2 Y3 Z13]
+ (0.006901238249797278) [X1 Z2 X3 Z13]
+ (0.007156934919856943) [Y4 X5 X8 Y9]
+ (0.007156934919856943) [X4 Y5 Y8 X9]
+ (0.00773142525077527) [Y0 X1 X10 Y11]
+ (0.00773142525077527) [X0 Y1 Y10 X11]
+ (0.008032520918821385) [Y0 Z1 Y2 Z6]
+ (0.008032520918821385) [X0 Z1 X2 Z6]
+ (0.008032520918821385) [Y1 Z2 Y3 Z7]
+ (0.008032520918821385) [X1 Z2 X3 Z7]
+ (0.009560705729135933) [Y8 X9 X10 Y11]
+ (0.009560705729135933) [X8 Y9 Y10 X11]
+ (0.011055020596132083) [Y0 Z1 Y2 Z8]
+ (0.011055020596132083) [X0 Z1 X2 Z8]
+ (0.011055020596132083) [Y1 Z2 Y3 Z9]
+ (0.011055020596132083) [X1 Z2 X3 Z9]
+ (0.011285190200840914) [Y5 Y6 X11 X12]
+ (0.011285190200840914) [X5 X6 Y11 Y12]
+ (0.011307274008848187) [Y7 Z8 Z9 Y11]
+ (0.011307274008848187) [X7 Z8 Z9 X11]
+ (0.011982389010247944) [Y4 X5 X6 Y7]
+ (0.011982389010247944) [X4 Y5 Y6 X7]
+ (0.013873381748426075) [Y6 X7 X8 Y9]
+ (0.013873381748426075) [X6 Y7 Y8 X9]
+ (0.014583648907612653) [Y0 X1 X2 Y3]
+ (0.014583648907612653) [X0 Y1 Y2 X3]
+ (0.01557720806397642) [Y2 X3 X12 Y13]
+ (0.01557720806397642) [X2 Y3 Y12 X13]
+ (0.01736611899465137) [Y6 X7 X12 Y13]
+ (0.01736611899465137) [X6 Y7 Y12 X13]
+ (0.01768006795248148) [Y4 X5 X10 Y11]
+ (0.01768006795248148) [X4 Y5 Y10 X11]
+ (0.0178251409957865) [Y6 X7 X10 Y11]
+ (0.0178251409957865) [X6 Y7 Y10 X11]
+ (0.019028242443847224) [Y3 X4 X11 Y12]
+ (0.019028242443847224) [X3 Y4 Y11 X12]
+ (0.025384657508457368) [Y2 X3 X10 Y11]
+ (0.025384657508457368) [X2 Y3 Y10 X11]
+ (0.028685183716105924) [Y10 X11 X12 Y13]
+ (0.028685183716105924) [X10 Y11 Y12 X13]
+ (0.029812424517345833) [Y6 Z7 Z8 Y10]
+ (0.029812424517345833) [X6 Z7 Z8 X10]
+ (0.029812424517345833) [Y7 Z9 Z10 Y11]
+ (0.029812424517345833) [X7 Z9 Z10 X11]
+ (0.03010462314345687) [Y6 Z7 Z9 Y10]
+ (0.03010462314345687) [X6 Z7 Z9 X10]
+ (0.03010462314345687) [Y7 Z8 Z10 Y11]
+ (0.03010462314345687) [X7 Z8 Z10 X11]
+ (0.030787505389143953) [Y6 Z8 Z9 Y10]
+ (0.030787505389143953) [X6 Z8 Z9 X10]
+ (0.031143817988967096) [Y2 X3 X6 Y7]
+ (0.031143817988967096) [X2 Y3 Y6 X7]
+ (0.035839567953353364) [Y2 X3 X4 Y5]
+ (0.035839567953353364) [X2 Y3 Y4 X5]
+ (0.03619412355904262) [Y2 X3 X8 Y9]
+ (0.03619412355904262) [X2 Y3 Y8 X9]
+ (0.03831467029480382) [Y4 X5 X12 Y13]
+ (0.03831467029480382) [X4 Y5 Y12 X13]
+ (0.10433064780651399) [Z0 Y1 Z2 Y3]
+ (0.10433064780651399) [Z0 X1 Z2 X3]
+ (-0.12133276911042297) [Y3 Z4 Z5 Z6 Y7]
+ (-0.12133276911042297) [X3 Z4 Z5 Z6 X7]
+ (-0.12133276911042296) [Y2 Z3 Z4 Z5 Y6]
+ (-0.12133276911042296) [X2 Z3 Z4 Z5 X6]
+ (3.2020768795563273e-06) [Y1 Z2 Z3 Z4 Y5]
+ (3.2020768795563273e-06) [X1 Z2 Z3 Z4 X5]
+ (3.2020768795563286e-06) [Y0 Z1 Z2 Z3 Y4]
+ (3.2020768795563286e-06) [X0 Z1 Z2 Z3 X4]
+ (0.22848106564918855) [Y7 Z8 Z9 Z10 Y11]
+ (0.22848106564918855) [X7 Z8 Z9 Z10 X11]
+ (0.2284810656491886) [Y6 Z7 Z8 Z9 Y10]
+ (0.2284810656491886) [X6 Z7 Z8 Z9 X10]
+ (-0.03276765782329042) [Z0 Y3 Z4 Z5 Z6 Y7]
+ (-0.03276765782329042) [Z0 X3 Z4 Z5 Z6 X7]
+ (-0.03276765782329042) [Z1 Y2 Z3 Z4 Z5 Y6]
+ (-0.03276765782329042) [Z1 X2 Z3 Z4 Z5 X6]
+ (-0.02711503684527309) [Z0 Y2 Z3 Z4 Z5 Y6]
+ (-0.02711503684527309) [Z0 X2 Z3 Z4 Z5 X6]
+ (-0.02711503684527309) [Z1 Y3 Z4 Z5 Z6 Y7]
+ (-0.02711503684527309) [Z1 X3 Z4 Z5 Z6 X7]
+ (-0.025996177598021097) [Y2 Z3 Z4 Z5 Y6 Z7]
+ (-0.025996177598021097) [X2 Z3 Z4 Z5 X6 Z7]
+ (-0.017561202409646127) [Y2 Z3 Z4 Z5 Y6 Z9]
+ (-0.017561202409646127) [X2 Z3 Z4 Z5 X6 Z9]
+ (-0.017561202409646127) [Y3 Z4 Z5 Z6 Y7 Z8]
+ (-0.017561202409646127) [X3 Z4 Z5 Z6 X7 Z8]
+ (-0.014564531231173006) [Y7 Z8 Z9 X10 X12 Y13]
+ (-0.014564531231173006) [Y7 Z8 Z9 Y10 Y12 Y13]
+ (-0.014564531231173006) [X7 Z8 Z9 X10 X12 X13]
+ (-0.014564531231173006) [X7 Z8 Z9 Y10 Y12 X13]
+ (-0.012215040997613958) [Y4 Z5 Y6 Y11 Z12 Y13]
+ (-0.012215040997613958) [Y4 Z5 Y6 X11 Z12 X13]
+ (-0.012215040997613958) [X4 Z5 X6 Y11 Z12 Y13]
+ (-0.012215040997613958) [X4 Z5 X6 X11 Z12 X13]
+ (-0.012215040997613958) [Y5 Z6 Y7 Y10 Z11 Y12]
+ (-0.012215040997613958) [Y5 Z6 Y7 X10 Z11 X12]
+ (-0.012215040997613958) [X5 Z6 X7 Y10 Z11 Y12]
+ (-0.012215040997613958) [X5 Z6 X7 X10 Z11 X12]
+ (-0.011756013419819227) [Y3 Z4 Z5 X6 X8 Y9]
+ (-0.011756013419819227) [Y3 Z4 Z5 Y6 Y8 Y9]
+ (-0.011756013419819227) [X3 Z4 Z5 X6 X8 X9]
+ (-0.011756013419819227) [X3 Z4 Z5 Y6 Y8 X9]
+ (-0.008764827575688734) [Y2 Z3 Z4 X5 X11 Y12]
+ (-0.008764827575688734) [Y2 Z3 Z4 Y5 Y11 Y12]
+ (-0.008764827575688734) [X2 Z3 Z4 X5 X11 X12]
+ (-0.008764827575688734) [X2 Z3 Z4 Y5 Y11 X12]
+ (-0.008764827575688734) [Y3 X4 X10 Z11 Z12 Y13]
+ (-0.008764827575688734) [Y3 Y4 Y10 Z11 Z12 Y13]
+ (-0.008764827575688734) [X3 X4 X10 Z11 Z12 X13]
+ (-0.008764827575688734) [X3 Y4 Y10 Z11 Z12 X13]
+ (-0.00812525192138102) [Y0 Z1 Z2 Y3 X8 X9]
+ (-0.00812525192138102) [X0 Z1 Z2 X3 Y8 Y9]
+ (-0.007306759928832955) [Y4 X5 X7 Z8 Z9 Y10]
+ (-0.007306759928832955) [Y4 Y5 Y7 Z8 Z9 Y10]
+ (-0.007306759928832955) [X4 X5 X7 Z8 Z9 X10]
+ (-0.007306759928832955) [X4 Y5 Y7 Z8 Z9 X10]
+ (-0.0058051889898269) [Y2 Z3 Z4 Z5 Y6 Z8]
+ (-0.0058051889898269) [X2 Z3 Z4 Z5 X6 Z8]
+ (-0.0058051889898269) [Y3 Z4 Z5 Z6 Y7 Z9]
+ (-0.0058051889898269) [X3 Z4 Z5 Z6 X7 Z9]
+ (-0.00565262097801733) [Y0 X1 X3 Z4 Z5 Y6]
+ (-0.00565262097801733) [Y0 Y1 Y3 Z4 Z5 Y6]
+ (-0.00565262097801733) [X0 X1 X3 Z4 Z5 X6]
+ (-0.00565262097801733) [X0 Y1 Y3 Z4 Z5 X6]
+ (-0.005143391768825111) [Y2 Z3 Y4 Y5 Z6 Y7]
+ (-0.005143391768825111) [Y2 Z3 Y4 X5 Z6 X7]
+ (-0.005143391768825111) [X2 Z3 X4 Y5 Z6 Y7]
+ (-0.005143391768825111) [X2 Z3 X4 X5 Z6 X7]
+ (-0.00466862031877629) [Y1 X2 X7 Z8 Z9 Y10]
+ (-0.00466862031877629) [X1 Y2 Y7 Z8 Z9 X10]
+ (-0.0045750076266391935) [Y0 Z1 Z2 Y3 X12 X13]
+ (-0.0045750076266391935) [X0 Z1 Z2 X3 Y12 Y13]
+ (-0.004424855449441847) [Y0 Z1 Z2 Y3 X4 X5]
+ (-0.004424855449441847) [X0 Z1 Z2 X3 Y4 Y5]
+ (-0.0041587973818400376) [Y3 Z4 Z5 X6 X12 Y13]
+ (-0.0041587973818400376) [Y3 Z4 Z5 Y6 Y12 Y13]
+ (-0.0041587973818400376) [X3 Z4 Z5 X6 X12 X13]
+ (-0.0041587973818400376) [X3 Z4 Z5 Y6 Y12 X13]
+ (-0.003493790359890091) [Y2 Z3 Z4 Z5 Y6 Z13]
+ (-0.003493790359890091) [X2 Z3 Z4 Z5 X6 Z13]
+ (-0.003493790359890091) [Y3 Z4 Z5 Z6 Y7 Z12]
+ (-0.003493790359890091) [X3 Z4 Z5 Z6 X7 Z12]
+ (-0.002779026799025532) [Y1 Z2 Z3 Z4 Z5 Y7]
+ (-0.002779026799025532) [X1 Z2 Z3 Z4 Z5 X7]
+ (-0.0022939566113524597) [Y1 X2 X3 Z4 Z5 Y6]
+ (-0.0022939566113524597) [X1 Y2 Y3 Z4 Z5 X6]
+ (-0.0017992194936630203) [Y0 Z1 Z2 Y3 X10 X11]
+ (-0.0017992194936630203) [X0 Z1 Z2 X3 Y10 Y11]
+ (-0.0017278753941369642) [Y1 Z2 Z3 X4 X11 Y12]
+ (-0.0017278753941369642) [X1 Z2 Z3 Y4 Y11 X12]
+ (-0.000929850796773045) [Y4 Z5 Y6 X10 Z11 X12]
+ (-0.000929850796773045) [X4 Z5 X6 Y10 Z11 Y12]
+ (-0.000929850796773045) [Y5 Z6 Y7 X11 Z12 X13]
+ (-0.000929850796773045) [X5 Z6 X7 Y11 Z12 Y13]
+ (-0.0008533856254125447) [Y1 Z2 Z3 Y4 X5 X6]
+ (-0.0008533856254125447) [X1 Z2 Z3 X4 Y5 Y6]
+ (-0.0008145313270956525) [Y2 Z3 Z4 Z5 Y6 Z10]
+ (-0.0008145313270956525) [X2 Z3 Z4 Z5 X6 Z10]
+ (-0.0008145313270956525) [Y3 Z4 Z5 Z6 Y7 Z11]
+ (-0.0008145313270956525) [X3 Z4 Z5 Z6 X7 Z11]
+ (-7.735036880589248e-05) [Y0 X1 X7 Z8 Z9 Y10]
+ (-7.735036880589248e-05) [Y0 Y1 Y7 Z8 Z9 Y10]
+ (-7.735036880589248e-05) [X0 X1 X7 Z8 Z9 X10]
+ (-7.735036880589248e-05) [X0 Y1 Y7 Z8 Z9 X10]
+ (-8.774817864439292e-06) [Y4 Z5 Z6 Z7 Z8 Y10]
+ (-8.774817864439292e-06) [X4 Z5 Z6 Z7 Z8 X10]
+ (-8.774817864439292e-06) [Y5 Z6 Z7 Z9 Z10 Y11]
+ (-8.774817864439292e-06) [X5 Z6 Z7 Z9 Z10 X11]
+ (-7.518362215572867e-06) [Y4 Z5 Z7 Z8 Z9 Y10]
+ (-7.518362215572867e-06) [X4 Z5 Z7 Z8 Z9 X10]
+ (-7.518362215572867e-06) [Y5 Z6 Z8 Z9 Z10 Y11]
+ (-7.518362215572867e-06) [X5 Z6 Z8 Z9 Z10 X11]
+ (-7.444344675797167e-06) [Y4 Z5 Z6 Z7 Z9 Y10]
+ (-7.444344675797167e-06) [X4 Z5 Z6 Z7 Z9 X10]
+ (-7.444344675797167e-06) [Y5 Z6 Z7 Z8 Z10 Y11]
+ (-7.444344675797167e-06) [X5 Z6 Z7 Z8 Z10 X11]
+ (-6.524373848392238e-06) [Y6 Z7 Z8 Z9 Z10 Y12]
+ (-6.524373848392238e-06) [X6 Z7 Z8 Z9 Z10 X12]
+ (-6.524373848392238e-06) [Y7 Z8 Z9 Z11 Z12 Y13]
+ (-6.524373848392238e-06) [X7 Z8 Z9 Z11 Z12 X13]
+ (-6.2900284330938225e-06) [Y4 Z5 Z6 Z8 Z9 Y10]
+ (-6.2900284330938225e-06) [X4 Z5 Z6 Z8 Z9 X10]
+ (-6.2900284330938225e-06) [Y5 Z7 Z8 Z9 Z10 Y11]
+ (-6.2900284330938225e-06) [X5 Z7 Z8 Z9 Z10 X11]
+ (-5.974311713323477e-06) [Y4 Z5 Z6 X7 X10 Y11]
+ (-5.974311713323477e-06) [X4 Z5 Z6 Y7 Y10 X11]
+ (-5.275883122027671e-06) [Y2 Z3 Z4 X5 X12 Y13]
+ (-5.275883122027671e-06) [X2 Z3 Z4 Y5 Y12 X13]
+ (-4.643051068408111e-06) [Y2 Z3 Z4 Y5 X10 X11]
+ (-4.643051068408111e-06) [X2 Z3 Z4 X5 Y10 Y11]
+ (-4.5565692180643775e-06) [Y4 Z5 Z6 Y7 X12 X13]
+ (-4.5565692180643775e-06) [X4 Z5 Z6 X7 Y12 Y13]
+ (-4.253224225523478e-06) [Y4 Z6 Z7 Z8 Z9 Y10]
+ (-4.253224225523478e-06) [X4 Z6 Z7 Z8 Z9 X10]
+ (-3.7696594518079268e-06) [Y6 Z8 Z9 Z10 Z11 Y12]
+ (-3.7696594518079268e-06) [X6 Z8 Z9 Z10 Z11 X12]
+ (-3.694513294394428e-06) [Y4 Y5 X10 Z11 Z12 X13]
+ (-3.694513294394428e-06) [X4 X5 Y10 Z11 Z12 Y13]
+ (-3.610297130419957e-06) [Y6 Z7 Z9 Z10 Z11 Y12]
+ (-3.610297130419957e-06) [X6 Z7 Z9 Z10 Z11 X12]
+ (-3.610297130419957e-06) [Y7 Z8 Z10 Z11 Z12 Y13]
+ (-3.610297130419957e-06) [X7 Z8 Z10 Z11 Z12 X13]
+ (-3.313145500095369e-06) [Y7 Z8 Z9 Y10 X11 X12]
+ (-3.313145500095369e-06) [X7 Z8 Z9 X10 Y11 Y12]
+ (-3.277483195359794e-06) [Y6 Z7 Z8 Z10 Z11 Y12]
+ (-3.277483195359794e-06) [X6 Z7 Z8 Z10 Z11 X12]
+ (-3.277483195359794e-06) [Y7 Z9 Z10 Z11 Z12 Y13]
+ (-3.277483195359794e-06) [X7 Z9 Z10 Z11 Z12 X13]
+ (-3.2112283482968683e-06) [Y6 Z7 Z8 Z9 Z11 Y12]
+ (-3.2112283482968683e-06) [X6 Z7 Z8 Z9 Z11 X12]
+ (-3.2112283482968683e-06) [Y7 Z8 Z9 Z10 Z12 Y13]
+ (-3.2112283482968683e-06) [X7 Z8 Z9 Z10 Z12 X13]
+ (-3.1513463111258515e-06) [Y3 Y4 X7 Z8 Z9 X10]
+ (-3.1513463111258515e-06) [X3 X4 Y7 Z8 Z9 Y10]
+ (-3.0882507112298002e-06) [Y3 Z4 Z5 Y6 X11 X12]
+ (-3.0882507112298002e-06) [X3 Z4 Z5 X6 Y11 Y12]
+ (-2.172669101430111e-06) [Y2 X3 X10 Z11 Z12 Y13]
+ (-2.172669101430111e-06) [X2 Y3 Y10 Z11 Z12 X13]
+ (-1.4548424490437363e-06) [Y2 Z3 Z4 Y5 X6 X7]
+ (-1.4548424490437363e-06) [X2 Z3 Z4 X5 Y6 Y7]
+ (-1.3304731886421252e-06) [Y5 Z6 Z7 Y8 X9 X10]
+ (-1.3304731886421252e-06) [X5 Z6 Z7 X8 Y9 Y10]
+ (-1.2283337824790442e-06) [Y5 X6 X7 Z8 Z9 Y10]
+ (-1.2283337824790442e-06) [X5 Y6 Y7 Z8 Z9 X10]
+ (-1.0358477601544873e-06) [Y6 Y7 X10 Z11 Z12 X13]
+ (-1.0358477601544873e-06) [X6 X7 Y10 Z11 Z12 Y13]
+ (-7.956895372271295e-07) [Y2 Z3 Z4 Y5 X8 X9]
+ (-7.956895372271295e-07) [X2 Z3 Z4 X5 Y8 Y9]
+ (-6.733197742222794e-07) [Y0 Z1 Z2 Z3 Y4 Z10]
+ (-6.733197742222794e-07) [X0 Z1 Z2 Z3 X4 Z10]
+ (-6.733197742222794e-07) [Y1 Z2 Z3 Z4 Y5 Z11]
+ (-6.733197742222794e-07) [X1 Z2 Z3 Z4 X5 Z11]
+ (-6.628614201527e-07) [Y8 X9 X10 Z11 Z12 Y13]
+ (-6.628614201527e-07) [X8 Y9 Y10 Z11 Z12 X13]
+ (-6.556281914491951e-07) [Y0 Z1 Y2 X10 Z11 X12]
+ (-6.556281914491951e-07) [X0 Z1 X2 Y10 Z11 Y12]
+ (-6.556281914491951e-07) [Y1 Z2 Y3 X11 Z12 X13]
+ (-6.556281914491951e-07) [X1 Z2 X3 Y11 Z12 Y13]
+ (-6.41829157449832e-07) [Y0 Z1 Y2 Y10 Z11 Y12]
+ (-6.41829157449832e-07) [X0 Z1 X2 X10 Z11 X12]
+ (-6.41829157449832e-07) [Y1 Z2 Y3 Y11 Z12 Y13]
+ (-6.41829157449832e-07) [X1 Z2 X3 X11 Z12 X13]
+ (-5.927453082672267e-07) [Y0 Z1 Z2 Z3 Y4 Z11]
+ (-5.927453082672267e-07) [X0 Z1 Z2 Z3 X4 Z11]
+ (-5.927453082672267e-07) [Y1 Z2 Z3 Z4 Y5 Z10]
+ (-5.927453082672267e-07) [X1 Z2 Z3 Z4 X5 Z10]
+ (-5.62785191128582e-07) [Y0 X1 X10 Z11 Z12 Y13]
+ (-5.62785191128582e-07) [X0 Y1 Y10 Z11 Z12 X13]
+ (-5.287660624569013e-07) [Y0 Z1 Z2 X3 X11 Y12]
+ (-5.287660624569013e-07) [Y0 Z1 Z2 Y3 Y11 Y12]
+ (-5.287660624569013e-07) [X0 Z1 Z2 X3 X11 X12]
+ (-5.287660624569013e-07) [X0 Z1 Z2 Y3 Y11 X12]
+ (-5.287660624569013e-07) [Y1 X2 X10 Z11 Z12 Y13]
+ (-5.287660624569013e-07) [Y1 Y2 Y10 Z11 Z12 Y13]
+ (-5.287660624569013e-07) [X1 X2 X10 Z11 Z12 X13]
+ (-5.287660624569013e-07) [X1 Y2 Y10 Z11 Z12 X13]
+ (-4.838052750798253e-07) [Y4 Z5 Z6 Y7 X8 X9]
+ (-4.838052750798253e-07) [X4 Z5 Z6 X7 Y8 Y9]
+ (-3.5707613289613943e-07) [Y0 Y1 X2 Z3 Z4 X5]
+ (-3.5707613289613943e-07) [X0 X1 Y2 Z3 Z4 Y5]
+ (-3.328139350601634e-07) [Y7 X8 X9 Z10 Z11 Y12]
+ (-3.328139350601634e-07) [X7 Y8 Y9 Z10 Z11 X12]
+ (-3.0868265650445167e-07) [Y1 Z2 Z3 X4 X12 Y13]
+ (-3.0868265650445167e-07) [Y1 Z2 Z3 Y4 Y12 Y13]
+ (-3.0868265650445167e-07) [X1 Z2 Z3 X4 X12 X13]
+ (-3.0868265650445167e-07) [X1 Z2 Z3 Y4 Y12 X13]
+ (-2.447323128746472e-07) [Y0 Y1 X4 Z5 Z6 X7]
+ (-2.447323128746472e-07) [X0 X1 Y4 Z5 Z6 Y7]
+ (-2.371328947832429e-07) [Y1 Z2 Z3 X4 X8 Y9]
+ (-2.371328947832429e-07) [Y1 Z2 Z3 Y4 Y8 Y9]
+ (-2.371328947832429e-07) [X1 Z2 Z3 X4 X8 X9]
+ (-2.371328947832429e-07) [X1 Z2 Z3 Y4 Y8 X9]
+ (-2.199051618388247e-07) [Y2 Y3 X4 Z5 Z6 X7]
+ (-2.199051618388247e-07) [X2 X3 Y4 Z5 Z6 Y7]
+ (-1.9332412770333193e-07) [Y0 Z1 Y2 Y3 Z4 Y5]
+ (-1.9332412770333193e-07) [Y0 Z1 Y2 X3 Z4 X5]
+ (-1.9332412770333193e-07) [X0 Z1 X2 Y3 Z4 Y5]
+ (-1.9332412770333193e-07) [X0 Z1 X2 X3 Z4 X5]
+ (-1.839420915421383e-07) [Y1 Z2 Z3 X4 X6 Y7]
+ (-1.839420915421383e-07) [Y1 Z2 Z3 Y4 Y6 Y7]
+ (-1.839420915421383e-07) [X1 Z2 Z3 X4 X6 X7]
+ (-1.839420915421383e-07) [X1 Z2 Z3 Y4 Y6 X7]
+ (-1.5510539176270624e-07) [Y0 Z1 Y2 Y4 Z5 Y6]
+ (-1.5510539176270624e-07) [X0 Z1 X2 X4 Z5 X6]
+ (-1.5510539176270624e-07) [Y1 Z2 Y3 Y5 Z6 Y7]
+ (-1.5510539176270624e-07) [X1 Z2 X3 X5 Z6 X7]
+ (-1.3807781480310107e-07) [Y0 Z1 Y2 Y5 Z6 Y7]
+ (-1.3807781480310107e-07) [Y0 Z1 Y2 X5 Z6 X7]
+ (-1.3807781480310107e-07) [X0 Z1 X2 Y5 Z6 Y7]
+ (-1.3807781480310107e-07) [X0 Z1 X2 X5 Z6 X7]
+ (-1.3807781480310107e-07) [Y1 Z2 Y3 Y4 Z5 Y6]
+ (-1.3807781480310107e-07) [Y1 Z2 Y3 X4 Z5 X6]
+ (-1.3807781480310107e-07) [X1 Z2 X3 Y4 Z5 Y6]
+ (-1.3807781480310107e-07) [X1 Z2 X3 X4 Z5 X6]
+ (-1.3807781480310104e-07) [Y0 Z1 Y2 X4 Z5 X6]
+ (-1.3807781480310104e-07) [X0 Z1 X2 Y4 Z5 Y6]
+ (-1.3807781480310104e-07) [Y1 Z2 Y3 X5 Z6 X7]
+ (-1.3807781480310104e-07) [X1 Z2 X3 Y5 Z6 Y7]
+ (-1.2919694861896926e-07) [Y0 Z1 Z2 Z3 Y4 Z5]
+ (-1.2919694861896926e-07) [X0 Z1 Z2 Z3 X4 Z5]
+ (-1.1076325599347152e-07) [Y0 Z1 Y2 Y11 Z12 Y13]
+ (-1.1076325599347152e-07) [Y0 Z1 Y2 X11 Z12 X13]
+ (-1.1076325599347152e-07) [X0 Z1 X2 Y11 Z12 Y13]
+ (-1.1076325599347152e-07) [X0 Z1 X2 X11 Z12 X13]
+ (-1.1076325599347152e-07) [Y1 Z2 Y3 Y10 Z11 Y12]
+ (-1.1076325599347152e-07) [Y1 Z2 Y3 X10 Z11 X12]
+ (-1.1076325599347152e-07) [X1 Z2 X3 Y10 Z11 Y12]
+ (-1.1076325599347152e-07) [X1 Z2 X3 X10 Z11 X12]
+ (8.057446595505265e-08) [Y1 Z2 Z3 X4 X10 Y11]
+ (8.057446595505265e-08) [Y1 Z2 Z3 Y4 Y10 Y11]
+ (8.057446595505265e-08) [X1 Z2 Z3 X4 X10 X11]
+ (8.057446595505265e-08) [X1 Z2 Z3 Y4 Y10 X11]
+ (8.649310133969222e-08) [Y0 Z1 Z2 Z3 Y4 Z9]
+ (8.649310133969222e-08) [X0 Z1 Z2 Z3 X4 Z9]
+ (8.649310133969222e-08) [Y1 Z2 Z3 Z4 Y5 Z8]
+ (8.649310133969222e-08) [X1 Z2 Z3 Z4 X5 Z8]
+ (1.8394209154213834e-07) [Y0 Z1 Z2 Z3 Y4 Z6]
+ (1.8394209154213834e-07) [X0 Z1 Z2 Z3 X4 Z6]
+ (1.8394209154213834e-07) [Y1 Z2 Z3 Z4 Y5 Z7]
+ (1.8394209154213834e-07) [X1 Z2 Z3 Z4 X5 Z7]
+ (2.199051618388247e-07) [Y2 X3 X4 Z5 Z6 Y7]
+ (2.199051618388247e-07) [X2 Y3 Y4 Z5 Z6 X7]
+ (2.447323128746472e-07) [Y0 X1 X4 Z5 Z6 Y7]
+ (2.447323128746472e-07) [X0 Y1 Y4 Z5 Z6 X7]
+ (3.2362599612293505e-07) [Y0 Z1 Z2 Z3 Y4 Z8]
+ (3.2362599612293505e-07) [X0 Z1 Z2 Z3 X4 Z8]
+ (3.2362599612293505e-07) [Y1 Z2 Z3 Z4 Y5 Z9]
+ (3.2362599612293505e-07) [X1 Z2 Z3 Z4 X5 Z9]
+ (3.328139350601634e-07) [Y7 Y8 X9 Z10 Z11 X12]
+ (3.328139350601634e-07) [X7 X8 Y9 Z10 Z11 Y12]
+ (3.5707613289613943e-07) [Y0 X1 X2 Z3 Z4 Y5]
+ (3.5707613289613943e-07) [X0 Y1 Y2 Z3 Z4 X5]
+ (4.838052750798253e-07) [Y4 Z5 Z6 X7 X8 Y9]
+ (4.838052750798253e-07) [X4 Z5 Z6 Y7 Y8 X9]
+ (5.62785191128582e-07) [Y0 Y1 X10 Z11 Z12 X13]
+ (5.62785191128582e-07) [X0 X1 Y10 Z11 Z12 Y13]
+ (6.628614201527e-07) [Y8 Y9 X10 Z11 Z12 X13]
+ (6.628614201527e-07) [X8 X9 Y10 Z11 Z12 Y13]
+ (7.956895372271295e-07) [Y2 Z3 Z4 X5 X8 Y9]
+ (7.956895372271295e-07) [X2 Z3 Z4 Y5 Y8 X9]
+ (9.306536651743258e-07) [Y0 Z1 Z2 Z3 Y4 Z13]
+ (9.306536651743258e-07) [X0 Z1 Z2 Z3 X4 Z13]
+ (9.306536651743258e-07) [Y1 Z2 Z3 Z4 Y5 Z12]
+ (9.306536651743258e-07) [X1 Z2 Z3 Z4 X5 Z12]
+ (1.0358477601544873e-06) [Y6 X7 X10 Z11 Z12 Y13]
+ (1.0358477601544873e-06) [X6 Y7 Y10 Z11 Z12 X13]
+ (1.2283337824790442e-06) [Y5 Y6 X7 Z8 Z9 X10]
+ (1.2283337824790442e-06) [X5 X6 Y7 Z8 Z9 Y10]
+ (1.2393363216787773e-06) [Y0 Z1 Z2 Z3 Y4 Z12]
+ (1.2393363216787773e-06) [X0 Z1 Z2 Z3 X4 Z12]
+ (1.2393363216787773e-06) [Y1 Z2 Z3 Z4 Y5 Z13]
+ (1.2393363216787773e-06) [X1 Z2 Z3 Z4 X5 Z13]
+ (1.3304731886421252e-06) [Y5 Z6 Z7 X8 X9 Y10]
+ (1.3304731886421252e-06) [X5 Z6 Z7 Y8 Y9 X10]
+ (1.4548424490437363e-06) [Y2 Z3 Z4 X5 X6 Y7]
+ (1.4548424490437363e-06) [X2 Z3 Z4 Y5 Y6 X7]
+ (2.172669101430111e-06) [Y2 Y3 X10 Z11 Z12 X13]
+ (2.172669101430111e-06) [X2 X3 Y10 Z11 Z12 Y13]
+ (3.0882507112298002e-06) [Y3 Z4 Z5 X6 X11 Y12]
+ (3.0882507112298002e-06) [X3 Z4 Z5 Y6 Y11 X12]
+ (3.1174479459494263e-06) [Z0 Y1 Z2 Z3 Z4 Y5]
+ (3.1174479459494263e-06) [Z0 X1 Z2 Z3 Z4 X5]
+ (3.1513463111258515e-06) [Y3 X4 X7 Z8 Z9 Y10]
+ (3.1513463111258515e-06) [X3 Y4 Y7 Z8 Z9 X10]
+ (3.313145500095369e-06) [Y7 Z8 Z9 X10 X11 Y12]
+ (3.313145500095369e-06) [X7 Z8 Z9 Y10 Y11 X12]
+ (3.3343312893668643e-06) [Y5 Z6 Z7 Z8 Z9 Y11]
+ (3.3343312893668643e-06) [X5 Z6 Z7 Z8 Z9 X11]
+ (3.694513294394428e-06) [Y4 X5 X10 Z11 Z12 Y13]
+ (3.694513294394428e-06) [X4 Y5 Y10 Z11 Z12 X13]
+ (4.18393255943899e-06) [Y7 Z8 Z9 Z10 Z11 Y13]
+ (4.18393255943899e-06) [X7 Z8 Z9 Z10 Z11 X13]
+ (4.5565692180643775e-06) [Y4 Z5 Z6 X7 X12 Y13]
+ (4.5565692180643775e-06) [X4 Z5 Z6 Y7 Y12 X13]
+ (4.643051068408111e-06) [Y2 Z3 Z4 X5 X10 Y11]
+ (4.643051068408111e-06) [X2 Z3 Z4 Y5 Y10 X11]
+ (5.275883122027671e-06) [Y2 Z3 Z4 Y5 X12 X13]
+ (5.275883122027671e-06) [X2 Z3 Z4 X5 Y12 Y13]
+ (5.974311713323477e-06) [Y4 Z5 Z6 Y7 X10 X11]
+ (5.974311713323477e-06) [X4 Z5 Z6 X7 Y10 Y11]
+ (0.0002921986261110375) [Y6 Z7 Y8 Y9 Z10 Y11]
+ (0.0002921986261110375) [Y6 Z7 Y8 X9 Z10 X11]
+ (0.0002921986261110375) [X6 Z7 X8 Y9 Z10 Y11]
+ (0.0002921986261110375) [X6 Z7 X8 X9 Z10 X11]
+ (0.0004956762314916223) [Z2 Y3 Z4 Z5 Z6 Y7]
+ (0.0004956762314916223) [Z2 X3 Z4 Z5 Z6 X7]
+ (0.0006650070219499471) [Y2 Z3 Z4 Z5 Y6 Z12]
+ (0.0006650070219499471) [X2 Z3 Z4 Z5 X6 Z12]
+ (0.0006650070219499471) [Y3 Z4 Z5 Z6 Y7 Z13]
+ (0.0006650070219499471) [X3 Z4 Z5 Z6 X7 Z13]
+ (0.0008533856254125447) [Y1 Z2 Z3 X4 X5 Y6]
+ (0.0008533856254125447) [X1 Z2 Z3 Y4 Y5 X6]
+ (0.0016095313817213737) [Y0 Z1 Z2 Z3 Z4 Y6]
+ (0.0016095313817213737) [X0 Z1 Z2 Z3 Z4 X6]
+ (0.0016095313817213737) [Y1 Z2 Z3 Z5 Z6 Y7]
+ (0.0016095313817213737) [X1 Z2 Z3 Z5 Z6 X7]
+ (0.00166760418114405) [Y0 Z1 Z3 Z4 Z5 Y6]
+ (0.00166760418114405) [X0 Z1 Z3 Z4 Z5 X6]
+ (0.00166760418114405) [Y1 Z2 Z4 Z5 Z6 Y7]
+ (0.00166760418114405) [X1 Z2 Z4 Z5 Z6 X7]
+ (0.0017278753941369642) [Y1 Z2 Z3 Y4 X11 X12]
+ (0.0017278753941369642) [X1 Z2 Z3 X4 Y11 Y12]
+ (0.0017992194936630203) [Y0 Z1 Z2 X3 X10 Y11]
+ (0.0017992194936630203) [X0 Z1 Z2 Y3 Y10 X11]
+ (0.0022939566113524597) [Y1 Y2 X3 Z4 Z5 X6]
+ (0.0022939566113524597) [X1 X2 Y3 Z4 Z5 Y6]
+ (0.0024629170071339187) [Y0 Z1 Z2 Z3 Z5 Y6]
+ (0.0024629170071339187) [X0 Z1 Z2 Z3 Z5 X6]
+ (0.0024629170071339187) [Y1 Z2 Z3 Z4 Z6 Y7]
+ (0.0024629170071339187) [X1 Z2 Z3 Z4 Z6 X7]
+ (0.003961560792496509) [Y0 Z1 Z2 Z4 Z5 Y6]
+ (0.003961560792496509) [X0 Z1 Z2 Z4 Z5 X6]
+ (0.003961560792496509) [Y1 Z3 Z4 Z5 Z6 Y7]
+ (0.003961560792496509) [X1 Z3 Z4 Z5 Z6 X7]
+ (0.004424855449441847) [Y0 Z1 Z2 X3 X4 Y5]
+ (0.004424855449441847) [X0 Z1 Z2 Y3 Y4 X5]
+ (0.0045750076266391935) [Y0 Z1 Z2 X3 X12 Y13]
+ (0.0045750076266391935) [X0 Z1 Z2 Y3 Y12 X13]
+ (0.00466862031877629) [Y1 Y2 X7 Z8 Z9 X10]
+ (0.00466862031877629) [X1 X2 Y7 Z8 Z9 Y10]
+ (0.005324835234221685) [Y2 Z3 Y4 X10 Z11 X12]
+ (0.005324835234221685) [X2 Z3 X4 Y10 Z11 Y12]
+ (0.005324835234221685) [Y3 Z4 Y5 X11 Z12 X13]
+ (0.005324835234221685) [X3 Z4 X5 Y11 Z12 Y13]
+ (0.0053686593581095746) [Y2 X3 X7 Z8 Z9 Y10]
+ (0.0053686593581095746) [Y2 Y3 Y7 Z8 Z9 Y10]
+ (0.0053686593581095746) [X2 X3 X7 Z8 Z9 X10]
+ (0.0053686593581095746) [X2 Y3 Y7 Z8 Z9 X10]
+ (0.007960880725921562) [Y4 Z5 Y6 Y10 Z11 Y12]
+ (0.007960880725921562) [X4 Z5 X6 X10 Z11 X12]
+ (0.007960880725921562) [Y5 Z6 Y7 Y11 Z12 Y13]
+ (0.007960880725921562) [X5 Z6 X7 X11 Z12 X13]
+ (0.00812525192138102) [Y0 Z1 Z2 X3 X8 Y9]
+ (0.00812525192138102) [X0 Z1 Z2 Y3 Y8 X9]
+ (0.008890731522694609) [Y4 Z5 X6 X10 Z11 Y12]
+ (0.008890731522694609) [X4 Z5 Y6 Y10 Z11 X12]
+ (0.008890731522694609) [Y5 Z6 X7 X11 Z12 Y13]
+ (0.008890731522694609) [X5 Z6 Y7 Y11 Z12 X13]
+ (0.010263414868158486) [Y2 Z3 X4 X10 Z11 Y12]
+ (0.010263414868158486) [X2 Z3 Y4 Y10 Z11 X12]
+ (0.010263414868158486) [Y3 Z4 X5 X11 Z12 Y13]
+ (0.010263414868158486) [X3 Z4 Y5 Y11 Z12 X13]
+ (0.010540425907671536) [Y6 Z7 Z8 Z9 Y10 Z13]
+ (0.010540425907671536) [X6 Z7 Z8 Z9 X10 Z13]
+ (0.010540425907671536) [Y7 Z8 Z9 Z10 Y11 Z12]
+ (0.010540425907671536) [X7 Z8 Z9 Z10 X11 Z12]
+ (0.010960074940542637) [Z4 Y7 Z8 Z9 Z10 Y11]
+ (0.010960074940542637) [Z4 X7 Z8 Z9 Z10 X11]
+ (0.010960074940542637) [Z5 Y6 Z7 Z8 Z9 Y10]
+ (0.010960074940542637) [Z5 X6 Z7 Z8 Z9 X10]
+ (0.011307274008848189) [Y6 Z7 Z8 Z9 Y10 Z11]
+ (0.011307274008848189) [X6 Z7 Z8 Z9 X10 Z11]
+ (0.014411099430130907) [Y2 Z3 Z4 Z5 Y6 Z11]
+ (0.014411099430130907) [X2 Z3 Z4 Z5 X6 Z11]
+ (0.014411099430130907) [Y3 Z4 Z5 Z6 Y7 Z10]
+ (0.014411099430130907) [X3 Z4 Z5 Z6 X7 Z10]
+ (0.01522563075722656) [Y3 Z4 Z5 X6 X10 Y11]
+ (0.01522563075722656) [Y3 Z4 Z5 Y6 Y10 Y11]
+ (0.01522563075722656) [X3 Z4 Z5 X6 X10 X11]
+ (0.01522563075722656) [X3 Z4 Z5 Y6 Y10 X11]
+ (0.015588250102380173) [Y2 Z3 Y4 Y10 Z11 Y12]
+ (0.015588250102380173) [X2 Z3 X4 X10 Z11 X12]
+ (0.015588250102380173) [Y3 Z4 Y5 Y11 Z12 Y13]
+ (0.015588250102380173) [X3 Z4 X5 X11 Z12 X13]
+ (0.018266834869375595) [Z4 Y6 Z7 Z8 Z9 Y10]
+ (0.018266834869375595) [Z4 X6 Z7 Z8 Z9 X10]
+ (0.018266834869375595) [Z5 Y7 Z8 Z9 Z10 Y11]
+ (0.018266834869375595) [Z5 X7 Z8 Z9 Z10 X11]
+ (0.019020423173039983) [Z2 Y6 Z7 Z8 Z9 Y10]
+ (0.019020423173039983) [Z2 X6 Z7 Z8 Z9 X10]
+ (0.019020423173039983) [Z3 Y7 Z8 Z9 Z10 Y11]
+ (0.019020423173039983) [Z3 X7 Z8 Z9 Z10 X11]
+ (0.020175921723535523) [Y4 Z5 Z6 X7 X11 Y12]
+ (0.020175921723535523) [Y4 Z5 Z6 Y7 Y11 Y12]
+ (0.020175921723535523) [X4 Z5 Z6 X7 X11 X12]
+ (0.020175921723535523) [X4 Z5 Z6 Y7 Y11 X12]
+ (0.020175921723535523) [Y5 X6 X10 Z11 Z12 Y13]
+ (0.020175921723535523) [Y5 Y6 Y10 Z11 Z12 Y13]
+ (0.020175921723535523) [X5 X6 X10 Z11 Z12 X13]
+ (0.020175921723535523) [X5 Y6 Y10 Z11 Z12 X13]
+ (0.024353077678068907) [Y2 Z3 Y4 Y11 Z12 Y13]
+ (0.024353077678068907) [Y2 Z3 Y4 X11 Z12 X13]
+ (0.024353077678068907) [X2 Z3 X4 Y11 Z12 Y13]
+ (0.024353077678068907) [X2 Z3 X4 X11 Z12 X13]
+ (0.024353077678068907) [Y3 Z4 Y5 Y10 Z11 Y12]
+ (0.024353077678068907) [Y3 Z4 Y5 X10 Z11 X12]
+ (0.024353077678068907) [X3 Z4 X5 Y10 Z11 Y12]
+ (0.024353077678068907) [X3 Z4 X5 X10 Z11 X12]
+ (0.024389082531149554) [Z2 Y7 Z8 Z9 Z10 Y11]
+ (0.024389082531149554) [Z2 X7 Z8 Z9 Z10 X11]
+ (0.024389082531149554) [Z3 Y6 Z7 Z8 Z9 Y10]
+ (0.024389082531149554) [Z3 X6 Z7 Z8 Z9 X10]
+ (0.025104957138844544) [Y6 Z7 Z8 Z9 Y10 Z12]
+ (0.025104957138844544) [X6 Z7 Z8 Z9 X10 Z12]
+ (0.025104957138844544) [Y7 Z8 Z9 Z10 Y11 Z13]
+ (0.025104957138844544) [X7 Z8 Z9 Z10 X11 Z13]
+ (0.030787505389143953) [Z6 Y7 Z8 Z9 Z10 Y11]
+ (0.030787505389143953) [Z6 X7 Z8 Z9 Z10 X11]
+ (0.045879470781297865) [Y0 Z2 Z3 Z4 Z5 Y6]
+ (0.045879470781297865) [X0 Z2 Z3 Z4 Z5 X6]
+ (0.05600733087780775) [Z0 Y7 Z8 Z9 Z10 Y11]
+ (0.05600733087780775) [Z0 X7 Z8 Z9 Z10 X11]
+ (0.05600733087780775) [Z1 Y6 Z7 Z8 Z9 Y10]
+ (0.05600733087780775) [Z1 X6 Z7 Z8 Z9 X10]
+ (0.056084681246613644) [Z0 Y6 Z7 Z8 Z9 Y10]
+ (0.056084681246613644) [Z0 X6 Z7 Z8 Z9 X10]
+ (0.056084681246613644) [Z1 Y7 Z8 Z9 Z10 Y11]
+ (0.056084681246613644) [Z1 X7 Z8 Z9 Z10 X11]
+ (-6.631277928309267e-05) [Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-6.631277928309267e-05) [X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-6.631277928309264e-05) [Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-6.631277928309264e-05) [X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-2.5950860068584745e-05) [Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.5950860068584745e-05) [X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.5950860068584732e-05) [Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.5950860068584732e-05) [X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.04274327701378219) [Y0 Z1 Z2 Z3 Z4 Z5 Y6]
+ (0.04274327701378219) [X0 Z1 Z2 Z3 Z4 Z5 X6]
+ (0.04274327701378219) [Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.04274327701378219) [X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-0.04764261217638303) [Y4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-0.04764261217638303) [X4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-0.04764261217638303) [Y5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-0.04764261217638303) [X5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-0.041718813839821685) [Y4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-0.041718813839821685) [X4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-0.041718813839821685) [Y5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-0.041718813839821685) [X5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-0.0395644163228932) [Y4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-0.0395644163228932) [X4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-0.0395644163228932) [Y5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0395644163228932) [X5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.039359168022053026) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (-0.039359168022053026) [X2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (-0.039359168022053026) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (-0.039359168022053026) [X3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (-0.039318051947197445) [Y4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.039318051947197445) [X4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.039318051947197445) [Y5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.039318051947197445) [X5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03560837898831251) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.03560837898831251) [X2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.029903789512624773) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (-0.029903789512624773) [X2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (-0.029903789512624773) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (-0.029903789512624773) [X3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (-0.028730779551905474) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.028730779551905474) [X2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.028730779551905474) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.028730779551905474) [X3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.02563723829602678) [Y4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-0.02563723829602678) [X4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-0.02563723829602678) [Y5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-0.02563723829602678) [X5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-0.02475546329289093) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (-0.02475546329289093) [X2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (-0.02475546329289093) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (-0.02475546329289093) [X3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (-0.024282117354692993) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.024282117354692993) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.023145130929528912) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (-0.023145130929528912) [X5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (-0.022528440196012967) [Y4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.022528440196012967) [X4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.02143381072160084) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (-0.02143381072160084) [X2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (-0.02143381072160084) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (-0.02143381072160084) [X3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251565) [Y3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.019257505095251565) [X3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.019028242443847224) [Y2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (-0.019028242443847224) [X2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (-0.01888903030494289) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-0.01888903030494289) [X2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-0.01888903030494289) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.01888903030494289) [X3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.016024603689179538) [Y5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-0.016024603689179538) [X5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-0.015225630757226556) [Y2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (-0.015225630757226556) [X2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (-0.014603704729162092) [Y3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.014603704729162092) [X3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.014564531231173003) [Y6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.014564531231173003) [X6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.011756013419819229) [Y2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.011756013419819229) [X2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.011285190200840914) [Y4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (-0.011285190200840914) [X4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (-0.009841749246962581) [Y3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (-0.009841749246962581) [X3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (-0.009612634606847246) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-0.009612634606847246) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-0.009612634606847246) [Y5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-0.009612634606847246) [X5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-0.007306759928832955) [Y4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-0.007306759928832955) [X4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005923798336561336) [Y5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (-0.005923798336561336) [X5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (-0.00565262097801733) [Y0 Y1 X2 Z3 Z4 Z5 Z6 X7]
+ (-0.00565262097801733) [X0 X1 Y2 Z3 Z4 Z5 Z6 Y7]
+ (-0.005368659358109573) [Y2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005368659358109573) [X2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.0041587973818400376) [Y2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.0041587973818400376) [X2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.0033566705638328775) [Y1 Z2 Z3 Z4 Z5 X6 X8 Y9]
+ (-0.0033566705638328775) [Y1 Z2 Z3 Z4 Z5 Y6 Y8 Y9]
+ (-0.0033566705638328775) [X1 Z2 Z3 Z4 Z5 X6 X8 X9]
+ (-0.0033566705638328775) [X1 Z2 Z3 Z4 Z5 Y6 Y8 X9]
+ (-0.0032675138544235385) [Y1 Z2 Z3 Z4 Z5 X6 X12 Y13]
+ (-0.0032675138544235385) [Y1 Z2 Z3 Z4 Z5 Y6 Y12 Y13]
+ (-0.0032675138544235385) [X1 Z2 Z3 Z4 Z5 X6 X12 X13]
+ (-0.0032675138544235385) [X1 Z2 Z3 Z4 Z5 Y6 Y12 X13]
+ (-0.002779026799025532) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7]
+ (-0.002779026799025532) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7]
+ (-0.0026860409778066137) [Y0 Z1 Z2 Z3 X4 X10 Z11 Y12]
+ (-0.0026860409778066137) [X0 Z1 Z2 Z3 Y4 Y10 Z11 X12]
+ (-0.0026860409778066137) [Y1 Z2 Z3 Z4 X5 X11 Z12 Y13]
+ (-0.0026860409778066137) [X1 Z2 Z3 Z4 Y5 Y11 Z12 X13]
+ (-0.0022939566113524597) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7]
+ (-0.0022939566113524597) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7]
+ (-0.0022939566113524597) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7]
+ (-0.0022939566113524597) [X0 Z1 X2 X3 Z4 Z5 Z6 X7]
+ (-0.0009581655836696498) [Y0 Z1 Z2 Z3 Z4 X5 X11 Y12]
+ (-0.0009581655836696498) [Y0 Z1 Z2 Z3 Z4 Y5 Y11 Y12]
+ (-0.0009581655836696498) [X0 Z1 Z2 Z3 Z4 X5 X11 X12]
+ (-0.0009581655836696498) [X0 Z1 Z2 Z3 Z4 Y5 Y11 X12]
+ (-0.0009581655836696498) [Y1 Z2 Z3 X4 X10 Z11 Z12 Y13]
+ (-0.0009581655836696498) [Y1 Z2 Z3 Y4 Y10 Z11 Z12 Y13]
+ (-0.0009581655836696498) [X1 Z2 Z3 X4 X10 Z11 Z12 X13]
+ (-0.0009581655836696498) [X1 Z2 Z3 Y4 Y10 Z11 Z12 X13]
+ (-0.0002463643756957641) [Y5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.0002463643756957641) [X5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.00013840177303550612) [Y1 Z2 Z3 Z4 Z5 X6 X10 Y11]
+ (-0.00013840177303550612) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Y11]
+ (-0.00013840177303550612) [X1 Z2 Z3 Z4 Z5 X6 X10 X11]
+ (-0.00013840177303550612) [X1 Z2 Z3 Z4 Z5 Y6 Y10 X11]
+ (-7.735036880589248e-05) [Y0 Y1 X6 Z7 Z8 Z9 Z10 X11]
+ (-7.735036880589248e-05) [X0 X1 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585305419293e-05) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585305419293e-05) [Z0 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.6103585305419293e-05) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.6103585305419293e-05) [Z1 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808795020314e-05) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.5316808795020314e-05) [Z0 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808795020314e-05) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5316808795020314e-05) [Z1 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-9.806102775044332e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-9.806102775044332e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-9.806102775044332e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-9.806102775044332e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-7.089799467394259e-06) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.089799467394259e-06) [Z2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.089799467394259e-06) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.089799467394259e-06) [Z3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-6.652209669196168e-06) [Z0 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.652209669196168e-06) [Z0 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-6.652209669196168e-06) [Z1 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.652209669196168e-06) [Z1 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.4818518336543455e-06) [Z0 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.4818518336543455e-06) [Z0 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.4818518336543455e-06) [Z1 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.4818518336543455e-06) [Z1 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-5.071480736403609e-06) [Y5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-5.071480736403609e-06) [Y5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-5.071480736403609e-06) [X5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-5.071480736403609e-06) [X5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-4.734622038640721e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-4.734622038640721e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-4.734622038640721e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-4.734622038640721e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-4.728843147138299e-06) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-4.728843147138299e-06) [Z2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-4.728843147138299e-06) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.728843147138299e-06) [Z3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.253224225523478e-06) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.253224225523478e-06) [Z4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.7696594518079268e-06) [Z6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.7696594518079268e-06) [Z6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.544395429208759e-06) [Y2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-3.544395429208759e-06) [Y2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-3.544395429208759e-06) [X2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-3.544395429208759e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-3.544395429208759e-06) [Y3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-3.544395429208759e-06) [Y3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-3.544395429208759e-06) [X3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-3.544395429208759e-06) [X3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-2.3609563202559597e-06) [Y2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-2.3609563202559597e-06) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-2.3609563202559597e-06) [X2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-2.3609563202559597e-06) [X2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-2.103215604582169e-06) [Z2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.103215604582169e-06) [Z2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.103215604582169e-06) [Z3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.103215604582169e-06) [Z3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.011122098128432e-06) [Z2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.011122098128432e-06) [Z2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.011122098128432e-06) [Z3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.011122098128432e-06) [Z3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.942946836515339e-06) [Z4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.942946836515339e-06) [Z4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.942946836515339e-06) [Z5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.942946836515339e-06) [Z5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.6541174769938513e-06) [Z4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.6541174769938513e-06) [Z4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.6541174769938513e-06) [Z5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.6541174769938513e-06) [Z5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.5224930676197047e-06) [Y2 Z3 Z4 X5 X7 Z8 Z9 Y10]
+ (-1.5224930676197047e-06) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Y10]
+ (-1.5224930676197047e-06) [X2 Z3 Z4 X5 X7 Z8 Z9 X10]
+ (-1.5224930676197047e-06) [X2 Z3 Z4 Y5 Y7 Z8 Z9 X10]
+ (-1.5224930676197047e-06) [Y3 X4 X6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930676197047e-06) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930676197047e-06) [X3 X4 X6 Z7 Z8 Z9 Z10 X11]
+ (-1.5224930676197047e-06) [X3 Y4 Y6 Z7 Z8 Z9 Z10 X11]
+ (-1.2283337824790442e-06) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (-1.2283337824790442e-06) [Y4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (-1.2283337824790442e-06) [X4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (-1.2283337824790442e-06) [X4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (-7.988770288499853e-07) [Y2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (-7.988770288499853e-07) [X2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (-7.988770288499853e-07) [Y3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (-7.988770288499853e-07) [X3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (-7.867765103989778e-07) [Y0 X1 X5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765103989778e-07) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765103989778e-07) [X0 X1 X5 Z6 Z7 Z8 Z9 X10]
+ (-7.867765103989778e-07) [X0 Y1 Y5 Z6 Z7 Z8 Z9 X10]
+ (-7.18999097513747e-07) [Y1 Y2 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.18999097513747e-07) [X1 X2 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-6.175246206959903e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X11 X12]
+ (-6.175246206959903e-07) [X1 Z2 Z3 Z4 Z5 X6 Y11 Y12]
+ (-5.471647744551827e-07) [Y0 Z1 Z2 Y3 X10 Z11 Z12 X13]
+ (-5.471647744551827e-07) [X0 Z1 Z2 X3 Y10 Z11 Z12 Y13]
+ (-4.561447179789591e-07) [Y2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (-4.561447179789591e-07) [X2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (-4.561447179789591e-07) [Y3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (-4.561447179789591e-07) [X3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (-4.523389677795042e-07) [Y1 Y2 X5 Z6 Z7 Z8 Z9 X10]
+ (-4.523389677795042e-07) [X1 X2 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-3.427323108710262e-07) [Y2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (-3.427323108710262e-07) [X2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (-3.427323108710262e-07) [Y3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (-3.427323108710262e-07) [X3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (-3.328139350601634e-07) [Y6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-3.328139350601634e-07) [Y6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-3.328139350601634e-07) [X6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-3.328139350601634e-07) [X6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-3.086826565044517e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X12 X13]
+ (-3.086826565044517e-07) [X0 Z1 Z2 Z3 Z4 X5 Y12 Y13]
+ (-2.8882935952148725e-07) [Y4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8882935952148725e-07) [Y4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-2.8882935952148725e-07) [X4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.8882935952148725e-07) [X4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-2.371328947832429e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X8 X9]
+ (-2.371328947832429e-07) [X0 Z1 Z2 Z3 Z4 X5 Y8 Y9]
+ (-1.8394209154213834e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7]
+ (-1.8394209154213834e-07) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7]
+ (-8.057446595505265e-08) [Y0 Z1 Z2 Z3 Z4 X5 X10 Y11]
+ (-8.057446595505265e-08) [X0 Z1 Z2 Z3 Z4 Y5 Y10 X11]
+ (4.53717809543726e-08) [X2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.53717809543726e-08) [Y2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.53717809543726e-08) [X3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (4.53717809543726e-08) [Y3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (8.057446595505265e-08) [Y0 Z1 Z2 Z3 Z4 Y5 X10 X11]
+ (8.057446595505265e-08) [X0 Z1 Z2 Z3 Z4 X5 Y10 Y11]
+ (9.209350645373718e-08) [Y2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350645373718e-08) [Y2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350645373718e-08) [X2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (9.209350645373718e-08) [X2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.703578355418216e-07) [Y0 X1 X7 Z8 Z9 Z10 Z11 Y12]
+ (1.703578355418216e-07) [Y0 Y1 Y7 Z8 Z9 Z10 Z11 Y12]
+ (1.703578355418216e-07) [X0 X1 X7 Z8 Z9 Z10 Z11 X12]
+ (1.703578355418216e-07) [X0 Y1 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.8394209154213834e-07) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7]
+ (1.8394209154213834e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7]
+ (2.371328947832429e-07) [Y0 Z1 Z2 Z3 Z4 X5 X8 Y9]
+ (2.371328947832429e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y8 X9]
+ (3.086826565044517e-07) [Y0 Z1 Z2 Z3 Z4 X5 X12 Y13]
+ (3.086826565044517e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y12 X13]
+ (4.523389677795042e-07) [Y1 X2 X5 Z6 Z7 Z8 Z9 Y10]
+ (4.523389677795042e-07) [X1 Y2 Y5 Z6 Z7 Z8 Z9 X10]
+ (5.471647744551827e-07) [Y0 Z1 Z2 X3 X10 Z11 Z12 Y13]
+ (5.471647744551827e-07) [X0 Z1 Z2 Y3 Y10 Z11 Z12 X13]
+ (6.175246206959903e-07) [Y1 Z2 Z3 Z4 Z5 X6 X11 Y12]
+ (6.175246206959903e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y11 X12]
+ (7.18999097513747e-07) [Y1 X2 X7 Z8 Z9 Z10 Z11 Y12]
+ (7.18999097513747e-07) [X1 Y2 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.3304731886421252e-06) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (1.3304731886421252e-06) [Y4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (1.3304731886421252e-06) [X4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (1.3304731886421252e-06) [X4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (1.6288532435061467e-06) [Y2 Z3 X4 X6 Z7 Z8 Z9 Y10]
+ (1.6288532435061467e-06) [X2 Z3 Y4 Y6 Z7 Z8 Z9 X10]
+ (1.6288532435061467e-06) [Y3 Z4 X5 X7 Z8 Z9 Z10 Y11]
+ (1.6288532435061467e-06) [X3 Z4 Y5 Y7 Z8 Z9 Z10 X11]
+ (1.6893489514452415e-06) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (1.6893489514452415e-06) [X2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (1.6893489514452415e-06) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (1.6893489514452415e-06) [X3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (2.745518400358774e-06) [Y2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (2.745518400358774e-06) [Y2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (2.745518400358774e-06) [X2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (2.745518400358774e-06) [X2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (2.745518400358774e-06) [Y3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (2.745518400358774e-06) [Y3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (2.745518400358774e-06) [X3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (2.745518400358774e-06) [X3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (3.211842019064946e-06) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (3.211842019064946e-06) [Y2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (3.211842019064946e-06) [X2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (3.211842019064946e-06) [X2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (3.211842019064946e-06) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (3.211842019064946e-06) [Y3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (3.211842019064946e-06) [X3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (3.211842019064946e-06) [X3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (3.313145500095369e-06) [Y6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (3.313145500095369e-06) [Y6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (3.313145500095369e-06) [X6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (3.313145500095369e-06) [X6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (3.3343312893668643e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (3.3343312893668643e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (4.183932559438991e-06) [Y6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (4.183932559438991e-06) [X6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (7.735036880589248e-05) [Y0 X1 X6 Z7 Z8 Z9 Z10 Y11]
+ (7.735036880589248e-05) [X0 Y1 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.0002463643756957641) [Y5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.0002463643756957641) [X5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.0004458535128840915) [Y0 Z1 X2 X6 Z7 Z8 Z9 Y10]
+ (0.0004458535128840915) [X0 Z1 Y2 Y6 Z7 Z8 Z9 X10]
+ (0.0004458535128840915) [Y1 Z2 X3 X7 Z8 Z9 Z10 Y11]
+ (0.0004458535128840915) [X1 Z2 Y3 Y7 Z8 Z9 Z10 X11]
+ (0.0005940221543005471) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005471) [Y0 Z1 Y2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005471) [X0 Z1 X2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005471) [X0 Z1 X2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005471) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005471) [Y1 Z2 Y3 X6 Z7 Z8 Z9 X10]
+ (0.0005940221543005471) [X1 Z2 X3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005471) [X1 Z2 X3 X6 Z7 Z8 Z9 X10]
+ (0.0008533856254125447) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7]
+ (0.0008533856254125447) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7]
+ (0.0008533856254125447) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7]
+ (0.0008533856254125447) [X0 Z1 Z2 Z3 X4 X5 Z6 X7]
+ (0.0010435246534907555) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z13]
+ (0.0010435246534907555) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z13]
+ (0.0010435246534907555) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z12]
+ (0.0010435246534907555) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z12]
+ (0.0012803060973496636) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z9]
+ (0.0012803060973496636) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z9]
+ (0.0012803060973496636) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z8]
+ (0.0012803060973496636) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z8]
+ (0.0013038004788126908) [Y0 Z1 Z2 Z3 Y4 Y10 Z11 Y12]
+ (0.0013038004788126908) [X0 Z1 Z2 Z3 X4 X10 Z11 X12]
+ (0.0013038004788126908) [Y1 Z2 Z3 Z4 Y5 Y11 Z12 Y13]
+ (0.0013038004788126908) [X1 Z2 Z3 Z4 X5 X11 Z12 X13]
+ (0.0022619660624823403) [Y0 Z1 Z2 Z3 Y4 Y11 Z12 Y13]
+ (0.0022619660624823403) [Y0 Z1 Z2 Z3 Y4 X11 Z12 X13]
+ (0.0022619660624823403) [X0 Z1 Z2 Z3 X4 Y11 Z12 Y13]
+ (0.0022619660624823403) [X0 Z1 Z2 Z3 X4 X11 Z12 X13]
+ (0.0022619660624823403) [Y1 Z2 Z3 Z4 Y5 Y10 Z11 Y12]
+ (0.0022619660624823403) [Y1 Z2 Z3 Z4 Y5 X10 Z11 X12]
+ (0.0022619660624823403) [X1 Z2 Z3 Z4 X5 Y10 Z11 Y12]
+ (0.0022619660624823403) [X1 Z2 Z3 Z4 X5 X10 Z11 X12]
+ (0.003989841456619304) [Y0 Z1 Z2 Z3 Y4 X10 Z11 X12]
+ (0.003989841456619304) [X0 Z1 Z2 Z3 X4 Y10 Z11 Y12]
+ (0.003989841456619304) [Y1 Z2 Z3 Z4 Y5 X11 Z12 X13]
+ (0.003989841456619304) [X1 Z2 Z3 Z4 X5 Y11 Z12 Y13]
+ (0.0041587973818400376) [Y2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.0041587973818400376) [X2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.004311038507914294) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z12]
+ (0.004311038507914294) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z12]
+ (0.004311038507914294) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z13]
+ (0.004311038507914294) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z13]
+ (0.004636976661182541) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z8]
+ (0.004636976661182541) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z8]
+ (0.004636976661182541) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z9]
+ (0.004636976661182541) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z9]
+ (0.005114473831660382) [Y0 Z1 Z2 X3 X7 Z8 Z9 Y10]
+ (0.005114473831660382) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Y10]
+ (0.005114473831660382) [X0 Z1 Z2 X3 X7 Z8 Z9 X10]
+ (0.005114473831660382) [X0 Z1 Z2 Y3 Y7 Z8 Z9 X10]
+ (0.005114473831660382) [Y1 X2 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.005114473831660382) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.005114473831660382) [X1 X2 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005114473831660382) [X1 Y2 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.005241535382803852) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z11]
+ (0.005241535382803852) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z11]
+ (0.005241535382803852) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z10]
+ (0.005241535382803852) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z10]
+ (0.005262642473076837) [Y0 Z1 Y2 X6 Z7 Z8 Z9 X10]
+ (0.005262642473076837) [X0 Z1 X2 Y6 Z7 Z8 Z9 Y10]
+ (0.005262642473076837) [Y1 Z2 Y3 X7 Z8 Z9 Z10 X11]
+ (0.005262642473076837) [X1 Z2 X3 Y7 Z8 Z9 Z10 Y11]
+ (0.005368659358109573) [Y2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005368659358109573) [X2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.005379937155839358) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z10]
+ (0.005379937155839358) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z10]
+ (0.005379937155839358) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z11]
+ (0.005379937155839358) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z11]
+ (0.00565262097801733) [Y0 X1 X2 Z3 Z4 Z5 Z6 Y7]
+ (0.00565262097801733) [X0 Y1 Y2 Z3 Z4 Z5 Z6 X7]
+ (0.0057084959859609275) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Y10]
+ (0.0057084959859609275) [X0 Z1 X2 X6 Z7 Z8 Z9 X10]
+ (0.0057084959859609275) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Y11]
+ (0.0057084959859609275) [X1 Z2 X3 X7 Z8 Z9 Z10 X11]
+ (0.005923798336561336) [Y5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (0.005923798336561336) [X5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (0.007306759928832955) [Y4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.007306759928832955) [X4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.009841749246962581) [Y3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (0.009841749246962581) [X3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (0.011285190200840914) [Y4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (0.011285190200840914) [X4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (0.011756013419819229) [Y2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.011756013419819229) [X2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.014564531231173003) [Y6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.014564531231173003) [X6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.014603704729162092) [Y3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.014603704729162092) [X3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.015225630757226556) [Y2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (0.015225630757226556) [X2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (0.016024603689179538) [Y5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (0.016024603689179538) [X5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (0.019028242443847224) [Y2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (0.019028242443847224) [X2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (0.019257505095251565) [Y3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.019257505095251565) [X3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.045879470781297865) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.045879470781297865) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-0.3693708936615608) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.3693708936615608) [X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.36937089366156073) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.36937089366156073) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.28164257767022804) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.28164257767022804) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.28164257767022793) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.28164257767022793) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.09065144207036464) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.09065144207036464) [Z0 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.09065144207036464) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.09065144207036464) [Z1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.08684737589863611) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.08684737589863611) [Z0 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.08684737589863611) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.08684737589863611) [Z1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.07635021950634999) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.07635021950634999) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.07635021950634999) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.07635021950634999) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214017) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.06752385099214017) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214017) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.06752385099214017) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03560837898831251) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.03560837898831251) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03490334337366172) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03490334337366172) [Z2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03490334337366172) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.03490334337366172) [Z3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.02459186088382992) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.02459186088382992) [Z2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.02459186088382992) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.02459186088382992) [Z3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.024282117354692996) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.024282117354692996) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.02314513092952891) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (-0.02314513092952891) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (-0.022528440196012963) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.022528440196012963) [Z4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.01953805031131467) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-0.01953805031131467) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-0.01953805031131467) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-0.01953805031131467) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-0.017091553155898796) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-0.017091553155898796) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-0.017091553155898796) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-0.017091553155898796) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-0.016024603689179538) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-0.016024603689179538) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-0.016024603689179538) [X4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-0.016024603689179538) [X4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-0.010311482489831799) [Y2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.010311482489831799) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.010311482489831799) [X2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.010311482489831799) [X2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.009841749246962581) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962581) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.009841749246962581) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962581) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209827) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209827) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209827) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008826368514209827) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008541996625454813) [Y2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454813) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454813) [X2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454813) [X2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454813) [Y3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454813) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454813) [X3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.008541996625454813) [X3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.00466862031877629) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.00466862031877629) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.003876470899336936) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.003876470899336936) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.003804066171728535) [Y0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.003804066171728535) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.003804066171728535) [X0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.003804066171728535) [X0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0034841573002178765) [Y1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0034841573002178765) [X1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.003356670563832877) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.003356670563832877) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.0032675138544235385) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.0032675138544235385) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.0021413612231015837) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.0021413612231015837) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.0017278753941369642) [Y0 Z1 Z2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (-0.0017278753941369642) [X0 Z1 Z2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (-0.0016407548553124122) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0016407548553124122) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.001452884321416889) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.001452884321416889) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.001452884321416889) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.001452884321416889) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0007870896771024439) [Y1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (-0.0007870896771024439) [X1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0005192743499487695) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 X10]
+ (-0.0005192743499487695) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Y10]
+ (-0.00019400857029756483) [Y1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.00019400857029756483) [X1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.00013840177303550612) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (-0.00013840177303550612) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (-7.141625221154189e-05) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-7.141625221154189e-05) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-7.141625221154189e-05) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.141625221154189e-05) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-5.0714807364036096e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-5.0714807364036096e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-3.1513463111258515e-06) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-3.1513463111258515e-06) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-3.0882507112298002e-06) [Y2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-3.0882507112298002e-06) [X2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-2.9885117063038555e-06) [Y3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.9885117063038555e-06) [X3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.874299071323573e-06) [Y3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-2.874299071323573e-06) [X3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-2.3609563202559597e-06) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-2.3609563202559597e-06) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.300294656220469e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-1.300294656220469e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-1.1468376507258735e-06) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.1468376507258735e-06) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.1468376507258735e-06) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.1468376507258735e-06) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.352332102843755e-07) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.352332102843755e-07) [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.352332102843755e-07) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.352332102843755e-07) [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.091637198901728e-07) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637198901728e-07) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637198901728e-07) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637198901728e-07) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637198901728e-07) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637198901728e-07) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637198901728e-07) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.091637198901728e-07) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.074305985713243e-07) [Y0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.074305985713243e-07) [X0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.074305985713243e-07) [Y1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.074305985713243e-07) [X1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.900128986152048e-07) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-7.900128986152048e-07) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.900128986152048e-07) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.900128986152048e-07) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.867765103989778e-07) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.867765103989778e-07) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.560692464651548e-07) [Y0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692464651548e-07) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692464651548e-07) [X0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692464651548e-07) [X0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692464651548e-07) [Y1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692464651548e-07) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692464651548e-07) [X1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.560692464651548e-07) [X1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-4.997018422083559e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-4.997018422083559e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-4.997018422083559e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-4.997018422083559e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-4.997018422083559e-07) [Y1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-4.997018422083559e-07) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-4.997018422083559e-07) [X1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-4.997018422083559e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-3.5682475211066863e-07) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.5682475211066863e-07) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.5682475211066863e-07) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.5682475211066863e-07) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393083570075e-07) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393083570075e-07) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393083570075e-07) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393083570075e-07) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393083570075e-07) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393083570075e-07) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.3767393083570075e-07) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393083570075e-07) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-2.8882935952148725e-07) [Y4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.8882935952148725e-07) [X4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.686381545112001e-07) [Y3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.686381545112001e-07) [X3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-1.703578355418216e-07) [Y0 X1 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.703578355418216e-07) [X0 Y1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-9.209350645373718e-08) [Y2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.209350645373718e-08) [X2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243839895e-08) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773243839895e-08) [Y0 Z1 Y2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243839895e-08) [X0 Z1 X2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773243839895e-08) [X0 Z1 X2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773243839895e-08) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773243839895e-08) [Y1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.379773243839895e-08) [X1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773243839895e-08) [X1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9742253792731144e-08) [X0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9742253792731144e-08) [Y0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.9742253792731144e-08) [X1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.9742253792731144e-08) [Y1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0474716554909741e-08) [Y0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.0474716554909741e-08) [X0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.0474716554909741e-08) [Y1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.0474716554909741e-08) [X1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (9.209350645373718e-08) [Y2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (9.209350645373718e-08) [X2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0717282183306397e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (1.0717282183306397e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (1.0717282183306397e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (1.0717282183306397e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (1.2004287493681206e-07) [X0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (1.2004287493681206e-07) [Y0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (1.2004287493681206e-07) [X1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (1.2004287493681206e-07) [Y1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (1.703578355418216e-07) [Y0 Y1 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.703578355418216e-07) [X0 X1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.3120943051534166e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (2.3120943051534166e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (2.3120943051534166e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (2.3120943051534166e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (2.686381545112001e-07) [Y3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (2.686381545112001e-07) [X3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (2.8882935952148725e-07) [Y4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.8882935952148725e-07) [X4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.0922506159990065e-07) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (4.0922506159990065e-07) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (4.0922506159990065e-07) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (4.0922506159990065e-07) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (4.0922506159990065e-07) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (4.0922506159990065e-07) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (4.0922506159990065e-07) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (4.0922506159990065e-07) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (4.4445978540241155e-07) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (4.4445978540241155e-07) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (4.4445978540241155e-07) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (4.4445978540241155e-07) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (4.68491509506465e-07) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.68491509506465e-07) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.68491509506465e-07) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (4.68491509506465e-07) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (7.246974425290543e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (7.246974425290543e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (7.246974425290543e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (7.246974425290543e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (7.246974425290543e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (7.246974425290543e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (7.246974425290543e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (7.246974425290543e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (7.867765103989778e-07) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (7.867765103989778e-07) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (1.300294656220469e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (1.300294656220469e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (2.3609563202559597e-06) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (2.3609563202559597e-06) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (2.874299071323573e-06) [Y3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (2.874299071323573e-06) [X3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (2.8836765759476904e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (2.8836765759476904e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (2.9473560115992383e-06) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.9473560115992383e-06) [X2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.9473560115992383e-06) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.9473560115992383e-06) [X3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.9885117063038555e-06) [Y3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.9885117063038555e-06) [X3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (3.0882507112298002e-06) [Y2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (3.0882507112298002e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (3.1513463111258515e-06) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (3.1513463111258515e-06) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (3.846201671166683e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (3.846201671166683e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (3.846201671166683e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (3.846201671166683e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (5.0714807364036096e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (5.0714807364036096e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (5.105526721841145e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (5.105526721841145e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (5.105526721841145e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (5.105526721841145e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (5.146496327387152e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (5.146496327387152e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (5.146496327387152e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (5.146496327387152e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (5.159350501789875e-06) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (5.159350501789875e-06) [X2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (5.159350501789875e-06) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.159350501789875e-06) [X3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.427988656301075e-06) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.427988656301075e-06) [X2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.427988656301075e-06) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.427988656301075e-06) [X3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.935867717903094e-06) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.935867717903094e-06) [X2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.935867717903094e-06) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.935867717903094e-06) [X3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.253273347887629e-06) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (7.253273347887629e-06) [X2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (7.979825793164718e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (7.979825793164718e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (7.979825793164718e-06) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (7.979825793164718e-06) [X3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (4.20554841121727e-05) [Y2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.20554841121727e-05) [X2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.20554841121727e-05) [Y3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.20554841121727e-05) [X3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00013840177303550612) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (0.00013840177303550612) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (0.00018787053389552285) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.00018787053389552285) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.00018787053389552285) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.00018787053389552285) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.00019400857029756483) [Y1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.00019400857029756483) [X1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.0002463643756957641) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0002463643756957641) [Y4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0002463643756957641) [X4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0002463643756957641) [X4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0005192743499487695) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Y10]
+ (0.0005192743499487695) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 X10]
+ (0.000715673424890902) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.000715673424890902) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.000715673424890902) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.000715673424890902) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024439) [Y1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007870896771024439) [X1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (0.0015324835230730509) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (0.0015324835230730509) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (0.0015324835230730509) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (0.0015324835230730509) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (0.0016407548553124122) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0016407548553124122) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0017278753941369642) [Y0 Z1 Z2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (0.0017278753941369642) [X0 Z1 Z2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (0.0024464971554158696) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (0.0024464971554158696) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (0.0024464971554158696) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (0.0024464971554158696) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (0.0032675138544235385) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.0032675138544235385) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.003356670563832877) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.003356670563832877) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.0034841573002178765) [Y1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0034841573002178765) [X1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.003876470899336936) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.003876470899336936) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.00466862031877629) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.00466862031877629) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.004767272188278106) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (0.004767272188278106) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (0.004767272188278106) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (0.004767272188278106) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (0.005286546538226876) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (0.005286546538226876) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (0.005286546538226876) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (0.005286546538226876) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (0.005408954422409987) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (0.005408954422409987) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (0.005408954422409987) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (0.005408954422409987) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (0.005923798336561336) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561336) [Y4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (0.005923798336561336) [X4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561336) [X4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (0.010715508469796752) [Y2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.010715508469796752) [X2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.010715508469796752) [Y3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010715508469796752) [X3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.010757563953908925) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.010757563953908925) [X2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.010757563953908925) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010757563953908925) [X3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.014603704729162092) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.014603704729162092) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.014603704729162092) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.014603704729162092) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.01929956057936374) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01929956057936374) [Y2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.01929956057936374) [X2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01929956057936374) [X2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.01929956057936374) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.01929956057936374) [Y3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.01929956057936374) [X3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.01929956057936374) [X3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0585919887338618) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0585919887338618) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (5.7759505270728144e-05) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.7759505270728144e-05) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.7759505270728144e-05) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.7759505270728144e-05) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.07165035181002592) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.07165035181002592) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.07165035181002595) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.07165035181002595) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251565) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.019257505095251565) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.010311482489831799) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.010311482489831799) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008826368514209827) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209827) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.007597464029770599) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.007597464029770599) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.007597464029770599) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.007597464029770599) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311861) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311861) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311861) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311861) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311861) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311861) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311861) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311861) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005348051582676613) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005348051582676613) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005348051582676613) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005348051582676613) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.003804066171728535) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.003804066171728535) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0029841661681219212) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-0.0029841661681219212) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-0.0029841661681219212) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-0.0029841661681219212) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-0.00244649715541587) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (-0.00244649715541587) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (-0.0022494124470939835) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0022494124470939835) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0022494124470939835) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0022494124470939835) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0021413612231015833) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.0021413612231015833) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.001863894282458737) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.001863894282458737) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.001863894282458737) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.001863894282458737) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.001863894282458737) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.001863894282458737) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.001863894282458737) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.001863894282458737) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.001640754855312412) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.001640754855312412) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.001640754855312412) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.001640754855312412) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0012223378081538284) [Y0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538284) [Y0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538284) [X0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538284) [X0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538284) [Y1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538284) [Y1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538284) [X1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0012223378081538284) [X1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0010283292378562635) [Y0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0010283292378562635) [X0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0010283292378562635) [Y1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0010283292378562635) [X1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.1463061452758899e-05) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.1463061452758899e-05) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.874299071323573e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-2.874299071323573e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-2.874299071323573e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-2.874299071323573e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.300294656220469e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-1.300294656220469e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-1.300294656220469e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-1.300294656220469e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-1.0444941297653458e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-1.0444941297653458e-06) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-1.0444941297653458e-06) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-1.0444941297653458e-06) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-9.956079229654066e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-9.956079229654066e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-9.956079229654066e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.956079229654066e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.105515036817915e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-8.105515036817915e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-8.105515036817915e-07) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.105515036817915e-07) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.661347212860195e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-7.661347212860195e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-7.661347212860195e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-7.661347212860195e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-7.540341413558876e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-7.540341413558876e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-7.18999097513747e-07) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.18999097513747e-07) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.876621658011838e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-6.876621658011838e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-6.876621658011838e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-6.876621658011838e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-6.175246206959903e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-6.175246206959903e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-4.523389677795042e-07) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.523389677795042e-07) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.0767325316384973e-07) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-3.0767325316384973e-07) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.0767325316384973e-07) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.0767325316384973e-07) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.0134714588652994e-07) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.0134714588652994e-07) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.904599884094581e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-2.904599884094581e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-2.904599884094581e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-2.904599884094581e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-2.666731754456804e-07) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.666731754456804e-07) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.666731754456804e-07) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.666731754456804e-07) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.8505641928361503e-07) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (-1.8505641928361503e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309316024613e-07) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.6569309316024613e-07) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309316024613e-07) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.6569309316024613e-07) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.8505641928361503e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (1.8505641928361503e-07) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (2.6863815451120014e-07) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.6863815451120014e-07) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.6863815451120014e-07) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.6863815451120014e-07) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714588652994e-07) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (3.0134714588652994e-07) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.523389677795042e-07) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (4.523389677795042e-07) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (4.670402390467761e-07) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.670402390467761e-07) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.670402390467761e-07) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (4.670402390467761e-07) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (6.175246206959903e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (6.175246206959903e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (7.18999097513747e-07) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.18999097513747e-07) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.540341413558876e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (7.540341413558876e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (8.94947648731904e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (8.94947648731904e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (1.7924939576602192e-06) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.7924939576602192e-06) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.7924939576602192e-06) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.7924939576602192e-06) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.88367657594769e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (2.88367657594769e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (2.9885117063038555e-06) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.9885117063038555e-06) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.9885117063038555e-06) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.9885117063038555e-06) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.253273347887629e-06) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.253273347887629e-06) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.401710973490429e-05) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.401710973490429e-05) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.401710973490429e-05) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.401710973490429e-05) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.580960369256451e-05) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.580960369256451e-05) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.580960369256451e-05) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.580960369256451e-05) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0005192743499487695) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (0.0005192743499487695) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (0.0005192743499487695) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (0.0005192743499487695) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (0.0007870896771024439) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024439) [Y0 Z1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024439) [X0 Z1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024439) [X0 Z1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0011726348316441848) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0011726348316441848) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0011726348316441848) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0011726348316441848) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0012366478019245426) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (0.0012366478019245426) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (0.0012366478019245426) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (0.0012366478019245426) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (0.0022009640695004485) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0022009640695004485) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0022009640695004485) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0022009640695004485) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798013) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798013) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002394972639798013) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798013) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002394972639798013) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002394972639798013) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.002394972639798013) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002394972639798013) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.00244649715541587) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (0.00244649715541587) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (0.003804066171728535) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.003804066171728535) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.003876470899336936) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.003876470899336936) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.003876470899336936) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.003876470899336936) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.0042208139700464645) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (0.0042208139700464645) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (0.0042208139700464645) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (0.0042208139700464645) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (0.008826368514209827) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.008826368514209827) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.010311482489831799) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010311482489831799) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.019257505095251565) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.019257505095251565) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0585919887338618) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0585919887338618) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.398700901425048e-05) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.398700901425048e-05) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.3987009014250477e-05) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.3987009014250477e-05) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0034841573002178765) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0034841573002178765) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.002984166168121921) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.002984166168121921) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.00019400857029756483) [Y0 Z1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.00019400857029756483) [X0 Z1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061452758899e-05) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061452758899e-05) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.792493957660219e-06) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.792493957660219e-06) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.540341413558876e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413558876e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-7.540341413558876e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413558876e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.8505641928361506e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.8505641928361506e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.8505641928361506e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.8505641928361506e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714588652994e-07) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.0134714588652994e-07) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.0134714588652994e-07) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.0134714588652994e-07) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (8.94947648731904e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (8.94947648731904e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (1.792493957660219e-06) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.792493957660219e-06) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756483) [Y0 Z1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756483) [X0 Z1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002984166168121921) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.002984166168121921) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.0034841573002178765) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0034841573002178765) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
  (-73.13873231352525) [I0]
+ (-0.18066792656583291) [Z7]
+ (-0.18066792656583286) [Z6]
+ (-0.15961432501809764) [Z4]
+ (-0.15961432501809764) [Z5]
+ (0.174199561550558) [Z2]
+ (0.17419956155055805) [Z3]
+ (0.22757269005453595) [Z0]
+ (0.22757269005453612) [Z1]
+ (-8.194261372280368e-06) [Y4 Y6]
+ (-8.194261372280368e-06) [X4 X6]
+ (7.95441317616607e-06) [Y5 Y7]
+ (7.95441317616607e-06) [X5 X7]
+ (0.11270386920332205) [Z4 Z6]
+ (0.11270386920332205) [Z5 Z7]
+ (0.11952438964682661) [Z0 Z4]
+ (0.11952438964682661) [Z1 Z5]
+ (0.13401715261963687) [Z0 Z6]
+ (0.13401715261963687) [Z1 Z7]
+ (0.13734953064261307) [Z0 Z5]
+ (0.13734953064261307) [Z1 Z4]
+ (0.13766872645852574) [Z2 Z4]
+ (0.13766872645852574) [Z3 Z5]
+ (0.14138905291942794) [Z4 Z7]
+ (0.14138905291942794) [Z5 Z6]
+ (0.14722943218766166) [Z2 Z5]
+ (0.14722943218766166) [Z3 Z4]
+ (0.14926355147388884) [Z4 Z5]
+ (0.14973486803496916) [Z2 Z6]
+ (0.14973486803496916) [Z3 Z7]
+ (0.15138327161428822) [Z0 Z7]
+ (0.15138327161428822) [Z1 Z6]
+ (0.15435748657223605) [Z6 Z7]
+ (0.15582269051553102) [Z2 Z7]
+ (0.15582269051553102) [Z3 Z6]
+ (0.16756653265461258) [Z0 Z2]
+ (0.16756653265461258) [Z1 Z3]
+ (0.18143991440303864) [Z0 Z3]
+ (0.18143991440303864) [Z1 Z2]
+ (0.1939253461327017) [Z0 Z1]
+ (0.2200397733437609) [Z2 Z3]
+ (-7.037887510703044e-06) [Y4 Z5 Y6]
+ (-7.037887510703044e-06) [X4 Z5 X6]
+ (-7.037887510703042e-06) [Y5 Z6 Y7]
+ (-7.037887510703042e-06) [X5 Z6 X7]
+ (-0.02868518371610588) [Y4 Y5 X6 X7]
+ (-0.02868518371610588) [X4 X5 Y6 Y7]
+ (-0.017825140995786443) [Y0 Y1 X4 X5]
+ (-0.017825140995786443) [X0 X1 Y4 Y5]
+ (-0.017366118994651358) [Y0 Y1 X6 X7]
+ (-0.017366118994651358) [X0 X1 Y6 Y7]
+ (-0.013873381748426087) [Y0 Y1 X2 X3]
+ (-0.013873381748426087) [X0 X1 Y2 Y3]
+ (-0.009560705729135933) [Y2 Y3 X4 X5]
+ (-0.009560705729135933) [X2 X3 Y4 Y5]
+ (-0.006087822480561857) [Y2 Y3 X6 X7]
+ (-0.006087822480561857) [X2 X3 Y6 Y7]
+ (-0.000292198626111055) [Y1 Y2 X3 X4]
+ (-0.000292198626111055) [X1 X2 Y3 Y4]
+ (-8.194261372280368e-06) [Z4 Y5 Z6 Y7]
+ (-8.194261372280368e-06) [Z4 X5 Z6 X7]
+ (-2.8909678817511698e-06) [Z0 Y5 Z6 Y7]
+ (-2.8909678817511698e-06) [Z0 X5 Z6 X7]
+ (-2.8909678817511698e-06) [Z1 Y4 Z5 Y6]
+ (-2.8909678817511698e-06) [Z1 X4 Z5 X6]
+ (-1.8551201216333243e-06) [Z0 Y4 Z5 Y6]
+ (-1.8551201216333243e-06) [Z0 X4 Z5 X6]
+ (-1.8551201216333243e-06) [Z1 Y5 Z6 Y7]
+ (-1.8551201216333243e-06) [Z1 X5 Z6 X7]
+ (-1.5973171978820999e-06) [Z2 Y4 Z5 Y6]
+ (-1.5973171978820999e-06) [Z2 X4 Z5 X6]
+ (-1.5973171978820999e-06) [Z3 Y5 Z6 Y7]
+ (-1.5973171978820999e-06) [Z3 X5 Z6 X7]
+ (-1.0358477601178457e-06) [Y0 X1 X5 Y6]
+ (-1.0358477601178457e-06) [Y0 Y1 Y5 Y6]
+ (-1.0358477601178457e-06) [X0 X1 X5 X6]
+ (-1.0358477601178457e-06) [X0 Y1 Y5 X6]
+ (-9.344557777276409e-07) [Z2 Y5 Z6 Y7]
+ (-9.344557777276409e-07) [Z2 X5 Z6 X7]
+ (-9.344557777276409e-07) [Z3 Y4 Z5 Y6]
+ (-9.344557777276409e-07) [Z3 X4 Z5 X6]
+ (6.628614201544589e-07) [Y2 X3 X5 Y6]
+ (6.628614201544589e-07) [Y2 Y3 Y5 Y6]
+ (6.628614201544589e-07) [X2 X3 X5 X6]
+ (6.628614201544589e-07) [X2 Y3 Y5 X6]
+ (7.95441317616607e-06) [Y4 Z5 Y6 Z7]
+ (7.95441317616607e-06) [X4 Z5 X6 Z7]
+ (0.000292198626111055) [Y1 X2 X3 Y4]
+ (0.000292198626111055) [X1 Y2 Y3 X4]
+ (0.006087822480561857) [Y2 X3 X6 Y7]
+ (0.006087822480561857) [X2 Y3 Y6 X7]
+ (0.009560705729135933) [Y2 X3 X4 Y5]
+ (0.009560705729135933) [X2 Y3 Y4 X5]
+ (0.011307274008848137) [Y1 Z2 Z3 Y5]
+ (0.011307274008848137) [X1 Z2 Z3 X5]
+ (0.013873381748426087) [Y0 X1 X2 Y3]
+ (0.013873381748426087) [X0 Y1 Y2 X3]
+ (0.017366118994651358) [Y0 X1 X6 Y7]
+ (0.017366118994651358) [X0 Y1 Y6 X7]
+ (0.017825140995786443) [Y0 X1 X4 Y5]
+ (0.017825140995786443) [X0 Y1 Y4 X5]
+ (0.02868518371610588) [Y4 X5 X6 Y7]
+ (0.02868518371610588) [X4 Y5 Y6 X7]
+ (0.029812424517345733) [Y0 Z1 Z2 Y4]
+ (0.029812424517345733) [X0 Z1 Z2 X4]
+ (0.029812424517345733) [Y1 Z3 Z4 Y5]
+ (0.029812424517345733) [X1 Z3 Z4 X5]
+ (0.030104623143456785) [Y0 Z1 Z3 Y4]
+ (0.030104623143456785) [X0 Z1 Z3 X4]
+ (0.030104623143456785) [Y1 Z2 Z4 Y5]
+ (0.030104623143456785) [X1 Z2 Z4 X5]
+ (0.030787505389143842) [Y0 Z2 Z3 Y4]
+ (0.030787505389143842) [X0 Z2 Z3 X4]
+ (0.04375263801066042) [Y0 Z1 Z2 Z3 Y4]
+ (0.04375263801066042) [X0 Z1 Z2 Z3 X4]
+ (0.04375263801066044) [Y1 Z2 Z3 Z4 Y5]
+ (0.04375263801066044) [X1 Z2 Z3 Z4 X5]
+ (-0.01456453123117297) [Y1 Z2 Z3 X4 X6 Y7]
+ (-0.01456453123117297) [Y1 Z2 Z3 Y4 Y6 Y7]
+ (-0.01456453123117297) [X1 Z2 Z3 X4 X6 X7]
+ (-0.01456453123117297) [X1 Z2 Z3 Y4 Y6 X7]
+ (-6.524373848564226e-06) [Y0 Z1 Z2 Z3 Z4 Y6]
+ (-6.524373848564226e-06) [X0 Z1 Z2 Z3 Z4 X6]
+ (-6.524373848564226e-06) [Y1 Z2 Z3 Z5 Z6 Y7]
+ (-6.524373848564226e-06) [X1 Z2 Z3 Z5 Z6 X7]
+ (-3.769659452029595e-06) [Y0 Z2 Z3 Z4 Z5 Y6]
+ (-3.769659452029595e-06) [X0 Z2 Z3 Z4 Z5 X6]
+ (-3.610297130611317e-06) [Y0 Z1 Z3 Z4 Z5 Y6]
+ (-3.610297130611317e-06) [X0 Z1 Z3 Z4 Z5 X6]
+ (-3.610297130611317e-06) [Y1 Z2 Z4 Z5 Z6 Y7]
+ (-3.610297130611317e-06) [X1 Z2 Z4 Z5 Z6 X7]
+ (-3.313145500114234e-06) [Y1 Z2 Z3 Y4 X5 X6]
+ (-3.313145500114234e-06) [X1 Z2 Z3 X4 Y5 Y6]
+ (-3.277483195560838e-06) [Y0 Z1 Z2 Z4 Z5 Y6]
+ (-3.277483195560838e-06) [X0 Z1 Z2 Z4 Z5 X6]
+ (-3.277483195560838e-06) [Y1 Z3 Z4 Z5 Z6 Y7]
+ (-3.277483195560838e-06) [X1 Z3 Z4 Z5 Z6 X7]
+ (-3.211228348449993e-06) [Y0 Z1 Z2 Z3 Z5 Y6]
+ (-3.211228348449993e-06) [X0 Z1 Z2 Z3 Z5 X6]
+ (-3.211228348449993e-06) [Y1 Z2 Z3 Z4 Z6 Y7]
+ (-3.211228348449993e-06) [X1 Z2 Z3 Z4 Z6 X7]
+ (-1.0358477601178457e-06) [Y0 Y1 X4 Z5 Z6 X7]
+ (-1.0358477601178457e-06) [X0 X1 Y4 Z5 Z6 Y7]
+ (-6.628614201544589e-07) [Y2 X3 X4 Z5 Z6 Y7]
+ (-6.628614201544589e-07) [X2 Y3 Y4 Z5 Z6 X7]
+ (-3.328139350504794e-07) [Y1 X2 X3 Z4 Z5 Y6]
+ (-3.328139350504794e-07) [X1 Y2 Y3 Z4 Z5 X6]
+ (3.328139350504794e-07) [Y1 Y2 X3 Z4 Z5 X6]
+ (3.328139350504794e-07) [X1 X2 Y3 Z4 Z5 Y6]
+ (6.628614201544589e-07) [Y2 Y3 X4 Z5 Z6 X7]
+ (6.628614201544589e-07) [X2 X3 Y4 Z5 Z6 Y7]
+ (1.0358477601178457e-06) [Y0 X1 X4 Z5 Z6 Y7]
+ (1.0358477601178457e-06) [X0 Y1 Y4 Z5 Z6 X7]
+ (3.313145500114234e-06) [Y1 Z2 Z3 X4 X5 Y6]
+ (3.313145500114234e-06) [X1 Z2 Z3 Y4 Y5 X6]
+ (4.183932559373347e-06) [Y1 Z2 Z3 Z4 Z5 Y7]
+ (4.183932559373347e-06) [X1 Z2 Z3 Z4 Z5 X7]
+ (0.00029219862611105495) [Y0 Z1 Y2 Y3 Z4 Y5]
+ (0.00029219862611105495) [Y0 Z1 Y2 X3 Z4 X5]
+ (0.00029219862611105495) [X0 Z1 X2 Y3 Z4 Y5]
+ (0.00029219862611105495) [X0 Z1 X2 X3 Z4 X5]
+ (0.010540425907671508) [Y0 Z1 Z2 Z3 Y4 Z7]
+ (0.010540425907671508) [X0 Z1 Z2 Z3 X4 Z7]
+ (0.010540425907671508) [Y1 Z2 Z3 Z4 Y5 Z6]
+ (0.010540425907671508) [X1 Z2 Z3 Z4 X5 Z6]
+ (0.011307274008848137) [Y0 Z1 Z2 Z3 Y4 Z5]
+ (0.011307274008848137) [X0 Z1 Z2 Z3 X4 Z5]
+ (0.025104957138844478) [Y0 Z1 Z2 Z3 Y4 Z6]
+ (0.025104957138844478) [X0 Z1 Z2 Z3 X4 Z6]
+ (0.025104957138844478) [Y1 Z2 Z3 Z4 Y5 Z7]
+ (0.025104957138844478) [X1 Z2 Z3 Z4 X5 Z7]
+ (0.030787505389143842) [Z0 Y1 Z2 Z3 Z4 Y5]
+ (0.030787505389143842) [Z0 X1 Z2 Z3 Z4 X5]
+ (-5.105396549895087e-06) [Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (-5.105396549895087e-06) [X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-5.105396549895083e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Y6]
+ (-5.105396549895083e-06) [X0 Z1 Z2 Z3 Z4 Z5 X6]
+ (-0.01456453123117297) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7]
+ (-0.01456453123117297) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7]
+ (-3.769659452029595e-06) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (-3.769659452029595e-06) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-3.328139350504794e-07) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7]
+ (-3.328139350504794e-07) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7]
+ (-3.328139350504794e-07) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7]
+ (-3.328139350504794e-07) [X0 Z1 X2 X3 Z4 Z5 Z6 X7]
+ (3.313145500114234e-06) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7]
+ (3.313145500114234e-06) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7]
+ (3.313145500114234e-06) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7]
+ (3.313145500114234e-06) [X0 Z1 Z2 Z3 X4 X5 Z6 X7]
+ (4.183932559373347e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7]
+ (4.183932559373347e-06) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7]
+ (0.01456453123117297) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7]
+ (0.01456453123117297) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7]
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_quantum_chemistry.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
(-46.46390678868897+0j) [] +
(-0.014583648907612741+0j) [X0 X1 Y2 Y3] +
(-3.5707613293267043e-07+0j) [X0 X1 Y2 Z3 Z4 Y5] +
(-0.005652620978017366+0j) [X0 X1 Y2 Z3 Z4 Z5 Z6 Y7] +
(-0.008826368514209844+0j) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.792493957818554e-06+0j) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-3.5707613293267043e-07+0j) [X0 X1 X3 X4] +
(-0.005652620978017367+0j) [X0 X1 X3 Z4 Z5 X6] +
(-0.008826368514209844+0j) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.7924939578185542e-06+0j) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.0027458364701868137+0j) [X0 X1 Y4 Y5] +
(-2.447323128996551e-07+0j) [X0 X1 Y4 Z5 Z6 Y7] +
(-7.867765104770313e-07+0j) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.003804066171728546+0j) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.447323128996551e-07+0j) [X0 X1 X5 X6] +
(-7.867765104770313e-07+0j) [X0 X1 X5 Z6 Z7 Z8 Z9 X10] +
(-0.003804066171728546+0j) [X0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.006888194352970544+0j) [X0 X1 Y6 Y7] +
(-7.735036880588225e-05+0j) [X0 X1 Y6 Z7 Z8 Z9 Z10 Y11] +
(1.7035783555108094e-07+0j) [X0 X1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.735036880588223e-05+0j) [X0 X1 X7 Z8 Z9 X10] +
(1.7035783555108094e-07+0j) [X0 X1 X7 Z8 Z9 Z10 Z11 X12] +
(-0.006509361201177245+0j) [X0 X1 Y8 Y9] +
(-0.007731425250775296+0j) [X0 X1 Y10 Y11] +
(5.62785191172058e-07+0j) [X0 X1 Y10 Z11 Z12 Y13] +
(5.62785191172058e-07+0j) [X0 X1 X11 X12] +
(-0.0052837764884029696+0j) [X0 X1 Y12 Y13] +
(0.014583648907612741+0j) [X0 Y1 Y2 X3] +
(3.5707613293267043e-07+0j) [X0 Y1 Y2 Z3 Z4 X5] +
(0.005652620978017366+0j) [X0 Y1 Y2 Z3 Z4 Z5 Z6 X7] +
(0.008826368514209844+0j) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-1.792493957818554e-06+0j) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.5707613293267043e-07+0j) [X0 Y1 Y3 X4] +
(-0.005652620978017367+0j) [X0 Y1 Y3 Z4 Z5 X6] +
(-0.008826368514209844+0j) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.7924939578185542e-06+0j) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0027458364701868137+0j) [X0 Y1 Y4 X5] +
(2.447323128996551e-07+0j) [X0 Y1 Y4 Z5 Z6 X7] +
(7.867765104770313e-07+0j) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.003804066171728546+0j) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.447323128996551e-07+0j) [X0 Y1 Y5 X6] +
(-7.867765104770313e-07+0j) [X0 Y1 Y5 Z6 Z7 Z8 Z9 X10] +
(-0.003804066171728546+0j) [X0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.006888194352970544+0j) [X0 Y1 Y6 X7] +
(7.735036880588225e-05+0j) [X0 Y1 Y6 Z7 Z8 Z9 Z10 X11] +
(-1.7035783555108094e-07+0j) [X0 Y1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-7.735036880588223e-05+0j) [X0 Y1 Y7 Z8 Z9 X10] +
(1.7035783555108094e-07+0j) [X0 Y1 Y7 Z8 Z9 Z10 Z11 X12] +
(0.006509361201177245+0j) [X0 Y1 Y8 X9] +
(0.007731425250775296+0j) [X0 Y1 Y10 X11] +
(-5.62785191172058e-07+0j) [X0 Y1 Y10 Z11 Z12 X13] +
(5.62785191172058e-07+0j) [X0 Y1 Y11 X12] +
(0.0052837764884029696+0j) [X0 Y1 Y12 X13] +
(0.12507032579772231+0j) [X0 Z1 X2] +
(-1.9332412771343883e-07+0j) [X0 Z1 X2 X3 Z4 X5] +
(-0.0022939566113524632+0j) [X0 Z1 X2 X3 Z4 Z5 Z6 X7] +
(-0.0016407548553124317+0j) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(3.013471459168116e-07+0j) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.9332412771343883e-07+0j) [X0 Z1 X2 Y3 Z4 Y5] +
(-0.0022939566113524632+0j) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7] +
(-0.0016407548553124317+0j) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(3.013471459168116e-07+0j) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.003276971931231688+0j) [X0 Z1 X2 Z3] +
(-1.5510539177941005e-07+0j) [X0 Z1 X2 X4 Z5 X6] +
(-1.1468376508414694e-06+0j) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.00759746402977063+0j) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.380778148181863e-07+0j) [X0 Z1 X2 Y4 Z5 Y6] +
(-7.900128986923677e-07+0j) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.005348051582676637+0j) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0055307592186315535+0j) [X0 Z1 X2 Z4] +
(-1.380778148181863e-07+0j) [X0 Z1 X2 X5 Z6 X7] +
(-3.376739308740483e-07+0j) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0018638942824587446+0j) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.380778148181863e-07+0j) [X0 Z1 X2 Y5 Z6 Y7] +
(-3.376739308740483e-07+0j) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0018638942824587446+0j) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0011059037691896936+0j) [X0 Z1 X2 Z5] +
(0.005708495985960965+0j) [X0 Z1 X2 X6 Z7 Z8 Z9 X10] +
(-8.352332103652438e-07+0j) [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 X12] +
1.9742253794014717e-08j [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.00526264247307686+0j) [X0 Z1 X2 Y6 Z7 Z8 Z9 Y10] +
(-8.074305986486427e-07+0j) [X0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.008032520918821373+0j) [X0 Z1 X2 Z6] +
(0.0005940221543005585+0j) [X0 Z1 X2 X7 Z8 Z9 Z10 X11] +
(-8.379773243913243e-08+0j) [X0 Z1 X2 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005940221543005585+0j) [X0 Z1 X2 Y7 Z8 Z9 Z10 Y11] +
(-8.379773243913243e-08+0j) [X0 Z1 X2 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0033476175306661705+0j) [X0 Z1 X2 Z7] +
(0.011055020596132108+0j) [X0 Z1 X2 Z8] +
(0.002929768674751065+0j) [X0 Z1 X2 Z9] +
(-6.418291575036267e-07+0j) [X0 Z1 X2 X10 Z11 X12] +
(-6.556281915019352e-07+0j) [X0 Z1 X2 Y10 Z11 Y12] +
(0.003555290195504337+0j) [X0 Z1 X2 Z10] +
(-1.1076325599025838e-07+0j) [X0 Z1 X2 X11 Z12 X13] +
(-1.1076325599025838e-07+0j) [X0 Z1 X2 Y11 Z12 Y13] +
(0.001756070701841277+0j) [X0 Z1 X2 Z11] +
(0.006901238249797298+0j) [X0 Z1 X2 Z12] +
(0.0023262306231580827+0j) [X0 Z1 X2 Z13] +
(-3.568247521491018e-07+0j) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.002249412447093992+0j) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.0474716555222244e-08+0j) [X0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.00044585351288410277+0j) [X0 Z1 Y2 Y6 Z7 Z8 Z9 X10] +
(-1.9742253793703326e-08+0j) [X0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004424855449441861+0j) [X0 Z1 Z2 X3 Y4 Y5] +
(-4.5233896781831927e-07+0j) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0034841573002178917+0j) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-8.09163719967421e-07+0j) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 X10] +
(-0.005733569747311883+0j) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004684903388155202+0j) [X0 Z1 Z2 X3 Y6 Y7] +
(0.004668620318776303+0j) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Y11] +
(-7.18999097590114e-07+0j) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005114473831660406+0j) [X0 Z1 Z2 X3 X7 Z8 Z9 X10] +
(-7.560692465455075e-07+0j) [X0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 X12] +
(-0.008125251921381043+0j) [X0 Z1 Z2 X3 Y8 Y9] +
(-0.0017992194936630602+0j) [X0 Z1 Z2 X3 Y10 Y11] +
(-5.471647745115407e-07+0j) [X0 Z1 Z2 X3 Y10 Z11 Z12 Y13] +
(-5.287660625135047e-07+0j) [X0 Z1 Z2 X3 X11 X12] +
(-0.004575007626639214+0j) [X0 Z1 Z2 X3 Y12 Y13] +
(0.004424855449441861+0j) [X0 Z1 Z2 Y3 Y4 X5] +
(4.5233896781831927e-07+0j) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.0034841573002178917+0j) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.09163719967421e-07+0j) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 X10] +
(-0.005733569747311883+0j) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.004684903388155202+0j) [X0 Z1 Z2 Y3 Y6 X7] +
(-0.004668620318776303+0j) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 X11] +
(7.18999097590114e-07+0j) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005114473831660406+0j) [X0 Z1 Z2 Y3 Y7 Z8 Z9 X10] +
(-7.560692465455075e-07+0j) [X0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 X12] +
(0.008125251921381043+0j) [X0 Z1 Z2 Y3 Y8 X9] +
(0.0017992194936630602+0j) [X0 Z1 Z2 Y3 Y10 X11] +
(5.471647745115407e-07+0j) [X0 Z1 Z2 Y3 Y10 Z11 Z12 X13] +
(-5.287660625135047e-07+0j) [X0 Z1 Z2 Y3 Y11 X12] +
(0.004575007626639214+0j) [X0 Z1 Z2 Y3 Y12 X13] +
(3.2020768809735752e-06+0j) [X0 Z1 Z2 Z3 X4] +
(0.000853385625412542+0j) [X0 Z1 Z2 Z3 X4 X5 Z6 X7] +
(0.0007870896771024483+0j) [X0 Z1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.000853385625412542+0j) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7] +
(0.0007870896771024483+0j) [X0 Z1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.291969486385335e-07+0j) [X0 Z1 Z2 Z3 X4 Z5] +
(4.444597854449394e-07+0j) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 X10] +
(0.0011726348316441972+0j) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.68491509551191e-07+0j) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Y10] +
(0.002200964069500453+0j) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.8394209155749533e-07+0j) [X0 Z1 Z2 Z3 X4 Z6] +
(4.09225061643495e-07+0j) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 X11] +
(0.002394972639798024+0j) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.09225061643495e-07+0j) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Y11] +
(0.002394972639798024+0j) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(3.2362599615205933e-07+0j) [X0 Z1 Z2 Z3 X4 Z8] +
(8.64931013511607e-08+0j) [X0 Z1 Z2 Z3 X4 Z9] +
(0.0013038004788126921+0j) [X0 Z1 Z2 Z3 X4 X10 Z11 X12] +
(0.0039898414566193+0j) [X0 Z1 Z2 Z3 X4 Y10 Z11 Y12] +
(-6.733197742908367e-07+0j) [X0 Z1 Z2 Z3 X4 Z10] +
(0.0022619660624823477+0j) [X0 Z1 Z2 Z3 X4 X11 Z12 X13] +
(0.0022619660624823477+0j) [X0 Z1 Z2 Z3 X4 Y11 Z12 Y13] +
(-5.927453083275253e-07+0j) [X0 Z1 Z2 Z3 X4 Z11] +
(1.2393363217830566e-06+0j) [X0 Z1 Z2 Z3 X4 Z12] +
(9.306536652542747e-07+0j) [X0 Z1 Z2 Z3 X4 Z13] +
(-0.0010283292378562557+0j) [X0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.0026860409778066067+0j) [X0 Z1 Z2 Z3 Y4 Y10 Z11 X12] +
(-1.8394209155749533e-07+0j) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7] +
(-0.0001940085702975716+0j) [X0 Z1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0012223378081538273+0j) [X0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12] +
(-2.3713289480089858e-07+0j) [X0 Z1 Z2 Z3 Z4 X5 Y8 Y9] +
(8.057446596331147e-08+0j) [X0 Z1 Z2 Z3 Z4 X5 Y10 Y11] +
(0.0017278753941369523+0j) [X0 Z1 Z2 Z3 Z4 X5 Y10 Z11 Z12 Y13] +
(-0.0009581655836696558+0j) [X0 Z1 Z2 Z3 Z4 X5 X11 X12] +
(-3.0868265652878185e-07+0j) [X0 Z1 Z2 Z3 Z4 X5 Y12 Y13] +
(1.8394209155749533e-07+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7] +
(0.0001940085702975716+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0012223378081538273+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12] +
(2.3713289480089858e-07+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y8 X9] +
(-8.057446596331147e-08+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y10 X11] +
(-0.0017278753941369523+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y10 Z11 Z12 X13] +
(-0.0009581655836696558+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y11 X12] +
(3.0868265652878185e-07+0j) [X0 Z1 Z2 Z3 Z4 Y5 Y12 X13] +
(0.042743277013781764+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6] +
(0.0005192743499487561+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11] +
(-1.8505641929553006e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005192743499487561+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11] +
(-1.8505641929553006e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.002779026799025551+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7] +
(0.00463697666118253+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z8] +
(0.0012803060973496428+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z9] +
(2.3120943054105456e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 X12] +
(1.0717282184453726e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y10 Z11 Y12] +
(0.005379937155839365+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z10] +
(7.246974426018278e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 X11 Z12 X13] +
(7.246974426018278e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y11 Z12 Y13] +
(0.005241535382803858+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z11] +
(0.004311038507914286+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z12] +
(0.001043524653490732+0j) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z13] +
(1.2004287494950345e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 X12] +
(-0.003356670563832887+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y8 Y9] +
(-0.00013840177303550726+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Y11] +
(-6.175246207572905e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13] +
(-4.997018422545968e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 X12] +
(-0.003267513854423554+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y12 Y13] +
(0.003356670563832887+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y8 X9] +
(0.00013840177303550726+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 X11] +
(6.175246207572905e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13] +
(-4.997018422545968e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 X12] +
(0.003267513854423554+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y12 X13] +
(0.0038764708993369494+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11] +
(-7.540341414242366e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(0.0038764708993369494+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11] +
(-7.540341414242366e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(0.0716503518100245+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.002141361223101637+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11] +
(0.004220813970046421+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12] +
(0.0012366478019244906+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13] +
(-0.0029841661681219308+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(0.0029841661681219308+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(-1.3987009015798951e-05+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(8.949476488106401e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(-6.87662165864606e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12] +
(-7.661347213523059e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12] +
(0.0015324835230729889+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 X10] +
(-2.904599884449085e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12] +
(0.005408954422409937+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 X10] +
(-1.0444941298691453e-06+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12] +
(0.004767272188278058+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 X10] +
(-8.105515037636442e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12] +
(0.005286546538226815+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 X10] +
(-9.956079230591742e-07+0j) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0016095313817213537+0j) [X0 Z1 Z2 Z3 Z4 X6] +
(-7.141625221159911e-05+0j) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 X10] +
(-2.6667317547039294e-07+0j) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0024629170071338957+0j) [X0 Z1 Z2 Z3 Z5 X6] +
(0.000715673424890849+0j) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 X10] +
(-3.0767325320641166e-07+0j) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(3.606071868119339e-07+0j) [X0 Z1 Z2 X4] +
(0.0039615607924964715+0j) [X0 Z1 Z2 Z4 Z5 X6] +
(0.00018787053389547175+0j) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.6569309317470705e-07+0j) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.737933262523489e-07+0j) [X0 Z1 Z3 X4] +
(0.0016676041811440087+0j) [X0 Z1 Z3 Z4 Z5 X6] +
(-0.0014528843214169599+0j) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(4.6704023909151857e-07+0j) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.10433064780651449+0j) [X0 X2] +
(3.117447946271872e-06+0j) [X0 Z2 Z3 X4] +
(0.04587947078129795+0j) [X0 Z2 Z3 Z4 Z5 X6] +
(0.058591988733861775+0j) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-1.1463061453797389e-05+0j) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.014583648907612741+0j) [Y0 X1 X2 Y3] +
(3.5707613293267043e-07+0j) [Y0 X1 X2 Z3 Z4 Y5] +
(0.005652620978017366+0j) [Y0 X1 X2 Z3 Z4 Z5 Z6 Y7] +
(0.008826368514209844+0j) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.792493957818554e-06+0j) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-3.5707613293267043e-07+0j) [Y0 X1 X3 Y4] +
(-0.005652620978017367+0j) [Y0 X1 X3 Z4 Z5 Y6] +
(-0.008826368514209844+0j) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.7924939578185542e-06+0j) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0027458364701868137+0j) [Y0 X1 X4 Y5] +
(2.447323128996551e-07+0j) [Y0 X1 X4 Z5 Z6 Y7] +
(7.867765104770313e-07+0j) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.003804066171728546+0j) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.447323128996551e-07+0j) [Y0 X1 X5 Y6] +
(-7.867765104770313e-07+0j) [Y0 X1 X5 Z6 Z7 Z8 Z9 Y10] +
(-0.003804066171728546+0j) [Y0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.006888194352970544+0j) [Y0 X1 X6 Y7] +
(7.735036880588225e-05+0j) [Y0 X1 X6 Z7 Z8 Z9 Z10 Y11] +
(-1.7035783555108094e-07+0j) [Y0 X1 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.735036880588223e-05+0j) [Y0 X1 X7 Z8 Z9 Y10] +
(1.7035783555108094e-07+0j) [Y0 X1 X7 Z8 Z9 Z10 Z11 Y12] +
(0.006509361201177245+0j) [Y0 X1 X8 Y9] +
(0.007731425250775296+0j) [Y0 X1 X10 Y11] +
(-5.62785191172058e-07+0j) [Y0 X1 X10 Z11 Z12 Y13] +
(5.62785191172058e-07+0j) [Y0 X1 X11 Y12] +
(0.0052837764884029696+0j) [Y0 X1 X12 Y13] +
(-0.014583648907612741+0j) [Y0 Y1 X2 X3] +
(-3.5707613293267043e-07+0j) [Y0 Y1 X2 Z3 Z4 X5] +
(-0.005652620978017366+0j) [Y0 Y1 X2 Z3 Z4 Z5 Z6 X7] +
(-0.008826368514209844+0j) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.792493957818554e-06+0j) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.5707613293267043e-07+0j) [Y0 Y1 Y3 Y4] +
(-0.005652620978017367+0j) [Y0 Y1 Y3 Z4 Z5 Y6] +
(-0.008826368514209844+0j) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.7924939578185542e-06+0j) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.0027458364701868137+0j) [Y0 Y1 X4 X5] +
(-2.447323128996551e-07+0j) [Y0 Y1 X4 Z5 Z6 X7] +
(-7.867765104770313e-07+0j) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.003804066171728546+0j) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.447323128996551e-07+0j) [Y0 Y1 Y5 Y6] +
(-7.867765104770313e-07+0j) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.003804066171728546+0j) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.006888194352970544+0j) [Y0 Y1 X6 X7] +
(-7.735036880588225e-05+0j) [Y0 Y1 X6 Z7 Z8 Z9 Z10 X11] +
(1.7035783555108094e-07+0j) [Y0 Y1 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-7.735036880588223e-05+0j) [Y0 Y1 Y7 Z8 Z9 Y10] +
(1.7035783555108094e-07+0j) [Y0 Y1 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.006509361201177245+0j) [Y0 Y1 X8 X9] +
(-0.007731425250775296+0j) [Y0 Y1 X10 X11] +
(5.62785191172058e-07+0j) [Y0 Y1 X10 Z11 Z12 X13] +
(5.62785191172058e-07+0j) [Y0 Y1 Y11 Y12] +
(-0.0052837764884029696+0j) [Y0 Y1 X12 X13] +
(-3.568247521491018e-07+0j) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.002249412447093992+0j) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.00044585351288410277+0j) [Y0 Z1 X2 X6 Z7 Z8 Z9 Y10] +
(-1.9742253793703326e-08+0j) [Y0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.0474716555222244e-08+0j) [Y0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.12507032579772231+0j) [Y0 Z1 Y2] +
(-1.9332412771343883e-07+0j) [Y0 Z1 Y2 X3 Z4 X5] +
(-0.0022939566113524632+0j) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7] +
(-0.0016407548553124317+0j) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(3.013471459168116e-07+0j) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.9332412771343883e-07+0j) [Y0 Z1 Y2 Y3 Z4 Y5] +
(-0.0022939566113524632+0j) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7] +
(-0.0016407548553124317+0j) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(3.013471459168116e-07+0j) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.003276971931231688+0j) [Y0 Z1 Y2 Z3] +
(-1.380778148181863e-07+0j) [Y0 Z1 Y2 X4 Z5 X6] +
(-7.900128986923677e-07+0j) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.005348051582676637+0j) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.5510539177941005e-07+0j) [Y0 Z1 Y2 Y4 Z5 Y6] +
(-1.1468376508414694e-06+0j) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.00759746402977063+0j) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0055307592186315535+0j) [Y0 Z1 Y2 Z4] +
(-1.380778148181863e-07+0j) [Y0 Z1 Y2 X5 Z6 X7] +
(-3.376739308740483e-07+0j) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0018638942824587446+0j) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.380778148181863e-07+0j) [Y0 Z1 Y2 Y5 Z6 Y7] +
(-3.376739308740483e-07+0j) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0018638942824587446+0j) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0011059037691896936+0j) [Y0 Z1 Y2 Z5] +
(0.00526264247307686+0j) [Y0 Z1 Y2 X6 Z7 Z8 Z9 X10] +
(-8.074305986486427e-07+0j) [Y0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.005708495985960965+0j) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Y10] +
-1.9742253794014717e-08j [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(-8.352332103652438e-07+0j) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.008032520918821373+0j) [Y0 Z1 Y2 Z6] +
(0.0005940221543005585+0j) [Y0 Z1 Y2 X7 Z8 Z9 Z10 X11] +
(-8.379773243913243e-08+0j) [Y0 Z1 Y2 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005940221543005585+0j) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Y11] +
(-8.379773243913243e-08+0j) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0033476175306661705+0j) [Y0 Z1 Y2 Z7] +
(0.011055020596132108+0j) [Y0 Z1 Y2 Z8] +
(0.002929768674751065+0j) [Y0 Z1 Y2 Z9] +
(-6.556281915019352e-07+0j) [Y0 Z1 Y2 X10 Z11 X12] +
(-6.418291575036267e-07+0j) [Y0 Z1 Y2 Y10 Z11 Y12] +
(0.003555290195504337+0j) [Y0 Z1 Y2 Z10] +
(-1.1076325599025838e-07+0j) [Y0 Z1 Y2 X11 Z12 X13] +
(-1.1076325599025838e-07+0j) [Y0 Z1 Y2 Y11 Z12 Y13] +
(0.001756070701841277+0j) [Y0 Z1 Y2 Z11] +
(0.006901238249797298+0j) [Y0 Z1 Y2 Z12] +
(0.0023262306231580827+0j) [Y0 Z1 Y2 Z13] +
(0.004424855449441861+0j) [Y0 Z1 Z2 X3 X4 Y5] +
(4.5233896781831927e-07+0j) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.0034841573002178917+0j) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-8.09163719967421e-07+0j) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Y10] +
(-0.005733569747311883+0j) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.004684903388155202+0j) [Y0 Z1 Z2 X3 X6 Y7] +
(-0.004668620318776303+0j) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Y11] +
(7.18999097590114e-07+0j) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.005114473831660406+0j) [Y0 Z1 Z2 X3 X7 Z8 Z9 Y10] +
(-7.560692465455075e-07+0j) [Y0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 Y12] +
(0.008125251921381043+0j) [Y0 Z1 Z2 X3 X8 Y9] +
(0.0017992194936630602+0j) [Y0 Z1 Z2 X3 X10 Y11] +
(5.471647745115407e-07+0j) [Y0 Z1 Z2 X3 X10 Z11 Z12 Y13] +
(-5.287660625135047e-07+0j) [Y0 Z1 Z2 X3 X11 Y12] +
(0.004575007626639214+0j) [Y0 Z1 Z2 X3 X12 Y13] +
(-0.004424855449441861+0j) [Y0 Z1 Z2 Y3 X4 X5] +
(-4.5233896781831927e-07+0j) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0034841573002178917+0j) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.09163719967421e-07+0j) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.005733569747311883+0j) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004684903388155202+0j) [Y0 Z1 Z2 Y3 X6 X7] +
(0.004668620318776303+0j) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 X11] +
(-7.18999097590114e-07+0j) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005114473831660406+0j) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Y10] +
(-7.560692465455075e-07+0j) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.008125251921381043+0j) [Y0 Z1 Z2 Y3 X8 X9] +
(-0.0017992194936630602+0j) [Y0 Z1 Z2 Y3 X10 X11] +
(-5.471647745115407e-07+0j) [Y0 Z1 Z2 Y3 X10 Z11 Z12 X13] +
(-5.287660625135047e-07+0j) [Y0 Z1 Z2 Y3 Y11 Y12] +
(-0.004575007626639214+0j) [Y0 Z1 Z2 Y3 X12 X13] +
(-0.0010283292378562557+0j) [Y0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.0026860409778066067+0j) [Y0 Z1 Z2 Z3 X4 X10 Z11 Y12] +
(3.2020768809735752e-06+0j) [Y0 Z1 Z2 Z3 Y4] +
(0.000853385625412542+0j) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7] +
(0.0007870896771024483+0j) [Y0 Z1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.000853385625412542+0j) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7] +
(0.0007870896771024483+0j) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.291969486385335e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z5] +
(4.68491509551191e-07+0j) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 X10] +
(0.002200964069500453+0j) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.444597854449394e-07+0j) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Y10] +
(0.0011726348316441972+0j) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.8394209155749533e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z6] +
(4.09225061643495e-07+0j) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 X11] +
(0.002394972639798024+0j) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.09225061643495e-07+0j) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Y11] +
(0.002394972639798024+0j) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(3.2362599615205933e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z8] +
(8.64931013511607e-08+0j) [Y0 Z1 Z2 Z3 Y4 Z9] +
(0.0039898414566193+0j) [Y0 Z1 Z2 Z3 Y4 X10 Z11 X12] +
(0.0013038004788126921+0j) [Y0 Z1 Z2 Z3 Y4 Y10 Z11 Y12] +
(-6.733197742908367e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z10] +
(0.0022619660624823477+0j) [Y0 Z1 Z2 Z3 Y4 X11 Z12 X13] +
(0.0022619660624823477+0j) [Y0 Z1 Z2 Z3 Y4 Y11 Z12 Y13] +
(-5.927453083275253e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z11] +
(1.2393363217830566e-06+0j) [Y0 Z1 Z2 Z3 Y4 Z12] +
(9.306536652542747e-07+0j) [Y0 Z1 Z2 Z3 Y4 Z13] +
(1.8394209155749533e-07+0j) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7] +
(0.0001940085702975716+0j) [Y0 Z1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0012223378081538273+0j) [Y0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12] +
(2.3713289480089858e-07+0j) [Y0 Z1 Z2 Z3 Z4 X5 X8 Y9] +
(-8.057446596331147e-08+0j) [Y0 Z1 Z2 Z3 Z4 X5 X10 Y11] +
(-0.0017278753941369523+0j) [Y0 Z1 Z2 Z3 Z4 X5 X10 Z11 Z12 Y13] +
(-0.0009581655836696558+0j) [Y0 Z1 Z2 Z3 Z4 X5 X11 Y12] +
(3.0868265652878185e-07+0j) [Y0 Z1 Z2 Z3 Z4 X5 X12 Y13] +
(-1.8394209155749533e-07+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7] +
(-0.0001940085702975716+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0012223378081538273+0j) [Y0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12] +
(-2.3713289480089858e-07+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X8 X9] +
(8.057446596331147e-08+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X10 X11] +
(0.0017278753941369523+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X10 Z11 Z12 X13] +
(-0.0009581655836696558+0j) [Y0 Z1 Z2 Z3 Z4 Y5 Y11 Y12] +
(-3.0868265652878185e-07+0j) [Y0 Z1 Z2 Z3 Z4 Y5 X12 X13] +
(1.2004287494950345e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 Y12] +
(0.042743277013781764+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6] +
(0.0005192743499487561+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11] +
(-1.8505641929553006e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0005192743499487561+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11] +
(-1.8505641929553006e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.002779026799025551+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7] +
(0.00463697666118253+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z8] +
(0.0012803060973496428+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z9] +
(1.0717282184453726e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X10 Z11 X12] +
(2.3120943054105456e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Y12] +
(0.005379937155839365+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z10] +
(7.246974426018278e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X11 Z12 X13] +
(7.246974426018278e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y11 Z12 Y13] +
(0.005241535382803858+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z11] +
(0.004311038507914286+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z12] +
(0.001043524653490732+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z13] +
(0.003356670563832887+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X8 Y9] +
(0.00013840177303550726+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Y11] +
(6.175246207572905e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13] +
(-4.997018422545968e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 Y12] +
(0.003267513854423554+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X12 Y13] +
(-0.003356670563832887+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X8 X9] +
(-0.00013840177303550726+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 X11] +
(-6.175246207572905e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13] +
(-4.997018422545968e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Y12] +
(-0.003267513854423554+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X12 X13] +
(0.0038764708993369494+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11] +
(-7.540341414242366e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(0.0038764708993369494+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11] +
(-7.540341414242366e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(0.0716503518100245+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.002141361223101637+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11] +
(0.004220813970046421+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12] +
(0.0012366478019244906+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13] +
(0.0029841661681219308+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(-0.0029841661681219308+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(-1.3987009015798951e-05+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(8.949476488106401e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(-6.87662165864606e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12] +
(-7.661347213523059e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12] +
(0.0015324835230729889+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Y10] +
(-2.904599884449085e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12] +
(0.005408954422409937+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Y10] +
(-1.0444941298691453e-06+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12] +
(0.004767272188278058+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Y10] +
(-8.105515037636442e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12] +
(0.005286546538226815+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Y10] +
(-9.956079230591742e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0016095313817213537+0j) [Y0 Z1 Z2 Z3 Z4 Y6] +
(-7.141625221159911e-05+0j) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Y10] +
(-2.6667317547039294e-07+0j) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0024629170071338957+0j) [Y0 Z1 Z2 Z3 Z5 Y6] +
(0.000715673424890849+0j) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Y10] +
(-3.0767325320641166e-07+0j) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(3.606071868119339e-07+0j) [Y0 Z1 Z2 Y4] +
(0.0039615607924964715+0j) [Y0 Z1 Z2 Z4 Z5 Y6] +
(0.00018787053389547175+0j) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.6569309317470705e-07+0j) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.737933262523489e-07+0j) [Y0 Z1 Z3 Y4] +
(0.0016676041811440087+0j) [Y0 Z1 Z3 Z4 Z5 Y6] +
(-0.0014528843214169599+0j) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(4.6704023909151857e-07+0j) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.10433064780651449+0j) [Y0 Y2] +
(3.117447946271872e-06+0j) [Y0 Z2 Z3 Y4] +
(0.04587947078129795+0j) [Y0 Z2 Z3 Z4 Z5 Y6] +
(0.058591988733861775+0j) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-1.1463061453797389e-05+0j) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(12.41263074211179+0j) [Z0] +
(0.10433064780651449+0j) [Z0 X1 Z2 X3] +
(3.117447946271872e-06+0j) [Z0 X1 Z2 Z3 Z4 X5] +
(0.04587947078129795+0j) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7] +
(0.05859198873386178+0j) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-1.1463061453797389e-05+0j) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.10433064780651449+0j) [Z0 Y1 Z2 Y3] +
(3.117447946271872e-06+0j) [Z0 Y1 Z2 Z3 Z4 Y5] +
(0.04587947078129795+0j) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7] +
(0.05859198873386178+0j) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-1.1463061453797389e-05+0j) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.1861763734860522+0j) [Z0 Z1] +
(-8.337746754282251e-07+0j) [Z0 X2 Z3 X4] +
(-0.027115036845273405+0j) [Z0 X2 Z3 Z4 Z5 X6] +
(-0.06752385099214028+0j) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.4017109736319852e-05+0j) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-8.337746754282251e-07+0j) [Z0 Y2 Z3 Y4] +
(-0.027115036845273405+0j) [Z0 Y2 Z3 Z4 Z5 Y6] +
(-0.06752385099214028+0j) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.4017109736319852e-05+0j) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.23671080783830456+0j) [Z0 Z2] +
(-1.1908508083608957e-06+0j) [Z0 X3 Z4 X5] +
(-0.032767657823290774+0j) [Z0 X3 Z4 Z5 Z6 X7] +
(-0.07635021950635013+0j) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.5809603694138405e-05+0j) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.1908508083608957e-06+0j) [Z0 Y3 Z4 Y5] +
(-0.032767657823290774+0j) [Z0 Y3 Z4 Z5 Z6 Y7] +
(-0.07635021950635013+0j) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.5809603694138405e-05+0j) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.2512944567459173+0j) [Z0 Z3] +
(-3.0993492438630966e-06+0j) [Z0 X4 Z5 X6] +
(-1.531680879645723e-05+0j) [Z0 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.08684737589863634+0j) [Z0 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-3.0993492438630966e-06+0j) [Z0 Y4 Z5 Y6] +
(-1.531680879645723e-05+0j) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.08684737589863634+0j) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.19661770890342156+0j) [Z0 Z4] +
(-3.344081556762752e-06+0j) [Z0 X5 Z6 X7] +
(-1.6103585306934262e-05+0j) [Z0 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.0906514420703649+0j) [Z0 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.344081556762752e-06+0j) [Z0 Y5 Z6 Y7] +
(-1.6103585306934262e-05+0j) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.0906514420703649+0j) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.1993635453736084+0j) [Z0 Z5] +
(0.05608468124661388+0j) [Z0 X6 Z7 Z8 Z9 X10] +
(-6.652209670011996e-06+0j) [Z0 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.05608468124661388+0j) [Z0 Y6 Z7 Z8 Z9 Y10] +
(-6.652209670011996e-06+0j) [Z0 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.24164663936017164+0j) [Z0 Z6] +
(0.056007330877808+0j) [Z0 X7 Z8 Z9 Z10 X11] +
(-6.481851834460914e-06+0j) [Z0 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.056007330877808+0j) [Z0 Y7 Z8 Z9 Z10 Y11] +
(-6.481851834460914e-06+0j) [Z0 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.24853483371314222+0j) [Z0 Z7] +
(0.272325183066057+0j) [Z0 Z8] +
(0.2788345442672343+0j) [Z0 Z9] +
(-2.1776646052595345e-06+0j) [Z0 X10 Z11 X12] +
(-2.1776646052595345e-06+0j) [Z0 Y10 Z11 Y12] +
(0.1929972393536431+0j) [Z0 Z10] +
(-1.6148794140874765e-06+0j) [Z0 X11 Z12 X13] +
(-1.6148794140874765e-06+0j) [Z0 Y11 Z12 Y13] +
(0.2007286646044184+0j) [Z0 Z11] +
(0.21102659849791547+0j) [Z0 Z12] +
(0.21631037498631844+0j) [Z0 Z13] +
(1.9332412771343883e-07+0j) [X1 X2 Y3 Y4] +
(0.0022939566113524632+0j) [X1 X2 Y3 Z4 Z5 Y6] +
(0.0016407548553124317+0j) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-3.013471459168116e-07+0j) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004424855449441861+0j) [X1 X2 X4 X5] +
(-8.09163719967421e-07+0j) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.005733569747311883+0j) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-4.5233896781831927e-07+0j) [X1 X2 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.0034841573002178917+0j) [X1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004684903388155202+0j) [X1 X2 X6 X7] +
(0.005114473831660406+0j) [X1 X2 X6 Z7 Z8 Z9 Z10 X11] +
(-7.560692465455075e-07+0j) [X1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.004668620318776303+0j) [X1 X2 Y7 Z8 Z9 Y10] +
(-7.18999097590114e-07+0j) [X1 X2 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.008125251921381043+0j) [X1 X2 X8 X9] +
(-0.0017992194936630602+0j) [X1 X2 X10 X11] +
(-5.287660625135047e-07+0j) [X1 X2 X10 Z11 Z12 X13] +
(-5.471647745115407e-07+0j) [X1 X2 Y11 Y12] +
(-0.004575007626639215+0j) [X1 X2 X12 X13] +
(-1.9332412771343883e-07+0j) [X1 Y2 Y3 X4] +
(-0.0022939566113524632+0j) [X1 Y2 Y3 Z4 Z5 X6] +
(-0.0016407548553124317+0j) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(3.013471459168116e-07+0j) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004424855449441861+0j) [X1 Y2 Y4 X5] +
(-8.09163719967421e-07+0j) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.005733569747311883+0j) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.5233896781831927e-07+0j) [X1 Y2 Y5 Z6 Z7 Z8 Z9 X10] +
(0.0034841573002178917+0j) [X1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004684903388155202+0j) [X1 Y2 Y6 X7] +
(0.005114473831660406+0j) [X1 Y2 Y6 Z7 Z8 Z9 Z10 X11] +
(-7.560692465455075e-07+0j) [X1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.004668620318776303+0j) [X1 Y2 Y7 Z8 Z9 X10] +
(7.18999097590114e-07+0j) [X1 Y2 Y7 Z8 Z9 Z10 Z11 X12] +
(-0.008125251921381043+0j) [X1 Y2 Y8 X9] +
(-0.0017992194936630602+0j) [X1 Y2 Y10 X11] +
(-5.287660625135047e-07+0j) [X1 Y2 Y10 Z11 Z12 X13] +
(5.471647745115407e-07+0j) [X1 Y2 Y11 X12] +
(-0.004575007626639215+0j) [X1 Y2 Y12 X13] +
(0.12507032579772231+0j) [X1 Z2 X3] +
(-1.380778148181863e-07+0j) [X1 Z2 X3 X4 Z5 X6] +
(-3.376739308740483e-07+0j) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0018638942824587446+0j) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.380778148181863e-07+0j) [X1 Z2 X3 Y4 Z5 Y6] +
(-3.376739308740483e-07+0j) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0018638942824587446+0j) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0011059037691896936+0j) [X1 Z2 X3 Z4] +
(-1.5510539177941005e-07+0j) [X1 Z2 X3 X5 Z6 X7] +
(-1.1468376508414694e-06+0j) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.00759746402977063+0j) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.380778148181863e-07+0j) [X1 Z2 X3 Y5 Z6 Y7] +
(-7.900128986923677e-07+0j) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.005348051582676637+0j) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0055307592186315535+0j) [X1 Z2 X3 Z5] +
(0.0005940221543005585+0j) [X1 Z2 X3 X6 Z7 Z8 Z9 X10] +
(-8.379773243913243e-08+0j) [X1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0005940221543005585+0j) [X1 Z2 X3 Y6 Z7 Z8 Z9 Y10] +
(-8.379773243913243e-08+0j) [X1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0033476175306661705+0j) [X1 Z2 X3 Z6] +
(0.005708495985960965+0j) [X1 Z2 X3 X7 Z8 Z9 Z10 X11] +
(-8.352332103652438e-07+0j) [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 X13] +
1.9742253794014717e-08j [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.00526264247307686+0j) [X1 Z2 X3 Y7 Z8 Z9 Z10 Y11] +
(-8.074305986486427e-07+0j) [X1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.008032520918821373+0j) [X1 Z2 X3 Z7] +
(0.002929768674751065+0j) [X1 Z2 X3 Z8] +
(0.011055020596132108+0j) [X1 Z2 X3 Z9] +
(-1.1076325599025838e-07+0j) [X1 Z2 X3 X10 Z11 X12] +
(-1.1076325599025838e-07+0j) [X1 Z2 X3 Y10 Z11 Y12] +
(0.001756070701841277+0j) [X1 Z2 X3 Z10] +
(-6.418291575036267e-07+0j) [X1 Z2 X3 X11 Z12 X13] +
(-6.556281915019352e-07+0j) [X1 Z2 X3 Y11 Z12 Y13] +
(0.003555290195504337+0j) [X1 Z2 X3 Z11] +
(0.0023262306231580827+0j) [X1 Z2 X3 Z12] +
(0.006901238249797298+0j) [X1 Z2 X3 Z13] +
(-3.568247521491018e-07+0j) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.002249412447093992+0j) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.0474716555222244e-08+0j) [X1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.00044585351288410277+0j) [X1 Z2 Y3 Y7 Z8 Z9 Z10 X11] +
(-1.9742253793703326e-08+0j) [X1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.000853385625412542+0j) [X1 Z2 Z3 X4 Y5 Y6] +
(-0.0007870896771024483+0j) [X1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Y10] +
(-1.8394209155749533e-07+0j) [X1 Z2 Z3 X4 X6 X7] +
(-0.0012223378081538273+0j) [X1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0001940085702975716+0j) [X1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Y12] +
(-2.371328948008986e-07+0j) [X1 Z2 Z3 X4 X8 X9] +
(8.057446596331147e-08+0j) [X1 Z2 Z3 X4 X10 X11] +
(-0.0009581655836696558+0j) [X1 Z2 Z3 X4 X10 Z11 Z12 X13] +
(0.0017278753941369523+0j) [X1 Z2 Z3 X4 Y11 Y12] +
(-3.086826565287818e-07+0j) [X1 Z2 Z3 X4 X12 X13] +
(0.000853385625412542+0j) [X1 Z2 Z3 Y4 Y5 X6] +
(0.0007870896771024483+0j) [X1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 X10] +
(-1.8394209155749533e-07+0j) [X1 Z2 Z3 Y4 Y6 X7] +
(-0.0012223378081538273+0j) [X1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0001940085702975716+0j) [X1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 X12] +
(-2.371328948008986e-07+0j) [X1 Z2 Z3 Y4 Y8 X9] +
(8.057446596331147e-08+0j) [X1 Z2 Z3 Y4 Y10 X11] +
(-0.0009581655836696558+0j) [X1 Z2 Z3 Y4 Y10 Z11 Z12 X13] +
(-0.0017278753941369523+0j) [X1 Z2 Z3 Y4 Y11 X12] +
(-3.086826565287818e-07+0j) [X1 Z2 Z3 Y4 Y12 X13] +
(3.202076880973575e-06+0j) [X1 Z2 Z3 Z4 X5] +
(4.09225061643495e-07+0j) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 X10] +
(0.002394972639798024+0j) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.09225061643495e-07+0j) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Y10] +
(0.002394972639798024+0j) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(4.444597854449394e-07+0j) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 X11] +
(0.0011726348316441972+0j) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.68491509551191e-07+0j) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Y11] +
(0.002200964069500453+0j) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.8394209155749533e-07+0j) [X1 Z2 Z3 Z4 X5 Z7] +
(8.64931013511607e-08+0j) [X1 Z2 Z3 Z4 X5 Z8] +
(3.2362599615205933e-07+0j) [X1 Z2 Z3 Z4 X5 Z9] +
(0.0022619660624823477+0j) [X1 Z2 Z3 Z4 X5 X10 Z11 X12] +
(0.0022619660624823477+0j) [X1 Z2 Z3 Z4 X5 Y10 Z11 Y12] +
(-5.927453083275253e-07+0j) [X1 Z2 Z3 Z4 X5 Z10] +
(0.0013038004788126921+0j) [X1 Z2 Z3 Z4 X5 X11 Z12 X13] +
(0.0039898414566193+0j) [X1 Z2 Z3 Z4 X5 Y11 Z12 Y13] +
(-6.733197742908367e-07+0j) [X1 Z2 Z3 Z4 X5 Z11] +
(9.306536652542747e-07+0j) [X1 Z2 Z3 Z4 X5 Z12] +
(1.2393363217830566e-06+0j) [X1 Z2 Z3 Z4 X5 Z13] +
(-0.0010283292378562557+0j) [X1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0026860409778066067+0j) [X1 Z2 Z3 Z4 Y5 Y11 Z12 X13] +
(-0.0005192743499487561+0j) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Y10] +
(1.8505641929553006e-07+0j) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.003356670563832887+0j) [X1 Z2 Z3 Z4 Z5 X6 X8 X9] +
(-0.00013840177303550726+0j) [X1 Z2 Z3 Z4 Z5 X6 X10 X11] +
(-4.997018422545968e-07+0j) [X1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 X13] +
(-6.175246207572905e-07+0j) [X1 Z2 Z3 Z4 Z5 X6 Y11 Y12] +
(-0.003267513854423554+0j) [X1 Z2 Z3 Z4 Z5 X6 X12 X13] +
(0.0005192743499487561+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 X10] +
(-1.8505641929553006e-07+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12] +
(-0.003356670563832887+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y8 X9] +
(-0.00013840177303550726+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y10 X11] +
(-4.997018422545968e-07+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 X13] +
(6.175246207572905e-07+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y11 X12] +
(-0.003267513854423554+0j) [X1 Z2 Z3 Z4 Z5 Y6 Y12 X13] +
(0.04274327701378175+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7] +
(0.0012803060973496428+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z8] +
(0.00463697666118253+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z9] +
(7.246974426018278e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 X12] +
(7.246974426018278e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Y12] +
(0.005241535382803858+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z10] +
(2.3120943054105456e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 X13] +
(1.0717282184453726e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y11 Z12 Y13] +
(0.005379937155839365+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z11] +
(0.001043524653490732+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z12] +
(0.004311038507914286+0j) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z13] +
(1.2004287494950345e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 X13] +
(-0.0038764708993369494+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Y10] +
(7.540341414242366e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12] +
(0.0038764708993369494+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 X10] +
(-7.540341414242366e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12] +
(-0.0029841661681219308+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13] +
(-0.0029841661681219308+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13] +
(0.0716503518100245+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.0012366478019244906+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12] +
(0.004220813970046421+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13] +
(-1.3987009015798948e-05+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(8.949476488106401e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13] +
(-7.661347213523059e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13] +
(-0.002141361223101637+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X11] +
(-6.87662165864606e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13] +
(0.005408954422409937+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 X11] +
(-1.0444941298691453e-06+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13] +
(0.0015324835230729889+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 X11] +
(-2.904599884449085e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13] +
(0.005286546538226815+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 X11] +
(-9.956079230591742e-07+0j) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.002779026799025551+0j) [X1 Z2 Z3 Z4 Z5 X7] +
(0.004767272188278058+0j) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 X11] +
(-8.105515037636442e-07+0j) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0024629170071338957+0j) [X1 Z2 Z3 Z4 Z6 X7] +
(0.000715673424890849+0j) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 X11] +
(-3.0767325320641166e-07+0j) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.291969486385335e-07+0j) [X1 Z2 Z3 X5] +
(0.0016095313817213537+0j) [X1 Z2 Z3 Z5 Z6 X7] +
(-7.141625221159911e-05+0j) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-2.6667317547039294e-07+0j) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.737933262523489e-07+0j) [X1 Z2 Z4 X5] +
(0.0016676041811440087+0j) [X1 Z2 Z4 Z5 Z6 X7] +
(-0.0014528843214169599+0j) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(4.6704023909151857e-07+0j) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.003276971931231688+0j) [X1 X3] +
(3.606071868119339e-07+0j) [X1 Z3 Z4 X5] +
(0.0039615607924964715+0j) [X1 Z3 Z4 Z5 Z6 X7] +
(0.00018787053389547175+0j) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.6569309317470705e-07+0j) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.9332412771343883e-07+0j) [Y1 X2 X3 Y4] +
(-0.0022939566113524632+0j) [Y1 X2 X3 Z4 Z5 Y6] +
(-0.0016407548553124317+0j) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(3.013471459168116e-07+0j) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004424855449441861+0j) [Y1 X2 X4 Y5] +
(-8.09163719967421e-07+0j) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.005733569747311883+0j) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(4.5233896781831927e-07+0j) [Y1 X2 X5 Z6 Z7 Z8 Z9 Y10] +
(0.0034841573002178917+0j) [Y1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.004684903388155202+0j) [Y1 X2 X6 Y7] +
(0.005114473831660406+0j) [Y1 X2 X6 Z7 Z8 Z9 Z10 Y11] +
(-7.560692465455075e-07+0j) [Y1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.004668620318776303+0j) [Y1 X2 X7 Z8 Z9 Y10] +
(7.18999097590114e-07+0j) [Y1 X2 X7 Z8 Z9 Z10 Z11 Y12] +
(-0.008125251921381043+0j) [Y1 X2 X8 Y9] +
(-0.0017992194936630602+0j) [Y1 X2 X10 Y11] +
(-5.287660625135047e-07+0j) [Y1 X2 X10 Z11 Z12 Y13] +
(5.471647745115407e-07+0j) [Y1 X2 X11 Y12] +
(-0.004575007626639215+0j) [Y1 X2 X12 Y13] +
(1.9332412771343883e-07+0j) [Y1 Y2 X3 X4] +
(0.0022939566113524632+0j) [Y1 Y2 X3 Z4 Z5 X6] +
(0.0016407548553124317+0j) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-3.013471459168116e-07+0j) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004424855449441861+0j) [Y1 Y2 Y4 Y5] +
(-8.09163719967421e-07+0j) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.005733569747311883+0j) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-4.5233896781831927e-07+0j) [Y1 Y2 X5 Z6 Z7 Z8 Z9 X10] +
(-0.0034841573002178917+0j) [Y1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.004684903388155202+0j) [Y1 Y2 Y6 Y7] +
(0.005114473831660406+0j) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Y11] +
(-7.560692465455075e-07+0j) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.004668620318776303+0j) [Y1 Y2 X7 Z8 Z9 X10] +
(-7.18999097590114e-07+0j) [Y1 Y2 X7 Z8 Z9 Z10 Z11 X12] +
(-0.008125251921381043+0j) [Y1 Y2 Y8 Y9] +
(-0.0017992194936630602+0j) [Y1 Y2 Y10 Y11] +
(-5.287660625135047e-07+0j) [Y1 Y2 Y10 Z11 Z12 Y13] +
(-5.471647745115407e-07+0j) [Y1 Y2 X11 X12] +
(-0.004575007626639215+0j) [Y1 Y2 Y12 Y13] +
(-3.568247521491018e-07+0j) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.002249412447093992+0j) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.00044585351288410277+0j) [Y1 Z2 X3 X7 Z8 Z9 Z10 Y11] +
(-1.9742253793703326e-08+0j) [Y1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.0474716555222244e-08+0j) [Y1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.12507032579772231+0j) [Y1 Z2 Y3] +
(-1.380778148181863e-07+0j) [Y1 Z2 Y3 X4 Z5 X6] +
(-3.376739308740483e-07+0j) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0018638942824587446+0j) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.380778148181863e-07+0j) [Y1 Z2 Y3 Y4 Z5 Y6] +
(-3.376739308740483e-07+0j) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0018638942824587446+0j) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0011059037691896936+0j) [Y1 Z2 Y3 Z4] +
(-1.380778148181863e-07+0j) [Y1 Z2 Y3 X5 Z6 X7] +
(-7.900128986923677e-07+0j) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.005348051582676637+0j) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.5510539177941005e-07+0j) [Y1 Z2 Y3 Y5 Z6 Y7] +
(-1.1468376508414694e-06+0j) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.00759746402977063+0j) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0055307592186315535+0j) [Y1 Z2 Y3 Z5] +
(0.0005940221543005585+0j) [Y1 Z2 Y3 X6 Z7 Z8 Z9 X10] +
(-8.379773243913243e-08+0j) [Y1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0005940221543005585+0j) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Y10] +
(-8.379773243913243e-08+0j) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0033476175306661705+0j) [Y1 Z2 Y3 Z6] +
(0.00526264247307686+0j) [Y1 Z2 Y3 X7 Z8 Z9 Z10 X11] +
(-8.074305986486427e-07+0j) [Y1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.005708495985960965+0j) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Y11] +
-1.9742253794014717e-08j [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.352332103652438e-07+0j) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.008032520918821373+0j) [Y1 Z2 Y3 Z7] +
(0.002929768674751065+0j) [Y1 Z2 Y3 Z8] +
(0.011055020596132108+0j) [Y1 Z2 Y3 Z9] +
(-1.1076325599025838e-07+0j) [Y1 Z2 Y3 X10 Z11 X12] +
(-1.1076325599025838e-07+0j) [Y1 Z2 Y3 Y10 Z11 Y12] +
(0.001756070701841277+0j) [Y1 Z2 Y3 Z10] +
(-6.556281915019352e-07+0j) [Y1 Z2 Y3 X11 Z12 X13] +
(-6.418291575036267e-07+0j) [Y1 Z2 Y3 Y11 Z12 Y13] +
(0.003555290195504337+0j) [Y1 Z2 Y3 Z11] +
(0.0023262306231580827+0j) [Y1 Z2 Y3 Z12] +
(0.006901238249797298+0j) [Y1 Z2 Y3 Z13] +
(0.000853385625412542+0j) [Y1 Z2 Z3 X4 X5 Y6] +
(0.0007870896771024483+0j) [Y1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Y10] +
(-1.8394209155749533e-07+0j) [Y1 Z2 Z3 X4 X6 Y7] +
(-0.0012223378081538273+0j) [Y1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0001940085702975716+0j) [Y1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Y12] +
(-2.371328948008986e-07+0j) [Y1 Z2 Z3 X4 X8 Y9] +
(8.057446596331147e-08+0j) [Y1 Z2 Z3 X4 X10 Y11] +
(-0.0009581655836696558+0j) [Y1 Z2 Z3 X4 X10 Z11 Z12 Y13] +
(-0.0017278753941369523+0j) [Y1 Z2 Z3 X4 X11 Y12] +
(-3.086826565287818e-07+0j) [Y1 Z2 Z3 X4 X12 Y13] +
(-0.000853385625412542+0j) [Y1 Z2 Z3 Y4 X5 X6] +
(-0.0007870896771024483+0j) [Y1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 X10] +
(-1.8394209155749533e-07+0j) [Y1 Z2 Z3 Y4 Y6 Y7] +
(-0.0012223378081538273+0j) [Y1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0001940085702975716+0j) [Y1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 X12] +
(-2.371328948008986e-07+0j) [Y1 Z2 Z3 Y4 Y8 Y9] +
(8.057446596331147e-08+0j) [Y1 Z2 Z3 Y4 Y10 Y11] +
(-0.0009581655836696558+0j) [Y1 Z2 Z3 Y4 Y10 Z11 Z12 Y13] +
(0.0017278753941369523+0j) [Y1 Z2 Z3 Y4 X11 X12] +
(-3.086826565287818e-07+0j) [Y1 Z2 Z3 Y4 Y12 Y13] +
(-0.0010283292378562557+0j) [Y1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0026860409778066067+0j) [Y1 Z2 Z3 Z4 X5 X11 Z12 Y13] +
(3.202076880973575e-06+0j) [Y1 Z2 Z3 Z4 Y5] +
(4.09225061643495e-07+0j) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 X10] +
(0.002394972639798024+0j) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.09225061643495e-07+0j) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Y10] +
(0.002394972639798024+0j) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(4.68491509551191e-07+0j) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 X11] +
(0.002200964069500453+0j) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.444597854449394e-07+0j) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Y11] +
(0.0011726348316441972+0j) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.8394209155749533e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z7] +
(8.64931013511607e-08+0j) [Y1 Z2 Z3 Z4 Y5 Z8] +
(3.2362599615205933e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z9] +
(0.0022619660624823477+0j) [Y1 Z2 Z3 Z4 Y5 X10 Z11 X12] +
(0.0022619660624823477+0j) [Y1 Z2 Z3 Z4 Y5 Y10 Z11 Y12] +
(-5.927453083275253e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z10] +
(0.0039898414566193+0j) [Y1 Z2 Z3 Z4 Y5 X11 Z12 X13] +
(0.0013038004788126921+0j) [Y1 Z2 Z3 Z4 Y5 Y11 Z12 Y13] +
(-6.733197742908367e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z11] +
(9.306536652542747e-07+0j) [Y1 Z2 Z3 Z4 Y5 Z12] +
(1.2393363217830566e-06+0j) [Y1 Z2 Z3 Z4 Y5 Z13] +
(0.0005192743499487561+0j) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Y10] +
(-1.8505641929553006e-07+0j) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12] +
(-0.003356670563832887+0j) [Y1 Z2 Z3 Z4 Z5 X6 X8 Y9] +
(-0.00013840177303550726+0j) [Y1 Z2 Z3 Z4 Z5 X6 X10 Y11] +
(-4.997018422545968e-07+0j) [Y1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 Y13] +
(6.175246207572905e-07+0j) [Y1 Z2 Z3 Z4 Z5 X6 X11 Y12] +
(-0.003267513854423554+0j) [Y1 Z2 Z3 Z4 Z5 X6 X12 Y13] +
(-0.0005192743499487561+0j) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 X10] +
(1.8505641929553006e-07+0j) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12] +
(-0.003356670563832887+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y8 Y9] +
(-0.00013840177303550726+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Y11] +
(-4.997018422545968e-07+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 Y13] +
(-6.175246207572905e-07+0j) [Y1 Z2 Z3 Z4 Z5 Y6 X11 X12] +
(-0.003267513854423554+0j) [Y1 Z2 Z3 Z4 Z5 Y6 Y12 Y13] +
(1.2004287494950345e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 Y13] +
(0.04274327701378175+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7] +
(0.0012803060973496428+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z8] +
(0.00463697666118253+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z9] +
(7.246974426018278e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 X12] +
(7.246974426018278e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Y12] +
(0.005241535382803858+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z10] +
(1.0717282184453726e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X11 Z12 X13] +
(2.3120943054105456e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 Y13] +
(0.005379937155839365+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z11] +
(0.001043524653490732+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z12] +
(0.004311038507914286+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z13] +
(0.0038764708993369494+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Y10] +
(-7.540341414242366e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12] +
(-0.0038764708993369494+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 X10] +
(7.540341414242366e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12] +
(-0.0029841661681219308+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13] +
(-0.0029841661681219308+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13] +
(0.0716503518100245+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.0012366478019244906+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12] +
(0.004220813970046421+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13] +
(-1.3987009015798948e-05+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(8.949476488106401e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13] +
(-7.661347213523059e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13] +
(-0.002141361223101637+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y11] +
(-6.87662165864606e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13] +
(0.005408954422409937+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Y11] +
(-1.0444941298691453e-06+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13] +
(0.0015324835230729889+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Y11] +
(-2.904599884449085e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13] +
(0.005286546538226815+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Y11] +
(-9.956079230591742e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.002779026799025551+0j) [Y1 Z2 Z3 Z4 Z5 Y7] +
(0.004767272188278058+0j) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Y11] +
(-8.105515037636442e-07+0j) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0024629170071338957+0j) [Y1 Z2 Z3 Z4 Z6 Y7] +
(0.000715673424890849+0j) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Y11] +
(-3.0767325320641166e-07+0j) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.291969486385335e-07+0j) [Y1 Z2 Z3 Y5] +
(0.0016095313817213537+0j) [Y1 Z2 Z3 Z5 Z6 Y7] +
(-7.141625221159911e-05+0j) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-2.6667317547039294e-07+0j) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.737933262523489e-07+0j) [Y1 Z2 Z4 Y5] +
(0.0016676041811440087+0j) [Y1 Z2 Z4 Z5 Z6 Y7] +
(-0.0014528843214169599+0j) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(4.6704023909151857e-07+0j) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.003276971931231688+0j) [Y1 Y3] +
(3.606071868119339e-07+0j) [Y1 Z3 Z4 Y5] +
(0.0039615607924964715+0j) [Y1 Z3 Z4 Z5 Z6 Y7] +
(0.00018787053389547175+0j) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.6569309317470705e-07+0j) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(12.41263074211179+0j) [Z1] +
(-1.1908508083608957e-06+0j) [Z1 X2 Z3 X4] +
(-0.032767657823290774+0j) [Z1 X2 Z3 Z4 Z5 X6] +
(-0.07635021950635013+0j) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(1.5809603694138405e-05+0j) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.1908508083608957e-06+0j) [Z1 Y2 Z3 Y4] +
(-0.032767657823290774+0j) [Z1 Y2 Z3 Z4 Z5 Y6] +
(-0.07635021950635013+0j) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(1.5809603694138405e-05+0j) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.2512944567459173+0j) [Z1 Z2] +
(-8.337746754282251e-07+0j) [Z1 X3 Z4 X5] +
(-0.027115036845273405+0j) [Z1 X3 Z4 Z5 Z6 X7] +
(-0.06752385099214028+0j) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(1.4017109736319852e-05+0j) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-8.337746754282251e-07+0j) [Z1 Y3 Z4 Y5] +
(-0.027115036845273405+0j) [Z1 Y3 Z4 Z5 Z6 Y7] +
(-0.06752385099214028+0j) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(1.4017109736319852e-05+0j) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.23671080783830456+0j) [Z1 Z3] +
(-3.344081556762752e-06+0j) [Z1 X4 Z5 X6] +
(-1.6103585306934262e-05+0j) [Z1 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.0906514420703649+0j) [Z1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-3.344081556762752e-06+0j) [Z1 Y4 Z5 Y6] +
(-1.6103585306934262e-05+0j) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.0906514420703649+0j) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.1993635453736084+0j) [Z1 Z4] +
(-3.0993492438630966e-06+0j) [Z1 X5 Z6 X7] +
(-1.531680879645723e-05+0j) [Z1 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.08684737589863634+0j) [Z1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.0993492438630966e-06+0j) [Z1 Y5 Z6 Y7] +
(-1.531680879645723e-05+0j) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.08684737589863634+0j) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.19661770890342156+0j) [Z1 Z5] +
(0.056007330877808+0j) [Z1 X6 Z7 Z8 Z9 X10] +
(-6.481851834460914e-06+0j) [Z1 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.056007330877808+0j) [Z1 Y6 Z7 Z8 Z9 Y10] +
(-6.481851834460914e-06+0j) [Z1 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.24853483371314222+0j) [Z1 Z6] +
(0.05608468124661388+0j) [Z1 X7 Z8 Z9 Z10 X11] +
(-6.652209670011996e-06+0j) [Z1 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.05608468124661388+0j) [Z1 Y7 Z8 Z9 Z10 Y11] +
(-6.652209670011996e-06+0j) [Z1 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.24164663936017164+0j) [Z1 Z7] +
(0.2788345442672343+0j) [Z1 Z8] +
(0.272325183066057+0j) [Z1 Z9] +
(-1.6148794140874765e-06+0j) [Z1 X10 Z11 X12] +
(-1.6148794140874765e-06+0j) [Z1 Y10 Z11 Y12] +
(0.2007286646044184+0j) [Z1 Z10] +
(-2.1776646052595345e-06+0j) [Z1 X11 Z12 X13] +
(-2.1776646052595345e-06+0j) [Z1 Y11 Z12 Y13] +
(0.1929972393536431+0j) [Z1 Z11] +
(0.21631037498631844+0j) [Z1 Z12] +
(0.21102659849791547+0j) [Z1 Z13] +
(-0.03583956795335347+0j) [X2 X3 Y4 Y5] +
(-2.1990516187860725e-07+0j) [X2 X3 Y4 Z5 Z6 Y7] +
(-2.36095632049585e-06+0j) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.010311482489831825+0j) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.1990516187860725e-07+0j) [X2 X3 X5 X6] +
(-2.36095632049585e-06+0j) [X2 X3 X5 Z6 Z7 Z8 Z9 X10] +
(-0.010311482489831826+0j) [X2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.031143817988967207+0j) [X2 X3 Y6 Y7] +
(0.0053686593581095884+0j) [X2 X3 Y6 Z7 Z8 Z9 Z10 Y11] +
(9.209350643187808e-08+0j) [X2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0053686593581095884+0j) [X2 X3 X7 Z8 Z9 X10] +
(9.209350643187808e-08+0j) [X2 X3 X7 Z8 Z9 Z10 Z11 X12] +
(-0.03619412355904265+0j) [X2 X3 Y8 Y9] +
(-0.02538465750845742+0j) [X2 X3 Y10 Y11] +
(2.172669101666623e-06+0j) [X2 X3 Y10 Z11 Z12 Y13] +
(2.1726691016666234e-06+0j) [X2 X3 X11 X12] +
(-0.01557720806397649+0j) [X2 X3 Y12 Y13] +
(0.03583956795335347+0j) [X2 Y3 Y4 X5] +
(2.1990516187860725e-07+0j) [X2 Y3 Y4 Z5 Z6 X7] +
(2.36095632049585e-06+0j) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(0.010311482489831825+0j) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.1990516187860725e-07+0j) [X2 Y3 Y5 X6] +
(-2.36095632049585e-06+0j) [X2 Y3 Y5 Z6 Z7 Z8 Z9 X10] +
(-0.010311482489831826+0j) [X2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.031143817988967207+0j) [X2 Y3 Y6 X7] +
(-0.0053686593581095884+0j) [X2 Y3 Y6 Z7 Z8 Z9 Z10 X11] +
(-9.209350643187808e-08+0j) [X2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0053686593581095884+0j) [X2 Y3 Y7 Z8 Z9 X10] +
(9.209350643187808e-08+0j) [X2 Y3 Y7 Z8 Z9 Z10 Z11 X12] +
(0.03619412355904265+0j) [X2 Y3 Y8 X9] +
(0.02538465750845742+0j) [X2 Y3 Y10 X11] +
(-2.172669101666623e-06+0j) [X2 Y3 Y10 Z11 Z12 X13] +
(2.1726691016666234e-06+0j) [X2 Y3 Y11 X12] +
(0.01557720806397649+0j) [X2 Y3 Y12 X13] +
(-3.887051673291464e-06+0j) [X2 Z3 X4] +
(-0.0051433917688252+0j) [X2 Z3 X4 X5 Z6 X7] +
(-0.009841749246962557+0j) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(2.9885117064760073e-06+0j) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0051433917688252+0j) [X2 Z3 X4 Y5 Z6 Y7] +
(-0.009841749246962557+0j) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(2.9885117064760073e-06+0j) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.76499411929081e-07+0j) [X2 Z3 X4 Z5] +
(1.6893489516081225e-06+0j) [X2 Z3 X4 X6 Z7 Z8 Z9 X10] +
(0.010757563953908991+0j) [X2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.5371780959323774e-08+0j) [X2 Z3 X4 Y6 Z7 Z8 Z9 Y10] +
(4.20554841121714e-05+0j) [X2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(2.5935343914064324e-07+0j) [X2 Z3 X4 Z6] +
(3.2118420193521272e-06+0j) [X2 Z3 X4 X7 Z8 Z9 Z10 X11] +
(0.019299560579363845+0j) [X2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(3.2118420193521272e-06+0j) [X2 Z3 X4 Y7 Z8 Z9 Z10 Y11] +
(0.019299560579363845+0j) [X2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.1954890100069747e-06+0j) [X2 Z3 X4 Z7] +
(2.186842377890564e-07+0j) [X2 Z3 X4 Z8] +
(-5.770052994983812e-07+0j) [X2 Z3 X4 Z9] +
(0.015588250102380158+0j) [X2 Z3 X4 X10 Z11 X12] +
(0.005324835234221693+0j) [X2 Z3 X4 Y10 Z11 Y12] +
(-3.1586564322371085e-06+0j) [X2 Z3 X4 Z10] +
(0.02435307767806891+0j) [X2 Z3 X4 X11 Z12 X13] +
(0.02435307767806891+0j) [X2 Z3 X4 Y11 Z12 Y13] +
(-7.801707501032105e-06+0j) [X2 Z3 X4 Z11] +
(3.53905418475785e-06+0j) [X2 Z3 X4 Z12] +
(8.81493730731487e-06+0j) [X2 Z3 X4 Z13] +
(1.628853243660854e-06+0j) [X2 Z3 Y4 Y6 Z7 Z8 Z9 X10] +
(0.010715508469796818+0j) [X2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.010263414868158467+0j) [X2 Z3 Y4 Y10 Z11 X12] +
(-1.4548424491476181e-06+0j) [X2 Z3 Z4 X5 Y6 Y7] +
(-3.1513463114048586e-06+0j) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Y11] +
(-0.019257505095251672+0j) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.5224930677440051e-06+0j) [X2 Z3 Z4 X5 X7 Z8 Z9 X10] +
(-0.00854199662545485+0j) [X2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12] +
(-7.956895372874376e-07+0j) [X2 Z3 Z4 X5 Y8 Y9] +
(-4.643051068794997e-06+0j) [X2 Z3 Z4 X5 Y10 Y11] +
(-0.019028242443847213+0j) [X2 Z3 Z4 X5 Y10 Z11 Z12 Y13] +
(-0.00876482757568875+0j) [X2 Z3 Z4 X5 X11 X12] +
(5.275883122557021e-06+0j) [X2 Z3 Z4 X5 Y12 Y13] +
(1.4548424491476181e-06+0j) [X2 Z3 Z4 Y5 Y6 X7] +
(3.1513463114048586e-06+0j) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 X11] +
(0.019257505095251672+0j) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.5224930677440051e-06+0j) [X2 Z3 Z4 Y5 Y7 Z8 Z9 X10] +
(-0.00854199662545485+0j) [X2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12] +
(7.956895372874376e-07+0j) [X2 Z3 Z4 Y5 Y8 X9] +
(4.643051068794997e-06+0j) [X2 Z3 Z4 Y5 Y10 X11] +
(0.019028242443847213+0j) [X2 Z3 Z4 Y5 Y10 Z11 Z12 X13] +
(-0.00876482757568875+0j) [X2 Z3 Z4 Y5 Y11 X12] +
(-5.275883122557021e-06+0j) [X2 Z3 Z4 Y5 Y12 X13] +
(-0.12133276911042402+0j) [X2 Z3 Z4 Z5 X6] +
(-0.008469978791024069+0j) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11] +
(2.6863815457997116e-07+0j) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.008469978791024069+0j) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11] +
(2.6863815457997116e-07+0j) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.025996177598021114+0j) [X2 Z3 Z4 Z5 X6 Z7] +
(-0.00580518898982703+0j) [X2 Z3 Z4 Z5 X6 Z8] +
(-0.017561202409646273+0j) [X2 Z3 Z4 Z5 X6 Z9] +
(-7.988770289017538e-07+0j) [X2 Z3 Z4 Z5 X6 X10 Z11 X12] +
(-3.427323108945354e-07+0j) [X2 Z3 Z4 Z5 X6 Y10 Z11 Y12] +
(-0.0008145313270957592+0j) [X2 Z3 Z4 Z5 X6 Z10] +
(2.7455184006846534e-06+0j) [X2 Z3 Z4 Z5 X6 X11 Z12 X13] +
(2.7455184006846534e-06+0j) [X2 Z3 Z4 Z5 X6 Y11 Z12 Y13] +
(0.014411099430130834+0j) [X2 Z3 Z4 Z5 X6 Z11] +
(0.0006650070219498469+0j) [X2 Z3 Z4 Z5 X6 Z12] +
(-0.003493790359890181+0j) [X2 Z3 Z4 Z5 X6 Z13] +
(-4.5614471800721865e-07+0j) [X2 Z3 Z4 Z5 Y6 Y10 Z11 X12] +
(-0.011756013419819245+0j) [X2 Z3 Z4 Z5 Z6 X7 Y8 Y9] +
(0.015225630757226593+0j) [X2 Z3 Z4 Z5 Z6 X7 Y10 Y11] +
(-3.088250711579188e-06+0j) [X2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13] +
(-3.544395429586407e-06+0j) [X2 Z3 Z4 Z5 Z6 X7 X11 X12] +
(-0.004158797381840028+0j) [X2 Z3 Z4 Z5 Z6 X7 Y12 Y13] +
(0.011756013419819245+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y8 X9] +
(-0.015225630757226593+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y10 X11] +
(3.088250711579188e-06+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13] +
(-3.544395429586407e-06+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y11 X12] +
(0.004158797381840028+0j) [X2 Z3 Z4 Z5 Z6 Y7 Y12 X13] +
(0.014603704729162103+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11] +
(-2.874299071600197e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(0.014603704729162103+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11] +
(-2.874299071600197e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(-0.28164257767022904+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(-1.3002946562801493e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13] +
(-1.3002946562801493e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13] +
(-0.024282117354693218+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11] +
(-0.019538050311314774+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12] +
(-0.017091553155898886+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13] +
(0.002446497155415883+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(-0.002446497155415883+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(5.7759505277320615e-05+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(2.88367657631775e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(5.146496327919046e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12] +
(3.846201671638895e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12] +
(-0.03935916802205304+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 X10] +
(7.979825794021258e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12] +
(-0.024755463292890943+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z9 X10] +
(5.10552672242106e-06+0j) [X2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12] +
(-0.021433810721600766+0j) [X2 Z3 Z4 Z5 Z6 Z8 Z9 X10] +
(5.159350502342575e-06+0j) [X2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12] +
(-0.029903789512624835+0j) [X2 Z3 Z4 Z5 Z7 Z8 Z9 X10] +
(5.427988656922546e-06+0j) [X2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12] +
(0.0016638798784907585+0j) [X2 Z3 Z4 X6] +
(-0.018889030304942947+0j) [X2 Z3 Z4 Z6 Z7 Z8 Z9 X10] +
(2.9473560120132917e-06+0j) [X2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.0034795118903344427+0j) [X2 Z3 Z5 X6] +
(-0.0287307795519055+0j) [X2 Z3 Z5 Z6 Z7 Z8 Z9 X10] +
(5.935867718489299e-06+0j) [X2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.6021167407663692e-06+0j) [X2 X4] +
(0.0004956762314914298+0j) [X2 Z4 Z5 X6] +
(-0.035608378988312546+0j) [X2 Z4 Z5 Z6 Z7 Z8 Z9 X10] +
(7.2532733486802115e-06+0j) [X2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.03583956795335347+0j) [Y2 X3 X4 Y5] +
(2.1990516187860725e-07+0j) [Y2 X3 X4 Z5 Z6 Y7] +
(2.36095632049585e-06+0j) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(0.010311482489831825+0j) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-2.1990516187860725e-07+0j) [Y2 X3 X5 Y6] +
(-2.36095632049585e-06+0j) [Y2 X3 X5 Z6 Z7 Z8 Z9 Y10] +
(-0.010311482489831826+0j) [Y2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.031143817988967207+0j) [Y2 X3 X6 Y7] +
(-0.0053686593581095884+0j) [Y2 X3 X6 Z7 Z8 Z9 Z10 Y11] +
(-9.209350643187808e-08+0j) [Y2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.0053686593581095884+0j) [Y2 X3 X7 Z8 Z9 Y10] +
(9.209350643187808e-08+0j) [Y2 X3 X7 Z8 Z9 Z10 Z11 Y12] +
(0.03619412355904265+0j) [Y2 X3 X8 Y9] +
(0.02538465750845742+0j) [Y2 X3 X10 Y11] +
(-2.172669101666623e-06+0j) [Y2 X3 X10 Z11 Z12 Y13] +
(2.1726691016666234e-06+0j) [Y2 X3 X11 Y12] +
(0.01557720806397649+0j) [Y2 X3 X12 Y13] +
(-0.03583956795335347+0j) [Y2 Y3 X4 X5] +
(-2.1990516187860725e-07+0j) [Y2 Y3 X4 Z5 Z6 X7] +
(-2.36095632049585e-06+0j) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.010311482489831825+0j) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-2.1990516187860725e-07+0j) [Y2 Y3 Y5 Y6] +
(-2.36095632049585e-06+0j) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Y10] +
(-0.010311482489831826+0j) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.031143817988967207+0j) [Y2 Y3 X6 X7] +
(0.0053686593581095884+0j) [Y2 Y3 X6 Z7 Z8 Z9 Z10 X11] +
(9.209350643187808e-08+0j) [Y2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.0053686593581095884+0j) [Y2 Y3 Y7 Z8 Z9 Y10] +
(9.209350643187808e-08+0j) [Y2 Y3 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.03619412355904265+0j) [Y2 Y3 X8 X9] +
(-0.02538465750845742+0j) [Y2 Y3 X10 X11] +
(2.172669101666623e-06+0j) [Y2 Y3 X10 Z11 Z12 X13] +
(2.1726691016666234e-06+0j) [Y2 Y3 Y11 Y12] +
(-0.01557720806397649+0j) [Y2 Y3 X12 X13] +
(1.628853243660854e-06+0j) [Y2 Z3 X4 X6 Z7 Z8 Z9 Y10] +
(0.010715508469796818+0j) [Y2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.010263414868158467+0j) [Y2 Z3 X4 X10 Z11 Y12] +
(-3.887051673291464e-06+0j) [Y2 Z3 Y4] +
(-0.0051433917688252+0j) [Y2 Z3 Y4 X5 Z6 X7] +
(-0.009841749246962557+0j) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(2.9885117064760073e-06+0j) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0051433917688252+0j) [Y2 Z3 Y4 Y5 Z6 Y7] +
(-0.009841749246962557+0j) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(2.9885117064760073e-06+0j) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.76499411929081e-07+0j) [Y2 Z3 Y4 Z5] +
(4.5371780959323774e-08+0j) [Y2 Z3 Y4 X6 Z7 Z8 Z9 X10] +
(4.20554841121714e-05+0j) [Y2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(1.6893489516081225e-06+0j) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Y10] +
(0.010757563953908991+0j) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(2.5935343914064324e-07+0j) [Y2 Z3 Y4 Z6] +
(3.2118420193521272e-06+0j) [Y2 Z3 Y4 X7 Z8 Z9 Z10 X11] +
(0.019299560579363845+0j) [Y2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(3.2118420193521272e-06+0j) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Y11] +
(0.019299560579363845+0j) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.1954890100069747e-06+0j) [Y2 Z3 Y4 Z7] +
(2.186842377890564e-07+0j) [Y2 Z3 Y4 Z8] +
(-5.770052994983812e-07+0j) [Y2 Z3 Y4 Z9] +
(0.005324835234221693+0j) [Y2 Z3 Y4 X10 Z11 X12] +
(0.015588250102380158+0j) [Y2 Z3 Y4 Y10 Z11 Y12] +
(-3.1586564322371085e-06+0j) [Y2 Z3 Y4 Z10] +
(0.02435307767806891+0j) [Y2 Z3 Y4 X11 Z12 X13] +
(0.02435307767806891+0j) [Y2 Z3 Y4 Y11 Z12 Y13] +
(-7.801707501032105e-06+0j) [Y2 Z3 Y4 Z11] +
(3.53905418475785e-06+0j) [Y2 Z3 Y4 Z12] +
(8.81493730731487e-06+0j) [Y2 Z3 Y4 Z13] +
(1.4548424491476181e-06+0j) [Y2 Z3 Z4 X5 X6 Y7] +
(3.1513463114048586e-06+0j) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Y11] +
(0.019257505095251672+0j) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.5224930677440051e-06+0j) [Y2 Z3 Z4 X5 X7 Z8 Z9 Y10] +
(-0.00854199662545485+0j) [Y2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12] +
(7.956895372874376e-07+0j) [Y2 Z3 Z4 X5 X8 Y9] +
(4.643051068794997e-06+0j) [Y2 Z3 Z4 X5 X10 Y11] +
(0.019028242443847213+0j) [Y2 Z3 Z4 X5 X10 Z11 Z12 Y13] +
(-0.00876482757568875+0j) [Y2 Z3 Z4 X5 X11 Y12] +
(-5.275883122557021e-06+0j) [Y2 Z3 Z4 X5 X12 Y13] +
(-1.4548424491476181e-06+0j) [Y2 Z3 Z4 Y5 X6 X7] +
(-3.1513463114048586e-06+0j) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 X11] +
(-0.019257505095251672+0j) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.5224930677440051e-06+0j) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Y10] +
(-0.00854199662545485+0j) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12] +
(-7.956895372874376e-07+0j) [Y2 Z3 Z4 Y5 X8 X9] +
(-4.643051068794997e-06+0j) [Y2 Z3 Z4 Y5 X10 X11] +
(-0.019028242443847213+0j) [Y2 Z3 Z4 Y5 X10 Z11 Z12 X13] +
(-0.00876482757568875+0j) [Y2 Z3 Z4 Y5 Y11 Y12] +
(5.275883122557021e-06+0j) [Y2 Z3 Z4 Y5 X12 X13] +
(-4.5614471800721865e-07+0j) [Y2 Z3 Z4 Z5 X6 X10 Z11 Y12] +
(-0.12133276911042402+0j) [Y2 Z3 Z4 Z5 Y6] +
(-0.008469978791024069+0j) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11] +
(2.6863815457997116e-07+0j) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.008469978791024069+0j) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11] +
(2.6863815457997116e-07+0j) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.025996177598021114+0j) [Y2 Z3 Z4 Z5 Y6 Z7] +
(-0.00580518898982703+0j) [Y2 Z3 Z4 Z5 Y6 Z8] +
(-0.017561202409646273+0j) [Y2 Z3 Z4 Z5 Y6 Z9] +
(-3.427323108945354e-07+0j) [Y2 Z3 Z4 Z5 Y6 X10 Z11 X12] +
(-7.988770289017538e-07+0j) [Y2 Z3 Z4 Z5 Y6 Y10 Z11 Y12] +
(-0.0008145313270957592+0j) [Y2 Z3 Z4 Z5 Y6 Z10] +
(2.7455184006846534e-06+0j) [Y2 Z3 Z4 Z5 Y6 X11 Z12 X13] +
(2.7455184006846534e-06+0j) [Y2 Z3 Z4 Z5 Y6 Y11 Z12 Y13] +
(0.014411099430130834+0j) [Y2 Z3 Z4 Z5 Y6 Z11] +
(0.0006650070219498469+0j) [Y2 Z3 Z4 Z5 Y6 Z12] +
(-0.003493790359890181+0j) [Y2 Z3 Z4 Z5 Y6 Z13] +
(0.011756013419819245+0j) [Y2 Z3 Z4 Z5 Z6 X7 X8 Y9] +
(-0.015225630757226593+0j) [Y2 Z3 Z4 Z5 Z6 X7 X10 Y11] +
(3.088250711579188e-06+0j) [Y2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13] +
(-3.544395429586407e-06+0j) [Y2 Z3 Z4 Z5 Z6 X7 X11 Y12] +
(0.004158797381840028+0j) [Y2 Z3 Z4 Z5 Z6 X7 X12 Y13] +
(-0.011756013419819245+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X8 X9] +
(0.015225630757226593+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X10 X11] +
(-3.088250711579188e-06+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13] +
(-3.544395429586407e-06+0j) [Y2 Z3 Z4 Z5 Z6 Y7 Y11 Y12] +
(-0.004158797381840028+0j) [Y2 Z3 Z4 Z5 Z6 Y7 X12 X13] +
(0.014603704729162103+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11] +
(-2.874299071600197e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(0.014603704729162103+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11] +
(-2.874299071600197e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(-0.28164257767022904+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-1.3002946562801493e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13] +
(-1.3002946562801493e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13] +
(-0.024282117354693218+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11] +
(-0.019538050311314774+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12] +
(-0.017091553155898886+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13] +
(-0.002446497155415883+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(0.002446497155415883+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(5.7759505277320615e-05+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(2.88367657631775e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(5.146496327919046e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12] +
(3.846201671638895e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12] +
(-0.03935916802205304+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Y10] +
(7.979825794021258e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12] +
(-0.024755463292890943+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Y10] +
(5.10552672242106e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12] +
(-0.021433810721600766+0j) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Y10] +
(5.159350502342575e-06+0j) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12] +
(-0.029903789512624835+0j) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Y10] +
(5.427988656922546e-06+0j) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.0016638798784907585+0j) [Y2 Z3 Z4 Y6] +
(-0.018889030304942947+0j) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Y10] +
(2.9473560120132917e-06+0j) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.0034795118903344427+0j) [Y2 Z3 Z5 Y6] +
(-0.0287307795519055+0j) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Y10] +
(5.935867718489299e-06+0j) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.6021167407663692e-06+0j) [Y2 Y4] +
(0.0004956762314914298+0j) [Y2 Z4 Z5 Y6] +
(-0.035608378988312546+0j) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Y10] +
(7.2532733486802115e-06+0j) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(1.6538942226831703+0j) [Z2] +
(1.6021167407663692e-06+0j) [Z2 X3 Z4 X5] +
(0.0004956762314914298+0j) [Z2 X3 Z4 Z5 Z6 X7] +
(-0.035608378988312546+0j) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(7.2532733486802115e-06+0j) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.6021167407663692e-06+0j) [Z2 Y3 Z4 Y5] +
(0.0004956762314914298+0j) [Z2 Y3 Z4 Z5 Z6 Y7] +
(-0.035608378988312546+0j) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(7.2532733486802115e-06+0j) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.18189085790751366+0j) [Z2 Z3] +
(-9.509249752487325e-07+0j) [Z2 X4 Z5 X6] +
(-4.728843147546514e-06+0j) [Z2 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.024591860883830006+0j) [Z2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-9.509249752487325e-07+0j) [Z2 Y4 Z5 Y6] +
(-4.728843147546514e-06+0j) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.024591860883830006+0j) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.12495807739503215+0j) [Z2 Z4] +
(-1.1708301371273398e-06+0j) [Z2 X5 Z6 X7] +
(-7.089799468042364e-06+0j) [Z2 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.03490334337366183+0j) [Z2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.1708301371273398e-06+0j) [Z2 Y5 Z6 Y7] +
(-7.089799468042364e-06+0j) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.03490334337366183+0j) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.16079764534838561+0j) [Z2 Z5] +
(0.019020423173040084+0j) [Z2 X6 Z7 Z8 Z9 X10] +
(-2.1032156048739384e-06+0j) [Z2 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.019020423173040084+0j) [Z2 Y6 Z7 Z8 Z9 Y10] +
(-2.1032156048739384e-06+0j) [Z2 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.13739104762683207+0j) [Z2 Z6] +
(0.024389082531149672+0j) [Z2 X7 Z8 Z9 Z10 X11] +
(-2.01112209844206e-06+0j) [Z2 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.024389082531149672+0j) [Z2 Y7 Z8 Z9 Z10 Y11] +
(-2.01112209844206e-06+0j) [Z2 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.16853486561579928+0j) [Z2 Z7] +
(0.15071408121008292+0j) [Z2 Z8] +
(0.1869082047691256+0j) [Z2 Z9] +
(-1.06322834249796e-06+0j) [Z2 X10 Z11 X12] +
(-1.06322834249796e-06+0j) [Z2 Y10 Z11 Y12] +
(0.12799502492468431+0j) [Z2 Z10] +
(1.1094407591686632e-06+0j) [Z2 X11 Z12 X13] +
(1.1094407591686632e-06+0j) [Z2 Y11 Z12 Y13] +
(0.15337968243314173+0j) [Z2 Z11] +
(0.14011289865354823+0j) [Z2 Z12] +
(0.15569010671752476+0j) [Z2 Z13] +
(0.0051433917688252+0j) [X3 X4 Y5 Y6] +
(0.009841749246962557+0j) [X3 X4 Y5 Z6 Z7 Z8 Z9 Y10] +
(-2.9885117064760073e-06+0j) [X3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.4548424491476181e-06+0j) [X3 X4 X6 X7] +
(-1.5224930677440051e-06+0j) [X3 X4 X6 Z7 Z8 Z9 Z10 X11] +
(-0.00854199662545485+0j) [X3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-3.1513463114048586e-06+0j) [X3 X4 Y7 Z8 Z9 Y10] +
(-0.019257505095251672+0j) [X3 X4 Y7 Z8 Z9 Z10 Z11 Y12] +
(-7.956895372874376e-07+0j) [X3 X4 X8 X9] +
(-4.643051068794997e-06+0j) [X3 X4 X10 X11] +
(-0.00876482757568875+0j) [X3 X4 X10 Z11 Z12 X13] +
(-0.019028242443847213+0j) [X3 X4 Y11 Y12] +
(5.275883122557022e-06+0j) [X3 X4 X12 X13] +
(-0.0051433917688252+0j) [X3 Y4 Y5 X6] +
(-0.009841749246962557+0j) [X3 Y4 Y5 Z6 Z7 Z8 Z9 X10] +
(2.9885117064760073e-06+0j) [X3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.4548424491476181e-06+0j) [X3 Y4 Y6 X7] +
(-1.5224930677440051e-06+0j) [X3 Y4 Y6 Z7 Z8 Z9 Z10 X11] +
(-0.00854199662545485+0j) [X3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(3.1513463114048586e-06+0j) [X3 Y4 Y7 Z8 Z9 X10] +
(0.019257505095251672+0j) [X3 Y4 Y7 Z8 Z9 Z10 Z11 X12] +
(-7.956895372874376e-07+0j) [X3 Y4 Y8 X9] +
(-4.643051068794997e-06+0j) [X3 Y4 Y10 X11] +
(-0.00876482757568875+0j) [X3 Y4 Y10 Z11 Z12 X13] +
(0.019028242443847213+0j) [X3 Y4 Y11 X12] +
(5.275883122557022e-06+0j) [X3 Y4 Y12 X13] +
(-3.887051673291462e-06+0j) [X3 Z4 X5] +
(3.2118420193521272e-06+0j) [X3 Z4 X5 X6 Z7 Z8 Z9 X10] +
(0.019299560579363845+0j) [X3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(3.2118420193521272e-06+0j) [X3 Z4 X5 Y6 Z7 Z8 Z9 Y10] +
(0.019299560579363845+0j) [X3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.1954890100069747e-06+0j) [X3 Z4 X5 Z6] +
(1.6893489516081225e-06+0j) [X3 Z4 X5 X7 Z8 Z9 Z10 X11] +
(0.010757563953908991+0j) [X3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.5371780959323774e-08+0j) [X3 Z4 X5 Y7 Z8 Z9 Z10 Y11] +
(4.20554841121714e-05+0j) [X3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(2.5935343914064324e-07+0j) [X3 Z4 X5 Z7] +
(-5.770052994983812e-07+0j) [X3 Z4 X5 Z8] +
(2.186842377890564e-07+0j) [X3 Z4 X5 Z9] +
(0.02435307767806891+0j) [X3 Z4 X5 X10 Z11 X12] +
(0.02435307767806891+0j) [X3 Z4 X5 Y10 Z11 Y12] +
(-7.801707501032105e-06+0j) [X3 Z4 X5 Z10] +
(0.015588250102380158+0j) [X3 Z4 X5 X11 Z12 X13] +
(0.005324835234221693+0j) [X3 Z4 X5 Y11 Z12 Y13] +
(-3.1586564322371085e-06+0j) [X3 Z4 X5 Z11] +
(8.81493730731487e-06+0j) [X3 Z4 X5 Z12] +
(3.53905418475785e-06+0j) [X3 Z4 X5 Z13] +
(1.628853243660854e-06+0j) [X3 Z4 Y5 Y7 Z8 Z9 Z10 X11] +
(0.010715508469796818+0j) [X3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.010263414868158467+0j) [X3 Z4 Y5 Y11 Z12 X13] +
(0.008469978791024069+0j) [X3 Z4 Z5 X6 Y7 Z8 Z9 Y10] +
(-2.6863815457997116e-07+0j) [X3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.011756013419819245+0j) [X3 Z4 Z5 X6 X8 X9] +
(0.015225630757226593+0j) [X3 Z4 Z5 X6 X10 X11] +
(-3.544395429586407e-06+0j) [X3 Z4 Z5 X6 X10 Z11 Z12 X13] +
(-3.088250711579188e-06+0j) [X3 Z4 Z5 X6 Y11 Y12] +
(-0.004158797381840028+0j) [X3 Z4 Z5 X6 X12 X13] +
(-0.008469978791024069+0j) [X3 Z4 Z5 Y6 Y7 Z8 Z9 X10] +
(2.6863815457997116e-07+0j) [X3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12] +
(-0.011756013419819245+0j) [X3 Z4 Z5 Y6 Y8 X9] +
(0.015225630757226593+0j) [X3 Z4 Z5 Y6 Y10 X11] +
(-3.544395429586407e-06+0j) [X3 Z4 Z5 Y6 Y10 Z11 Z12 X13] +
(3.088250711579188e-06+0j) [X3 Z4 Z5 Y6 Y11 X12] +
(-0.004158797381840028+0j) [X3 Z4 Z5 Y6 Y12 X13] +
(-0.12133276911042402+0j) [X3 Z4 Z5 Z6 X7] +
(-0.017561202409646273+0j) [X3 Z4 Z5 Z6 X7 Z8] +
(-0.00580518898982703+0j) [X3 Z4 Z5 Z6 X7 Z9] +
(2.7455184006846534e-06+0j) [X3 Z4 Z5 Z6 X7 X10 Z11 X12] +
(2.7455184006846534e-06+0j) [X3 Z4 Z5 Z6 X7 Y10 Z11 Y12] +
(0.014411099430130834+0j) [X3 Z4 Z5 Z6 X7 Z10] +
(-7.988770289017538e-07+0j) [X3 Z4 Z5 Z6 X7 X11 Z12 X13] +
(-3.427323108945354e-07+0j) [X3 Z4 Z5 Z6 X7 Y11 Z12 Y13] +
(-0.0008145313270957592+0j) [X3 Z4 Z5 Z6 X7 Z11] +
(-0.003493790359890181+0j) [X3 Z4 Z5 Z6 X7 Z12] +
(0.0006650070219498469+0j) [X3 Z4 Z5 Z6 X7 Z13] +
(-4.5614471800721865e-07+0j) [X3 Z4 Z5 Z6 Y7 Y11 Z12 X13] +
(-0.014603704729162103+0j) [X3 Z4 Z5 Z6 Z7 X8 Y9 Y10] +
(2.874299071600197e-06+0j) [X3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12] +
(0.014603704729162103+0j) [X3 Z4 Z5 Z6 Z7 Y8 Y9 X10] +
(-2.874299071600197e-06+0j) [X3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12] +
(1.3002946562801493e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Y12] +
(0.002446497155415883+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13] +
(-1.3002946562801493e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 X12] +
(0.002446497155415883+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13] +
(-0.28164257767022916+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.017091553155898886+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12] +
(-0.019538050311314774+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13] +
(5.775950527732062e-05+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(2.8836765763177506e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13] +
(3.846201671638895e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13] +
(-0.024282117354693218+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X11] +
(5.146496327919046e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13] +
(-0.024755463292890943+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z10 X11] +
(5.10552672242106e-06+0j) [X3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13] +
(-0.03935916802205304+0j) [X3 Z4 Z5 Z6 Z7 Z9 Z10 X11] +
(7.979825794021258e-06+0j) [X3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13] +
(-0.029903789512624835+0j) [X3 Z4 Z5 Z6 Z8 Z9 Z10 X11] +
(5.427988656922546e-06+0j) [X3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.025996177598021114+0j) [X3 Z4 Z5 X7] +
(-0.021433810721600766+0j) [X3 Z4 Z5 Z7 Z8 Z9 Z10 X11] +
(5.159350502342575e-06+0j) [X3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0034795118903344427+0j) [X3 Z4 Z6 X7] +
(-0.0287307795519055+0j) [X3 Z4 Z6 Z7 Z8 Z9 Z10 X11] +
(5.935867718489299e-06+0j) [X3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-7.76499411929081e-07+0j) [X3 X5] +
(0.0016638798784907585+0j) [X3 Z5 Z6 X7] +
(-0.018889030304942947+0j) [X3 Z5 Z6 Z7 Z8 Z9 Z10 X11] +
(2.9473560120132917e-06+0j) [X3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0051433917688252+0j) [Y3 X4 X5 Y6] +
(-0.009841749246962557+0j) [Y3 X4 X5 Z6 Z7 Z8 Z9 Y10] +
(2.9885117064760073e-06+0j) [Y3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.4548424491476181e-06+0j) [Y3 X4 X6 Y7] +
(-1.5224930677440051e-06+0j) [Y3 X4 X6 Z7 Z8 Z9 Z10 Y11] +
(-0.00854199662545485+0j) [Y3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(3.1513463114048586e-06+0j) [Y3 X4 X7 Z8 Z9 Y10] +
(0.019257505095251672+0j) [Y3 X4 X7 Z8 Z9 Z10 Z11 Y12] +
(-7.956895372874376e-07+0j) [Y3 X4 X8 Y9] +
(-4.643051068794997e-06+0j) [Y3 X4 X10 Y11] +
(-0.00876482757568875+0j) [Y3 X4 X10 Z11 Z12 Y13] +
(0.019028242443847213+0j) [Y3 X4 X11 Y12] +
(5.275883122557022e-06+0j) [Y3 X4 X12 Y13] +
(0.0051433917688252+0j) [Y3 Y4 X5 X6] +
(0.009841749246962557+0j) [Y3 Y4 X5 Z6 Z7 Z8 Z9 X10] +
(-2.9885117064760073e-06+0j) [Y3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.4548424491476181e-06+0j) [Y3 Y4 Y6 Y7] +
(-1.5224930677440051e-06+0j) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Y11] +
(-0.00854199662545485+0j) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-3.1513463114048586e-06+0j) [Y3 Y4 X7 Z8 Z9 X10] +
(-0.019257505095251672+0j) [Y3 Y4 X7 Z8 Z9 Z10 Z11 X12] +
(-7.956895372874376e-07+0j) [Y3 Y4 Y8 Y9] +
(-4.643051068794997e-06+0j) [Y3 Y4 Y10 Y11] +
(-0.00876482757568875+0j) [Y3 Y4 Y10 Z11 Z12 Y13] +
(-0.019028242443847213+0j) [Y3 Y4 X11 X12] +
(5.275883122557022e-06+0j) [Y3 Y4 Y12 Y13] +
(1.628853243660854e-06+0j) [Y3 Z4 X5 X7 Z8 Z9 Z10 Y11] +
(0.010715508469796818+0j) [Y3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.010263414868158467+0j) [Y3 Z4 X5 X11 Z12 Y13] +
(-3.887051673291462e-06+0j) [Y3 Z4 Y5] +
(3.2118420193521272e-06+0j) [Y3 Z4 Y5 X6 Z7 Z8 Z9 X10] +
(0.019299560579363845+0j) [Y3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(3.2118420193521272e-06+0j) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Y10] +
(0.019299560579363845+0j) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-1.1954890100069747e-06+0j) [Y3 Z4 Y5 Z6] +
(4.5371780959323774e-08+0j) [Y3 Z4 Y5 X7 Z8 Z9 Z10 X11] +
(4.20554841121714e-05+0j) [Y3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(1.6893489516081225e-06+0j) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Y11] +
(0.010757563953908991+0j) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(2.5935343914064324e-07+0j) [Y3 Z4 Y5 Z7] +
(-5.770052994983812e-07+0j) [Y3 Z4 Y5 Z8] +
(2.186842377890564e-07+0j) [Y3 Z4 Y5 Z9] +
(0.02435307767806891+0j) [Y3 Z4 Y5 X10 Z11 X12] +
(0.02435307767806891+0j) [Y3 Z4 Y5 Y10 Z11 Y12] +
(-7.801707501032105e-06+0j) [Y3 Z4 Y5 Z10] +
(0.005324835234221693+0j) [Y3 Z4 Y5 X11 Z12 X13] +
(0.015588250102380158+0j) [Y3 Z4 Y5 Y11 Z12 Y13] +
(-3.1586564322371085e-06+0j) [Y3 Z4 Y5 Z11] +
(8.81493730731487e-06+0j) [Y3 Z4 Y5 Z12] +
(3.53905418475785e-06+0j) [Y3 Z4 Y5 Z13] +
(-0.008469978791024069+0j) [Y3 Z4 Z5 X6 X7 Z8 Z9 Y10] +
(2.6863815457997116e-07+0j) [Y3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12] +
(-0.011756013419819245+0j) [Y3 Z4 Z5 X6 X8 Y9] +
(0.015225630757226593+0j) [Y3 Z4 Z5 X6 X10 Y11] +
(-3.544395429586407e-06+0j) [Y3 Z4 Z5 X6 X10 Z11 Z12 Y13] +
(3.088250711579188e-06+0j) [Y3 Z4 Z5 X6 X11 Y12] +
(-0.004158797381840028+0j) [Y3 Z4 Z5 X6 X12 Y13] +
(0.008469978791024069+0j) [Y3 Z4 Z5 Y6 X7 Z8 Z9 X10] +
(-2.6863815457997116e-07+0j) [Y3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12] +
(-0.011756013419819245+0j) [Y3 Z4 Z5 Y6 Y8 Y9] +
(0.015225630757226593+0j) [Y3 Z4 Z5 Y6 Y10 Y11] +
(-3.544395429586407e-06+0j) [Y3 Z4 Z5 Y6 Y10 Z11 Z12 Y13] +
(-3.088250711579188e-06+0j) [Y3 Z4 Z5 Y6 X11 X12] +
(-0.004158797381840028+0j) [Y3 Z4 Z5 Y6 Y12 Y13] +
(-4.5614471800721865e-07+0j) [Y3 Z4 Z5 Z6 X7 X11 Z12 Y13] +
(-0.12133276911042402+0j) [Y3 Z4 Z5 Z6 Y7] +
(-0.017561202409646273+0j) [Y3 Z4 Z5 Z6 Y7 Z8] +
(-0.00580518898982703+0j) [Y3 Z4 Z5 Z6 Y7 Z9] +
(2.7455184006846534e-06+0j) [Y3 Z4 Z5 Z6 Y7 X10 Z11 X12] +
(2.7455184006846534e-06+0j) [Y3 Z4 Z5 Z6 Y7 Y10 Z11 Y12] +
(0.014411099430130834+0j) [Y3 Z4 Z5 Z6 Y7 Z10] +
(-3.427323108945354e-07+0j) [Y3 Z4 Z5 Z6 Y7 X11 Z12 X13] +
(-7.988770289017538e-07+0j) [Y3 Z4 Z5 Z6 Y7 Y11 Z12 Y13] +
(-0.0008145313270957592+0j) [Y3 Z4 Z5 Z6 Y7 Z11] +
(-0.003493790359890181+0j) [Y3 Z4 Z5 Z6 Y7 Z12] +
(0.0006650070219498469+0j) [Y3 Z4 Z5 Z6 Y7 Z13] +
(0.014603704729162103+0j) [Y3 Z4 Z5 Z6 Z7 X8 X9 Y10] +
(-2.874299071600197e-06+0j) [Y3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12] +
(-0.014603704729162103+0j) [Y3 Z4 Z5 Z6 Z7 Y8 X9 X10] +
(2.874299071600197e-06+0j) [Y3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12] +
(-1.3002946562801493e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Y12] +
(0.002446497155415883+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13] +
(1.3002946562801493e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 X12] +
(0.002446497155415883+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13] +
(-0.28164257767022916+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.017091553155898886+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12] +
(-0.019538050311314774+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13] +
(5.775950527732062e-05+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(2.8836765763177506e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13] +
(3.846201671638895e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13] +
(-0.024282117354693218+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y11] +
(5.146496327919046e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13] +
(-0.024755463292890943+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Y11] +
(5.10552672242106e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13] +
(-0.03935916802205304+0j) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Y11] +
(7.979825794021258e-06+0j) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13] +
(-0.029903789512624835+0j) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Y11] +
(5.427988656922546e-06+0j) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.025996177598021114+0j) [Y3 Z4 Z5 Y7] +
(-0.021433810721600766+0j) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Y11] +
(5.159350502342575e-06+0j) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0034795118903344427+0j) [Y3 Z4 Z6 Y7] +
(-0.0287307795519055+0j) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Y11] +
(5.935867718489299e-06+0j) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-7.76499411929081e-07+0j) [Y3 Y5] +
(0.0016638798784907585+0j) [Y3 Z5 Z6 Y7] +
(-0.018889030304942947+0j) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Y11] +
(2.9473560120132917e-06+0j) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(1.65389422268317+0j) [Z3] +
(-1.1708301371273398e-06+0j) [Z3 X4 Z5 X6] +
(-7.089799468042364e-06+0j) [Z3 X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.03490334337366183+0j) [Z3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-1.1708301371273398e-06+0j) [Z3 Y4 Z5 Y6] +
(-7.089799468042364e-06+0j) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.03490334337366183+0j) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.16079764534838561+0j) [Z3 Z4] +
(-9.509249752487325e-07+0j) [Z3 X5 Z6 X7] +
(-4.728843147546514e-06+0j) [Z3 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.024591860883830006+0j) [Z3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-9.509249752487325e-07+0j) [Z3 Y5 Z6 Y7] +
(-4.728843147546514e-06+0j) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.024591860883830006+0j) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.12495807739503215+0j) [Z3 Z5] +
(0.024389082531149672+0j) [Z3 X6 Z7 Z8 Z9 X10] +
(-2.01112209844206e-06+0j) [Z3 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.024389082531149672+0j) [Z3 Y6 Z7 Z8 Z9 Y10] +
(-2.01112209844206e-06+0j) [Z3 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.16853486561579928+0j) [Z3 Z6] +
(0.019020423173040084+0j) [Z3 X7 Z8 Z9 Z10 X11] +
(-2.1032156048739384e-06+0j) [Z3 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.019020423173040084+0j) [Z3 Y7 Z8 Z9 Z10 Y11] +
(-2.1032156048739384e-06+0j) [Z3 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.13739104762683207+0j) [Z3 Z7] +
(0.1869082047691256+0j) [Z3 Z8] +
(0.15071408121008292+0j) [Z3 Z9] +
(1.1094407591686632e-06+0j) [Z3 X10 Z11 X12] +
(1.1094407591686632e-06+0j) [Z3 Y10 Z11 Y12] +
(0.15337968243314173+0j) [Z3 Z10] +
(-1.06322834249796e-06+0j) [Z3 X11 Z12 X13] +
(-1.06322834249796e-06+0j) [Z3 Y11 Z12 Y13] +
(0.12799502492468431+0j) [Z3 Z11] +
(0.15569010671752476+0j) [Z3 Z12] +
(0.14011289865354823+0j) [Z3 Z13] +
(-0.011982389010248009+0j) [X4 X5 Y6 Y7] +
(-0.0073067599288329935+0j) [X4 X5 Y6 Z7 Z8 Z9 Z10 Y11] +
(-2.8882935955911817e-07+0j) [X4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0073067599288329935+0j) [X4 X5 X7 Z8 Z9 X10] +
(-2.8882935955911817e-07+0j) [X4 X5 X7 Z8 Z9 Z10 Z11 X12] +
(-0.007156934919856939+0j) [X4 X5 Y8 Y9] +
(-0.017680067952481438+0j) [X4 X5 Y10 Y11] +
(-3.6945132947786487e-06+0j) [X4 X5 Y10 Z11 Z12 Y13] +
(-3.694513294778648e-06+0j) [X4 X5 X11 X12] +
(-0.0383146702948039+0j) [X4 X5 Y12 Y13] +
(0.011982389010248009+0j) [X4 Y5 Y6 X7] +
(0.0073067599288329935+0j) [X4 Y5 Y6 Z7 Z8 Z9 Z10 X11] +
(2.8882935955911817e-07+0j) [X4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0073067599288329935+0j) [X4 Y5 Y7 Z8 Z9 X10] +
(-2.8882935955911817e-07+0j) [X4 Y5 Y7 Z8 Z9 Z10 Z11 X12] +
(0.007156934919856939+0j) [X4 Y5 Y8 X9] +
(0.017680067952481438+0j) [X4 Y5 Y10 X11] +
(3.6945132947786487e-06+0j) [X4 Y5 Y10 Z11 Z12 X13] +
(-3.694513294778648e-06+0j) [X4 Y5 Y11 X12] +
(0.0383146702948039+0j) [X4 Y5 Y12 X13] +
(-1.226048498997459e-05+0j) [X4 Z5 X6] +
(-1.2283337825544143e-06+0j) [X4 Z5 X6 X7 Z8 Z9 Z10 X11] +
(0.0002463643756956662+0j) [X4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2283337825544143e-06+0j) [X4 Z5 X6 Y7 Z8 Z9 Z10 Y11] +
(0.0002463643756956662+0j) [X4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.8540608581190336e-06+0j) [X4 Z5 X6 Z7] +
(-1.3980449082421664e-06+0j) [X4 Z5 X6 Z8] +
(-1.8818501833592722e-06+0j) [X4 Z5 X6 Z9] +
(0.00796088072592159+0j) [X4 Z5 X6 X10 Z11 X12] +
(-0.0009298507967730881+0j) [X4 Z5 X6 Y10 Z11 Y12] +
(-1.6923978287233736e-06+0j) [X4 Z5 X6 Z10] +
(-0.012215040997614035+0j) [X4 Z5 X6 X11 Z12 X13] +
(-0.012215040997614035+0j) [X4 Z5 X6 Y11 Z12 Y13] +
(4.281913885118194e-06+0j) [X4 Z5 X6 Z11] +
(-4.5888551560321e-06+0j) [X4 Z5 X6 Z13] +
(0.008890731522694678+0j) [X4 Z5 Y6 Y10 Z11 X12] +
(-4.838052751171057e-07+0j) [X4 Z5 Z6 X7 Y8 Y9] +
(5.974311713841568e-06+0j) [X4 Z5 Z6 X7 Y10 Y11] +
(0.011285190200840945+0j) [X4 Z5 Z6 X7 Y10 Z11 Z12 Y13] +
(0.02017592172353563+0j) [X4 Z5 Z6 X7 X11 X12] +
(-4.556569218488707e-06+0j) [X4 Z5 Z6 X7 Y12 Y13] +
(4.838052751171057e-07+0j) [X4 Z5 Z6 Y7 Y8 X9] +
(-5.974311713841568e-06+0j) [X4 Z5 Z6 Y7 Y10 X11] +
(-0.011285190200840945+0j) [X4 Z5 Z6 Y7 Y10 Z11 Z12 X13] +
(0.02017592172353563+0j) [X4 Z5 Z6 Y7 Y11 X12] +
(4.556569218488707e-06+0j) [X4 Z5 Z6 Y7 Y12 X13] +
(1.3304731887619207e-06+0j) [X4 Z5 Z6 Z7 X8 X9 Z10 X11] +
(0.005923798336561343+0j) [X4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(1.3304731887619207e-06+0j) [X4 Z5 Z6 Z7 X8 Y9 Z10 Y11] +
(0.005923798336561343+0j) [X4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(-6.63127792894981e-05+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10] +
(-0.01602460368917943+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13] +
(-0.01602460368917943+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13] +
(3.3343312896348418e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z11] +
(-4.7346220390994505e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z12] +
(-9.806102775923066e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z13] +
(-5.071480736823616e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(5.071480736823616e-06+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(-0.3693708936615614+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(-0.023145130929529037+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(-0.009612634606847435+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X12] +
(-0.025637238296026862+0j) [X4 Z5 Z6 Z7 Z8 Z9 Z11 X12] +
(-8.774817865228907e-06+0j) [X4 Z5 Z6 Z7 Z8 X10] +
(-0.047642612176383076+0j) [X4 Z5 Z6 Z7 Z8 Z10 Z11 X12] +
(-7.444344676466986e-06+0j) [X4 Z5 Z6 Z7 Z9 X10] +
(-0.04171881383982173+0j) [X4 Z5 Z6 Z7 Z9 Z10 Z11 X12] +
(-6.29002843369774e-06+0j) [X4 Z5 Z6 Z8 Z9 X10] +
(-0.039564416322893134+0j) [X4 Z5 Z6 Z8 Z9 Z10 Z11 X12] +
(-7.518362216252154e-06+0j) [X4 Z5 Z7 Z8 Z9 X10] +
(-0.039318051947197466+0j) [X4 Z5 Z7 Z8 Z9 Z10 Z11 X12] +
(-5.929765816199472e-07+0j) [X4 X6] +
(-4.253224225860006e-06+0j) [X4 Z6 Z7 Z8 Z9 X10] +
(-0.02252844019601299+0j) [X4 Z6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.011982389010248009+0j) [Y4 X5 X6 Y7] +
(0.0073067599288329935+0j) [Y4 X5 X6 Z7 Z8 Z9 Z10 Y11] +
(2.8882935955911817e-07+0j) [Y4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.0073067599288329935+0j) [Y4 X5 X7 Z8 Z9 Y10] +
(-2.8882935955911817e-07+0j) [Y4 X5 X7 Z8 Z9 Z10 Z11 Y12] +
(0.007156934919856939+0j) [Y4 X5 X8 Y9] +
(0.017680067952481438+0j) [Y4 X5 X10 Y11] +
(3.6945132947786487e-06+0j) [Y4 X5 X10 Z11 Z12 Y13] +
(-3.694513294778648e-06+0j) [Y4 X5 X11 Y12] +
(0.0383146702948039+0j) [Y4 X5 X12 Y13] +
(-0.011982389010248009+0j) [Y4 Y5 X6 X7] +
(-0.0073067599288329935+0j) [Y4 Y5 X6 Z7 Z8 Z9 Z10 X11] +
(-2.8882935955911817e-07+0j) [Y4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.0073067599288329935+0j) [Y4 Y5 Y7 Z8 Z9 Y10] +
(-2.8882935955911817e-07+0j) [Y4 Y5 Y7 Z8 Z9 Z10 Z11 Y12] +
(-0.007156934919856939+0j) [Y4 Y5 X8 X9] +
(-0.017680067952481438+0j) [Y4 Y5 X10 X11] +
(-3.6945132947786487e-06+0j) [Y4 Y5 X10 Z11 Z12 X13] +
(-3.694513294778648e-06+0j) [Y4 Y5 Y11 Y12] +
(-0.0383146702948039+0j) [Y4 Y5 X12 X13] +
(0.008890731522694678+0j) [Y4 Z5 X6 X10 Z11 Y12] +
(-1.226048498997459e-05+0j) [Y4 Z5 Y6] +
(-1.2283337825544143e-06+0j) [Y4 Z5 Y6 X7 Z8 Z9 Z10 X11] +
(0.0002463643756956662+0j) [Y4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2283337825544143e-06+0j) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Y11] +
(0.0002463643756956662+0j) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.8540608581190336e-06+0j) [Y4 Z5 Y6 Z7] +
(-1.3980449082421664e-06+0j) [Y4 Z5 Y6 Z8] +
(-1.8818501833592722e-06+0j) [Y4 Z5 Y6 Z9] +
(-0.0009298507967730881+0j) [Y4 Z5 Y6 X10 Z11 X12] +
(0.00796088072592159+0j) [Y4 Z5 Y6 Y10 Z11 Y12] +
(-1.6923978287233736e-06+0j) [Y4 Z5 Y6 Z10] +
(-0.012215040997614035+0j) [Y4 Z5 Y6 X11 Z12 X13] +
(-0.012215040997614035+0j) [Y4 Z5 Y6 Y11 Z12 Y13] +
(4.281913885118194e-06+0j) [Y4 Z5 Y6 Z11] +
(-4.5888551560321e-06+0j) [Y4 Z5 Y6 Z13] +
(4.838052751171057e-07+0j) [Y4 Z5 Z6 X7 X8 Y9] +
(-5.974311713841568e-06+0j) [Y4 Z5 Z6 X7 X10 Y11] +
(-0.011285190200840945+0j) [Y4 Z5 Z6 X7 X10 Z11 Z12 Y13] +
(0.02017592172353563+0j) [Y4 Z5 Z6 X7 X11 Y12] +
(4.556569218488707e-06+0j) [Y4 Z5 Z6 X7 X12 Y13] +
(-4.838052751171057e-07+0j) [Y4 Z5 Z6 Y7 X8 X9] +
(5.974311713841568e-06+0j) [Y4 Z5 Z6 Y7 X10 X11] +
(0.011285190200840945+0j) [Y4 Z5 Z6 Y7 X10 Z11 Z12 X13] +
(0.02017592172353563+0j) [Y4 Z5 Z6 Y7 Y11 Y12] +
(-4.556569218488707e-06+0j) [Y4 Z5 Z6 Y7 X12 X13] +
(1.3304731887619207e-06+0j) [Y4 Z5 Z6 Z7 Y8 X9 Z10 X11] +
(0.005923798336561343+0j) [Y4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(1.3304731887619207e-06+0j) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Y11] +
(0.005923798336561343+0j) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(-6.63127792894981e-05+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10] +
(-0.01602460368917943+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13] +
(-0.01602460368917943+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13] +
(3.3343312896348418e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z11] +
(-4.7346220390994505e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z12] +
(-9.806102775923066e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z13] +
(5.071480736823616e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(-5.071480736823616e-06+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(-0.3693708936615614+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-0.023145130929529037+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(-0.009612634606847435+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y12] +
(-0.025637238296026862+0j) [Y4 Z5 Z6 Z7 Z8 Z9 Z11 Y12] +
(-8.774817865228907e-06+0j) [Y4 Z5 Z6 Z7 Z8 Y10] +
(-0.047642612176383076+0j) [Y4 Z5 Z6 Z7 Z8 Z10 Z11 Y12] +
(-7.444344676466986e-06+0j) [Y4 Z5 Z6 Z7 Z9 Y10] +
(-0.04171881383982173+0j) [Y4 Z5 Z6 Z7 Z9 Z10 Z11 Y12] +
(-6.29002843369774e-06+0j) [Y4 Z5 Z6 Z8 Z9 Y10] +
(-0.039564416322893134+0j) [Y4 Z5 Z6 Z8 Z9 Z10 Z11 Y12] +
(-7.518362216252154e-06+0j) [Y4 Z5 Z7 Z8 Z9 Y10] +
(-0.039318051947197466+0j) [Y4 Z5 Z7 Z8 Z9 Z10 Z11 Y12] +
(-5.929765816199472e-07+0j) [Y4 Y6] +
(-4.253224225860006e-06+0j) [Y4 Z6 Z7 Z8 Z9 Y10] +
(-0.02252844019601299+0j) [Y4 Z6 Z7 Z8 Z9 Z10 Z11 Y12] +
(-5.929765816199472e-07+0j) [Z4 X5 Z6 X7] +
(-4.2532242258600056e-06+0j) [Z4 X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-0.02252844019601299+0j) [Z4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-5.929765816199472e-07+0j) [Z4 Y5 Z6 Y7] +
(-4.2532242258600056e-06+0j) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-0.02252844019601299+0j) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.15755314797985653+0j) [Z4 Z5] +
(0.018266834869375657+0j) [Z4 X6 Z7 Z8 Z9 X10] +
(-1.6541174772827849e-06+0j) [Z4 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.018266834869375657+0j) [Z4 Y6 Z7 Z8 Z9 Y10] +
(-1.6541174772827849e-06+0j) [Z4 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.13701191674040727+0j) [Z4 Z6] +
(0.010960074940542665+0j) [Z4 X7 Z8 Z9 Z10 X11] +
(-1.942946836841903e-06+0j) [Z4 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.010960074940542665+0j) [Z4 Y7 Z8 Z9 Z10 Y11] +
(-1.942946836841903e-06+0j) [Z4 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.14899430575065528+0j) [Z4 Z7] +
(1.8782101248552699e-06+0j) [Z4 X10 Z11 X12] +
(1.8782101248552699e-06+0j) [Z4 Y10 Z11 Y12] +
(0.12489990917237617+0j) [Z4 Z10] +
(-1.8163031699233784e-06+0j) [Z4 X11 Z12 X13] +
(-1.8163031699233784e-06+0j) [Z4 Y11 Z12 Y13] +
(1.2283337825544143e-06+0j) [X5 X6 Y7 Z8 Z9 Y10] +
(-0.0002463643756956662+0j) [X5 X6 Y7 Z8 Z9 Z10 Z11 Y12] +
(-4.838052751171057e-07+0j) [X5 X6 X8 X9] +
(5.974311713841568e-06+0j) [X5 X6 X10 X11] +
(0.02017592172353563+0j) [X5 X6 X10 Z11 Z12 X13] +
(0.011285190200840945+0j) [X5 X6 Y11 Y12] +
(-4.556569218488706e-06+0j) [X5 X6 X12 X13] +
(-1.2283337825544143e-06+0j) [X5 Y6 Y7 Z8 Z9 X10] +
(0.0002463643756956662+0j) [X5 Y6 Y7 Z8 Z9 Z10 Z11 X12] +
(-4.838052751171057e-07+0j) [X5 Y6 Y8 X9] +
(5.974311713841568e-06+0j) [X5 Y6 Y10 X11] +
(0.02017592172353563+0j) [X5 Y6 Y10 Z11 Z12 X13] +
(-0.011285190200840945+0j) [X5 Y6 Y11 X12] +
(-4.556569218488706e-06+0j) [X5 Y6 Y12 X13] +
(-1.2260484989974585e-05+0j) [X5 Z6 X7] +
(-1.8818501833592722e-06+0j) [X5 Z6 X7 Z8] +
(-1.3980449082421664e-06+0j) [X5 Z6 X7 Z9] +
(-0.012215040997614035+0j) [X5 Z6 X7 X10 Z11 X12] +
(-0.012215040997614035+0j) [X5 Z6 X7 Y10 Z11 Y12] +
(4.281913885118194e-06+0j) [X5 Z6 X7 Z10] +
(0.00796088072592159+0j) [X5 Z6 X7 X11 Z12 X13] +
(-0.0009298507967730881+0j) [X5 Z6 X7 Y11 Z12 Y13] +
(-1.6923978287233736e-06+0j) [X5 Z6 X7 Z11] +
(-4.5888551560321e-06+0j) [X5 Z6 X7 Z12] +
(0.008890731522694678+0j) [X5 Z6 Y7 Y11 Z12 X13] +
(-1.3304731887619205e-06+0j) [X5 Z6 Z7 X8 Y9 Y10] +
(-0.005923798336561343+0j) [X5 Z6 Z7 X8 Y9 Z10 Z11 Y12] +
(1.3304731887619205e-06+0j) [X5 Z6 Z7 Y8 Y9 X10] +
(0.005923798336561343+0j) [X5 Z6 Z7 Y8 Y9 Z10 Z11 X12] +
(0.01602460368917943+0j) [X5 Z6 Z7 Z8 Z9 X10 Y11 Y12] +
(-5.071480736823616e-06+0j) [X5 Z6 Z7 Z8 Z9 X10 X12 X13] +
(-0.01602460368917943+0j) [X5 Z6 Z7 Z8 Z9 Y10 Y11 X12] +
(-5.071480736823616e-06+0j) [X5 Z6 Z7 Z8 Z9 Y10 Y12 X13] +
(-6.631277928949807e-05+0j) [X5 Z6 Z7 Z8 Z9 Z10 X11] +
(-9.806102775923066e-06+0j) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z12] +
(-4.7346220390994505e-06+0j) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z13] +
(-0.3693708936615614+0j) [X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-0.023145130929529037+0j) [X5 Z6 Z7 Z8 Z9 Z10 Z11 X13] +
(-0.025637238296026862+0j) [X5 Z6 Z7 Z8 Z9 Z10 Z12 X13] +
(3.3343312896348418e-06+0j) [X5 Z6 Z7 Z8 Z9 X11] +
(-0.009612634606847435+0j) [X5 Z6 Z7 Z8 Z9 Z11 Z12 X13] +
(-7.444344676466986e-06+0j) [X5 Z6 Z7 Z8 Z10 X11] +
(-0.04171881383982173+0j) [X5 Z6 Z7 Z8 Z10 Z11 Z12 X13] +
(-8.774817865228907e-06+0j) [X5 Z6 Z7 Z9 Z10 X11] +
(-0.047642612176383076+0j) [X5 Z6 Z7 Z9 Z10 Z11 Z12 X13] +
(-7.518362216252154e-06+0j) [X5 Z6 Z8 Z9 Z10 X11] +
(-0.039318051947197466+0j) [X5 Z6 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.8540608581190336e-06+0j) [X5 X7] +
(-6.29002843369774e-06+0j) [X5 Z7 Z8 Z9 Z10 X11] +
(-0.039564416322893134+0j) [X5 Z7 Z8 Z9 Z10 Z11 Z12 X13] +
(-1.2283337825544143e-06+0j) [Y5 X6 X7 Z8 Z9 Y10] +
(0.0002463643756956662+0j) [Y5 X6 X7 Z8 Z9 Z10 Z11 Y12] +
(-4.838052751171057e-07+0j) [Y5 X6 X8 Y9] +
(5.974311713841568e-06+0j) [Y5 X6 X10 Y11] +
(0.02017592172353563+0j) [Y5 X6 X10 Z11 Z12 Y13] +
(-0.011285190200840945+0j) [Y5 X6 X11 Y12] +
(-4.556569218488706e-06+0j) [Y5 X6 X12 Y13] +
(1.2283337825544143e-06+0j) [Y5 Y6 X7 Z8 Z9 X10] +
(-0.0002463643756956662+0j) [Y5 Y6 X7 Z8 Z9 Z10 Z11 X12] +
(-4.838052751171057e-07+0j) [Y5 Y6 Y8 Y9] +
(5.974311713841568e-06+0j) [Y5 Y6 Y10 Y11] +
(0.02017592172353563+0j) [Y5 Y6 Y10 Z11 Z12 Y13] +
(0.011285190200840945+0j) [Y5 Y6 X11 X12] +
(-4.556569218488706e-06+0j) [Y5 Y6 Y12 Y13] +
(0.008890731522694678+0j) [Y5 Z6 X7 X11 Z12 Y13] +
(-1.2260484989974585e-05+0j) [Y5 Z6 Y7] +
(-1.8818501833592722e-06+0j) [Y5 Z6 Y7 Z8] +
(-1.3980449082421664e-06+0j) [Y5 Z6 Y7 Z9] +
(-0.012215040997614035+0j) [Y5 Z6 Y7 X10 Z11 X12] +
(-0.012215040997614035+0j) [Y5 Z6 Y7 Y10 Z11 Y12] +
(4.281913885118194e-06+0j) [Y5 Z6 Y7 Z10] +
(-0.0009298507967730881+0j) [Y5 Z6 Y7 X11 Z12 X13] +
(0.00796088072592159+0j) [Y5 Z6 Y7 Y11 Z12 Y13] +
(-1.6923978287233736e-06+0j) [Y5 Z6 Y7 Z11] +
(-4.5888551560321e-06+0j) [Y5 Z6 Y7 Z12] +
(1.3304731887619205e-06+0j) [Y5 Z6 Z7 X8 X9 Y10] +
(0.005923798336561343+0j) [Y5 Z6 Z7 X8 X9 Z10 Z11 Y12] +
(-1.3304731887619205e-06+0j) [Y5 Z6 Z7 Y8 X9 X10] +
(-0.005923798336561343+0j) [Y5 Z6 Z7 Y8 X9 Z10 Z11 X12] +
(-0.01602460368917943+0j) [Y5 Z6 Z7 Z8 Z9 X10 X11 Y12] +
(-5.071480736823616e-06+0j) [Y5 Z6 Z7 Z8 Z9 X10 X12 Y13] +
(0.01602460368917943+0j) [Y5 Z6 Z7 Z8 Z9 Y10 X11 X12] +
(-5.071480736823616e-06+0j) [Y5 Z6 Z7 Z8 Z9 Y10 Y12 Y13] +
(-6.631277928949807e-05+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Y11] +
(-9.806102775923066e-06+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z12] +
(-4.7346220390994505e-06+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z13] +
(-0.3693708936615614+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(-0.023145130929529037+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y13] +
(-0.025637238296026862+0j) [Y5 Z6 Z7 Z8 Z9 Z10 Z12 Y13] +
(3.3343312896348418e-06+0j) [Y5 Z6 Z7 Z8 Z9 Y11] +
(-0.009612634606847435+0j) [Y5 Z6 Z7 Z8 Z9 Z11 Z12 Y13] +
(-7.444344676466986e-06+0j) [Y5 Z6 Z7 Z8 Z10 Y11] +
(-0.04171881383982173+0j) [Y5 Z6 Z7 Z8 Z10 Z11 Z12 Y13] +
(-8.774817865228907e-06+0j) [Y5 Z6 Z7 Z9 Z10 Y11] +
(-0.047642612176383076+0j) [Y5 Z6 Z7 Z9 Z10 Z11 Z12 Y13] +
(-7.518362216252154e-06+0j) [Y5 Z6 Z8 Z9 Z10 Y11] +
(-0.039318051947197466+0j) [Y5 Z6 Z8 Z9 Z10 Z11 Z12 Y13] +
(-1.8540608581190336e-06+0j) [Y5 Y7] +
(-6.29002843369774e-06+0j) [Y5 Z7 Z8 Z9 Z10 Y11] +
(-0.039564416322893134+0j) [Y5 Z7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.010960074940542665+0j) [Z5 X6 Z7 Z8 Z9 X10] +
(-1.942946836841903e-06+0j) [Z5 X6 Z7 Z8 Z9 Z10 Z11 X12] +
(0.010960074940542665+0j) [Z5 Y6 Z7 Z8 Z9 Y10] +
(-1.942946836841903e-06+0j) [Z5 Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(0.14899430575065528+0j) [Z5 Z6] +
(0.018266834869375657+0j) [Z5 X7 Z8 Z9 Z10 X11] +
(-1.6541174772827849e-06+0j) [Z5 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.018266834869375657+0j) [Z5 Y7 Z8 Z9 Z10 Y11] +
(-1.6541174772827849e-06+0j) [Z5 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.13701191674040727+0j) [Z5 Z7] +
(-1.8163031699233784e-06+0j) [Z5 X10 Z11 X12] +
(-1.8163031699233784e-06+0j) [Z5 Y10 Z11 Y12] +
(1.8782101248552699e-06+0j) [Z5 X11 Z12 X13] +
(1.8782101248552699e-06+0j) [Z5 Y11 Z12 Y13] +
(0.12489990917237617+0j) [Z5 Z11] +
(-0.013873381748426046+0j) [X6 X7 Y8 Y9] +
(-0.01782514099578664+0j) [X6 X7 Y10 Y11] +
(-1.0358477601970897e-06+0j) [X6 X7 Y10 Z11 Z12 Y13] +
(-1.0358477601970897e-06+0j) [X6 X7 X11 X12] +
(-0.01736611899465146+0j) [X6 X7 Y12 Y13] +
(0.013873381748426046+0j) [X6 Y7 Y8 X9] +
(0.01782514099578664+0j) [X6 Y7 Y10 X11] +
(1.0358477601970897e-06+0j) [X6 Y7 Y10 Z11 Z12 X13] +
(-1.0358477601970897e-06+0j) [X6 Y7 Y11 X12] +
(0.01736611899465146+0j) [X6 Y7 Y12 X13] +
(0.0002921986261110251+0j) [X6 Z7 X8 X9 Z10 X11] +
(-3.32813935080572e-07+0j) [X6 Z7 X8 X9 Z10 Z11 Z12 X13] +
(0.0002921986261110251+0j) [X6 Z7 X8 Y9 Z10 Y11] +
(-3.32813935080572e-07+0j) [X6 Z7 X8 Y9 Z10 Z11 Z12 Y13] +
(0.2284810656491901+0j) [X6 Z7 Z8 Z9 X10] +
(3.3131455003606387e-06+0j) [X6 Z7 Z8 Z9 X10 X11 Z12 X13] +
(3.3131455003606387e-06+0j) [X6 Z7 Z8 Z9 X10 Y11 Z12 Y13] +
(0.011307274008848373+0j) [X6 Z7 Z8 Z9 X10 Z11] +
(0.02510495713884463+0j) [X6 Z7 Z8 Z9 X10 Z12] +
(0.0105404259076716+0j) [X6 Z7 Z8 Z9 X10 Z13] +
(-0.014564531231173027+0j) [X6 Z7 Z8 Z9 Z10 X11 Y12 Y13] +
(0.014564531231173027+0j) [X6 Z7 Z8 Z9 Z10 Y11 Y12 X13] +
(-2.5950860072140552e-05+0j) [X6 Z7 Z8 Z9 Z10 Z11 X12] +
(4.183932559682478e-06+0j) [X6 Z7 Z8 Z9 Z10 Z11 X12 Z13] +
(-6.524373849042973e-06+0j) [X6 Z7 Z8 Z9 Z10 X12] +
(-3.211228348682334e-06+0j) [X6 Z7 Z8 Z9 Z11 X12] +
(0.02981242451734594+0j) [X6 Z7 Z8 X10] +
(-3.2774831957999545e-06+0j) [X6 Z7 Z8 Z10 Z11 X12] +
(0.030104623143456972+0j) [X6 Z7 Z9 X10] +
(-3.6102971308805263e-06+0j) [X6 Z7 Z9 Z10 Z11 X12] +
(0.030787505389143974+0j) [X6 Z8 Z9 X10] +
(-3.7696594523070155e-06+0j) [X6 Z8 Z9 Z10 Z11 X12] +
(0.013873381748426046+0j) [Y6 X7 X8 Y9] +
(0.01782514099578664+0j) [Y6 X7 X10 Y11] +
(1.0358477601970897e-06+0j) [Y6 X7 X10 Z11 Z12 Y13] +
(-1.0358477601970897e-06+0j) [Y6 X7 X11 Y12] +
(0.01736611899465146+0j) [Y6 X7 X12 Y13] +
(-0.013873381748426046+0j) [Y6 Y7 X8 X9] +
(-0.01782514099578664+0j) [Y6 Y7 X10 X11] +
(-1.0358477601970897e-06+0j) [Y6 Y7 X10 Z11 Z12 X13] +
(-1.0358477601970897e-06+0j) [Y6 Y7 Y11 Y12] +
(-0.01736611899465146+0j) [Y6 Y7 X12 X13] +
(0.0002921986261110251+0j) [Y6 Z7 Y8 X9 Z10 X11] +
(-3.32813935080572e-07+0j) [Y6 Z7 Y8 X9 Z10 Z11 Z12 X13] +
(0.0002921986261110251+0j) [Y6 Z7 Y8 Y9 Z10 Y11] +
(-3.32813935080572e-07+0j) [Y6 Z7 Y8 Y9 Z10 Z11 Z12 Y13] +
(0.2284810656491901+0j) [Y6 Z7 Z8 Z9 Y10] +
(3.3131455003606387e-06+0j) [Y6 Z7 Z8 Z9 Y10 X11 Z12 X13] +
(3.3131455003606387e-06+0j) [Y6 Z7 Z8 Z9 Y10 Y11 Z12 Y13] +
(0.011307274008848373+0j) [Y6 Z7 Z8 Z9 Y10 Z11] +
(0.02510495713884463+0j) [Y6 Z7 Z8 Z9 Y10 Z12] +
(0.0105404259076716+0j) [Y6 Z7 Z8 Z9 Y10 Z13] +
(0.014564531231173027+0j) [Y6 Z7 Z8 Z9 Z10 X11 X12 Y13] +
(-0.014564531231173027+0j) [Y6 Z7 Z8 Z9 Z10 Y11 X12 X13] +
(-2.5950860072140552e-05+0j) [Y6 Z7 Z8 Z9 Z10 Z11 Y12] +
(4.183932559682478e-06+0j) [Y6 Z7 Z8 Z9 Z10 Z11 Y12 Z13] +
(-6.524373849042973e-06+0j) [Y6 Z7 Z8 Z9 Z10 Y12] +
(-3.211228348682334e-06+0j) [Y6 Z7 Z8 Z9 Z11 Y12] +
(0.02981242451734594+0j) [Y6 Z7 Z8 Y10] +
(-3.2774831957999545e-06+0j) [Y6 Z7 Z8 Z10 Z11 Y12] +
(0.030104623143456972+0j) [Y6 Z7 Z9 Y10] +
(-3.6102971308805263e-06+0j) [Y6 Z7 Z9 Z10 Z11 Y12] +
(0.030787505389143974+0j) [Y6 Z8 Z9 Y10] +
(-3.7696594523070155e-06+0j) [Y6 Z8 Z9 Z10 Z11 Y12] +
(1.3096862988615383+0j) [Z6] +
(0.030787505389143974+0j) [Z6 X7 Z8 Z9 Z10 X11] +
(-3.7696594523070155e-06+0j) [Z6 X7 Z8 Z9 Z10 Z11 Z12 X13] +
(0.030787505389143974+0j) [Z6 Y7 Z8 Z9 Z10 Y11] +
(-3.7696594523070155e-06+0j) [Z6 Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(0.1939253461327012+0j) [Z6 Z7] +
(0.1675665326546123+0j) [Z6 Z8] +
(0.18143991440303836+0j) [Z6 Z9] +
(-1.8551201217281695e-06+0j) [Z6 X10 Z11 X12] +
(-1.8551201217281695e-06+0j) [Z6 Y10 Z11 Y12] +
(0.11952438964682674+0j) [Z6 Z10] +
(-2.8909678819252596e-06+0j) [Z6 X11 Z12 X13] +
(-2.8909678819252596e-06+0j) [Z6 Y11 Z12 Y13] +
(0.1373495306426134+0j) [Z6 Z11] +
(0.13401715261963693+0j) [Z6 Z12] +
(0.15138327161428838+0j) [Z6 Z13] +
(-0.0002921986261110251+0j) [X7 X8 Y9 Y10] +
(3.32813935080572e-07+0j) [X7 X8 Y9 Z10 Z11 Y12] +
(0.0002921986261110251+0j) [X7 Y8 Y9 X10] +
(-3.32813935080572e-07+0j) [X7 Y8 Y9 Z10 Z11 X12] +
(-3.3131455003606395e-06+0j) [X7 Z8 Z9 X10 Y11 Y12] +
(-0.014564531231173027+0j) [X7 Z8 Z9 X10 X12 X13] +
(3.3131455003606395e-06+0j) [X7 Z8 Z9 Y10 Y11 X12] +
(-0.014564531231173027+0j) [X7 Z8 Z9 Y10 Y12 X13] +
(0.22848106564919016+0j) [X7 Z8 Z9 Z10 X11] +
(0.0105404259076716+0j) [X7 Z8 Z9 Z10 X11 Z12] +
(0.02510495713884463+0j) [X7 Z8 Z9 Z10 X11 Z13] +
(-2.5950860072140556e-05+0j) [X7 Z8 Z9 Z10 Z11 Z12 X13] +
(4.183932559682478e-06+0j) [X7 Z8 Z9 Z10 Z11 X13] +
(-3.211228348682334e-06+0j) [X7 Z8 Z9 Z10 Z12 X13] +
(0.011307274008848373+0j) [X7 Z8 Z9 X11] +
(-6.524373849042973e-06+0j) [X7 Z8 Z9 Z11 Z12 X13] +
(0.030104623143456972+0j) [X7 Z8 Z10 X11] +
(-3.6102971308805263e-06+0j) [X7 Z8 Z10 Z11 Z12 X13] +
(0.02981242451734594+0j) [X7 Z9 Z10 X11] +
(-3.2774831957999545e-06+0j) [X7 Z9 Z10 Z11 Z12 X13] +
(0.0002921986261110251+0j) [Y7 X8 X9 Y10] +
(-3.32813935080572e-07+0j) [Y7 X8 X9 Z10 Z11 Y12] +
(-0.0002921986261110251+0j) [Y7 Y8 X9 X10] +
(3.32813935080572e-07+0j) [Y7 Y8 X9 Z10 Z11 X12] +
(3.3131455003606395e-06+0j) [Y7 Z8 Z9 X10 X11 Y12] +
(-0.014564531231173027+0j) [Y7 Z8 Z9 X10 X12 Y13] +
(-3.3131455003606395e-06+0j) [Y7 Z8 Z9 Y10 X11 X12] +
(-0.014564531231173027+0j) [Y7 Z8 Z9 Y10 Y12 Y13] +
(0.22848106564919016+0j) [Y7 Z8 Z9 Z10 Y11] +
(0.0105404259076716+0j) [Y7 Z8 Z9 Z10 Y11 Z12] +
(0.02510495713884463+0j) [Y7 Z8 Z9 Z10 Y11 Z13] +
(-2.5950860072140556e-05+0j) [Y7 Z8 Z9 Z10 Z11 Z12 Y13] +
(4.183932559682478e-06+0j) [Y7 Z8 Z9 Z10 Z11 Y13] +
(-3.211228348682334e-06+0j) [Y7 Z8 Z9 Z10 Z12 Y13] +
(0.011307274008848373+0j) [Y7 Z8 Z9 Y11] +
(-6.524373849042973e-06+0j) [Y7 Z8 Z9 Z11 Z12 Y13] +
(0.030104623143456972+0j) [Y7 Z8 Z10 Y11] +
(-3.6102971308805263e-06+0j) [Y7 Z8 Z10 Z11 Z12 Y13] +
(0.02981242451734594+0j) [Y7 Z9 Z10 Y11] +
(-3.2774831957999545e-06+0j) [Y7 Z9 Z10 Z11 Z12 Y13] +
(1.3096862988615383+0j) [Z7] +
(0.18143991440303836+0j) [Z7 Z8] +
(0.1675665326546123+0j) [Z7 Z9] +
(-2.8909678819252596e-06+0j) [Z7 X10 Z11 X12] +
(-2.8909678819252596e-06+0j) [Z7 Y10 Z11 Y12] +
(0.1373495306426134+0j) [Z7 Z10] +
(-1.8551201217281695e-06+0j) [Z7 X11 Z12 X13] +
(-1.8551201217281695e-06+0j) [Z7 Y11 Z12 Y13] +
(0.11952438964682674+0j) [Z7 Z11] +
(0.15138327161428838+0j) [Z7 Z12] +
(0.13401715261963693+0j) [Z7 Z13] +
(-0.00956070572913597+0j) [X8 X9 Y10 Y11] +
(6.628614202127936e-07+0j) [X8 X9 Y10 Z11 Z12 Y13] +
(6.628614202127936e-07+0j) [X8 X9 X11 X12] +
(0.00956070572913597+0j) [X8 Y9 Y10 X11] +
(-6.628614202127936e-07+0j) [X8 Y9 Y10 Z11 Z12 X13] +
(6.628614202127936e-07+0j) [X8 Y9 Y11 X12] +
(0.00956070572913597+0j) [Y8 X9 X10 Y11] +
(-6.628614202127936e-07+0j) [Y8 X9 X10 Z11 Z12 Y13] +
(6.628614202127936e-07+0j) [Y8 X9 X11 Y12] +
(-0.00956070572913597+0j) [Y8 Y9 X10 X11] +
(6.628614202127936e-07+0j) [Y8 Y9 X10 Z11 Z12 X13] +
(6.628614202127936e-07+0j) [Y8 Y9 Y11 Y12] +
(1.3693525634718158+0j) [Z8] +
(-1.5973171979640867e-06+0j) [Z8 X10 Z11 X12] +
(-1.5973171979640867e-06+0j) [Z8 Y10 Z11 Y12] +
(0.13766872645852596+0j) [Z8 Z10] +
(-9.34455777751293e-07+0j) [Z8 X11 Z12 X13] +
(-9.34455777751293e-07+0j) [Z8 Y11 Z12 Y13] +
(0.14722943218766193+0j) [Z8 Z11] +
(0.14973486803496933+0j) [Z8 Z12] +
(0.15582269051553116+0j) [Z8 Z13] +
(1.3693525634718158+0j) [Z9] +
(-9.34455777751293e-07+0j) [Z9 X10 Z11 X12] +
(-9.34455777751293e-07+0j) [Z9 Y10 Z11 Y12] +
(0.14722943218766193+0j) [Z9 Z10] +
(-1.5973171979640867e-06+0j) [Z9 X11 Z12 X13] +
(-1.5973171979640867e-06+0j) [Z9 Y11 Z12 Y13] +
(0.13766872645852596+0j) [Z9 Z11] +
(0.15582269051553116+0j) [Z9 Z12] +
(0.14973486803496933+0j) [Z9 Z13] +
(-0.028685183716105813+0j) [X10 X11 Y12 Y13] +
(0.028685183716105813+0j) [X10 Y11 Y12 X13] +
(-1.0722312158186212e-05+0j) [X10 Z11 X12] +
(7.954413176843053e-06+0j) [X10 Z11 X12 Z13] +
(-8.194261372780246e-06+0j) [X10 X12] +
(0.028685183716105813+0j) [Y10 X11 X12 Y13] +
(-0.028685183716105813+0j) [Y10 Y11 X12 X13] +
(-1.0722312158186212e-05+0j) [Y10 Z11 Y12] +
(7.954413176843053e-06+0j) [Y10 Z11 Y12 Z13] +
(-8.194261372780246e-06+0j) [Y10 Y12] +
(0.7829661725950199+0j) [Z10] +
(-8.194261372780246e-06+0j) [Z10 X11 Z12 X13] +
(-8.194261372780246e-06+0j) [Z10 Y11 Z12 Y13] +
(0.14926355147388926+0j) [Z10 Z11] +
(0.1127038692033225+0j) [Z10 Z12] +
(0.14138905291942833+0j) [Z10 Z13] +
(-1.0722312158186208e-05+0j) [X11 Z12 X13] +
(7.954413176843053e-06+0j) [X11 X13] +
(-1.0722312158186208e-05+0j) [Y11 Z12 Y13] +
(7.954413176843053e-06+0j) [Y11 Y13] +
(0.7829661725950201+0j) [Z11] +
(0.14138905291942833+0j) [Z11 Z12] +
(0.1127038692033225+0j) [Z11 Z13] +
(0.8084581961720485+0j) [Z12] +
(0.15435748657223652+0j) [Z12 Z13] +
(0.8084581961720486+0j) [Z13]
  (-46.463906788688966) [I0]
+ (0.7829661725950183) [Z10]
+ (0.7829661725950187) [Z11]
+ (0.8084581961720492) [Z12]
+ (0.8084581961720493) [Z13]
+ (1.2034402289145625) [Z5]
+ (1.2034402289145627) [Z4]
+ (1.3096862988615439) [Z6]
+ (1.3693525634718184) [Z8]
+ (1.3693525634718189) [Z9]
+ (1.6538942226831708) [Z2]
+ (1.653894222683171) [Z3]
+ (12.412630742111762) [Z0]
+ (12.412630742111762) [Z1]
+ (-8.19426137219499e-06) [Y10 Y12]
+ (-8.19426137219499e-06) [X10 X12]
+ (-1.8540608579308985e-06) [Y5 Y7]
+ (-1.8540608579308985e-06) [X5 X7]
+ (-7.764994119521683e-07) [Y3 Y5]
+ (-7.764994119521683e-07) [X3 X5]
+ (-5.929765815671338e-07) [Y4 Y6]
+ (-5.929765815671338e-07) [X4 X6]
+ (1.6021167404240067e-06) [Y2 Y4]
+ (1.6021167404240067e-06) [X2 X4]
+ (7.954413176119456e-06) [Y11 Y13]
+ (7.954413176119456e-06) [X11 X13]
+ (0.0032769719312316166) [Y1 Y3]
+ (0.0032769719312316166) [X1 X3]
+ (0.10433064780651385) [Y0 Y2]
+ (0.10433064780651385) [X0 X2]
+ (0.11270386920332229) [Z10 Z12]
+ (0.11270386920332229) [Z11 Z13]
+ (0.11383573679388657) [Z4 Z12]
+ (0.11383573679388657) [Z5 Z13]
+ (0.11952438964682688) [Z6 Z10]
+ (0.11952438964682688) [Z7 Z11]
+ (0.12489990917237609) [Z4 Z10]
+ (0.12489990917237609) [Z5 Z11]
+ (0.1249580773950321) [Z2 Z4]
+ (0.1249580773950321) [Z3 Z5]
+ (0.12799502492468415) [Z2 Z10]
+ (0.12799502492468415) [Z3 Z11]
+ (0.13401715261963718) [Z6 Z12]
+ (0.13401715261963718) [Z7 Z13]
+ (0.1370119167404076) [Z4 Z6]
+ (0.1370119167404076) [Z5 Z7]
+ (0.13734953064261335) [Z6 Z11]
+ (0.13734953064261335) [Z7 Z10]
+ (0.13739104762683232) [Z2 Z6]
+ (0.13739104762683232) [Z3 Z7]
+ (0.13766872645852582) [Z8 Z10]
+ (0.13766872645852582) [Z9 Z11]
+ (0.14011289865354803) [Z2 Z12]
+ (0.14011289865354803) [Z3 Z13]
+ (0.14138905291942813) [Z10 Z13]
+ (0.14138905291942813) [Z11 Z12]
+ (0.14257997712485765) [Z4 Z11]
+ (0.14257997712485765) [Z5 Z10]
+ (0.14722943218766177) [Z8 Z11]
+ (0.14722943218766177) [Z9 Z10]
+ (0.14899430575065556) [Z4 Z7]
+ (0.14899430575065556) [Z5 Z6]
+ (0.14926355147388914) [Z10 Z11]
+ (0.14960702684445293) [Z4 Z8]
+ (0.14960702684445293) [Z5 Z9]
+ (0.1497348680349693) [Z8 Z12]
+ (0.1497348680349693) [Z9 Z13]
+ (0.1507140812100828) [Z2 Z8]
+ (0.1507140812100828) [Z3 Z9]
+ (0.15138327161428858) [Z6 Z13]
+ (0.15138327161428858) [Z7 Z12]
+ (0.15215040708869043) [Z4 Z13]
+ (0.15215040708869043) [Z5 Z12]
+ (0.15337968243314157) [Z2 Z11]
+ (0.15337968243314157) [Z3 Z10]
+ (0.15435748657223636) [Z12 Z13]
+ (0.15569010671752448) [Z2 Z13]
+ (0.15569010671752448) [Z3 Z12]
+ (0.1558226905155312) [Z8 Z13]
+ (0.1558226905155312) [Z9 Z12]
+ (0.15676396176430984) [Z4 Z9]
+ (0.15676396176430984) [Z5 Z8]
+ (0.15755314797985664) [Z4 Z5]
+ (0.16079764534838553) [Z2 Z5]
+ (0.16079764534838553) [Z3 Z4]
+ (0.16756653265461283) [Z6 Z8]
+ (0.16756653265461283) [Z7 Z9]
+ (0.16853486561579945) [Z2 Z7]
+ (0.16853486561579945) [Z3 Z6]
+ (0.18143991440303897) [Z6 Z9]
+ (0.18143991440303897) [Z7 Z8]
+ (0.18189085790751353) [Z2 Z3]
+ (0.1869082047691254) [Z2 Z9]
+ (0.1869082047691254) [Z3 Z8]
+ (0.19299723935364238) [Z0 Z10]
+ (0.19299723935364238) [Z1 Z11]
+ (0.1939253461327024) [Z6 Z7]
+ (0.19661770890342117) [Z0 Z4]
+ (0.19661770890342117) [Z1 Z5]
+ (0.19936354537360798) [Z0 Z5]
+ (0.19936354537360798) [Z1 Z4]
+ (0.20072866460441766) [Z0 Z11]
+ (0.20072866460441766) [Z1 Z10]
+ (0.2110265984979151) [Z0 Z12]
+ (0.2110265984979151) [Z1 Z13]
+ (0.21631037498631805) [Z0 Z13]
+ (0.21631037498631805) [Z1 Z12]
+ (0.23671080783830395) [Z0 Z2]
+ (0.23671080783830395) [Z1 Z3]
+ (0.24164663936017214) [Z0 Z6]
+ (0.24164663936017214) [Z1 Z7]
+ (0.2485348337131427) [Z0 Z7]
+ (0.2485348337131427) [Z1 Z6]
+ (0.25129445674591655) [Z0 Z3]
+ (0.25129445674591655) [Z1 Z2]
+ (0.2723251830660567) [Z0 Z8]
+ (0.2723251830660567) [Z1 Z9]
+ (1.1861763734860487) [Z0 Z1]
+ (-1.2260484988858313e-05) [Y4 Z5 Y6]
+ (-1.2260484988858313e-05) [X4 Z5 X6]
+ (-1.2260484988858311e-05) [Y5 Z6 Y7]
+ (-1.2260484988858311e-05) [X5 Z6 X7]
+ (-1.0722312157697418e-05) [Y11 Z12 Y13]
+ (-1.0722312157697418e-05) [X11 Z12 X13]
+ (-1.0722312157697416e-05) [Y10 Z11 Y12]
+ (-1.0722312157697416e-05) [X10 Z11 X12]
+ (-3.887051673762513e-06) [Y2 Z3 Y4]
+ (-3.887051673762513e-06) [X2 Z3 X4]
+ (-3.887051673762512e-06) [Y3 Z4 Y5]
+ (-3.887051673762512e-06) [X3 Z4 X5]
+ (0.1250703257977191) [Y1 Z2 Y3]
+ (0.1250703257977191) [X1 Z2 X3]
+ (0.12507032579771915) [Y0 Z1 Y2]
+ (0.12507032579771915) [X0 Z1 X2]
+ (-0.03831467029480388) [Y4 Y5 X12 X13]
+ (-0.03831467029480388) [X4 X5 Y12 Y13]
+ (-0.03619412355904259) [Y2 Y3 X8 X9]
+ (-0.03619412355904259) [X2 X3 Y8 Y9]
+ (-0.03583956795335345) [Y2 Y3 X4 X5]
+ (-0.03583956795335345) [X2 X3 Y4 Y5]
+ (-0.0311438179889671) [Y2 Y3 X6 X7]
+ (-0.0311438179889671) [X2 X3 Y6 Y7]
+ (-0.02868518371610585) [Y10 Y11 X12 X13]
+ (-0.02868518371610585) [X10 X11 Y12 Y13]
+ (-0.025996177598021288) [Y3 Z4 Z5 Y7]
+ (-0.025996177598021288) [X3 Z4 Z5 X7]
+ (-0.025384657508457427) [Y2 Y3 X10 X11]
+ (-0.025384657508457427) [X2 X3 Y10 Y11]
+ (-0.019028242443847296) [Y3 Y4 X11 X12]
+ (-0.019028242443847296) [X3 X4 Y11 Y12]
+ (-0.017825140995786474) [Y6 Y7 X10 X11]
+ (-0.017825140995786474) [X6 X7 Y10 Y11]
+ (-0.017680067952481556) [Y4 Y5 X10 X11]
+ (-0.017680067952481556) [X4 X5 Y10 Y11]
+ (-0.017366118994651403) [Y6 Y7 X12 X13]
+ (-0.017366118994651403) [X6 X7 Y12 Y13]
+ (-0.01557720806397647) [Y2 Y3 X12 X13]
+ (-0.01557720806397647) [X2 X3 Y12 Y13]
+ (-0.014583648907612632) [Y0 Y1 X2 X3]
+ (-0.014583648907612632) [X0 X1 Y2 Y3]
+ (-0.013873381748426141) [Y6 Y7 X8 X9]
+ (-0.013873381748426141) [X6 X7 Y8 Y9]
+ (-0.011982389010247962) [Y4 Y5 X6 X7]
+ (-0.011982389010247962) [X4 X5 Y6 Y7]
+ (-0.01128519020084091) [Y5 X6 X11 Y12]
+ (-0.01128519020084091) [X5 Y6 Y11 X12]
+ (-0.00956070572913595) [Y8 Y9 X10 X11]
+ (-0.00956070572913595) [X8 X9 Y10 Y11]
+ (-0.008125251921381025) [Y1 X2 X8 Y9]
+ (-0.008125251921381025) [Y1 Y2 Y8 Y9]
+ (-0.008125251921381025) [X1 X2 X8 X9]
+ (-0.008125251921381025) [X1 Y2 Y8 X9]
+ (-0.007731425250775277) [Y0 Y1 X10 X11]
+ (-0.007731425250775277) [X0 X1 Y10 Y11]
+ (-0.007156934919856931) [Y4 Y5 X8 X9]
+ (-0.007156934919856931) [X4 X5 Y8 Y9]
+ (-0.006888194352970577) [Y0 Y1 X6 X7]
+ (-0.006888194352970577) [X0 X1 Y6 Y7]
+ (-0.006509361201177234) [Y0 Y1 X8 X9]
+ (-0.006509361201177234) [X0 X1 Y8 Y9]
+ (-0.006087822480561869) [Y8 Y9 X12 X13]
+ (-0.006087822480561869) [X8 X9 Y12 Y13]
+ (-0.005283776488402963) [Y0 Y1 X12 X13]
+ (-0.005283776488402963) [X0 X1 Y12 Y13]
+ (-0.005143391768825133) [Y3 X4 X5 Y6]
+ (-0.005143391768825133) [X3 Y4 Y5 X6]
+ (-0.00457500762663921) [Y1 X2 X12 Y13]
+ (-0.00457500762663921) [Y1 Y2 Y12 Y13]
+ (-0.00457500762663921) [X1 X2 X12 X13]
+ (-0.00457500762663921) [X1 Y2 Y12 X13]
+ (-0.004424855449441842) [Y1 X2 X4 Y5]
+ (-0.004424855449441842) [Y1 Y2 Y4 Y5]
+ (-0.004424855449441842) [X1 X2 X4 X5]
+ (-0.004424855449441842) [X1 Y2 Y4 X5]
+ (-0.0034795118903343586) [Y2 Z3 Z5 Y6]
+ (-0.0034795118903343586) [X2 Z3 Z5 X6]
+ (-0.0034795118903343586) [Y3 Z4 Z6 Y7]
+ (-0.0034795118903343586) [X3 Z4 Z6 X7]
+ (-0.002745836470186801) [Y0 Y1 X4 X5]
+ (-0.002745836470186801) [X0 X1 Y4 Y5]
+ (-0.00179921949366303) [Y1 X2 X10 Y11]
+ (-0.00179921949366303) [Y1 Y2 Y10 Y11]
+ (-0.00179921949366303) [X1 X2 X10 X11]
+ (-0.00179921949366303) [X1 Y2 Y10 X11]
+ (-0.0002921986261110728) [Y7 Y8 X9 X10]
+ (-0.0002921986261110728) [X7 X8 Y9 Y10]
+ (-8.19426137219499e-06) [Z10 Y11 Z12 Y13]
+ (-8.19426137219499e-06) [Z10 X11 Z12 X13]
+ (-7.801707500498473e-06) [Y2 Z3 Y4 Z11]
+ (-7.801707500498473e-06) [X2 Z3 X4 Z11]
+ (-7.801707500498473e-06) [Y3 Z4 Y5 Z10]
+ (-7.801707500498473e-06) [X3 Z4 X5 Z10]
+ (-4.643051068420231e-06) [Y3 X4 X10 Y11]
+ (-4.643051068420231e-06) [Y3 Y4 Y10 Y11]
+ (-4.643051068420231e-06) [X3 X4 X10 X11]
+ (-4.643051068420231e-06) [X3 Y4 Y10 X11]
+ (-4.588855155585933e-06) [Y4 Z5 Y6 Z13]
+ (-4.588855155585933e-06) [X4 Z5 X6 Z13]
+ (-4.588855155585933e-06) [Y5 Z6 Y7 Z12]
+ (-4.588855155585933e-06) [X5 Z6 X7 Z12]
+ (-4.556569218049105e-06) [Y5 X6 X12 Y13]
+ (-4.556569218049105e-06) [Y5 Y6 Y12 Y13]
+ (-4.556569218049105e-06) [X5 X6 X12 X13]
+ (-4.556569218049105e-06) [X5 Y6 Y12 X13]
+ (-3.694513294434133e-06) [Y4 X5 X11 Y12]
+ (-3.694513294434133e-06) [Y4 Y5 Y11 Y12]
+ (-3.694513294434133e-06) [X4 X5 X11 X12]
+ (-3.694513294434133e-06) [X4 Y5 Y11 X12]
+ (-3.3440815564468682e-06) [Z0 Y5 Z6 Y7]
+ (-3.3440815564468682e-06) [Z0 X5 Z6 X7]
+ (-3.3440815564468682e-06) [Z1 Y4 Z5 Y6]
+ (-3.3440815564468682e-06) [Z1 X4 Z5 X6]
+ (-3.15865643207824e-06) [Y2 Z3 Y4 Z10]
+ (-3.15865643207824e-06) [X2 Z3 X4 Z10]
+ (-3.15865643207824e-06) [Y3 Z4 Y5 Z11]
+ (-3.15865643207824e-06) [X3 Z4 X5 Z11]
+ (-3.0993492435670654e-06) [Z0 Y4 Z5 Y6]
+ (-3.0993492435670654e-06) [Z0 X4 Z5 X6]
+ (-3.0993492435670654e-06) [Z1 Y5 Z6 Y7]
+ (-3.0993492435670654e-06) [Z1 X5 Z6 X7]
+ (-2.890967881702135e-06) [Z6 Y11 Z12 Y13]
+ (-2.890967881702135e-06) [Z6 X11 Z12 X13]
+ (-2.890967881702135e-06) [Z7 Y10 Z11 Y12]
+ (-2.890967881702135e-06) [Z7 X10 Z11 X12]
+ (-2.177664604980604e-06) [Z0 Y10 Z11 Y12]
+ (-2.177664604980604e-06) [Z0 X10 Z11 X12]
+ (-2.177664604980604e-06) [Z1 Y11 Z12 Y13]
+ (-2.177664604980604e-06) [Z1 X11 Z12 X13]
+ (-1.8818501831851722e-06) [Y4 Z5 Y6 Z9]
+ (-1.8818501831851722e-06) [X4 Z5 X6 Z9]
+ (-1.8818501831851722e-06) [Y5 Z6 Y7 Z8]
+ (-1.8818501831851722e-06) [X5 Z6 X7 Z8]
+ (-1.8551201215389877e-06) [Z6 Y10 Z11 Y12]
+ (-1.8551201215389877e-06) [Z6 X10 Z11 X12]
+ (-1.8551201215389877e-06) [Z7 Y11 Z12 Y13]
+ (-1.8551201215389877e-06) [Z7 X11 Z12 X13]
+ (-1.8540608579308985e-06) [Y4 Z5 Y6 Z7]
+ (-1.8540608579308985e-06) [X4 Z5 X6 Z7]
+ (-1.8163031697162827e-06) [Z4 Y11 Z12 Y13]
+ (-1.8163031697162827e-06) [Z4 X11 Z12 X13]
+ (-1.8163031697162827e-06) [Z5 Y10 Z11 Y12]
+ (-1.8163031697162827e-06) [Z5 X10 Z11 X12]
+ (-1.6923978285366039e-06) [Y4 Z5 Y6 Z10]
+ (-1.6923978285366039e-06) [X4 Z5 X6 Z10]
+ (-1.6923978285366039e-06) [Y5 Z6 Y7 Z11]
+ (-1.6923978285366039e-06) [X5 Z6 X7 Z11]
+ (-1.6148794138390522e-06) [Z0 Y11 Z12 Y13]
+ (-1.6148794138390522e-06) [Z0 X11 Z12 X13]
+ (-1.6148794138390522e-06) [Z1 Y10 Z11 Y12]
+ (-1.6148794138390522e-06) [Z1 X10 Z11 X12]
+ (-1.597317197780584e-06) [Z8 Y10 Z11 Y12]
+ (-1.597317197780584e-06) [Z8 X10 Z11 X12]
+ (-1.597317197780584e-06) [Z9 Y11 Z12 Y13]
+ (-1.597317197780584e-06) [Z9 X11 Z12 X13]
+ (-1.4548424490644835e-06) [Y3 X4 X6 Y7]
+ (-1.4548424490644835e-06) [Y3 Y4 Y6 Y7]
+ (-1.4548424490644835e-06) [X3 X4 X6 X7]
+ (-1.4548424490644835e-06) [X3 Y4 Y6 X7]
+ (-1.3980449081001558e-06) [Y4 Z5 Y6 Z8]
+ (-1.3980449081001558e-06) [X4 Z5 X6 Z8]
+ (-1.3980449081001558e-06) [Y5 Z6 Y7 Z9]
+ (-1.3980449081001558e-06) [X5 Z6 X7 Z9]
+ (-1.1954890100677503e-06) [Y2 Z3 Y4 Z7]
+ (-1.1954890100677503e-06) [X2 Z3 X4 Z7]
+ (-1.1954890100677503e-06) [Y3 Z4 Y5 Z6]
+ (-1.1954890100677503e-06) [X3 Z4 X5 Z6]
+ (-1.1908508085187172e-06) [Z0 Y3 Z4 Y5]
+ (-1.1908508085187172e-06) [Z0 X3 Z4 X5]
+ (-1.1908508085187172e-06) [Z1 Y2 Z3 Y4]
+ (-1.1908508085187172e-06) [Z1 X2 Z3 X4]
+ (-1.1708301369915206e-06) [Z2 Y5 Z6 Y7]
+ (-1.1708301369915206e-06) [Z2 X5 Z6 X7]
+ (-1.1708301369915206e-06) [Z3 Y4 Z5 Y6]
+ (-1.1708301369915206e-06) [Z3 X4 Z5 X6]
+ (-1.0632283423774209e-06) [Z2 Y10 Z11 Y12]
+ (-1.0632283423774209e-06) [Z2 X10 Z11 X12]
+ (-1.0632283423774209e-06) [Z3 Y11 Z12 Y13]
+ (-1.0632283423774209e-06) [Z3 X11 Z12 X13]
+ (-1.0358477601631472e-06) [Y6 X7 X11 Y12]
+ (-1.0358477601631472e-06) [Y6 Y7 Y11 Y12]
+ (-1.0358477601631472e-06) [X6 X7 X11 X12]
+ (-1.0358477601631472e-06) [X6 Y7 Y11 X12]
+ (-9.50924975145427e-07) [Z2 Y4 Z5 Y6]
+ (-9.50924975145427e-07) [Z2 X4 Z5 X6]
+ (-9.50924975145427e-07) [Z3 Y5 Z6 Y7]
+ (-9.50924975145427e-07) [Z3 X5 Z6 X7]
+ (-9.344557776168779e-07) [Z8 Y11 Z12 Y13]
+ (-9.344557776168779e-07) [Z8 X11 Z12 X13]
+ (-9.344557776168779e-07) [Z9 Y10 Z11 Y12]
+ (-9.344557776168779e-07) [Z9 X10 Z11 X12]
+ (-8.337746756042582e-07) [Z0 Y2 Z3 Y4]
+ (-8.337746756042582e-07) [Z0 X2 Z3 X4]
+ (-8.337746756042582e-07) [Z1 Y3 Z4 Y5]
+ (-8.337746756042582e-07) [Z1 X3 Z4 X5]
+ (-7.956895372534156e-07) [Y3 X4 X8 Y9]
+ (-7.956895372534156e-07) [Y3 Y4 Y8 Y9]
+ (-7.956895372534156e-07) [X3 X4 X8 X9]
+ (-7.956895372534156e-07) [X3 Y4 Y8 X9]
+ (-7.764994119521683e-07) [Y2 Z3 Y4 Z5]
+ (-7.764994119521683e-07) [X2 Z3 X4 Z5]
+ (-5.929765815671338e-07) [Z4 Y5 Z6 Y7]
+ (-5.929765815671338e-07) [Z4 X5 Z6 X7]
+ (-5.770052996282556e-07) [Y2 Z3 Y4 Z9]
+ (-5.770052996282556e-07) [X2 Z3 X4 Z9]
+ (-5.770052996282556e-07) [Y3 Z4 Y5 Z8]
+ (-5.770052996282556e-07) [X3 Z4 X5 Z8]
+ (-5.471647744574968e-07) [Y1 Y2 X11 X12]
+ (-5.471647744574968e-07) [X1 X2 Y11 Y12]
+ (-4.838052750850165e-07) [Y5 X6 X8 Y9]
+ (-4.838052750850165e-07) [Y5 Y6 Y8 Y9]
+ (-4.838052750850165e-07) [X5 X6 X8 X9]
+ (-4.838052750850165e-07) [X5 Y6 Y8 X9]
+ (-3.5707613291445906e-07) [Y0 X1 X3 Y4]
+ (-3.5707613291445906e-07) [Y0 Y1 Y3 Y4]
+ (-3.5707613291445906e-07) [X0 X1 X3 X4]
+ (-3.5707613291445906e-07) [X0 Y1 Y3 X4]
+ (-2.44732312879803e-07) [Y0 X1 X5 Y6]
+ (-2.44732312879803e-07) [Y0 Y1 Y5 Y6]
+ (-2.44732312879803e-07) [X0 X1 X5 X6]
+ (-2.44732312879803e-07) [X0 Y1 Y5 X6]
+ (-2.1990516184609328e-07) [Y2 X3 X5 Y6]
+ (-2.1990516184609328e-07) [Y2 Y3 Y5 Y6]
+ (-2.1990516184609328e-07) [X2 X3 X5 X6]
+ (-2.1990516184609328e-07) [X2 Y3 Y5 X6]
+ (-1.9332412770552596e-07) [Y1 X2 X3 Y4]
+ (-1.9332412770552596e-07) [X1 Y2 Y3 X4]
+ (-1.2919694861266598e-07) [Y1 Z2 Z3 Y5]
+ (-1.2919694861266598e-07) [X1 Z2 Z3 X5]
+ (1.7379332624229607e-07) [Y0 Z1 Z3 Y4]
+ (1.7379332624229607e-07) [X0 Z1 Z3 X4]
+ (1.7379332624229607e-07) [Y1 Z2 Z4 Y5]
+ (1.7379332624229607e-07) [X1 Z2 Z4 X5]
+ (1.9332412770552596e-07) [Y1 Y2 X3 X4]
+ (1.9332412770552596e-07) [X1 X2 Y3 Y4]
+ (2.1868423762516004e-07) [Y2 Z3 Y4 Z8]
+ (2.1868423762516004e-07) [X2 Z3 X4 Z8]
+ (2.1868423762516004e-07) [Y3 Z4 Y5 Z9]
+ (2.1868423762516004e-07) [X3 Z4 X5 Z9]
+ (2.593534389967332e-07) [Y2 Z3 Y4 Z6]
+ (2.593534389967332e-07) [X2 Z3 X4 Z6]
+ (2.593534389967332e-07) [Y3 Z4 Y5 Z7]
+ (2.593534389967332e-07) [X3 Z4 X5 Z7]
+ (3.606071867928252e-07) [Y0 Z1 Z2 Y4]
+ (3.606071867928252e-07) [X0 Z1 Z2 X4]
+ (3.606071867928252e-07) [Y1 Z3 Z4 Y5]
+ (3.606071867928252e-07) [X1 Z3 Z4 X5]
+ (5.471647744574968e-07) [Y1 X2 X11 Y12]
+ (5.471647744574968e-07) [X1 Y2 Y11 X12]
+ (5.627851911415513e-07) [Y0 X1 X11 Y12]
+ (5.627851911415513e-07) [Y0 Y1 Y11 Y12]
+ (5.627851911415513e-07) [X0 X1 X11 X12]
+ (5.627851911415513e-07) [X0 Y1 Y11 X12]
+ (6.628614201637059e-07) [Y8 X9 X11 Y12]
+ (6.628614201637059e-07) [Y8 Y9 Y11 Y12]
+ (6.628614201637059e-07) [X8 X9 X11 X12]
+ (6.628614201637059e-07) [X8 Y9 Y11 X12]
+ (1.1094407590777048e-06) [Z2 Y11 Z12 Y13]
+ (1.1094407590777048e-06) [Z2 X11 Z12 X13]
+ (1.1094407590777048e-06) [Z3 Y10 Z11 Y12]
+ (1.1094407590777048e-06) [Z3 X10 Z11 X12]
+ (1.6021167404240067e-06) [Z2 Y3 Z4 Y5]
+ (1.6021167404240067e-06) [Z2 X3 Z4 X5]
+ (1.8782101247178498e-06) [Z4 Y10 Z11 Y12]
+ (1.8782101247178498e-06) [Z4 X10 Z11 X12]
+ (1.8782101247178498e-06) [Z5 Y11 Z12 Y13]
+ (1.8782101247178498e-06) [Z5 X11 Z12 X13]
+ (2.1726691014551256e-06) [Y2 X3 X11 Y12]
+ (2.1726691014551256e-06) [Y2 Y3 Y11 Y12]
+ (2.1726691014551256e-06) [X2 X3 X11 X12]
+ (2.1726691014551256e-06) [X2 Y3 Y11 X12]
+ (3.1174479460915516e-06) [Y0 Z2 Z3 Y4]
+ (3.1174479460915516e-06) [X0 Z2 Z3 X4]
+ (3.539054184356327e-06) [Y2 Z3 Y4 Z12]
+ (3.539054184356327e-06) [X2 Z3 X4 Z12]
+ (3.539054184356327e-06) [Y3 Z4 Y5 Z13]
+ (3.539054184356327e-06) [X3 Z4 X5 Z13]
+ (4.28191388481797e-06) [Y4 Z5 Y6 Z11]
+ (4.28191388481797e-06) [X4 Z5 X6 Z11]
+ (4.28191388481797e-06) [Y5 Z6 Y7 Z10]
+ (4.28191388481797e-06) [X5 Z6 X7 Z10]
+ (5.275883122040939e-06) [Y3 X4 X12 Y13]
+ (5.275883122040939e-06) [Y3 Y4 Y12 Y13]
+ (5.275883122040939e-06) [X3 X4 X12 X13]
+ (5.275883122040939e-06) [X3 Y4 Y12 X13]
+ (5.974311713354573e-06) [Y5 X6 X10 Y11]
+ (5.974311713354573e-06) [Y5 Y6 Y10 Y11]
+ (5.974311713354573e-06) [X5 X6 X10 X11]
+ (5.974311713354573e-06) [X5 Y6 Y10 X11]
+ (7.954413176119456e-06) [Y10 Z11 Y12 Z13]
+ (7.954413176119456e-06) [X10 Z11 X12 Z13]
+ (8.814937306397266e-06) [Y2 Z3 Y4 Z13]
+ (8.814937306397266e-06) [X2 Z3 X4 Z13]
+ (8.814937306397266e-06) [Y3 Z4 Y5 Z12]
+ (8.814937306397266e-06) [X3 Z4 X5 Z12]
+ (0.0002921986261110728) [Y7 X8 X9 Y10]
+ (0.0002921986261110728) [X7 Y8 Y9 X10]
+ (0.0004956762314916399) [Y2 Z4 Z5 Y6]
+ (0.0004956762314916399) [X2 Z4 Z5 X6]
+ (0.0011059037691896632) [Y0 Z1 Y2 Z5]
+ (0.0011059037691896632) [X0 Z1 X2 Z5]
+ (0.0011059037691896632) [Y1 Z2 Y3 Z4]
+ (0.0011059037691896632) [X1 Z2 X3 Z4]
+ (0.0016638798784907745) [Y2 Z3 Z4 Y6]
+ (0.0016638798784907745) [X2 Z3 Z4 X6]
+ (0.0016638798784907745) [Y3 Z5 Z6 Y7]
+ (0.0016638798784907745) [X3 Z5 Z6 X7]
+ (0.0017560707018412214) [Y0 Z1 Y2 Z11]
+ (0.0017560707018412214) [X0 Z1 X2 Z11]
+ (0.0017560707018412214) [Y1 Z2 Y3 Z10]
+ (0.0017560707018412214) [X1 Z2 X3 Z10]
+ (0.0023262306231580524) [Y0 Z1 Y2 Z13]
+ (0.0023262306231580524) [X0 Z1 X2 Z13]
+ (0.0023262306231580524) [Y1 Z2 Y3 Z12]
+ (0.0023262306231580524) [X1 Z2 X3 Z12]
+ (0.002745836470186801) [Y0 X1 X4 Y5]
+ (0.002745836470186801) [X0 Y1 Y4 X5]
+ (0.0029297686747510204) [Y0 Z1 Y2 Z9]
+ (0.0029297686747510204) [X0 Z1 X2 Z9]
+ (0.0029297686747510204) [Y1 Z2 Y3 Z8]
+ (0.0029297686747510204) [X1 Z2 X3 Z8]
+ (0.003276971931231616) [Y0 Z1 Y2 Z3]
+ (0.003276971931231616) [X0 Z1 X2 Z3]
+ (0.003347617530666164) [Y0 Z1 Y2 Z7]
+ (0.003347617530666164) [X0 Z1 X2 Z7]
+ (0.003347617530666164) [Y1 Z2 Y3 Z6]
+ (0.003347617530666164) [X1 Z2 X3 Z6]
+ (0.0035552901955042517) [Y0 Z1 Y2 Z10]
+ (0.0035552901955042517) [X0 Z1 X2 Z10]
+ (0.0035552901955042517) [Y1 Z2 Y3 Z11]
+ (0.0035552901955042517) [X1 Z2 X3 Z11]
+ (0.005143391768825133) [Y3 Y4 X5 X6]
+ (0.005143391768825133) [X3 X4 Y5 Y6]
+ (0.005283776488402963) [Y0 X1 X12 Y13]
+ (0.005283776488402963) [X0 Y1 Y12 X13]
+ (0.005530759218631506) [Y0 Z1 Y2 Z4]
+ (0.005530759218631506) [X0 Z1 X2 Z4]
+ (0.005530759218631506) [Y1 Z2 Y3 Z5]
+ (0.005530759218631506) [X1 Z2 X3 Z5]
+ (0.006087822480561869) [Y8 X9 X12 Y13]
+ (0.006087822480561869) [X8 Y9 Y12 X13]
+ (0.006509361201177234) [Y0 X1 X8 Y9]
+ (0.006509361201177234) [X0 Y1 Y8 X9]
+ (0.006888194352970577) [Y0 X1 X6 Y7]
+ (0.006888194352970577) [X0 Y1 Y6 X7]
+ (0.0069012382497972615) [Y0 Z1 Y2 Z12]
+ (0.0069012382497972615) [X0 Z1 X2 Z12]
+ (0.0069012382497972615) [Y1 Z2 Y3 Z13]
+ (0.0069012382497972615) [X1 Z2 X3 Z13]
+ (0.007156934919856931) [Y4 X5 X8 Y9]
+ (0.007156934919856931) [X4 Y5 Y8 X9]
+ (0.007731425250775277) [Y0 X1 X10 Y11]
+ (0.007731425250775277) [X0 Y1 Y10 X11]
+ (0.008032520918821364) [Y0 Z1 Y2 Z6]
+ (0.008032520918821364) [X0 Z1 X2 Z6]
+ (0.008032520918821364) [Y1 Z2 Y3 Z7]
+ (0.008032520918821364) [X1 Z2 X3 Z7]
+ (0.00956070572913595) [Y8 X9 X10 Y11]
+ (0.00956070572913595) [X8 Y9 Y10 X11]
+ (0.011055020596132047) [Y0 Z1 Y2 Z8]
+ (0.011055020596132047) [X0 Z1 X2 Z8]
+ (0.011055020596132047) [Y1 Z2 Y3 Z9]
+ (0.011055020596132047) [X1 Z2 X3 Z9]
+ (0.01128519020084091) [Y5 Y6 X11 X12]
+ (0.01128519020084091) [X5 X6 Y11 Y12]
+ (0.011307274008848164) [Y7 Z8 Z9 Y11]
+ (0.011307274008848164) [X7 Z8 Z9 X11]
+ (0.011982389010247962) [Y4 X5 X6 Y7]
+ (0.011982389010247962) [X4 Y5 Y6 X7]
+ (0.013873381748426141) [Y6 X7 X8 Y9]
+ (0.013873381748426141) [X6 Y7 Y8 X9]
+ (0.014583648907612632) [Y0 X1 X2 Y3]
+ (0.014583648907612632) [X0 Y1 Y2 X3]
+ (0.01557720806397647) [Y2 X3 X12 Y13]
+ (0.01557720806397647) [X2 Y3 Y12 X13]
+ (0.017366118994651403) [Y6 X7 X12 Y13]
+ (0.017366118994651403) [X6 Y7 Y12 X13]
+ (0.017680067952481556) [Y4 X5 X10 Y11]
+ (0.017680067952481556) [X4 Y5 Y10 X11]
+ (0.017825140995786474) [Y6 X7 X10 Y11]
+ (0.017825140995786474) [X6 Y7 Y10 X11]
+ (0.019028242443847296) [Y3 X4 X11 Y12]
+ (0.019028242443847296) [X3 Y4 Y11 X12]
+ (0.025384657508457427) [Y2 X3 X10 Y11]
+ (0.025384657508457427) [X2 Y3 Y10 X11]
+ (0.02868518371610585) [Y10 X11 X12 Y13]
+ (0.02868518371610585) [X10 Y11 Y12 X13]
+ (0.029812424517345774) [Y6 Z7 Z8 Y10]
+ (0.029812424517345774) [X6 Z7 Z8 X10]
+ (0.029812424517345774) [Y7 Z9 Z10 Y11]
+ (0.029812424517345774) [X7 Z9 Z10 X11]
+ (0.030104623143456848) [Y6 Z7 Z9 Y10]
+ (0.030104623143456848) [X6 Z7 Z9 X10]
+ (0.030104623143456848) [Y7 Z8 Z10 Y11]
+ (0.030104623143456848) [X7 Z8 Z10 X11]
+ (0.030787505389143967) [Y6 Z8 Z9 Y10]
+ (0.030787505389143967) [X6 Z8 Z9 X10]
+ (0.0311438179889671) [Y2 X3 X6 Y7]
+ (0.0311438179889671) [X2 Y3 Y6 X7]
+ (0.03583956795335345) [Y2 X3 X4 Y5]
+ (0.03583956795335345) [X2 Y3 Y4 X5]
+ (0.03619412355904259) [Y2 X3 X8 Y9]
+ (0.03619412355904259) [X2 Y3 Y8 X9]
+ (0.03831467029480388) [Y4 X5 X12 Y13]
+ (0.03831467029480388) [X4 Y5 Y12 X13]
+ (0.10433064780651385) [Z0 Y1 Z2 Y3]
+ (0.10433064780651385) [Z0 X1 Z2 X3]
+ (-0.12133276911042418) [Y3 Z4 Z5 Z6 Y7]
+ (-0.12133276911042418) [X3 Z4 Z5 Z6 X7]
+ (-0.12133276911042414) [Y2 Z3 Z4 Z5 Y6]
+ (-0.12133276911042414) [X2 Z3 Z4 Z5 X6]
+ (3.2020768802727385e-06) [Y0 Z1 Z2 Z3 Y4]
+ (3.2020768802727385e-06) [X0 Z1 Z2 Z3 X4]
+ (3.2020768802727393e-06) [Y1 Z2 Z3 Z4 Y5]
+ (3.2020768802727393e-06) [X1 Z2 Z3 Z4 X5]
+ (0.2284810656491883) [Y6 Z7 Z8 Z9 Y10]
+ (0.2284810656491883) [X6 Z7 Z8 Z9 X10]
+ (0.22848106564918838) [Y7 Z8 Z9 Z10 Y11]
+ (0.22848106564918838) [X7 Z8 Z9 Z10 X11]
+ (-0.03276765782329052) [Z0 Y3 Z4 Z5 Z6 Y7]
+ (-0.03276765782329052) [Z0 X3 Z4 Z5 Z6 X7]
+ (-0.03276765782329052) [Z1 Y2 Z3 Z4 Z5 Y6]
+ (-0.03276765782329052) [Z1 X2 Z3 Z4 Z5 X6]
+ (-0.027115036845273176) [Z0 Y2 Z3 Z4 Z5 Y6]
+ (-0.027115036845273176) [Z0 X2 Z3 Z4 Z5 X6]
+ (-0.027115036845273176) [Z1 Y3 Z4 Z5 Z6 Y7]
+ (-0.027115036845273176) [Z1 X3 Z4 Z5 Z6 X7]
+ (-0.025996177598021288) [Y2 Z3 Z4 Z5 Y6 Z7]
+ (-0.025996177598021288) [X2 Z3 Z4 Z5 X6 Z7]
+ (-0.017561202409646197) [Y2 Z3 Z4 Z5 Y6 Z9]
+ (-0.017561202409646197) [X2 Z3 Z4 Z5 X6 Z9]
+ (-0.017561202409646197) [Y3 Z4 Z5 Z6 Y7 Z8]
+ (-0.017561202409646197) [X3 Z4 Z5 Z6 X7 Z8]
+ (-0.014564531231172961) [Y7 Z8 Z9 X10 X12 Y13]
+ (-0.014564531231172961) [Y7 Z8 Z9 Y10 Y12 Y13]
+ (-0.014564531231172961) [X7 Z8 Z9 X10 X12 X13]
+ (-0.014564531231172961) [X7 Z8 Z9 Y10 Y12 X13]
+ (-0.01221504099761394) [Y4 Z5 Y6 Y11 Z12 Y13]
+ (-0.01221504099761394) [Y4 Z5 Y6 X11 Z12 X13]
+ (-0.01221504099761394) [X4 Z5 X6 Y11 Z12 Y13]
+ (-0.01221504099761394) [X4 Z5 X6 X11 Z12 X13]
+ (-0.01221504099761394) [Y5 Z6 Y7 Y10 Z11 Y12]
+ (-0.01221504099761394) [Y5 Z6 Y7 X10 Z11 X12]
+ (-0.01221504099761394) [X5 Z6 X7 Y10 Z11 Y12]
+ (-0.01221504099761394) [X5 Z6 X7 X10 Z11 X12]
+ (-0.011756013419819283) [Y3 Z4 Z5 X6 X8 Y9]
+ (-0.011756013419819283) [Y3 Z4 Z5 Y6 Y8 Y9]
+ (-0.011756013419819283) [X3 Z4 Z5 X6 X8 X9]
+ (-0.011756013419819283) [X3 Z4 Z5 Y6 Y8 X9]
+ (-0.008764827575688763) [Y2 Z3 Z4 X5 X11 Y12]
+ (-0.008764827575688763) [Y2 Z3 Z4 Y5 Y11 Y12]
+ (-0.008764827575688763) [X2 Z3 Z4 X5 X11 X12]
+ (-0.008764827575688763) [X2 Z3 Z4 Y5 Y11 X12]
+ (-0.008764827575688763) [Y3 X4 X10 Z11 Z12 Y13]
+ (-0.008764827575688763) [Y3 Y4 Y10 Z11 Z12 Y13]
+ (-0.008764827575688763) [X3 X4 X10 Z11 Z12 X13]
+ (-0.008764827575688763) [X3 Y4 Y10 Z11 Z12 X13]
+ (-0.008125251921381025) [Y0 Z1 Z2 Y3 X8 X9]
+ (-0.008125251921381025) [X0 Z1 Z2 X3 Y8 Y9]
+ (-0.007306759928832991) [Y4 X5 X7 Z8 Z9 Y10]
+ (-0.007306759928832991) [Y4 Y5 Y7 Z8 Z9 Y10]
+ (-0.007306759928832991) [X4 X5 X7 Z8 Z9 X10]
+ (-0.007306759928832991) [X4 Y5 Y7 Z8 Z9 X10]
+ (-0.005805188989826918) [Y2 Z3 Z4 Z5 Y6 Z8]
+ (-0.005805188989826918) [X2 Z3 Z4 Z5 X6 Z8]
+ (-0.005805188989826918) [Y3 Z4 Z5 Z6 Y7 Z9]
+ (-0.005805188989826918) [X3 Z4 Z5 Z6 X7 Z9]
+ (-0.005652620978017351) [Y0 X1 X3 Z4 Z5 Y6]
+ (-0.005652620978017351) [Y0 Y1 Y3 Z4 Z5 Y6]
+ (-0.005652620978017351) [X0 X1 X3 Z4 Z5 X6]
+ (-0.005652620978017351) [X0 Y1 Y3 Z4 Z5 X6]
+ (-0.005143391768825133) [Y2 Z3 Y4 Y5 Z6 Y7]
+ (-0.005143391768825133) [Y2 Z3 Y4 X5 Z6 X7]
+ (-0.005143391768825133) [X2 Z3 X4 Y5 Z6 Y7]
+ (-0.005143391768825133) [X2 Z3 X4 X5 Z6 X7]
+ (-0.004668620318776302) [Y1 X2 X7 Z8 Z9 Y10]
+ (-0.004668620318776302) [X1 Y2 Y7 Z8 Z9 X10]
+ (-0.004575007626639211) [Y0 Z1 Z2 Y3 X12 X13]
+ (-0.004575007626639211) [X0 Z1 Z2 X3 Y12 Y13]
+ (-0.004424855449441842) [Y0 Z1 Z2 Y3 X4 X5]
+ (-0.004424855449441842) [X0 Z1 Z2 X3 Y4 Y5]
+ (-0.004158797381840081) [Y3 Z4 Z5 X6 X12 Y13]
+ (-0.004158797381840081) [Y3 Z4 Z5 Y6 Y12 Y13]
+ (-0.004158797381840081) [X3 Z4 Z5 X6 X12 X13]
+ (-0.004158797381840081) [X3 Z4 Z5 Y6 Y12 X13]
+ (-0.003493790359890225) [Y2 Z3 Z4 Z5 Y6 Z13]
+ (-0.003493790359890225) [X2 Z3 Z4 Z5 X6 Z13]
+ (-0.003493790359890225) [Y3 Z4 Z5 Z6 Y7 Z12]
+ (-0.003493790359890225) [X3 Z4 Z5 Z6 X7 Z12]
+ (-0.0027790267990255614) [Y1 Z2 Z3 Z4 Z5 Y7]
+ (-0.0027790267990255614) [X1 Z2 Z3 Z4 Z5 X7]
+ (-0.0022939566113524663) [Y1 X2 X3 Z4 Z5 Y6]
+ (-0.0022939566113524663) [X1 Y2 Y3 Z4 Z5 X6]
+ (-0.00179921949366303) [Y0 Z1 Z2 Y3 X10 X11]
+ (-0.00179921949366303) [X0 Z1 Z2 X3 Y10 Y11]
+ (-0.0017278753941369484) [Y1 Z2 Z3 X4 X11 Y12]
+ (-0.0017278753941369484) [X1 Z2 Z3 Y4 Y11 X12]
+ (-0.0009298507967730287) [Y4 Z5 Y6 X10 Z11 X12]
+ (-0.0009298507967730287) [X4 Z5 X6 Y10 Z11 Y12]
+ (-0.0009298507967730287) [Y5 Z6 Y7 X11 Z12 X13]
+ (-0.0009298507967730287) [X5 Z6 X7 Y11 Z12 Y13]
+ (-0.000853385625412549) [Y1 Z2 Z3 Y4 X5 X6]
+ (-0.000853385625412549) [X1 Z2 Z3 X4 Y5 Y6]
+ (-0.0008145313270956998) [Y2 Z3 Z4 Z5 Y6 Z10]
+ (-0.0008145313270956998) [X2 Z3 Z4 Z5 X6 Z10]
+ (-0.0008145313270956998) [Y3 Z4 Z5 Z6 Y7 Z11]
+ (-0.0008145313270956998) [X3 Z4 Z5 Z6 X7 Z11]
+ (-7.73503688059091e-05) [Y0 X1 X7 Z8 Z9 Y10]
+ (-7.73503688059091e-05) [Y0 Y1 Y7 Z8 Z9 Y10]
+ (-7.73503688059091e-05) [X0 X1 X7 Z8 Z9 X10]
+ (-7.73503688059091e-05) [X0 Y1 Y7 Z8 Z9 X10]
+ (-8.774817864465264e-06) [Y4 Z5 Z6 Z7 Z8 Y10]
+ (-8.774817864465264e-06) [X4 Z5 Z6 Z7 Z8 X10]
+ (-8.774817864465264e-06) [Y5 Z6 Z7 Z9 Z10 Y11]
+ (-8.774817864465264e-06) [X5 Z6 Z7 Z9 Z10 X11]
+ (-7.518362215591566e-06) [Y4 Z5 Z7 Z8 Z9 Y10]
+ (-7.518362215591566e-06) [X4 Z5 Z7 Z8 Z9 X10]
+ (-7.518362215591566e-06) [Y5 Z6 Z8 Z9 Z10 Y11]
+ (-7.518362215591566e-06) [X5 Z6 Z8 Z9 Z10 X11]
+ (-7.444344675812155e-06) [Y4 Z5 Z6 Z7 Z9 Y10]
+ (-7.444344675812155e-06) [X4 Z5 Z6 Z7 Z9 X10]
+ (-7.444344675812155e-06) [Y5 Z6 Z7 Z8 Z10 Y11]
+ (-7.444344675812155e-06) [X5 Z6 Z7 Z8 Z10 X11]
+ (-6.524373848515009e-06) [Y6 Z7 Z8 Z9 Z10 Y12]
+ (-6.524373848515009e-06) [X6 Z7 Z8 Z9 Z10 X12]
+ (-6.524373848515009e-06) [Y7 Z8 Z9 Z11 Z12 Y13]
+ (-6.524373848515009e-06) [X7 Z8 Z9 Z11 Z12 X13]
+ (-6.2900284331040335e-06) [Y4 Z5 Z6 Z8 Z9 Y10]
+ (-6.2900284331040335e-06) [X4 Z5 Z6 Z8 Z9 X10]
+ (-6.2900284331040335e-06) [Y5 Z7 Z8 Z9 Z10 Y11]
+ (-6.2900284331040335e-06) [X5 Z7 Z8 Z9 Z10 X11]
+ (-5.974311713354573e-06) [Y4 Z5 Z6 X7 X10 Y11]
+ (-5.974311713354573e-06) [X4 Z5 Z6 Y7 Y10 X11]
+ (-5.275883122040938e-06) [Y2 Z3 Z4 X5 X12 Y13]
+ (-5.275883122040938e-06) [X2 Z3 Z4 Y5 Y12 X13]
+ (-4.643051068420232e-06) [Y2 Z3 Z4 Y5 X10 X11]
+ (-4.643051068420232e-06) [X2 Z3 Z4 X5 Y10 Y11]
+ (-4.556569218049105e-06) [Y4 Z5 Z6 Y7 X12 X13]
+ (-4.556569218049105e-06) [X4 Z5 Z6 X7 Y12 Y13]
+ (-4.253224225550497e-06) [Y4 Z6 Z7 Z8 Z9 Y10]
+ (-4.253224225550497e-06) [X4 Z6 Z7 Z8 Z9 X10]
+ (-3.769659451902788e-06) [Y6 Z8 Z9 Z10 Z11 Y12]
+ (-3.769659451902788e-06) [X6 Z8 Z9 Z10 Z11 X12]
+ (-3.694513294434133e-06) [Y4 Y5 X10 Z11 Z12 X13]
+ (-3.694513294434133e-06) [X4 X5 Y10 Z11 Z12 Y13]
+ (-3.610297130489855e-06) [Y6 Z7 Z9 Z10 Z11 Y12]
+ (-3.610297130489855e-06) [X6 Z7 Z9 Z10 Z11 X12]
+ (-3.610297130489855e-06) [Y7 Z8 Z10 Z11 Z12 Y13]
+ (-3.610297130489855e-06) [X7 Z8 Z10 Z11 Z12 X13]
+ (-3.3131455001526633e-06) [Y7 Z8 Z9 Y10 X11 X12]
+ (-3.3131455001526633e-06) [X7 Z8 Z9 X10 Y11 Y12]
+ (-3.2774831954255384e-06) [Y6 Z7 Z8 Z10 Z11 Y12]
+ (-3.2774831954255384e-06) [X6 Z7 Z8 Z10 Z11 X12]
+ (-3.2774831954255384e-06) [Y7 Z9 Z10 Z11 Z12 Y13]
+ (-3.2774831954255384e-06) [X7 Z9 Z10 Z11 Z12 X13]
+ (-3.2112283483623452e-06) [Y6 Z7 Z8 Z9 Z11 Y12]
+ (-3.2112283483623452e-06) [X6 Z7 Z8 Z9 Z11 X12]
+ (-3.2112283483623452e-06) [Y7 Z8 Z9 Z10 Z12 Y13]
+ (-3.2112283483623452e-06) [X7 Z8 Z9 Z10 Z12 X13]
+ (-3.151346311126544e-06) [Y3 Y4 X7 Z8 Z9 X10]
+ (-3.151346311126544e-06) [X3 X4 Y7 Z8 Z9 Y10]
+ (-3.088250711247478e-06) [Y3 Z4 Z5 Y6 X11 X12]
+ (-3.088250711247478e-06) [X3 Z4 Z5 X6 Y11 Y12]
+ (-2.172669101455125e-06) [Y2 X3 X10 Z11 Z12 Y13]
+ (-2.172669101455125e-06) [X2 Y3 Y10 Z11 Z12 X13]
+ (-1.4548424490644837e-06) [Y2 Z3 Z4 Y5 X6 X7]
+ (-1.4548424490644837e-06) [X2 Z3 Z4 X5 Y6 Y7]
+ (-1.3304731886531085e-06) [Y5 Z6 Z7 Y8 X9 X10]
+ (-1.3304731886531085e-06) [X5 Z6 Z7 X8 Y9 Y10]
+ (-1.2283337824875313e-06) [Y5 X6 X7 Z8 Z9 Y10]
+ (-1.2283337824875313e-06) [X5 Y6 Y7 Z8 Z9 X10]
+ (-1.0358477601631472e-06) [Y6 Y7 X10 Z11 Z12 X13]
+ (-1.0358477601631472e-06) [X6 X7 Y10 Z11 Z12 Y13]
+ (-7.956895372534156e-07) [Y2 Z3 Z4 Y5 X8 X9]
+ (-7.956895372534156e-07) [X2 Z3 Z4 X5 Y8 Y9]
+ (-6.733197742121356e-07) [Y0 Z1 Z2 Z3 Y4 Z10]
+ (-6.733197742121356e-07) [X0 Z1 Z2 Z3 X4 Z10]
+ (-6.733197742121356e-07) [Y1 Z2 Z3 Z4 Y5 Z11]
+ (-6.733197742121356e-07) [X1 Z2 Z3 Z4 X5 Z11]
+ (-6.628614201637058e-07) [Y8 X9 X10 Z11 Z12 Y13]
+ (-6.628614201637058e-07) [X8 Y9 Y10 Z11 Z12 X13]
+ (-6.5562819143643e-07) [Y0 Z1 Y2 X10 Z11 X12]
+ (-6.5562819143643e-07) [X0 Z1 X2 Y10 Z11 Y12]
+ (-6.5562819143643e-07) [Y1 Z2 Y3 X11 Z12 X13]
+ (-6.5562819143643e-07) [X1 Z2 X3 Y11 Z12 Y13]
+ (-6.418291574438302e-07) [Y0 Z1 Y2 Y10 Z11 Y12]
+ (-6.418291574438302e-07) [X0 Z1 X2 X10 Z11 X12]
+ (-6.418291574438302e-07) [Y1 Z2 Y3 Y11 Z12 Y13]
+ (-6.418291574438302e-07) [X1 Z2 X3 X11 Z12 X13]
+ (-5.927453082584184e-07) [Y0 Z1 Z2 Z3 Y4 Z11]
+ (-5.927453082584184e-07) [X0 Z1 Z2 Z3 X4 Z11]
+ (-5.927453082584184e-07) [Y1 Z2 Z3 Z4 Y5 Z10]
+ (-5.927453082584184e-07) [X1 Z2 Z3 Z4 X5 Z10]
+ (-5.627851911415513e-07) [Y0 X1 X10 Z11 Z12 Y13]
+ (-5.627851911415513e-07) [X0 Y1 Y10 Z11 Z12 X13]
+ (-5.28766062467047e-07) [Y0 Z1 Z2 X3 X11 Y12]
+ (-5.28766062467047e-07) [Y0 Z1 Z2 Y3 Y11 Y12]
+ (-5.28766062467047e-07) [X0 Z1 Z2 X3 X11 X12]
+ (-5.28766062467047e-07) [X0 Z1 Z2 Y3 Y11 X12]
+ (-5.28766062467047e-07) [Y1 X2 X10 Z11 Z12 Y13]
+ (-5.28766062467047e-07) [Y1 Y2 Y10 Z11 Z12 Y13]
+ (-5.28766062467047e-07) [X1 X2 X10 Z11 Z12 X13]
+ (-5.28766062467047e-07) [X1 Y2 Y10 Z11 Z12 X13]
+ (-4.838052750850165e-07) [Y4 Z5 Z6 Y7 X8 X9]
+ (-4.838052750850165e-07) [X4 Z5 Z6 X7 Y8 Y9]
+ (-3.5707613291445906e-07) [Y0 Y1 X2 Z3 Z4 X5]
+ (-3.5707613291445906e-07) [X0 X1 Y2 Z3 Z4 Y5]
+ (-3.3281393506431665e-07) [Y7 X8 X9 Z10 Z11 Y12]
+ (-3.3281393506431665e-07) [X7 Y8 Y9 Z10 Z11 X12]
+ (-3.086826565124548e-07) [Y1 Z2 Z3 X4 X12 Y13]
+ (-3.086826565124548e-07) [Y1 Z2 Z3 Y4 Y12 Y13]
+ (-3.086826565124548e-07) [X1 Z2 Z3 X4 X12 X13]
+ (-3.086826565124548e-07) [X1 Z2 Z3 Y4 Y12 X13]
+ (-2.44732312879803e-07) [Y0 Y1 X4 Z5 Z6 X7]
+ (-2.44732312879803e-07) [X0 X1 Y4 Z5 Z6 Y7]
+ (-2.371328947878356e-07) [Y1 Z2 Z3 X4 X8 Y9]
+ (-2.371328947878356e-07) [Y1 Z2 Z3 Y4 Y8 Y9]
+ (-2.371328947878356e-07) [X1 Z2 Z3 X4 X8 X9]
+ (-2.371328947878356e-07) [X1 Z2 Z3 Y4 Y8 X9]
+ (-2.1990516184609328e-07) [Y2 Y3 X4 Z5 Z6 X7]
+ (-2.1990516184609328e-07) [X2 X3 Y4 Z5 Z6 Y7]
+ (-1.9332412770552596e-07) [Y0 Z1 Y2 Y3 Z4 Y5]
+ (-1.9332412770552596e-07) [Y0 Z1 Y2 X3 Z4 X5]
+ (-1.9332412770552596e-07) [X0 Z1 X2 Y3 Z4 Y5]
+ (-1.9332412770552596e-07) [X0 Z1 X2 X3 Z4 X5]
+ (-1.839420915456096e-07) [Y1 Z2 Z3 X4 X6 Y7]
+ (-1.839420915456096e-07) [Y1 Z2 Z3 Y4 Y6 Y7]
+ (-1.839420915456096e-07) [X1 Z2 Z3 X4 X6 X7]
+ (-1.839420915456096e-07) [X1 Z2 Z3 Y4 Y6 X7]
+ (-1.5510539176005066e-07) [Y0 Z1 Y2 Y4 Z5 Y6]
+ (-1.5510539176005066e-07) [X0 Z1 X2 X4 Z5 X6]
+ (-1.5510539176005066e-07) [Y1 Z2 Y3 Y5 Z6 Y7]
+ (-1.5510539176005066e-07) [X1 Z2 X3 X5 Z6 X7]
+ (-1.3807781480594408e-07) [Y0 Z1 Y2 X4 Z5 X6]
+ (-1.3807781480594408e-07) [X0 Z1 X2 Y4 Z5 Y6]
+ (-1.3807781480594408e-07) [Y0 Z1 Y2 Y5 Z6 Y7]
+ (-1.3807781480594408e-07) [Y0 Z1 Y2 X5 Z6 X7]
+ (-1.3807781480594408e-07) [X0 Z1 X2 Y5 Z6 Y7]
+ (-1.3807781480594408e-07) [X0 Z1 X2 X5 Z6 X7]
+ (-1.3807781480594408e-07) [Y1 Z2 Y3 Y4 Z5 Y6]
+ (-1.3807781480594408e-07) [Y1 Z2 Y3 X4 Z5 X6]
+ (-1.3807781480594408e-07) [X1 Z2 X3 Y4 Z5 Y6]
+ (-1.3807781480594408e-07) [X1 Z2 X3 X4 Z5 X6]
+ (-1.3807781480594408e-07) [Y1 Z2 Y3 X5 Z6 X7]
+ (-1.3807781480594408e-07) [X1 Z2 X3 Y5 Z6 Y7]
+ (-1.2919694861266596e-07) [Y0 Z1 Z2 Z3 Y4 Z5]
+ (-1.2919694861266596e-07) [X0 Z1 Z2 Z3 X4 Z5]
+ (-1.1076325597785792e-07) [Y0 Z1 Y2 Y11 Z12 Y13]
+ (-1.1076325597785792e-07) [Y0 Z1 Y2 X11 Z12 X13]
+ (-1.1076325597785792e-07) [X0 Z1 X2 Y11 Z12 Y13]
+ (-1.1076325597785792e-07) [X0 Z1 X2 X11 Z12 X13]
+ (-1.1076325597785792e-07) [Y1 Z2 Y3 Y10 Z11 Y12]
+ (-1.1076325597785792e-07) [Y1 Z2 Y3 X10 Z11 X12]
+ (-1.1076325597785792e-07) [X1 Z2 X3 Y10 Z11 Y12]
+ (-1.1076325597785792e-07) [X1 Z2 X3 X10 Z11 X12]
+ (8.057446595371729e-08) [Y1 Z2 Z3 X4 X10 Y11]
+ (8.057446595371729e-08) [Y1 Z2 Z3 Y4 Y10 Y11]
+ (8.057446595371729e-08) [X1 Z2 Z3 X4 X10 X11]
+ (8.057446595371729e-08) [X1 Z2 Z3 Y4 Y10 X11]
+ (8.649310135841302e-08) [Y0 Z1 Z2 Z3 Y4 Z9]
+ (8.649310135841302e-08) [X0 Z1 Z2 Z3 X4 Z9]
+ (8.649310135841302e-08) [Y1 Z2 Z3 Z4 Y5 Z8]
+ (8.649310135841302e-08) [X1 Z2 Z3 Z4 X5 Z8]
+ (1.8394209154560958e-07) [Y0 Z1 Z2 Z3 Y4 Z6]
+ (1.8394209154560958e-07) [X0 Z1 Z2 Z3 X4 Z6]
+ (1.8394209154560958e-07) [Y1 Z2 Z3 Z4 Y5 Z7]
+ (1.8394209154560958e-07) [X1 Z2 Z3 Z4 X5 Z7]
+ (2.1990516184609328e-07) [Y2 X3 X4 Z5 Z6 Y7]
+ (2.1990516184609328e-07) [X2 Y3 Y4 Z5 Z6 X7]
+ (2.44732312879803e-07) [Y0 X1 X4 Z5 Z6 Y7]
+ (2.44732312879803e-07) [X0 Y1 Y4 Z5 Z6 X7]
+ (3.2362599614624863e-07) [Y0 Z1 Z2 Z3 Y4 Z8]
+ (3.2362599614624863e-07) [X0 Z1 Z2 Z3 X4 Z8]
+ (3.2362599614624863e-07) [Y1 Z2 Z3 Z4 Y5 Z9]
+ (3.2362599614624863e-07) [X1 Z2 Z3 Z4 X5 Z9]
+ (3.3281393506431665e-07) [Y7 Y8 X9 Z10 Z11 X12]
+ (3.3281393506431665e-07) [X7 X8 Y9 Z10 Z11 Y12]
+ (3.5707613291445906e-07) [Y0 X1 X2 Z3 Z4 Y5]
+ (3.5707613291445906e-07) [X0 Y1 Y2 Z3 Z4 X5]
+ (4.838052750850165e-07) [Y4 Z5 Z6 X7 X8 Y9]
+ (4.838052750850165e-07) [X4 Z5 Z6 Y7 Y8 X9]
+ (5.627851911415513e-07) [Y0 Y1 X10 Z11 Z12 X13]
+ (5.627851911415513e-07) [X0 X1 Y10 Z11 Z12 Y13]
+ (6.628614201637058e-07) [Y8 Y9 X10 Z11 Z12 X13]
+ (6.628614201637058e-07) [X8 X9 Y10 Z11 Z12 Y13]
+ (7.956895372534156e-07) [Y2 Z3 Z4 X5 X8 Y9]
+ (7.956895372534156e-07) [X2 Z3 Z4 Y5 Y8 X9]
+ (9.306536651890273e-07) [Y0 Z1 Z2 Z3 Y4 Z13]
+ (9.306536651890273e-07) [X0 Z1 Z2 Z3 X4 Z13]
+ (9.306536651890273e-07) [Y1 Z2 Z3 Z4 Y5 Z12]
+ (9.306536651890273e-07) [X1 Z2 Z3 Z4 X5 Z12]
+ (1.0358477601631472e-06) [Y6 X7 X10 Z11 Z12 Y13]
+ (1.0358477601631472e-06) [X6 Y7 Y10 Z11 Z12 X13]
+ (1.2283337824875313e-06) [Y5 Y6 X7 Z8 Z9 X10]
+ (1.2283337824875313e-06) [X5 X6 Y7 Z8 Z9 Y10]
+ (1.239336321701482e-06) [Y0 Z1 Z2 Z3 Y4 Z12]
+ (1.239336321701482e-06) [X0 Z1 Z2 Z3 X4 Z12]
+ (1.239336321701482e-06) [Y1 Z2 Z3 Z4 Y5 Z13]
+ (1.239336321701482e-06) [X1 Z2 Z3 Z4 X5 Z13]
+ (1.3304731886531085e-06) [Y5 Z6 Z7 X8 X9 Y10]
+ (1.3304731886531085e-06) [X5 Z6 Z7 Y8 Y9 X10]
+ (1.4548424490644837e-06) [Y2 Z3 Z4 X5 X6 Y7]
+ (1.4548424490644837e-06) [X2 Z3 Z4 Y5 Y6 X7]
+ (2.172669101455125e-06) [Y2 Y3 X10 Z11 Z12 X13]
+ (2.172669101455125e-06) [X2 X3 Y10 Z11 Z12 Y13]
+ (3.088250711247478e-06) [Y3 Z4 Z5 X6 X11 Y12]
+ (3.088250711247478e-06) [X3 Z4 Z5 Y6 Y11 X12]
+ (3.1174479460915516e-06) [Z0 Y1 Z2 Z3 Z4 Y5]
+ (3.1174479460915516e-06) [Z0 X1 Z2 Z3 Z4 X5]
+ (3.151346311126544e-06) [Y3 X4 X7 Z8 Z9 Y10]
+ (3.151346311126544e-06) [X3 Y4 Y7 Z8 Z9 X10]
+ (3.3131455001526633e-06) [Y7 Z8 Z9 X10 X11 Y12]
+ (3.3131455001526633e-06) [X7 Z8 Z9 Y10 Y11 X12]
+ (3.3343312893981367e-06) [Y5 Z6 Z7 Z8 Z9 Y11]
+ (3.3343312893981367e-06) [X5 Z6 Z7 Z8 Z9 X11]
+ (3.694513294434133e-06) [Y4 X5 X10 Z11 Z12 Y13]
+ (3.694513294434133e-06) [X4 Y5 Y10 Z11 Z12 X13]
+ (4.183932559328526e-06) [Y7 Z8 Z9 Z10 Z11 Y13]
+ (4.183932559328526e-06) [X7 Z8 Z9 Z10 Z11 X13]
+ (4.556569218049105e-06) [Y4 Z5 Z6 X7 X12 Y13]
+ (4.556569218049105e-06) [X4 Z5 Z6 Y7 Y12 X13]
+ (4.643051068420232e-06) [Y2 Z3 Z4 X5 X10 Y11]
+ (4.643051068420232e-06) [X2 Z3 Z4 Y5 Y10 X11]
+ (5.275883122040938e-06) [Y2 Z3 Z4 Y5 X12 X13]
+ (5.275883122040938e-06) [X2 Z3 Z4 X5 Y12 Y13]
+ (5.974311713354573e-06) [Y4 Z5 Z6 Y7 X10 X11]
+ (5.974311713354573e-06) [X4 Z5 Z6 X7 Y10 Y11]
+ (0.00029219862611107273) [Y6 Z7 Y8 Y9 Z10 Y11]
+ (0.00029219862611107273) [Y6 Z7 Y8 X9 Z10 X11]
+ (0.00029219862611107273) [X6 Z7 X8 Y9 Z10 Y11]
+ (0.00029219862611107273) [X6 Z7 X8 X9 Z10 X11]
+ (0.0004956762314916399) [Z2 Y3 Z4 Z5 Z6 Y7]
+ (0.0004956762314916399) [Z2 X3 Z4 Z5 Z6 X7]
+ (0.0006650070219498559) [Y2 Z3 Z4 Z5 Y6 Z12]
+ (0.0006650070219498559) [X2 Z3 Z4 Z5 X6 Z12]
+ (0.0006650070219498559) [Y3 Z4 Z5 Z6 Y7 Z13]
+ (0.0006650070219498559) [X3 Z4 Z5 Z6 X7 Z13]
+ (0.000853385625412549) [Y1 Z2 Z3 X4 X5 Y6]
+ (0.000853385625412549) [X1 Z2 Z3 Y4 Y5 X6]
+ (0.001609531381721375) [Y0 Z1 Z2 Z3 Z4 Y6]
+ (0.001609531381721375) [X0 Z1 Z2 Z3 Z4 X6]
+ (0.001609531381721375) [Y1 Z2 Z3 Z5 Z6 Y7]
+ (0.001609531381721375) [X1 Z2 Z3 Z5 Z6 X7]
+ (0.0016676041811440568) [Y0 Z1 Z3 Z4 Z5 Y6]
+ (0.0016676041811440568) [X0 Z1 Z3 Z4 Z5 X6]
+ (0.0016676041811440568) [Y1 Z2 Z4 Z5 Z6 Y7]
+ (0.0016676041811440568) [X1 Z2 Z4 Z5 Z6 X7]
+ (0.0017278753941369484) [Y1 Z2 Z3 Y4 X11 X12]
+ (0.0017278753941369484) [X1 Z2 Z3 X4 Y11 Y12]
+ (0.00179921949366303) [Y0 Z1 Z2 X3 X10 Y11]
+ (0.00179921949366303) [X0 Z1 Z2 Y3 Y10 X11]
+ (0.0022939566113524663) [Y1 Y2 X3 Z4 Z5 X6]
+ (0.0022939566113524663) [X1 X2 Y3 Z4 Z5 Y6]
+ (0.0024629170071339235) [Y0 Z1 Z2 Z3 Z5 Y6]
+ (0.0024629170071339235) [X0 Z1 Z2 Z3 Z5 X6]
+ (0.0024629170071339235) [Y1 Z2 Z3 Z4 Z6 Y7]
+ (0.0024629170071339235) [X1 Z2 Z3 Z4 Z6 X7]
+ (0.003961560792496523) [Y0 Z1 Z2 Z4 Z5 Y6]
+ (0.003961560792496523) [X0 Z1 Z2 Z4 Z5 X6]
+ (0.003961560792496523) [Y1 Z3 Z4 Z5 Z6 Y7]
+ (0.003961560792496523) [X1 Z3 Z4 Z5 Z6 X7]
+ (0.004424855449441842) [Y0 Z1 Z2 X3 X4 Y5]
+ (0.004424855449441842) [X0 Z1 Z2 Y3 Y4 X5]
+ (0.004575007626639211) [Y0 Z1 Z2 X3 X12 Y13]
+ (0.004575007626639211) [X0 Z1 Z2 Y3 Y12 X13]
+ (0.004668620318776302) [Y1 Y2 X7 Z8 Z9 X10]
+ (0.004668620318776302) [X1 X2 Y7 Z8 Z9 Y10]
+ (0.005324835234221661) [Y2 Z3 Y4 X10 Z11 X12]
+ (0.005324835234221661) [X2 Z3 X4 Y10 Z11 Y12]
+ (0.005324835234221661) [Y3 Z4 Y5 X11 Z12 X13]
+ (0.005324835234221661) [X3 Z4 X5 Y11 Z12 Y13]
+ (0.005368659358109524) [Y2 X3 X7 Z8 Z9 Y10]
+ (0.005368659358109524) [Y2 Y3 Y7 Z8 Z9 Y10]
+ (0.005368659358109524) [X2 X3 X7 Z8 Z9 X10]
+ (0.005368659358109524) [X2 Y3 Y7 Z8 Z9 X10]
+ (0.007960880725921566) [Y4 Z5 Y6 Y10 Z11 Y12]
+ (0.007960880725921566) [X4 Z5 X6 X10 Z11 X12]
+ (0.007960880725921566) [Y5 Z6 Y7 Y11 Z12 Y13]
+ (0.007960880725921566) [X5 Z6 X7 X11 Z12 X13]
+ (0.008125251921381025) [Y0 Z1 Z2 X3 X8 Y9]
+ (0.008125251921381025) [X0 Z1 Z2 Y3 Y8 X9]
+ (0.008890731522694595) [Y4 Z5 X6 X10 Z11 Y12]
+ (0.008890731522694595) [X4 Z5 Y6 Y10 Z11 X12]
+ (0.008890731522694595) [Y5 Z6 X7 X11 Z12 Y13]
+ (0.008890731522694595) [X5 Z6 Y7 Y11 Z12 X13]
+ (0.010263414868158535) [Y2 Z3 X4 X10 Z11 Y12]
+ (0.010263414868158535) [X2 Z3 Y4 Y10 Z11 X12]
+ (0.010263414868158535) [Y3 Z4 X5 X11 Z12 Y13]
+ (0.010263414868158535) [X3 Z4 Y5 Y11 Z12 X13]
+ (0.010540425907671562) [Y6 Z7 Z8 Z9 Y10 Z13]
+ (0.010540425907671562) [X6 Z7 Z8 Z9 X10 Z13]
+ (0.010540425907671562) [Y7 Z8 Z9 Z10 Y11 Z12]
+ (0.010540425907671562) [X7 Z8 Z9 Z10 X11 Z12]
+ (0.010960074940542505) [Z4 Y7 Z8 Z9 Z10 Y11]
+ (0.010960074940542505) [Z4 X7 Z8 Z9 Z10 X11]
+ (0.010960074940542505) [Z5 Y6 Z7 Z8 Z9 Y10]
+ (0.010960074940542505) [Z5 X6 Z7 Z8 Z9 X10]
+ (0.011307274008848166) [Y6 Z7 Z8 Z9 Y10 Z11]
+ (0.011307274008848166) [X6 Z7 Z8 Z9 X10 Z11]
+ (0.014411099430130886) [Y2 Z3 Z4 Z5 Y6 Z11]
+ (0.014411099430130886) [X2 Z3 Z4 Z5 X6 Z11]
+ (0.014411099430130886) [Y3 Z4 Z5 Z6 Y7 Z10]
+ (0.014411099430130886) [X3 Z4 Z5 Z6 X7 Z10]
+ (0.015225630757226587) [Y3 Z4 Z5 X6 X10 Y11]
+ (0.015225630757226587) [Y3 Z4 Z5 Y6 Y10 Y11]
+ (0.015225630757226587) [X3 Z4 Z5 X6 X10 X11]
+ (0.015225630757226587) [X3 Z4 Z5 Y6 Y10 X11]
+ (0.015588250102380198) [Y2 Z3 Y4 Y10 Z11 Y12]
+ (0.015588250102380198) [X2 Z3 X4 X10 Z11 X12]
+ (0.015588250102380198) [Y3 Z4 Y5 Y11 Z12 Y13]
+ (0.015588250102380198) [X3 Z4 X5 X11 Z12 X13]
+ (0.018266834869375494) [Z4 Y6 Z7 Z8 Z9 Y10]
+ (0.018266834869375494) [Z4 X6 Z7 Z8 Z9 X10]
+ (0.018266834869375494) [Z5 Y7 Z8 Z9 Z10 Y11]
+ (0.018266834869375494) [Z5 X7 Z8 Z9 Z10 X11]
+ (0.019020423173039945) [Z2 Y6 Z7 Z8 Z9 Y10]
+ (0.019020423173039945) [Z2 X6 Z7 Z8 Z9 X10]
+ (0.019020423173039945) [Z3 Y7 Z8 Z9 Z10 Y11]
+ (0.019020423173039945) [Z3 X7 Z8 Z9 Z10 X11]
+ (0.020175921723535505) [Y4 Z5 Z6 X7 X11 Y12]
+ (0.020175921723535505) [Y4 Z5 Z6 Y7 Y11 Y12]
+ (0.020175921723535505) [X4 Z5 Z6 X7 X11 X12]
+ (0.020175921723535505) [X4 Z5 Z6 Y7 Y11 X12]
+ (0.020175921723535505) [Y5 X6 X10 Z11 Z12 Y13]
+ (0.020175921723535505) [Y5 Y6 Y10 Z11 Z12 Y13]
+ (0.020175921723535505) [X5 X6 X10 Z11 Z12 X13]
+ (0.020175921723535505) [X5 Y6 Y10 Z11 Z12 X13]
+ (0.02435307767806896) [Y2 Z3 Y4 Y11 Z12 Y13]
+ (0.02435307767806896) [Y2 Z3 Y4 X11 Z12 X13]
+ (0.02435307767806896) [X2 Z3 X4 Y11 Z12 Y13]
+ (0.02435307767806896) [X2 Z3 X4 X11 Z12 X13]
+ (0.02435307767806896) [Y3 Z4 Y5 Y10 Z11 Y12]
+ (0.02435307767806896) [Y3 Z4 Y5 X10 Z11 X12]
+ (0.02435307767806896) [X3 Z4 X5 Y10 Z11 Y12]
+ (0.02435307767806896) [X3 Z4 X5 X10 Z11 X12]
+ (0.02438908253114947) [Z2 Y7 Z8 Z9 Z10 Y11]
+ (0.02438908253114947) [Z2 X7 Z8 Z9 Z10 X11]
+ (0.02438908253114947) [Z3 Y6 Z7 Z8 Z9 Y10]
+ (0.02438908253114947) [Z3 X6 Z7 Z8 Z9 X10]
+ (0.025104957138844523) [Y6 Z7 Z8 Z9 Y10 Z12]
+ (0.025104957138844523) [X6 Z7 Z8 Z9 X10 Z12]
+ (0.025104957138844523) [Y7 Z8 Z9 Z10 Y11 Z13]
+ (0.025104957138844523) [X7 Z8 Z9 Z10 X11 Z13]
+ (0.03078750538914397) [Z6 Y7 Z8 Z9 Z10 Y11]
+ (0.03078750538914397) [Z6 X7 Z8 Z9 Z10 X11]
+ (0.04587947078129807) [Y0 Z2 Z3 Z4 Z5 Y6]
+ (0.04587947078129807) [X0 Z2 Z3 Z4 Z5 X6]
+ (0.0560073308778076) [Z0 Y7 Z8 Z9 Z10 Y11]
+ (0.0560073308778076) [Z0 X7 Z8 Z9 Z10 X11]
+ (0.0560073308778076) [Z1 Y6 Z7 Z8 Z9 Y10]
+ (0.0560073308778076) [Z1 X6 Z7 Z8 Z9 X10]
+ (0.05608468124661351) [Z0 Y6 Z7 Z8 Z9 Y10]
+ (0.05608468124661351) [Z0 X6 Z7 Z8 Z9 X10]
+ (0.05608468124661351) [Z1 Y7 Z8 Z9 Z10 Y11]
+ (0.05608468124661351) [Z1 X7 Z8 Z9 Z10 X11]
+ (-6.631277928327274e-05) [Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-6.631277928327274e-05) [X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-6.631277928327274e-05) [Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-6.631277928327274e-05) [X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-2.5950860069396833e-05) [Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.5950860069396833e-05) [X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.5950860069396826e-05) [Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.5950860069396826e-05) [X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.042743277013782395) [Y0 Z1 Z2 Z3 Z4 Z5 Y6]
+ (0.042743277013782395) [X0 Z1 Z2 Z3 Z4 Z5 X6]
+ (0.04274327701378241) [Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.04274327701378241) [X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-0.0476426121763831) [Y4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-0.0476426121763831) [X4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-0.0476426121763831) [Y5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-0.0476426121763831) [X5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-0.04171881383982176) [Y4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-0.04171881383982176) [X4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-0.04171881383982176) [Y5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-0.04171881383982176) [X5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-0.03956441632289341) [Y4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-0.03956441632289341) [X4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-0.03956441632289341) [Y5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03956441632289341) [X5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03935916802205314) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (-0.03935916802205314) [X2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (-0.03935916802205314) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (-0.03935916802205314) [X3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (-0.039318051947197605) [Y4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.039318051947197605) [X4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.039318051947197605) [Y5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.039318051947197605) [X5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03560837898831262) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.03560837898831262) [X2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.029903789512624904) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (-0.029903789512624904) [X2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (-0.029903789512624904) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (-0.029903789512624904) [X3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (-0.028730779551905596) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.028730779551905596) [X2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.028730779551905596) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.028730779551905596) [X3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.025637238296026862) [Y4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-0.025637238296026862) [X4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-0.025637238296026862) [Y5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-0.025637238296026862) [X5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-0.024755463292891015) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (-0.024755463292891015) [X2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (-0.024755463292891015) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (-0.024755463292891015) [X3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (-0.024282117354693062) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.024282117354693062) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.023145130929529148) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (-0.023145130929529148) [X5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (-0.02252844019601294) [Y4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.02252844019601294) [X4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.021433810721600968) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (-0.021433810721600968) [X2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (-0.021433810721600968) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (-0.021433810721600968) [X3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251592) [Y3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.019257505095251592) [X3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.019028242443847296) [Y2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (-0.019028242443847296) [X2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (-0.01888903030494294) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-0.01888903030494294) [X2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-0.01888903030494294) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.01888903030494294) [X3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.016024603689179545) [Y5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-0.016024603689179545) [X5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-0.015225630757226587) [Y2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (-0.015225630757226587) [X2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (-0.014603704729162118) [Y3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.014603704729162118) [X3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.014564531231172961) [Y6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.014564531231172961) [X6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.01175601341981928) [Y2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.01175601341981928) [X2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.01128519020084091) [Y4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (-0.01128519020084091) [X4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (-0.009841749246962656) [Y3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (-0.009841749246962656) [X3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (-0.009612634606847314) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-0.009612634606847314) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-0.009612634606847314) [Y5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-0.009612634606847314) [X5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-0.007306759928832993) [Y4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-0.007306759928832993) [X4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005923798336561346) [Y5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (-0.005923798336561346) [X5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (-0.005652620978017351) [Y0 Y1 X2 Z3 Z4 Z5 Z6 X7]
+ (-0.005652620978017351) [X0 X1 Y2 Z3 Z4 Z5 Z6 Y7]
+ (-0.005368659358109524) [Y2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.005368659358109524) [X2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.004158797381840081) [Y2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.004158797381840081) [X2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.0033566705638328966) [Y1 Z2 Z3 Z4 Z5 X6 X8 Y9]
+ (-0.0033566705638328966) [Y1 Z2 Z3 Z4 Z5 Y6 Y8 Y9]
+ (-0.0033566705638328966) [X1 Z2 Z3 Z4 Z5 X6 X8 X9]
+ (-0.0033566705638328966) [X1 Z2 Z3 Z4 Z5 Y6 Y8 X9]
+ (-0.0032675138544235585) [Y1 Z2 Z3 Z4 Z5 X6 X12 Y13]
+ (-0.0032675138544235585) [Y1 Z2 Z3 Z4 Z5 Y6 Y12 Y13]
+ (-0.0032675138544235585) [X1 Z2 Z3 Z4 Z5 X6 X12 X13]
+ (-0.0032675138544235585) [X1 Z2 Z3 Z4 Z5 Y6 Y12 X13]
+ (-0.0027790267990255614) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7]
+ (-0.0027790267990255614) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7]
+ (-0.002686040977806598) [Y0 Z1 Z2 Z3 X4 X10 Z11 Y12]
+ (-0.002686040977806598) [X0 Z1 Z2 Z3 Y4 Y10 Z11 X12]
+ (-0.002686040977806598) [Y1 Z2 Z3 Z4 X5 X11 Z12 Y13]
+ (-0.002686040977806598) [X1 Z2 Z3 Z4 Y5 Y11 Z12 X13]
+ (-0.002293956611352466) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7]
+ (-0.002293956611352466) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7]
+ (-0.002293956611352466) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7]
+ (-0.002293956611352466) [X0 Z1 X2 X3 Z4 Z5 Z6 X7]
+ (-0.0009581655836696506) [Y0 Z1 Z2 Z3 Z4 X5 X11 Y12]
+ (-0.0009581655836696506) [Y0 Z1 Z2 Z3 Z4 Y5 Y11 Y12]
+ (-0.0009581655836696506) [X0 Z1 Z2 Z3 Z4 X5 X11 X12]
+ (-0.0009581655836696506) [X0 Z1 Z2 Z3 Z4 Y5 Y11 X12]
+ (-0.0009581655836696506) [Y1 Z2 Z3 X4 X10 Z11 Z12 Y13]
+ (-0.0009581655836696506) [Y1 Z2 Z3 Y4 Y10 Z11 Z12 Y13]
+ (-0.0009581655836696506) [X1 Z2 Z3 X4 X10 Z11 Z12 X13]
+ (-0.0009581655836696506) [X1 Z2 Z3 Y4 Y10 Z11 Z12 X13]
+ (-0.00024636437569580905) [Y5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.00024636437569580905) [X5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.00013840177303549783) [Y1 Z2 Z3 Z4 Z5 X6 X10 Y11]
+ (-0.00013840177303549783) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Y11]
+ (-0.00013840177303549783) [X1 Z2 Z3 Z4 Z5 X6 X10 X11]
+ (-0.00013840177303549783) [X1 Z2 Z3 Z4 Z5 Y6 Y10 X11]
+ (-7.73503688059091e-05) [Y0 Y1 X6 Z7 Z8 Z9 Z10 X11]
+ (-7.73503688059091e-05) [X0 X1 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585305495614e-05) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.6103585305495614e-05) [Z0 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.6103585305495614e-05) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.6103585305495614e-05) [Z1 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808795087104e-05) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.5316808795087104e-05) [Z0 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.5316808795087104e-05) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5316808795087104e-05) [Z1 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-9.806102775032995e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-9.806102775032995e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-9.806102775032995e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-9.806102775032995e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-7.089799467424675e-06) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.089799467424675e-06) [Z2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.089799467424675e-06) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.089799467424675e-06) [Z3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-6.652209669289179e-06) [Z0 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.652209669289179e-06) [Z0 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-6.652209669289179e-06) [Z1 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.652209669289179e-06) [Z1 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.481851833739379e-06) [Z0 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.481851833739379e-06) [Z0 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-6.481851833739379e-06) [Z1 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-6.481851833739379e-06) [Z1 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-5.071480736342247e-06) [Y5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-5.071480736342247e-06) [Y5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-5.071480736342247e-06) [X5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-5.071480736342247e-06) [X5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-4.734622038690748e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-4.734622038690748e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-4.734622038690748e-06) [Y5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-4.734622038690748e-06) [X5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-4.7288431471273695e-06) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-4.7288431471273695e-06) [Z2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-4.7288431471273695e-06) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.7288431471273695e-06) [Z3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.253224225550497e-06) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-4.253224225550497e-06) [Z4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.769659451902788e-06) [Z6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.769659451902788e-06) [Z6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.5443954292254646e-06) [Y2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-3.5443954292254646e-06) [Y2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-3.5443954292254646e-06) [X2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-3.5443954292254646e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-3.5443954292254646e-06) [Y3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-3.5443954292254646e-06) [Y3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-3.5443954292254646e-06) [X3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-3.5443954292254646e-06) [X3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-2.360956320297306e-06) [Y2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-2.360956320297306e-06) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-2.360956320297306e-06) [X2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-2.360956320297306e-06) [X2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-2.1032156046441625e-06) [Z2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.1032156046441625e-06) [Z2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.1032156046441625e-06) [Z3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.1032156046441625e-06) [Z3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.0111220982168214e-06) [Z2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.0111220982168214e-06) [Z2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.0111220982168214e-06) [Z3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.0111220982168214e-06) [Z3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.942946836617482e-06) [Z4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.942946836617482e-06) [Z4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.942946836617482e-06) [Z5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.942946836617482e-06) [Z5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.6541174770798392e-06) [Z4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.6541174770798392e-06) [Z4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.6541174770798392e-06) [Z5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.6541174770798392e-06) [Z5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.5224930676085792e-06) [Y2 Z3 Z4 X5 X7 Z8 Z9 Y10]
+ (-1.5224930676085792e-06) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Y10]
+ (-1.5224930676085792e-06) [X2 Z3 Z4 X5 X7 Z8 Z9 X10]
+ (-1.5224930676085792e-06) [X2 Z3 Z4 Y5 Y7 Z8 Z9 X10]
+ (-1.5224930676085792e-06) [Y3 X4 X6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930676085792e-06) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-1.5224930676085792e-06) [X3 X4 X6 Z7 Z8 Z9 Z10 X11]
+ (-1.5224930676085792e-06) [X3 Y4 Y6 Z7 Z8 Z9 Z10 X11]
+ (-1.228333782487531e-06) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (-1.228333782487531e-06) [Y4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (-1.228333782487531e-06) [X4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (-1.228333782487531e-06) [X4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (-7.988770288593438e-07) [Y2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (-7.988770288593438e-07) [X2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (-7.988770288593438e-07) [Y3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (-7.988770288593438e-07) [X3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (-7.867765104085116e-07) [Y0 X1 X5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765104085116e-07) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-7.867765104085116e-07) [X0 X1 X5 Z6 Z7 Z8 Z9 X10]
+ (-7.867765104085116e-07) [X0 Y1 Y5 Z6 Z7 Z8 Z9 X10]
+ (-7.189990975214972e-07) [Y1 Y2 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.189990975214972e-07) [X1 X2 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-6.175246207055031e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X11 X12]
+ (-6.175246207055031e-07) [X1 Z2 Z3 Z4 Z5 X6 Y11 Y12]
+ (-5.471647744574968e-07) [Y0 Z1 Z2 Y3 X10 Z11 Z12 X13]
+ (-5.471647744574968e-07) [X0 Z1 Z2 X3 Y10 Z11 Z12 Y13]
+ (-4.561447179779868e-07) [Y2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (-4.561447179779868e-07) [X2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (-4.561447179779868e-07) [Y3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (-4.561447179779868e-07) [X3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (-4.5233896777403046e-07) [Y1 Y2 X5 Z6 Z7 Z8 Z9 X10]
+ (-4.5233896777403046e-07) [X1 X2 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-3.427323108813569e-07) [Y2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (-3.427323108813569e-07) [X2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (-3.427323108813569e-07) [Y3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (-3.427323108813569e-07) [X3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (-3.3281393506431665e-07) [Y6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-3.3281393506431665e-07) [Y6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-3.3281393506431665e-07) [X6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-3.3281393506431665e-07) [X6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-3.086826565124548e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X12 X13]
+ (-3.086826565124548e-07) [X0 Z1 Z2 Z3 Z4 X5 Y12 Y13]
+ (-2.888293595376429e-07) [Y4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-2.888293595376429e-07) [Y4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-2.888293595376429e-07) [X4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.888293595376429e-07) [X4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-2.371328947878356e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X8 X9]
+ (-2.371328947878356e-07) [X0 Z1 Z2 Z3 Z4 X5 Y8 Y9]
+ (-1.839420915456096e-07) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7]
+ (-1.839420915456096e-07) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7]
+ (-8.057446595371729e-08) [Y0 Z1 Z2 Z3 Z4 X5 X10 Y11]
+ (-8.057446595371729e-08) [X0 Z1 Z2 Z3 Z4 Y5 Y10 X11]
+ (4.5371780940966876e-08) [X2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.5371780940966876e-08) [Y2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.5371780940966876e-08) [X3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (4.5371780940966876e-08) [Y3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (8.057446595371729e-08) [Y0 Z1 Z2 Z3 Z4 Y5 X10 X11]
+ (8.057446595371729e-08) [X0 Z1 Z2 Z3 Z4 X5 Y10 Y11]
+ (9.209350642734126e-08) [Y2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350642734126e-08) [Y2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (9.209350642734126e-08) [X2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (9.209350642734126e-08) [X2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.703578355497995e-07) [Y0 X1 X7 Z8 Z9 Z10 Z11 Y12]
+ (1.703578355497995e-07) [Y0 Y1 Y7 Z8 Z9 Z10 Z11 Y12]
+ (1.703578355497995e-07) [X0 X1 X7 Z8 Z9 Z10 Z11 X12]
+ (1.703578355497995e-07) [X0 Y1 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.839420915456096e-07) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7]
+ (1.839420915456096e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7]
+ (2.371328947878356e-07) [Y0 Z1 Z2 Z3 Z4 X5 X8 Y9]
+ (2.371328947878356e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y8 X9]
+ (3.086826565124548e-07) [Y0 Z1 Z2 Z3 Z4 X5 X12 Y13]
+ (3.086826565124548e-07) [X0 Z1 Z2 Z3 Z4 Y5 Y12 X13]
+ (4.5233896777403046e-07) [Y1 X2 X5 Z6 Z7 Z8 Z9 Y10]
+ (4.5233896777403046e-07) [X1 Y2 Y5 Z6 Z7 Z8 Z9 X10]
+ (5.471647744574968e-07) [Y0 Z1 Z2 X3 X10 Z11 Z12 Y13]
+ (5.471647744574968e-07) [X0 Z1 Z2 Y3 Y10 Z11 Z12 X13]
+ (6.175246207055031e-07) [Y1 Z2 Z3 Z4 Z5 X6 X11 Y12]
+ (6.175246207055031e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y11 X12]
+ (7.189990975214972e-07) [Y1 X2 X7 Z8 Z9 Z10 Z11 Y12]
+ (7.189990975214972e-07) [X1 Y2 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.3304731886531085e-06) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (1.3304731886531085e-06) [Y4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (1.3304731886531085e-06) [X4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (1.3304731886531085e-06) [X4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (1.628853243517965e-06) [Y2 Z3 X4 X6 Z7 Z8 Z9 Y10]
+ (1.628853243517965e-06) [X2 Z3 Y4 Y6 Z7 Z8 Z9 X10]
+ (1.628853243517965e-06) [Y3 Z4 X5 X7 Z8 Z9 Z10 Y11]
+ (1.628853243517965e-06) [X3 Z4 Y5 Y7 Z8 Z9 Z10 X11]
+ (1.689348951439938e-06) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (1.689348951439938e-06) [X2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (1.689348951439938e-06) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (1.689348951439938e-06) [X3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (2.745518400366121e-06) [Y2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (2.745518400366121e-06) [Y2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (2.745518400366121e-06) [X2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (2.745518400366121e-06) [X2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (2.745518400366121e-06) [Y3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (2.745518400366121e-06) [Y3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (2.745518400366121e-06) [X3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (2.745518400366121e-06) [X3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (3.2118420190485176e-06) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (3.2118420190485176e-06) [Y2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (3.2118420190485176e-06) [X2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (3.2118420190485176e-06) [X2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (3.2118420190485176e-06) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (3.2118420190485176e-06) [Y3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (3.2118420190485176e-06) [X3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (3.2118420190485176e-06) [X3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (3.313145500152663e-06) [Y6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (3.313145500152663e-06) [Y6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (3.313145500152663e-06) [X6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (3.313145500152663e-06) [X6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (3.334331289398137e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (3.334331289398137e-06) [X4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (4.183932559328526e-06) [Y6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (4.183932559328526e-06) [X6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (7.73503688059091e-05) [Y0 X1 X6 Z7 Z8 Z9 Z10 Y11]
+ (7.73503688059091e-05) [X0 Y1 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.00024636437569580905) [Y5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.00024636437569580905) [X5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.0004458535128840785) [Y0 Z1 X2 X6 Z7 Z8 Z9 Y10]
+ (0.0004458535128840785) [X0 Z1 Y2 Y6 Z7 Z8 Z9 X10]
+ (0.0004458535128840785) [Y1 Z2 X3 X7 Z8 Z9 Z10 Y11]
+ (0.0004458535128840785) [X1 Z2 Y3 Y7 Z8 Z9 Z10 X11]
+ (0.0005940221543005372) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005372) [Y0 Z1 Y2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005372) [X0 Z1 X2 Y7 Z8 Z9 Z10 Y11]
+ (0.0005940221543005372) [X0 Z1 X2 X7 Z8 Z9 Z10 X11]
+ (0.0005940221543005372) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005372) [Y1 Z2 Y3 X6 Z7 Z8 Z9 X10]
+ (0.0005940221543005372) [X1 Z2 X3 Y6 Z7 Z8 Z9 Y10]
+ (0.0005940221543005372) [X1 Z2 X3 X6 Z7 Z8 Z9 X10]
+ (0.000853385625412549) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7]
+ (0.000853385625412549) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7]
+ (0.000853385625412549) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7]
+ (0.000853385625412549) [X0 Z1 Z2 Z3 X4 X5 Z6 X7]
+ (0.0010435246534907484) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z13]
+ (0.0010435246534907484) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z13]
+ (0.0010435246534907484) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z12]
+ (0.0010435246534907484) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z12]
+ (0.0012803060973496626) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z9]
+ (0.0012803060973496626) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z9]
+ (0.0012803060973496626) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z8]
+ (0.0012803060973496626) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z8]
+ (0.0013038004788126951) [Y0 Z1 Z2 Z3 Y4 Y10 Z11 Y12]
+ (0.0013038004788126951) [X0 Z1 Z2 Z3 X4 X10 Z11 X12]
+ (0.0013038004788126951) [Y1 Z2 Z3 Z4 Y5 Y11 Z12 Y13]
+ (0.0013038004788126951) [X1 Z2 Z3 Z4 X5 X11 Z12 X13]
+ (0.0022619660624823455) [Y0 Z1 Z2 Z3 Y4 Y11 Z12 Y13]
+ (0.0022619660624823455) [Y0 Z1 Z2 Z3 Y4 X11 Z12 X13]
+ (0.0022619660624823455) [X0 Z1 Z2 Z3 X4 Y11 Z12 Y13]
+ (0.0022619660624823455) [X0 Z1 Z2 Z3 X4 X11 Z12 X13]
+ (0.0022619660624823455) [Y1 Z2 Z3 Z4 Y5 Y10 Z11 Y12]
+ (0.0022619660624823455) [Y1 Z2 Z3 Z4 Y5 X10 Z11 X12]
+ (0.0022619660624823455) [X1 Z2 Z3 Z4 X5 Y10 Z11 Y12]
+ (0.0022619660624823455) [X1 Z2 Z3 Z4 X5 X10 Z11 X12]
+ (0.003989841456619293) [Y0 Z1 Z2 Z3 Y4 X10 Z11 X12]
+ (0.003989841456619293) [X0 Z1 Z2 Z3 X4 Y10 Z11 Y12]
+ (0.003989841456619293) [Y1 Z2 Z3 Z4 Y5 X11 Z12 X13]
+ (0.003989841456619293) [X1 Z2 Z3 Z4 X5 Y11 Z12 Y13]
+ (0.004158797381840081) [Y2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.004158797381840081) [X2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.0043110385079143075) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z12]
+ (0.0043110385079143075) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z12]
+ (0.0043110385079143075) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z13]
+ (0.0043110385079143075) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z13]
+ (0.004636976661182559) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z8]
+ (0.004636976661182559) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z8]
+ (0.004636976661182559) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z9]
+ (0.004636976661182559) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z9]
+ (0.00511447383166038) [Y0 Z1 Z2 X3 X7 Z8 Z9 Y10]
+ (0.00511447383166038) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Y10]
+ (0.00511447383166038) [X0 Z1 Z2 X3 X7 Z8 Z9 X10]
+ (0.00511447383166038) [X0 Z1 Z2 Y3 Y7 Z8 Z9 X10]
+ (0.00511447383166038) [Y1 X2 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.00511447383166038) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.00511447383166038) [X1 X2 X6 Z7 Z8 Z9 Z10 X11]
+ (0.00511447383166038) [X1 Y2 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.0052415353828038705) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z11]
+ (0.0052415353828038705) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z11]
+ (0.0052415353828038705) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z10]
+ (0.0052415353828038705) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z10]
+ (0.0052626424730768395) [Y0 Z1 Y2 X6 Z7 Z8 Z9 X10]
+ (0.0052626424730768395) [X0 Z1 X2 Y6 Z7 Z8 Z9 Y10]
+ (0.0052626424730768395) [Y1 Z2 Y3 X7 Z8 Z9 Z10 X11]
+ (0.0052626424730768395) [X1 Z2 X3 Y7 Z8 Z9 Z10 Y11]
+ (0.005368659358109524) [Y2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.005368659358109524) [X2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.005379937155839369) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z10]
+ (0.005379937155839369) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z10]
+ (0.005379937155839369) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Z11]
+ (0.005379937155839369) [X1 Z2 Z3 Z4 Z5 Z6 X7 Z11]
+ (0.005652620978017351) [Y0 X1 X2 Z3 Z4 Z5 Z6 Y7]
+ (0.005652620978017351) [X0 Y1 Y2 Z3 Z4 Z5 Z6 X7]
+ (0.005708495985960918) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Y10]
+ (0.005708495985960918) [X0 Z1 X2 X6 Z7 Z8 Z9 X10]
+ (0.005708495985960918) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Y11]
+ (0.005708495985960918) [X1 Z2 X3 X7 Z8 Z9 Z10 X11]
+ (0.005923798336561346) [Y5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (0.005923798336561346) [X5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (0.007306759928832993) [Y4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (0.007306759928832993) [X4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (0.009841749246962656) [Y3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (0.009841749246962656) [X3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (0.01128519020084091) [Y4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (0.01128519020084091) [X4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (0.01175601341981928) [Y2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.01175601341981928) [X2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.014564531231172961) [Y6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.014564531231172961) [X6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.014603704729162118) [Y3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.014603704729162118) [X3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.015225630757226587) [Y2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (0.015225630757226587) [X2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (0.016024603689179545) [Y5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (0.016024603689179545) [X5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (0.019028242443847296) [Y2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (0.019028242443847296) [X2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (0.019257505095251592) [Y3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.019257505095251592) [X3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.04587947078129807) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (0.04587947078129807) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-0.3693708936615625) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.3693708936615625) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.3693708936615625) [Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.3693708936615625) [X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.2816425776702292) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.2816425776702292) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.2816425776702291) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.2816425776702291) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.09065144207036473) [Z0 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.09065144207036473) [Z0 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.09065144207036473) [Z1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.09065144207036473) [Z1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0868473758986362) [Z0 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0868473758986362) [Z0 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0868473758986362) [Z1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0868473758986362) [Z1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.07635021950635015) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.07635021950635015) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.07635021950635015) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.07635021950635015) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214031) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.06752385099214031) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.06752385099214031) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.06752385099214031) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03560837898831262) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.03560837898831262) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.03490334337366175) [Z2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.03490334337366175) [Z2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.03490334337366175) [Z3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.03490334337366175) [Z3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.024591860883829954) [Z2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.024591860883829954) [Z2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.024591860883829954) [Z3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.024591860883829954) [Z3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.024282117354693062) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.024282117354693062) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.02314513092952915) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (-0.02314513092952915) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (-0.02252844019601294) [Z4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.02252844019601294) [Z4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.01953805031131477) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (-0.01953805031131477) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (-0.01953805031131477) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (-0.01953805031131477) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (-0.017091553155898928) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (-0.017091553155898928) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (-0.017091553155898928) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (-0.017091553155898928) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (-0.016024603689179545) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-0.016024603689179545) [Y4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-0.016024603689179545) [X4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-0.016024603689179545) [X4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-0.010311482489831792) [Y2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.010311482489831792) [Y2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.010311482489831792) [X2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.010311482489831792) [X2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.009841749246962656) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962656) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.009841749246962656) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.009841749246962656) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209834) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209834) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.008826368514209834) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008826368514209834) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.008541996625454833) [Y2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454833) [Y2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.008541996625454833) [X2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454833) [X2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.008541996625454833) [Y3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454833) [Y3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008541996625454833) [X3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.008541996625454833) [X3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.004668620318776302) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Y11]
+ (-0.004668620318776302) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 X11]
+ (-0.0038764708993369477) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 X10]
+ (-0.0038764708993369477) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Y10]
+ (-0.0038040661717285355) [Y0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0038040661717285355) [Y0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0038040661717285355) [X0 X1 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0038040661717285355) [X0 Y1 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.003484157300217881) [Y1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.003484157300217881) [X1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0033566705638328966) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X8 X9]
+ (-0.0033566705638328966) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y8 Y9]
+ (-0.0032675138544235593) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X12 X13]
+ (-0.0032675138544235593) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y12 Y13]
+ (-0.002141361223101616) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y11]
+ (-0.002141361223101616) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X11]
+ (-0.0017278753941369484) [Y0 Z1 Z2 Z3 Z4 X5 X10 Z11 Z12 Y13]
+ (-0.0017278753941369484) [X0 Z1 Z2 Z3 Z4 Y5 Y10 Z11 Z12 X13]
+ (-0.0016407548553124041) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0016407548553124041) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0014528843214169445) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0014528843214169445) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-0.0014528843214169445) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0014528843214169445) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0007870896771024433) [Y1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 X10]
+ (-0.0007870896771024433) [X1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-0.0005192743499487676) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 X10]
+ (-0.0005192743499487676) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Y10]
+ (-0.00019400857029756562) [Y1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.00019400857029756562) [X1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.00013840177303549783) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 X11]
+ (-0.00013840177303549783) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Y11]
+ (-7.141625221158707e-05) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Y10]
+ (-7.141625221158707e-05) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 X10]
+ (-7.141625221158707e-05) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.141625221158707e-05) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-5.071480736342247e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-5.071480736342247e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-3.151346311126544e-06) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 X11]
+ (-3.151346311126544e-06) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Y11]
+ (-3.088250711247478e-06) [Y2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-3.088250711247478e-06) [X2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-2.988511706329663e-06) [Y3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.988511706329663e-06) [X3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.874299071349054e-06) [Y3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-2.874299071349054e-06) [X3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-2.360956320297306e-06) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-2.360956320297306e-06) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.3002946562341135e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Y12]
+ (-1.3002946562341135e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 X12]
+ (-1.1468376507262833e-06) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-1.1468376507262833e-06) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-1.1468376507262833e-06) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-1.1468376507262833e-06) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.35233210283542e-07) [Y0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.35233210283542e-07) [X0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.35233210283542e-07) [Y1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.35233210283542e-07) [X1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.091637198851759e-07) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637198851759e-07) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Y10]
+ (-8.091637198851759e-07) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637198851759e-07) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 X10]
+ (-8.091637198851759e-07) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637198851759e-07) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-8.091637198851759e-07) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.091637198851759e-07) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-8.074305985689017e-07) [Y0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.074305985689017e-07) [X0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.074305985689017e-07) [Y1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.074305985689017e-07) [X1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.900128986151376e-07) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-7.900128986151376e-07) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-7.900128986151376e-07) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.900128986151376e-07) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.867765104085116e-07) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-7.867765104085116e-07) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-7.560692464745365e-07) [Y0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692464745365e-07) [Y0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-7.560692464745365e-07) [X0 Z1 Z2 X3 X7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692464745365e-07) [X0 Z1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 X12]
+ (-7.560692464745365e-07) [Y1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692464745365e-07) [Y1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-7.560692464745365e-07) [X1 X2 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.560692464745365e-07) [X1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-4.997018422045016e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 Y12]
+ (-4.997018422045016e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Y12]
+ (-4.997018422045016e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X11 X12]
+ (-4.997018422045016e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 X12]
+ (-4.997018422045016e-07) [Y1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 Y13]
+ (-4.997018422045016e-07) [Y1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 Y13]
+ (-4.997018422045016e-07) [X1 Z2 Z3 Z4 Z5 X6 X10 Z11 Z12 X13]
+ (-4.997018422045016e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Z12 X13]
+ (-3.568247521111455e-07) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.568247521111455e-07) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.568247521111455e-07) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.568247521111455e-07) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393084110715e-07) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393084110715e-07) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393084110715e-07) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.3767393084110715e-07) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-3.3767393084110715e-07) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393084110715e-07) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-3.3767393084110715e-07) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (-3.3767393084110715e-07) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 X10]
+ (-2.888293595376429e-07) [Y4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-2.888293595376429e-07) [X4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.686381544946514e-07) [Y3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (-2.686381544946514e-07) [X3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-1.7035783554979954e-07) [Y0 X1 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.7035783554979954e-07) [X0 Y1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-9.209350642734126e-08) [Y2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.209350642734126e-08) [X2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773242820493e-08) [Y0 Z1 Y2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773242820493e-08) [Y0 Z1 Y2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773242820493e-08) [X0 Z1 X2 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.379773242820493e-08) [X0 Z1 X2 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.379773242820493e-08) [Y1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773242820493e-08) [Y1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-8.379773242820493e-08) [X1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-8.379773242820493e-08) [X1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9742253791557355e-08) [X0 Z1 Y2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-1.9742253791557355e-08) [Y0 Z1 X2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.9742253791557355e-08) [X1 Z2 Y3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.9742253791557355e-08) [Y1 Z2 X3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0474716553895512e-08) [Y0 Z1 X2 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.0474716553895512e-08) [X0 Z1 Y2 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.0474716553895512e-08) [Y1 Z2 X3 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.0474716553895512e-08) [X1 Z2 Y3 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (9.209350642734126e-08) [Y2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (9.209350642734126e-08) [X2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.0717282183089337e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X10 Z11 X12]
+ (1.0717282183089337e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y10 Z11 Y12]
+ (1.0717282183089337e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X11 Z12 X13]
+ (1.0717282183089337e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y11 Z12 Y13]
+ (1.2004287494097354e-07) [X0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 X12]
+ (1.2004287494097354e-07) [Y0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 Y12]
+ (1.2004287494097354e-07) [X1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 X13]
+ (1.2004287494097354e-07) [Y1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 Y13]
+ (1.7035783554979954e-07) [Y0 Y1 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.7035783554979954e-07) [X0 X1 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.3120943052321452e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X10 Z11 X12]
+ (2.3120943052321452e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y10 Z11 Y12]
+ (2.3120943052321452e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X11 Z12 X13]
+ (2.3120943052321452e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y11 Z12 Y13]
+ (2.686381544946514e-07) [Y3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (2.686381544946514e-07) [X3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (2.888293595376429e-07) [Y4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.888293595376429e-07) [X4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.0922506160438813e-07) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Y11]
+ (4.0922506160438813e-07) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 X11]
+ (4.0922506160438813e-07) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Y11]
+ (4.0922506160438813e-07) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 X11]
+ (4.0922506160438813e-07) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Y10]
+ (4.0922506160438813e-07) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 X10]
+ (4.0922506160438813e-07) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Y10]
+ (4.0922506160438813e-07) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 X10]
+ (4.4445978540877277e-07) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Y10]
+ (4.4445978540877277e-07) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 X10]
+ (4.4445978540877277e-07) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Y11]
+ (4.4445978540877277e-07) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 X11]
+ (4.6849150951266256e-07) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 X10]
+ (4.6849150951266256e-07) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Y10]
+ (4.6849150951266256e-07) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 X11]
+ (4.6849150951266256e-07) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Y11]
+ (7.246974425363964e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y11 Z12 Y13]
+ (7.246974425363964e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X11 Z12 X13]
+ (7.246974425363964e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y11 Z12 Y13]
+ (7.246974425363964e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X11 Z12 X13]
+ (7.246974425363964e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Y12]
+ (7.246974425363964e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 X12]
+ (7.246974425363964e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Y12]
+ (7.246974425363964e-07) [X1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 X12]
+ (7.867765104085116e-07) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (7.867765104085116e-07) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (1.3002946562341135e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 X12]
+ (1.3002946562341135e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Y12]
+ (2.360956320297306e-06) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (2.360956320297306e-06) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (2.874299071349054e-06) [Y3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (2.874299071349054e-06) [X3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (2.883676576043658e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (2.883676576043658e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (2.947356011672761e-06) [Y2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.947356011672761e-06) [X2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.947356011672761e-06) [Y3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.947356011672761e-06) [X3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.988511706329663e-06) [Y3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (2.988511706329663e-06) [X3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (3.088250711247478e-06) [Y2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (3.088250711247478e-06) [X2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (3.151346311126544e-06) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Y11]
+ (3.151346311126544e-06) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 X11]
+ (3.846201671227249e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (3.846201671227249e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (3.846201671227249e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (3.846201671227249e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (5.071480736342247e-06) [Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (5.071480736342247e-06) [X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (5.105526721906978e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (5.105526721906978e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (5.105526721906978e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (5.105526721906978e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (5.146496327461363e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (5.146496327461363e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (5.146496327461363e-06) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (5.146496327461363e-06) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (5.1593505018600095e-06) [Y2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (5.1593505018600095e-06) [X2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (5.1593505018600095e-06) [Y3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.1593505018600095e-06) [X3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.427988656354662e-06) [Y2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.427988656354662e-06) [X2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.427988656354662e-06) [Y3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.427988656354662e-06) [X3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.935867718002424e-06) [Y2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.935867718002424e-06) [X2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (5.935867718002424e-06) [Y3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.935867718002424e-06) [X3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.2532733479729966e-06) [Y2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (7.2532733479729966e-06) [X2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (7.979825793256031e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (7.979825793256031e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (7.979825793256031e-06) [Y3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (7.979825793256031e-06) [X3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (4.205548411218918e-05) [Y2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.205548411218918e-05) [X2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.205548411218918e-05) [Y3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (4.205548411218918e-05) [X3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00013840177303549783) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Y11]
+ (0.00013840177303549783) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 X11]
+ (0.00018787053389545983) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.00018787053389545983) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.00018787053389545983) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.00018787053389545983) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.00019400857029756562) [Y1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Y12]
+ (0.00019400857029756562) [X1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 X12]
+ (0.000246364375695809) [Y4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.000246364375695809) [Y4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.000246364375695809) [X4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.000246364375695809) [X4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0005192743499487676) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Y10]
+ (0.0005192743499487676) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 X10]
+ (0.0007156734248908563) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007156734248908563) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0007156734248908563) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007156734248908563) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024433) [Y1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Y10]
+ (0.0007870896771024433) [X1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 X10]
+ (0.0015324835230730025) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Y10]
+ (0.0015324835230730025) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 X10]
+ (0.0015324835230730025) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Y11]
+ (0.0015324835230730025) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 X11]
+ (0.0016407548553124041) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.0016407548553124041) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.0017278753941369484) [Y0 Z1 Z2 Z3 Z4 Y5 X10 Z11 Z12 X13]
+ (0.0017278753941369484) [X0 Z1 Z2 Z3 Z4 X5 Y10 Z11 Z12 Y13]
+ (0.002446497155415841) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (0.002446497155415841) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (0.002446497155415841) [X3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (0.002446497155415841) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (0.0032675138544235593) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X12 Y13]
+ (0.0032675138544235593) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y12 X13]
+ (0.0033566705638328966) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X8 Y9]
+ (0.0033566705638328966) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y8 X9]
+ (0.003484157300217881) [Y1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.003484157300217881) [X1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0038764708993369477) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Y10]
+ (0.0038764708993369477) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 X10]
+ (0.004668620318776302) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 X11]
+ (0.004668620318776302) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Y11]
+ (0.004767272188278092) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Y10]
+ (0.004767272188278092) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 X10]
+ (0.004767272188278092) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Y11]
+ (0.004767272188278092) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 X11]
+ (0.0052865465382268585) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Y10]
+ (0.0052865465382268585) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 X10]
+ (0.0052865465382268585) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Y11]
+ (0.0052865465382268585) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 X11]
+ (0.005408954422409951) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Y10]
+ (0.005408954422409951) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 X10]
+ (0.005408954422409951) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Y11]
+ (0.005408954422409951) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 X11]
+ (0.005923798336561346) [Y4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561346) [Y4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (0.005923798336561346) [X4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (0.005923798336561346) [X4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (0.010715508469796757) [Y2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.010715508469796757) [X2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.010715508469796757) [Y3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010715508469796757) [X3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.010757563953908946) [Y2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.010757563953908946) [X2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.010757563953908946) [Y3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010757563953908946) [X3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.014603704729162118) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.014603704729162118) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.014603704729162118) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.014603704729162118) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.01929956057936378) [Y2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01929956057936378) [Y2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.01929956057936378) [X2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.01929956057936378) [X2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.01929956057936378) [Y3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.01929956057936378) [Y3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.01929956057936378) [X3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.01929956057936378) [X3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.05859198873386176) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.05859198873386176) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (5.775950527186713e-05) [Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (5.775950527186713e-05) [X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (5.7759505271867146e-05) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (5.7759505271867146e-05) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.07165035181002492) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10]
+ (0.07165035181002492) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10]
+ (0.07165035181002492) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.07165035181002492) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.019257505095251592) [Y2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.019257505095251592) [X2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.010311482489831792) [Y2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.010311482489831792) [X2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.008826368514209836) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.008826368514209836) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.007597464029770597) [Y0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.007597464029770597) [X0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.007597464029770597) [Y1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.007597464029770597) [X1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311873) [Y0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311873) [Y0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005733569747311873) [X0 Z1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311873) [X0 Z1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005733569747311873) [Y1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311873) [Y1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.005733569747311873) [X1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005733569747311873) [X1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005348051582676605) [Y0 Z1 Y2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.005348051582676605) [X0 Z1 X2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.005348051582676605) [Y1 Z2 Y3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.005348051582676605) [X1 Z2 X3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0038040661717285355) [Y0 Y1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0038040661717285355) [X0 X1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0029841661681219355) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 Y13]
+ (-0.0029841661681219355) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 Y13]
+ (-0.0029841661681219355) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X12 X13]
+ (-0.0029841661681219355) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y12 X13]
+ (-0.0024464971554158405) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (-0.0024464971554158405) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (-0.0022494124470939913) [Y0 Z1 X2 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0022494124470939913) [X0 Z1 Y2 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0022494124470939913) [Y1 Z2 X3 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0022494124470939913) [X1 Z2 Y3 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.002141361223101616) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z11]
+ (-0.002141361223101616) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z11]
+ (-0.0018638942824587249) [Y0 Z1 Y2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0018638942824587249) [Y0 Z1 Y2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0018638942824587249) [X0 Z1 X2 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0018638942824587249) [X0 Z1 X2 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0018638942824587249) [Y1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0018638942824587249) [Y1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0018638942824587249) [X1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0018638942824587249) [X1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0016407548553124041) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0016407548553124041) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0016407548553124041) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-0.0016407548553124041) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-0.0012223378081538366) [Y0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538366) [Y0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0012223378081538366) [X0 Z1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538366) [X0 Z1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 X12]
+ (-0.0012223378081538366) [Y1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538366) [Y1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0012223378081538366) [X1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0012223378081538366) [X1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.0010283292378562708) [Y0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-0.0010283292378562708) [X0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.0010283292378562708) [Y1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0010283292378562708) [X1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.1463061452937545e-05) [Y0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.1463061452937545e-05) [X0 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.8742990713490545e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-2.8742990713490545e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-2.8742990713490545e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-2.8742990713490545e-06) [X2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.3002946562341135e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Y11 Z12 Y13]
+ (-1.3002946562341135e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 X11 Z12 X13]
+ (-1.3002946562341135e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Y11 Z12 Y13]
+ (-1.3002946562341135e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 X11 Z12 X13]
+ (-1.0444941297899426e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Y12]
+ (-1.0444941297899426e-06) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 X12]
+ (-1.0444941297899426e-06) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 Y13]
+ (-1.0444941297899426e-06) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Z12 X13]
+ (-9.956079229830224e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-9.956079229830224e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 X12]
+ (-9.956079229830224e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-9.956079229830224e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Z12 X13]
+ (-8.105515036978925e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 Y12]
+ (-8.105515036978925e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z8 Z9 Z10 Z11 X12]
+ (-8.105515036978925e-07) [Y1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-8.105515036978925e-07) [X1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.661347212896294e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Y12]
+ (-7.661347212896294e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 X12]
+ (-7.661347212896294e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 Y13]
+ (-7.661347212896294e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z12 X13]
+ (-7.540341413625508e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Y12]
+ (-7.540341413625508e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 X12]
+ (-7.189990975214972e-07) [Y0 Z1 Z2 Y3 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.189990975214972e-07) [X0 Z1 Z2 X3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-6.87662165809068e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y12]
+ (-6.87662165809068e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X12]
+ (-6.87662165809068e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 Y13]
+ (-6.87662165809068e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z11 Z12 X13]
+ (-6.175246207055031e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 X10 Z11 Z12 X13]
+ (-6.175246207055031e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 X7 Y10 Z11 Z12 Y13]
+ (-4.5233896777403046e-07) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-4.5233896777403046e-07) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (-3.076732531820912e-07) [Y0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-3.076732531820912e-07) [X0 Z1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.076732531820912e-07) [Y1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-3.076732531820912e-07) [X1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-3.013471458941422e-07) [Y1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-3.013471458941422e-07) [X1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.904599884273918e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 Y12]
+ (-2.904599884273918e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z10 Z11 X12]
+ (-2.904599884273918e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 Y13]
+ (-2.904599884273918e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z9 Z10 Z11 Z12 X13]
+ (-2.6667317545507827e-07) [Y0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-2.6667317545507827e-07) [X0 Z1 Z2 Z3 Z4 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-2.6667317545507827e-07) [Y1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-2.6667317545507827e-07) [X1 Z2 Z3 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.8505641928513003e-07) [Y1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Y12]
+ (-1.8505641928513003e-07) [X1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309314436787e-07) [Y0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.6569309314436787e-07) [X0 Z1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.6569309314436787e-07) [Y1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.6569309314436787e-07) [X1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.8505641928513003e-07) [Y1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 X12]
+ (1.8505641928513003e-07) [X1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Y12]
+ (2.686381544946514e-07) [Y2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.686381544946514e-07) [Y2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.686381544946514e-07) [X2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.686381544946514e-07) [X2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.013471458941422e-07) [Y1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (3.013471458941422e-07) [X1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.5233896777403046e-07) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (4.5233896777403046e-07) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (4.670402390385101e-07) [Y0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (4.670402390385101e-07) [X0 Z1 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (4.670402390385101e-07) [Y1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (4.670402390385101e-07) [X1 Z2 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (6.175246207055031e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 X7 X10 Z11 Z12 Y13]
+ (6.175246207055031e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Y7 Y10 Z11 Z12 X13]
+ (7.189990975214972e-07) [Y0 Z1 Z2 X3 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.189990975214972e-07) [X0 Z1 Z2 Y3 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.540341413625508e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 X12]
+ (7.540341413625508e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Y12]
+ (8.94947648727113e-07) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y13]
+ (8.94947648727113e-07) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X13]
+ (1.7924939576783897e-06) [Y0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.7924939576783897e-06) [Y0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.7924939576783897e-06) [X0 X1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.7924939576783897e-06) [X0 Y1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (2.8836765760436584e-06) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (2.8836765760436584e-06) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (2.988511706329663e-06) [Y2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.988511706329663e-06) [Y2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (2.988511706329663e-06) [X2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (2.988511706329663e-06) [X2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (7.2532733479729966e-06) [Z2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (7.2532733479729966e-06) [Z2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.4017109735002228e-05) [Z0 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.4017109735002228e-05) [Z0 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (1.4017109735002228e-05) [Z1 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.4017109735002228e-05) [Z1 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.5809603692680617e-05) [Z0 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (1.5809603692680617e-05) [Z0 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.5809603692680617e-05) [Z1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (1.5809603692680617e-05) [Z1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0005192743499487676) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Y11]
+ (0.0005192743499487676) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 X11]
+ (0.0005192743499487676) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Y11]
+ (0.0005192743499487676) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 X11]
+ (0.0007870896771024433) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024433) [Y0 Z1 Z2 Z3 Y4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0007870896771024433) [X0 Z1 Z2 Z3 X4 Y5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.0007870896771024433) [X0 Z1 Z2 Z3 X4 X5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.0011726348316441863) [Y0 Z1 Z2 Z3 Y4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0011726348316441863) [X0 Z1 Z2 Z3 X4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0011726348316441863) [Y1 Z2 Z3 Z4 Y5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0011726348316441863) [X1 Z2 Z3 Z4 X5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.001236647801924506) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z13]
+ (0.001236647801924506) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z13]
+ (0.001236647801924506) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z12]
+ (0.001236647801924506) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z12]
+ (0.0022009640695004576) [Y0 Z1 Z2 Z3 Y4 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0022009640695004576) [X0 Z1 Z2 Z3 X4 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.0022009640695004576) [Y1 Z2 Z3 Z4 Y5 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0022009640695004576) [X1 Z2 Z3 Z4 X5 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798023) [Y0 Z1 Z2 Z3 Y4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798023) [Y0 Z1 Z2 Z3 Y4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002394972639798023) [X0 Z1 Z2 Z3 X4 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.002394972639798023) [X0 Z1 Z2 Z3 X4 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.002394972639798023) [Y1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002394972639798023) [Y1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.002394972639798023) [X1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (0.002394972639798023) [X1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 X12]
+ (0.0024464971554158405) [Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (0.0024464971554158405) [X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (0.0038040661717285355) [Y0 X1 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.0038040661717285355) [X0 Y1 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0038764708993369477) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Y11]
+ (0.0038764708993369477) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 X11]
+ (0.0038764708993369477) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Y11]
+ (0.0038764708993369477) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 X11]
+ (0.004220813970046441) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Y10 Z12]
+ (0.004220813970046441) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 X10 Z12]
+ (0.004220813970046441) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Z13]
+ (0.004220813970046441) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Z13]
+ (0.008826368514209836) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.008826368514209836) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (0.010311482489831792) [Y2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.010311482489831792) [X2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.019257505095251592) [Y2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.019257505095251592) [X2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.05859198873386176) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11]
+ (0.05859198873386176) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11]
+ (-1.3987009015661437e-05) [Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.3987009015661437e-05) [X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.3987009015661434e-05) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12]
+ (-1.3987009015661434e-05) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12]
+ (-0.003484157300217881) [Y0 Z1 Z2 Y3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.003484157300217881) [X0 Z1 Z2 X3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-0.0029841661681219355) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 X12 X13]
+ (-0.0029841661681219355) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 Y12 Y13]
+ (-0.00019400857029756562) [Y0 Z1 Z2 Z3 Z4 Y5 X6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-0.00019400857029756562) [X0 Z1 Z2 Z3 Z4 X5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061452937547e-05) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.1463061452937547e-05) [Z0 X1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.7924939576783897e-06) [Y0 X1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.7924939576783897e-06) [X0 Y1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-7.540341413625509e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413625509e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Y8 X9 Z10 Z11 Z12 X13]
+ (-7.540341413625509e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 Y9 Z10 Z11 Z12 Y13]
+ (-7.540341413625509e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 X8 X9 Z10 Z11 Z12 X13]
+ (-1.8505641928513003e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.8505641928513003e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (-1.8505641928513003e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 Y7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (-1.8505641928513003e-07) [X0 Z1 Z2 Z3 Z4 Z5 X6 X7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.013471458941422e-07) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.013471458941422e-07) [Y0 Z1 Y2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (3.013471458941422e-07) [X0 Z1 X2 Y3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (3.013471458941422e-07) [X0 Z1 X2 X3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (8.94947648727113e-07) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Y12 Z13]
+ (8.94947648727113e-07) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 X12 Z13]
+ (1.7924939576783897e-06) [Y0 Y1 X2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (1.7924939576783897e-06) [X0 X1 Y2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756562) [Y0 Z1 Z2 Z3 Z4 X5 X6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.00019400857029756562) [X0 Z1 Z2 Z3 Z4 Y5 Y6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
+ (0.0029841661681219355) [Y0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 X11 X12 Y13]
+ (0.0029841661681219355) [X0 Z1 Z2 Z3 Z4 Z5 Z6 Z7 Z8 Z9 Z10 Y11 Y12 X13]
+ (0.003484157300217881) [Y0 Z1 Z2 X3 X4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 Y13]
+ (0.003484157300217881) [X0 Z1 Z2 Y3 Y4 Z5 Z6 Z7 Z8 Z9 Z10 Z11 Z12 X13]
  (-73.1387323135253) [I0]
+ (-0.1806679265658331) [Z7]
+ (-0.18066792656583303) [Z6]
+ (-0.1596143250181005) [Z5]
+ (-0.15961432501810047) [Z4]
+ (0.17419956155055763) [Z2]
+ (0.17419956155055796) [Z3]
+ (0.22757269005453437) [Z1]
+ (0.22757269005453457) [Z0]
+ (-8.194261371867471e-06) [Y4 Y6]
+ (-8.194261371867471e-06) [X4 X6]
+ (7.954413175959008e-06) [Y5 Y7]
+ (7.954413175959008e-06) [X5 X7]
+ (0.11270386920332241) [Z4 Z6]
+ (0.11270386920332241) [Z5 Z7]
+ (0.11952438964682688) [Z0 Z4]
+ (0.11952438964682688) [Z1 Z5]
+ (0.13401715261963718) [Z0 Z6]
+ (0.13401715261963718) [Z1 Z7]
+ (0.13734953064261335) [Z0 Z5]
+ (0.13734953064261335) [Z1 Z4]
+ (0.13766872645852593) [Z2 Z4]
+ (0.13766872645852593) [Z3 Z5]
+ (0.14138905291942827) [Z4 Z7]
+ (0.14138905291942827) [Z5 Z6]
+ (0.14722943218766193) [Z2 Z5]
+ (0.14722943218766193) [Z3 Z4]
+ (0.1492635514738893) [Z4 Z5]
+ (0.1497348680349694) [Z2 Z6]
+ (0.1497348680349694) [Z3 Z7]
+ (0.15138327161428855) [Z0 Z7]
+ (0.15138327161428855) [Z1 Z6]
+ (0.15435748657223647) [Z6 Z7]
+ (0.1558226905155313) [Z2 Z7]
+ (0.1558226905155313) [Z3 Z6]
+ (0.1675665326546128) [Z0 Z2]
+ (0.1675665326546128) [Z1 Z3]
+ (0.18143991440303892) [Z0 Z3]
+ (0.18143991440303892) [Z1 Z2]
+ (0.19392534613270218) [Z0 Z1]
+ (0.22003977334376112) [Z2 Z3]
+ (-7.037887511148907e-06) [Y4 Z5 Y6]
+ (-7.037887511148907e-06) [X4 Z5 X6]
+ (-7.037887511148903e-06) [Y5 Z6 Y7]
+ (-7.037887511148903e-06) [X5 Z6 X7]
+ (-0.028685183716105876) [Y4 Y5 X6 X7]
+ (-0.028685183716105876) [X4 X5 Y6 Y7]
+ (-0.017825140995786467) [Y0 Y1 X4 X5]
+ (-0.017825140995786467) [X0 X1 Y4 Y5]
+ (-0.017366118994651413) [Y0 Y1 X6 X7]
+ (-0.017366118994651413) [X0 X1 Y6 Y7]
+ (-0.013873381748426143) [Y0 Y1 X2 X3]
+ (-0.013873381748426143) [X0 X1 Y2 Y3]
+ (-0.009560705729135975) [Y2 Y3 X4 X5]
+ (-0.009560705729135975) [X2 X3 Y4 Y5]
+ (-0.0060878224805618695) [Y2 Y3 X6 X7]
+ (-0.0060878224805618695) [X2 X3 Y6 Y7]
+ (-0.0002921986261110821) [Y1 Y2 X3 X4]
+ (-0.0002921986261110821) [X1 X2 Y3 Y4]
+ (-8.194261371867471e-06) [Z4 Y5 Z6 Y7]
+ (-8.194261371867471e-06) [Z4 X5 Z6 X7]
+ (-2.890967881595839e-06) [Z0 Y5 Z6 Y7]
+ (-2.890967881595839e-06) [Z0 X5 Z6 X7]
+ (-2.890967881595839e-06) [Z1 Y4 Z5 Y6]
+ (-2.890967881595839e-06) [Z1 X4 Z5 X6]
+ (-1.8551201214532934e-06) [Z0 Y4 Z5 Y6]
+ (-1.8551201214532934e-06) [Z0 X4 Z5 X6]
+ (-1.8551201214532934e-06) [Z1 Y5 Z6 Y7]
+ (-1.8551201214532934e-06) [Z1 X5 Z6 X7]
+ (-1.5973171977374321e-06) [Z2 Y4 Z5 Y6]
+ (-1.5973171977374321e-06) [Z2 X4 Z5 X6]
+ (-1.5973171977374321e-06) [Z3 Y5 Z6 Y7]
+ (-1.5973171977374321e-06) [Z3 X5 Z6 X7]
+ (-1.0358477601425463e-06) [Y0 X1 X5 Y6]
+ (-1.0358477601425463e-06) [Y0 Y1 Y5 Y6]
+ (-1.0358477601425463e-06) [X0 X1 X5 X6]
+ (-1.0358477601425463e-06) [X0 Y1 Y5 X6]
+ (-9.344557775919814e-07) [Z2 Y5 Z6 Y7]
+ (-9.344557775919814e-07) [Z2 X5 Z6 X7]
+ (-9.344557775919814e-07) [Z3 Y4 Z5 Y6]
+ (-9.344557775919814e-07) [Z3 X4 Z5 X6]
+ (6.628614201454511e-07) [Y2 X3 X5 Y6]
+ (6.628614201454511e-07) [Y2 Y3 Y5 Y6]
+ (6.628614201454511e-07) [X2 X3 X5 X6]
+ (6.628614201454511e-07) [X2 Y3 Y5 X6]
+ (7.954413175959008e-06) [Y4 Z5 Y6 Z7]
+ (7.954413175959008e-06) [X4 Z5 X6 Z7]
+ (0.0002921986261110821) [Y1 X2 X3 Y4]
+ (0.0002921986261110821) [X1 Y2 Y3 X4]
+ (0.0060878224805618695) [Y2 X3 X6 Y7]
+ (0.0060878224805618695) [X2 Y3 Y6 X7]
+ (0.009560705729135975) [Y2 X3 X4 Y5]
+ (0.009560705729135975) [X2 Y3 Y4 X5]
+ (0.011307274008848206) [Y1 Z2 Z3 Y5]
+ (0.011307274008848206) [X1 Z2 Z3 X5]
+ (0.013873381748426143) [Y0 X1 X2 Y3]
+ (0.013873381748426143) [X0 Y1 Y2 X3]
+ (0.017366118994651413) [Y0 X1 X6 Y7]
+ (0.017366118994651413) [X0 Y1 Y6 X7]
+ (0.017825140995786467) [Y0 X1 X4 Y5]
+ (0.017825140995786467) [X0 Y1 Y4 X5]
+ (0.028685183716105876) [Y4 X5 X6 Y7]
+ (0.028685183716105876) [X4 Y5 Y6 X7]
+ (0.02981242451734578) [Y0 Z1 Z2 Y4]
+ (0.02981242451734578) [X0 Z1 Z2 X4]
+ (0.02981242451734578) [Y1 Z3 Z4 Y5]
+ (0.02981242451734578) [X1 Z3 Z4 X5]
+ (0.03010462314345686) [Y0 Z1 Z3 Y4]
+ (0.03010462314345686) [X0 Z1 Z3 X4]
+ (0.03010462314345686) [Y1 Z2 Z4 Y5]
+ (0.03010462314345686) [X1 Z2 Z4 X5]
+ (0.030787505389143956) [Y0 Z2 Z3 Y4]
+ (0.030787505389143956) [X0 Z2 Z3 X4]
+ (0.04375263801065959) [Y0 Z1 Z2 Z3 Y4]
+ (0.04375263801065959) [X0 Z1 Z2 Z3 X4]
+ (0.0437526380106596) [Y1 Z2 Z3 Z4 Y5]
+ (0.0437526380106596) [X1 Z2 Z3 Z4 X5]
+ (-0.014564531231172986) [Y1 Z2 Z3 X4 X6 Y7]
+ (-0.014564531231172986) [Y1 Z2 Z3 Y4 Y6 Y7]
+ (-0.014564531231172986) [X1 Z2 Z3 X4 X6 X7]
+ (-0.014564531231172986) [X1 Z2 Z3 Y4 Y6 X7]
+ (-6.524373848295766e-06) [Y0 Z1 Z2 Z3 Z4 Y6]
+ (-6.524373848295766e-06) [X0 Z1 Z2 Z3 Z4 X6]
+ (-6.524373848295766e-06) [Y1 Z2 Z3 Z5 Z6 Y7]
+ (-6.524373848295766e-06) [X1 Z2 Z3 Z5 Z6 X7]
+ (-3.769659451782258e-06) [Y0 Z2 Z3 Z4 Z5 Y6]
+ (-3.769659451782258e-06) [X0 Z2 Z3 Z4 Z5 X6]
+ (-3.610297130378097e-06) [Y0 Z1 Z3 Z4 Z5 Y6]
+ (-3.610297130378097e-06) [X0 Z1 Z3 Z4 Z5 X6]
+ (-3.610297130378097e-06) [Y1 Z2 Z4 Z5 Z6 Y7]
+ (-3.610297130378097e-06) [X1 Z2 Z4 Z5 Z6 X7]
+ (-3.3131455000397635e-06) [Y1 Z2 Z3 Y4 X5 X6]
+ (-3.3131455000397635e-06) [X1 Z2 Z3 X4 Y5 Y6]
+ (-3.277483195315645e-06) [Y0 Z1 Z2 Z4 Z5 Y6]
+ (-3.277483195315645e-06) [X0 Z1 Z2 Z4 Z5 X6]
+ (-3.277483195315645e-06) [Y1 Z3 Z4 Z5 Z6 Y7]
+ (-3.277483195315645e-06) [X1 Z3 Z4 Z5 Z6 X7]
+ (-3.2112283482560015e-06) [Y0 Z1 Z2 Z3 Z5 Y6]
+ (-3.2112283482560015e-06) [X0 Z1 Z2 Z3 Z5 X6]
+ (-3.2112283482560015e-06) [Y1 Z2 Z3 Z4 Z6 Y7]
+ (-3.2112283482560015e-06) [X1 Z2 Z3 Z4 Z6 X7]
+ (-1.0358477601425463e-06) [Y0 Y1 X4 Z5 Z6 X7]
+ (-1.0358477601425463e-06) [X0 X1 Y4 Z5 Z6 Y7]
+ (-6.628614201454511e-07) [Y2 X3 X4 Z5 Z6 Y7]
+ (-6.628614201454511e-07) [X2 Y3 Y4 Z5 Z6 X7]
+ (-3.32813935062452e-07) [Y1 X2 X3 Z4 Z5 Y6]
+ (-3.32813935062452e-07) [X1 Y2 Y3 Z4 Z5 X6]
+ (3.32813935062452e-07) [Y1 Y2 X3 Z4 Z5 X6]
+ (3.32813935062452e-07) [X1 X2 Y3 Z4 Z5 Y6]
+ (6.628614201454511e-07) [Y2 Y3 X4 Z5 Z6 X7]
+ (6.628614201454511e-07) [X2 X3 Y4 Z5 Z6 Y7]
+ (1.0358477601425463e-06) [Y0 X1 X4 Z5 Z6 Y7]
+ (1.0358477601425463e-06) [X0 Y1 Y4 Z5 Z6 X7]
+ (3.3131455000397635e-06) [Y1 Z2 Z3 X4 X5 Y6]
+ (3.3131455000397635e-06) [X1 Z2 Z3 Y4 Y5 X6]
+ (4.183932559248208e-06) [Y1 Z2 Z3 Z4 Z5 Y7]
+ (4.183932559248208e-06) [X1 Z2 Z3 Z4 Z5 X7]
+ (0.0002921986261110821) [Y0 Z1 Y2 Y3 Z4 Y5]
+ (0.0002921986261110821) [Y0 Z1 Y2 X3 Z4 X5]
+ (0.0002921986261110821) [X0 Z1 X2 Y3 Z4 Y5]
+ (0.0002921986261110821) [X0 Z1 X2 X3 Z4 X5]
+ (0.010540425907671552) [Y0 Z1 Z2 Z3 Y4 Z7]
+ (0.010540425907671552) [X0 Z1 Z2 Z3 X4 Z7]
+ (0.010540425907671552) [Y1 Z2 Z3 Z4 Y5 Z6]
+ (0.010540425907671552) [X1 Z2 Z3 Z4 X5 Z6]
+ (0.011307274008848206) [Y0 Z1 Z2 Z3 Y4 Z5]
+ (0.011307274008848206) [X0 Z1 Z2 Z3 X4 Z5]
+ (0.025104957138844537) [Y0 Z1 Z2 Z3 Y4 Z6]
+ (0.025104957138844537) [X0 Z1 Z2 Z3 X4 Z6]
+ (0.025104957138844537) [Y1 Z2 Z3 Z4 Y5 Z7]
+ (0.025104957138844537) [X1 Z2 Z3 Z4 X5 Z7]
+ (0.030787505389143956) [Z0 Y1 Z2 Z3 Z4 Y5]
+ (0.030787505389143956) [Z0 X1 Z2 Z3 Z4 X5]
+ (-5.105396549362896e-06) [Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (-5.105396549362896e-06) [X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-5.1053965493628955e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Y6]
+ (-5.1053965493628955e-06) [X0 Z1 Z2 Z3 Z4 Z5 X6]
+ (-0.014564531231172986) [Y0 Z1 Z2 Z3 Z4 Y5 X6 X7]
+ (-0.014564531231172986) [X0 Z1 Z2 Z3 Z4 X5 Y6 Y7]
+ (-3.769659451782258e-06) [Z0 Y1 Z2 Z3 Z4 Z5 Z6 Y7]
+ (-3.769659451782258e-06) [Z0 X1 Z2 Z3 Z4 Z5 Z6 X7]
+ (-3.32813935062452e-07) [Y0 Z1 Y2 Y3 Z4 Z5 Z6 Y7]
+ (-3.32813935062452e-07) [Y0 Z1 Y2 X3 Z4 Z5 Z6 X7]
+ (-3.32813935062452e-07) [X0 Z1 X2 Y3 Z4 Z5 Z6 Y7]
+ (-3.32813935062452e-07) [X0 Z1 X2 X3 Z4 Z5 Z6 X7]
+ (3.3131455000397635e-06) [Y0 Z1 Z2 Z3 Y4 Y5 Z6 Y7]
+ (3.3131455000397635e-06) [Y0 Z1 Z2 Z3 Y4 X5 Z6 X7]
+ (3.3131455000397635e-06) [X0 Z1 Z2 Z3 X4 Y5 Z6 Y7]
+ (3.3131455000397635e-06) [X0 Z1 Z2 Z3 X4 X5 Z6 X7]
+ (4.183932559248208e-06) [Y0 Z1 Z2 Z3 Z4 Z5 Y6 Z7]
+ (4.183932559248208e-06) [X0 Z1 Z2 Z3 Z4 Z5 X6 Z7]
+ (0.014564531231172986) [Y0 Z1 Z2 Z3 Z4 X5 X6 Y7]
+ (0.014564531231172986) [X0 Z1 Z2 Z3 Z4 Y5 Y6 X7]
 </code>
 </pre>
 </details>

---

## 14. tutorial_rosalin.html <a name="demo13"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_rosalin.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
-0.8395887630997874
Step 0: cost = -0.47971271815214855 shots used = 0
Step 1: cost = -1.6879973520840041 shots used = 8000
Step 2: cost = -2.437928256197112 shots used = 16000
Step 3: cost = -2.9300968884147647 shots used = 24000
Step 4: cost = -3.7779069617997116 shots used = 32000
Step 5: cost = -3.8889841568955115 shots used = 40000
Step 6: cost = -4.508059711766957 shots used = 48000
Step 7: cost = -4.71114219758592 shots used = 56000
Step 8: cost = -4.984457128293103 shots used = 64000
Step 9: cost = -5.597084424095087 shots used = 72000
Step 10: cost = -5.456976403687039 shots used = 80000
Step 11: cost = -5.736752824027413 shots used = 88000
Step 12: cost = -6.220317925041974 shots used = 96000
Step 13: cost = -6.45162161927903 shots used = 104000
Step 14: cost = -6.563539211112225 shots used = 112000
Step 15: cost = -6.487339064303318 shots used = 120000
Step 16: cost = -6.69261841162329 shots used = 128000
Step 17: cost = -6.909230576241427 shots used = 136000
Step 18: cost = -7.05156660241221 shots used = 144000
Step 19: cost = -7.163688069859358 shots used = 152000
Step 20: cost = -7.191791478058647 shots used = 160000
Step 21: cost = -7.191694602776715 shots used = 168000
Step 22: cost = -7.430122007574104 shots used = 176000
Step 23: cost = -7.245621601209081 shots used = 184000
Step 24: cost = -7.539044265851978 shots used = 192000
Step 25: cost = -7.532847998808006 shots used = 200000
Step 26: cost = -7.44257222073886 shots used = 208000
Step 27: cost = -7.439951968648378 shots used = 216000
Step 28: cost = -7.734568855081575 shots used = 224000
Step 29: cost = -7.618221322585628 shots used = 232000
Step 30: cost = -7.651544920606065 shots used = 240000
Step 31: cost = -7.5069088885777155 shots used = 248000
Step 32: cost = -7.780301321189146 shots used = 256000
Step 33: cost = -7.4456447455856445 shots used = 264000
Step 34: cost = -7.403560444278863 shots used = 272000
Step 35: cost = -7.666718876831026 shots used = 280000
Step 36: cost = -7.7178910518866415 shots used = 288000
Step 37: cost = -7.375680885292107 shots used = 296000
Step 38: cost = -7.665568049279896 shots used = 304000
Step 39: cost = -7.568101693343673 shots used = 312000
Step 40: cost = -7.524188200359864 shots used = 320000
Step 41: cost = -7.525528734255245 shots used = 328000
Step 42: cost = -7.57734861403185 shots used = 336000
Step 43: cost = -7.76844833198197 shots used = 344000
Step 44: cost = -7.797619087079373 shots used = 352000
Step 45: cost = -7.879148884805528 shots used = 360000
Step 46: cost = -7.744030492750696 shots used = 368000
Step 47: cost = -7.6484739221198765 shots used = 376000
Step 48: cost = -7.679623095926702 shots used = 384000
Step 49: cost = -7.607476988501242 shots used = 392000
Step 50: cost = -7.856041856821188 shots used = 400000
Step 51: cost = -7.644473030321983 shots used = 408000
Step 52: cost = -7.593159311741706 shots used = 416000
Step 53: cost = -7.606939212888227 shots used = 424000
Step 54: cost = -7.621128949485829 shots used = 432000
Step 55: cost = -7.743568287057952 shots used = 440000
Step 56: cost = -7.6325929460598525 shots used = 448000
Step 57: cost = -7.718256562367575 shots used = 456000
Step 58: cost = -7.861601938446393 shots used = 464000
Step 59: cost = -7.666115854972354 shots used = 472000
Step 60: cost = -7.644148944168839 shots used = 480000
Step 61: cost = -7.771569192260795 shots used = 488000
Step 62: cost = -7.776898446282362 shots used = 496000
Step 63: cost = -7.711006891533269 shots used = 504000
Step 64: cost = -7.748650044666392 shots used = 512000
Step 65: cost = -7.690723991927554 shots used = 520000
Step 66: cost = -7.694117031088106 shots used = 528000
Step 67: cost = -7.793250125674997 shots used = 536000
Step 68: cost = -7.926049735334674 shots used = 544000
Step 69: cost = -7.686292326080605 shots used = 552000
Step 70: cost = -7.745774212716911 shots used = 560000
Step 71: cost = -7.625346751584894 shots used = 568000
Step 72: cost = -7.846664469958039 shots used = 576000
Step 73: cost = -7.860275655123486 shots used = 584000
Step 74: cost = -7.593043619614097 shots used = 592000
Step 75: cost = -7.7969799318129045 shots used = 600000
Step 76: cost = -7.837545360539077 shots used = 608000
Step 77: cost = -7.845253964960701 shots used = 616000
Step 78: cost = -7.941652692590529 shots used = 624000
Step 79: cost = -7.967099906804574 shots used = 632000
Step 80: cost = -7.803163356121793 shots used = 640000
Step 81: cost = -7.665600401510319 shots used = 648000
Step 82: cost = -8.09158124610039 shots used = 656000
Step 83: cost = -7.774883584668083 shots used = 664000
Step 84: cost = -7.758175214036924 shots used = 672000
Step 85: cost = -7.9169924228411865 shots used = 680000
Step 86: cost = -7.670199051467696 shots used = 688000
Step 87: cost = -8.085682024006845 shots used = 696000
Step 88: cost = -7.8433919424579095 shots used = 704000
Step 89: cost = -7.755236580472145 shots used = 712000
Step 90: cost = -7.847624689390126 shots used = 720000
Step 91: cost = -8.122239105086607 shots used = 728000
Step 92: cost = -7.922374192271718 shots used = 736000
Step 93: cost = -7.904676929818973 shots used = 744000
Step 94: cost = -7.909417248833883 shots used = 752000
Step 95: cost = -8.06033491620787 shots used = 760000
Step 96: cost = -7.765636196903123 shots used = 768000
Step 97: cost = -7.801666008865329 shots used = 776000
Step 98: cost = -8.066513329432457 shots used = 784000
Step 99: cost = -7.8942080196569675 shots used = 792000
Step 0: cost = -0.38250000000000006 shots used = 0
Step 1: cost = -1.7450000000000006 shots used = 8000
Step 2: cost = -2.54875 shots used = 16000
Step 3: cost = -2.91 shots used = 24000
Step 4: cost = -3.4762500000000003 shots used = 32000
Step 5: cost = -4.08875 shots used = 40000
Step 6: cost = -4.586250000000001 shots used = 48000
Step 7: cost = -4.805 shots used = 56000
Step 8: cost = -4.925 shots used = 64000
Step 9: cost = -5.385000000000001 shots used = 72000
Step 10: cost = -5.4725 shots used = 80000
Step 11: cost = -5.63875 shots used = 88000
Step 12: cost = -5.796250000000001 shots used = 96000
Step 13: cost = -6.308750000000001 shots used = 104000
Step 14: cost = -6.2524999999999995 shots used = 112000
Step 15: cost = -6.706249999999999 shots used = 120000
Step 16: cost = -6.711250000000001 shots used = 128000
Step 17: cost = -6.803749999999999 shots used = 136000
Step 18: cost = -6.94375 shots used = 144000
Step 19: cost = -7.2837499999999995 shots used = 152000
Step 20: cost = -7.4 shots used = 160000
Step 21: cost = -7.38375 shots used = 168000
Step 22: cost = -7.40125 shots used = 176000
Step 23: cost = -7.4775 shots used = 184000
Step 24: cost = -7.58 shots used = 192000
Step 25: cost = -7.623749999999999 shots used = 200000
Step 26: cost = -7.49625 shots used = 208000
Step 27: cost = -7.58375 shots used = 216000
Step 28: cost = -7.6312500000000005 shots used = 224000
Step 29: cost = -7.13375 shots used = 232000
Step 30: cost = -7.47 shots used = 240000
Step 31: cost = -7.6075 shots used = 248000
Step 32: cost = -7.34875 shots used = 256000
Step 33: cost = -7.6525 shots used = 264000
Step 34: cost = -7.572500000000001 shots used = 272000
Step 35: cost = -7.390000000000001 shots used = 280000
Step 36: cost = -7.76375 shots used = 288000
Step 37: cost = -7.49 shots used = 296000
Step 38: cost = -7.61625 shots used = 304000
Step 39: cost = -7.695 shots used = 312000
Step 40: cost = -7.702499999999999 shots used = 320000
Step 41: cost = -7.59625 shots used = 328000
Step 42: cost = -7.733750000000001 shots used = 336000
Step 43: cost = -7.6875 shots used = 344000
Step 44: cost = -7.75875 shots used = 352000
Step 45: cost = -7.796250000000001 shots used = 360000
Step 46: cost = -7.7387500000000005 shots used = 368000
Step 47: cost = -7.92375 shots used = 376000
Step 48: cost = -7.6225 shots used = 384000
Step 49: cost = -7.8425 shots used = 392000
Step 50: cost = -7.74 shots used = 400000
Step 51: cost = -7.661250000000001 shots used = 408000
Step 52: cost = -7.786250000000001 shots used = 416000
Step 53: cost = -7.78875 shots used = 424000
Step 54: cost = -7.62375 shots used = 432000
Step 55: cost = -7.9375 shots used = 440000
Step 56: cost = -7.71625 shots used = 448000
Step 57: cost = -7.72375 shots used = 456000
Step 58: cost = -7.741250000000001 shots used = 464000
Step 59: cost = -7.811249999999999 shots used = 472000
Step 60: cost = -7.89 shots used = 480000
Step 61: cost = -7.74 shots used = 488000
Step 62: cost = -7.751250000000001 shots used = 496000
Step 63: cost = -7.71875 shots used = 504000
Step 64: cost = -7.695 shots used = 512000
Step 65: cost = -7.7325 shots used = 520000
Step 66: cost = -7.819999999999999 shots used = 528000
Step 67: cost = -7.981249999999999 shots used = 536000
Step 68: cost = -7.8 shots used = 544000
Step 69: cost = -7.89 shots used = 552000
Step 70: cost = -7.7125 shots used = 560000
Step 71: cost = -7.993750000000001 shots used = 568000
Step 72: cost = -7.772499999999999 shots used = 576000
Step 73: cost = -8.01125 shots used = 584000
Step 74: cost = -8.116249999999999 shots used = 592000
Step 75: cost = -7.9662500000000005 shots used = 600000
Step 76: cost = -7.7125 shots used = 608000
Step 77: cost = -7.8925 shots used = 616000
Step 78: cost = -7.967499999999999 shots used = 624000
Step 79: cost = -7.91375 shots used = 632000
Step 80: cost = -7.797499999999999 shots used = 640000
Step 81: cost = -7.9975000000000005 shots used = 648000
Step 82: cost = -7.99 shots used = 656000
Step 83: cost = -7.7124999999999995 shots used = 664000
Step 84: cost = -7.76875 shots used = 672000
Step 85: cost = -7.62 shots used = 680000
Step 86: cost = -7.822500000000001 shots used = 688000
Step 87: cost = -7.74625 shots used = 696000
Step 88: cost = -7.9137499999999985 shots used = 704000
Step 89: cost = -7.86125 shots used = 712000
Step 90: cost = -7.975 shots used = 720000
Step 91: cost = -7.89375 shots used = 728000
Step 92: cost = -8.1075 shots used = 736000
Step 93: cost = -7.775 shots used = 744000
Step 94: cost = -7.8999999999999995 shots used = 752000
Step 95: cost = -7.85625 shots used = 760000
Step 96: cost = -7.925000000000001 shots used = 768000
Step 97: cost = -8.0 shots used = 776000
Step 98: cost = -7.825000000000001 shots used = 784000
Step 99: cost = -7.999999999999999 shots used = 792000
Step 0: cost = -5.976611864639143, shots_used = 240
Step 1: cost = -3.9696542358660727, shots_used = 288
Step 2: cost = -4.960189727105254, shots_used = 360
Step 3: cost = -4.580003760087767, shots_used = 456
Step 4: cost = -2.230216749128693, shots_used = 552
Step 5: cost = -3.6390262209635624, shots_used = 696
Step 6: cost = -6.407579837465835, shots_used = 1050
Step 7: cost = -7.4366536874312565, shots_used = 1578
Step 8: cost = -7.259604321778904, shots_used = 2250
Step 9: cost = -7.062132684694287, shots_used = 2970
Step 10: cost = -7.5539381823528915, shots_used = 3738
Step 11: cost = -7.530120251217975, shots_used = 4866
Step 12: cost = -7.620064018172076, shots_used = 6474
Step 13: cost = -7.749105026853709, shots_used = 8288
Step 14: cost = -7.7584669100105454, shots_used = 10388
Step 15: cost = -7.547668090788587, shots_used = 12404
Step 16: cost = -7.802606000681813, shots_used = 14660
Step 17: cost = -7.819375105495885, shots_used = 17180
Step 18: cost = -7.813893056373781, shots_used = 19700
Step 19: cost = -7.818976697763795, shots_used = 22796
Step 20: cost = -7.847655565015213, shots_used = 26372
Step 21: cost = -7.854512274045721, shots_used = 30810
Step 22: cost = -7.855665819254089, shots_used = 35538
Step 23: cost = -7.843276666680198, shots_used = 40770
Step 24: cost = -7.82813895796069, shots_used = 45762
Step 25: cost = -7.796501914990248, shots_used = 51162
Step 26: cost = -7.871130124788932, shots_used = 56466
Step 27: cost = -7.866190872563943, shots_used = 62010
Step 28: cost = -7.780118268373553, shots_used = 68250
Step 29: cost = -7.843565291223448, shots_used = 74946
Step 30: cost = -7.840084824878835, shots_used = 81762
Step 31: cost = -7.863430860462219, shots_used = 88962
Step 32: cost = -7.863400771365601, shots_used = 96786
Step 33: cost = -7.828392469226825, shots_used = 104730
Step 34: cost = -7.845758777555817, shots_used = 114532
Step 35: cost = -7.862280441095794, shots_used = 122908
Step 36: cost = -7.866212335569502, shots_used = 131836
Step 37: cost = -7.859430128177042, shots_used = 140500
Step 38: cost = -7.856087432905534, shots_used = 150076
Step 39: cost = -7.850323433779115, shots_used = 159676
Step 40: cost = -7.834403598788763, shots_used = 170116
Step 41: cost = -7.849769789802028, shots_used = 181300
Step 42: cost = -7.86693841353118, shots_used = 192700
Step 43: cost = -7.865653895759861, shots_used = 204460
Step 44: cost = -7.853522061269157, shots_used = 217900
Step 45: cost = -7.885272132729725, shots_used = 231748
Step 46: cost = -7.88224395467864, shots_used = 245644
Step 47: cost = -7.884376349618622, shots_used = 259852
Step 48: cost = -7.8808911781003825, shots_used = 275164
Step 49: cost = -7.881035167671664, shots_used = 292444
Step 50: cost = -7.881931152903569, shots_used = 310300
Step 51: cost = -7.873486288144938, shots_used = 329452
Step 52: cost = -7.842973314288795, shots_used = 348532
Step 53: cost = -7.87101794797729, shots_used = 368644
Step 54: cost = -7.880857865087542, shots_used = 388828
Step 55: cost = -7.884163217633474, shots_used = 409132
Step 56: cost = -7.866452206380498, shots_used = 429076
Step 57: cost = -7.876255345278057, shots_used = 451468
Step 58: cost = -7.87369984074766, shots_used = 475348
Step 59: cost = -7.890243502630163, shots_used = 501460
2400
Step 0: cost = -2.03376839972733 shots_used = 2400
Step 1: cost = -3.0397515887713897 shots_used = 4800
Step 2: cost = -3.8459175082365666 shots_used = 7200
Step 3: cost = -4.505506895275778 shots_used = 9600
Step 4: cost = -5.0488106623708084 shots_used = 12000
Step 5: cost = -5.482162129547712 shots_used = 14400
Step 6: cost = -5.83880726147689 shots_used = 16800
Step 7: cost = -6.143933494222608 shots_used = 19200
Step 8: cost = -6.412317130720796 shots_used = 21600
Step 9: cost = -6.6534666682698 shots_used = 24000
Step 10: cost = -6.86746547637287 shots_used = 26400
Step 11: cost = -7.057043661341395 shots_used = 28800
Step 12: cost = -7.219548494479429 shots_used = 31200
Step 13: cost = -7.3445177518694456 shots_used = 33600
Step 14: cost = -7.435753942420535 shots_used = 36000
Step 15: cost = -7.497138548636965 shots_used = 38400
Step 16: cost = -7.529946318655265 shots_used = 40800
Step 17: cost = -7.537070813893377 shots_used = 43200
Step 18: cost = -7.525225697166624 shots_used = 45600
Step 19: cost = -7.5048251159723405 shots_used = 48000
Step 20: cost = -7.481487171246212 shots_used = 50400
Step 21: cost = -7.461106527571478 shots_used = 52800
Step 22: cost = -7.4490325775024075 shots_used = 55200
Step 23: cost = -7.444817343084735 shots_used = 57600
Step 24: cost = -7.4494913586937574 shots_used = 60000
Step 25: cost = -7.462969617594349 shots_used = 62400
Step 26: cost = -7.484518392550573 shots_used = 64800
Step 27: cost = -7.509533957688121 shots_used = 67200
Step 28: cost = -7.535240804873656 shots_used = 69600
Step 29: cost = -7.560642729685874 shots_used = 72000
Step 30: cost = -7.586205677180162 shots_used = 74400
Step 31: cost = -7.61260475402048 shots_used = 76800
Step 32: cost = -7.637117815005769 shots_used = 79200
Step 33: cost = -7.661716123608457 shots_used = 81600
Step 34: cost = -7.6852319189727165 shots_used = 84000
Step 35: cost = -7.708583289744081 shots_used = 86400
Step 36: cost = -7.729551671925802 shots_used = 88800
Step 37: cost = -7.7462558125604595 shots_used = 91200
Step 38: cost = -7.758965992155235 shots_used = 93600
Step 39: cost = -7.764889692835303 shots_used = 96000
Step 40: cost = -7.770298814247658 shots_used = 98400
Step 41: cost = -7.771938304013664 shots_used = 100800
Step 42: cost = -7.771490419427766 shots_used = 103200
Step 43: cost = -7.771665932203987 shots_used = 105600
Step 44: cost = -7.771775966399097 shots_used = 108000
Step 45: cost = -7.772019786144459 shots_used = 110400
Step 46: cost = -7.774409408800273 shots_used = 112800
Step 47: cost = -7.777544198411677 shots_used = 115200
Step 48: cost = -7.78057842461007 shots_used = 117600
Step 49: cost = -7.7865146226898805 shots_used = 120000
Step 50: cost = -7.793839215454196 shots_used = 122400
Step 51: cost = -7.802144039740554 shots_used = 124800
Step 52: cost = -7.809859012081808 shots_used = 127200
Step 53: cost = -7.818330164675909 shots_used = 129600
Step 54: cost = -7.826930993976666 shots_used = 132000
Step 55: cost = -7.834969848723968 shots_used = 134400
Step 56: cost = -7.842454395123664 shots_used = 136800
Step 57: cost = -7.849335152675151 shots_used = 139200
Step 58: cost = -7.853951071633944 shots_used = 141600
Step 59: cost = -7.858296868696565 shots_used = 144000
Step 60: cost = -7.862867672169834 shots_used = 146400
Step 61: cost = -7.865540080202736 shots_used = 148800
Step 62: cost = -7.867577632485199 shots_used = 151200
Step 63: cost = -7.869035010771334 shots_used = 153600
Step 64: cost = -7.870496374034538 shots_used = 156000
Step 65: cost = -7.871678720443278 shots_used = 158400
Step 66: cost = -7.872542373444428 shots_used = 160800
Step 67: cost = -7.873739299675017 shots_used = 163200
Step 68: cost = -7.874314293738313 shots_used = 165600
Step 69: cost = -7.875793149514538 shots_used = 168000
Step 70: cost = -7.877051911492931 shots_used = 170400
Step 71: cost = -7.878207264678217 shots_used = 172800
Step 72: cost = -7.879198045006914 shots_used = 175200
Step 73: cost = -7.880726987471535 shots_used = 177600
Step 74: cost = -7.882055795432435 shots_used = 180000
Step 75: cost = -7.88215282515028 shots_used = 182400
Step 76: cost = -7.881947191378357 shots_used = 184800
Step 77: cost = -7.881566349945106 shots_used = 187200
Step 78: cost = -7.881659168988012 shots_used = 189600
Step 79: cost = -7.881276797156975 shots_used = 192000
Step 80: cost = -7.879976174007023 shots_used = 194400
Step 81: cost = -7.878714918643873 shots_used = 196800
Step 82: cost = -7.877964404670651 shots_used = 199200
Step 83: cost = -7.8771022016203665 shots_used = 201600
Step 84: cost = -7.875562772172711 shots_used = 204000
Step 85: cost = -7.875602350174969 shots_used = 206400
Step 86: cost = -7.877141380119034 shots_used = 208800
Step 87: cost = -7.87925788505365 shots_used = 211200
Step 88: cost = -7.881144761009377 shots_used = 213600
Step 89: cost = -7.882250363744701 shots_used = 216000
Step 90: cost = -7.881748113564451 shots_used = 218400
Step 91: cost = -7.883533319932514 shots_used = 220800
Step 92: cost = -7.884779159318079 shots_used = 223200
Step 93: cost = -7.8868911005436555 shots_used = 225600
Step 94: cost = -7.888524224480213 shots_used = 228000
Step 95: cost = -7.888123287772768 shots_used = 230400
Step 96: cost = -7.8867800801467896 shots_used = 232800
Step 97: cost = -7.8853107450636415 shots_used = 235200
Step 98: cost = -7.883507674089132 shots_used = 237600
Step 99: cost = -7.881351067687096 shots_used = 240000
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_rosalin.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
/home/runner/work/qml/qml/demonstrations/tutorial_rosalin.py:217: UserWarning: The init module will be deprecated soon, since templates can now provide a method that returns the shape of parameter tensors.
-0.8395887630997874
Step 0: cost = -0.47971271815214855 shots used = 0
Step 1: cost = -1.6879973520840041 shots used = 8000
Step 2: cost = -2.437928256197112 shots used = 16000
Step 3: cost = -2.9300968884147647 shots used = 24000
Step 4: cost = -3.7779069617997116 shots used = 32000
Step 5: cost = -3.8889841568955115 shots used = 40000
Step 6: cost = -4.508059711766957 shots used = 48000
Step 7: cost = -4.71114219758592 shots used = 56000
Step 8: cost = -4.984457128293103 shots used = 64000
Step 9: cost = -5.597084424095087 shots used = 72000
Step 10: cost = -5.456976403687039 shots used = 80000
Step 11: cost = -5.736752824027413 shots used = 88000
Step 12: cost = -6.220317925041974 shots used = 96000
Step 13: cost = -6.45162161927903 shots used = 104000
Step 14: cost = -6.563539211112225 shots used = 112000
Step 15: cost = -6.487339064303318 shots used = 120000
Step 16: cost = -6.69261841162329 shots used = 128000
Step 17: cost = -6.909230576241427 shots used = 136000
Step 18: cost = -7.05156660241221 shots used = 144000
Step 19: cost = -7.163688069859358 shots used = 152000
Step 20: cost = -7.191791478058647 shots used = 160000
Step 21: cost = -7.191694602776715 shots used = 168000
Step 22: cost = -7.430122007574104 shots used = 176000
Step 23: cost = -7.245621601209081 shots used = 184000
Step 24: cost = -7.539044265851978 shots used = 192000
Step 25: cost = -7.532847998808006 shots used = 200000
Step 26: cost = -7.44257222073886 shots used = 208000
Step 27: cost = -7.439951968648378 shots used = 216000
Step 28: cost = -7.734568855081575 shots used = 224000
Step 29: cost = -7.618221322585628 shots used = 232000
Step 30: cost = -7.651544920606065 shots used = 240000
Step 31: cost = -7.5069088885777155 shots used = 248000
Step 32: cost = -7.780301321189146 shots used = 256000
Step 33: cost = -7.4456447455856445 shots used = 264000
Step 34: cost = -7.403560444278863 shots used = 272000
Step 35: cost = -7.666718876831026 shots used = 280000
Step 36: cost = -7.7178910518866415 shots used = 288000
Step 37: cost = -7.375680885292107 shots used = 296000
Step 38: cost = -7.665568049279896 shots used = 304000
Step 39: cost = -7.568101693343673 shots used = 312000
Step 40: cost = -7.524188200359864 shots used = 320000
Step 41: cost = -7.525528734255245 shots used = 328000
Step 42: cost = -7.57734861403185 shots used = 336000
Step 43: cost = -7.76844833198197 shots used = 344000
Step 44: cost = -7.797619087079373 shots used = 352000
Step 45: cost = -7.879148884805528 shots used = 360000
Step 46: cost = -7.744030492750696 shots used = 368000
Step 47: cost = -7.6484739221198765 shots used = 376000
Step 48: cost = -7.679623095926702 shots used = 384000
Step 49: cost = -7.607476988501242 shots used = 392000
Step 50: cost = -7.856041856821188 shots used = 400000
Step 51: cost = -7.644473030321983 shots used = 408000
Step 52: cost = -7.593159311741706 shots used = 416000
Step 53: cost = -7.606939212888227 shots used = 424000
Step 54: cost = -7.621128949485829 shots used = 432000
Step 55: cost = -7.743568287057952 shots used = 440000
Step 56: cost = -7.6325929460598525 shots used = 448000
Step 57: cost = -7.718256562367575 shots used = 456000
Step 58: cost = -7.861601938446393 shots used = 464000
Step 59: cost = -7.666115854972354 shots used = 472000
Step 60: cost = -7.644148944168839 shots used = 480000
Step 61: cost = -7.771569192260795 shots used = 488000
Step 62: cost = -7.776898446282362 shots used = 496000
Step 63: cost = -7.711006891533269 shots used = 504000
Step 64: cost = -7.748650044666392 shots used = 512000
Step 65: cost = -7.690723991927554 shots used = 520000
Step 66: cost = -7.694117031088106 shots used = 528000
Step 67: cost = -7.793250125674997 shots used = 536000
Step 68: cost = -7.926049735334674 shots used = 544000
Step 69: cost = -7.686292326080605 shots used = 552000
Step 70: cost = -7.745774212716911 shots used = 560000
Step 71: cost = -7.625346751584894 shots used = 568000
Step 72: cost = -7.846664469958039 shots used = 576000
Step 73: cost = -7.860275655123486 shots used = 584000
Step 74: cost = -7.593043619614097 shots used = 592000
Step 75: cost = -7.7969799318129045 shots used = 600000
Step 76: cost = -7.837545360539077 shots used = 608000
Step 77: cost = -7.845253964960701 shots used = 616000
Step 78: cost = -7.941652692590529 shots used = 624000
Step 79: cost = -7.967099906804574 shots used = 632000
Step 80: cost = -7.803163356121793 shots used = 640000
Step 81: cost = -7.665600401510319 shots used = 648000
Step 82: cost = -8.09158124610039 shots used = 656000
Step 83: cost = -7.774883584668083 shots used = 664000
Step 84: cost = -7.758175214036924 shots used = 672000
Step 85: cost = -7.9169924228411865 shots used = 680000
Step 86: cost = -7.670199051467696 shots used = 688000
Step 87: cost = -8.085682024006845 shots used = 696000
Step 88: cost = -7.8433919424579095 shots used = 704000
Step 89: cost = -7.755236580472145 shots used = 712000
Step 90: cost = -7.847624689390126 shots used = 720000
Step 91: cost = -8.122239105086607 shots used = 728000
Step 92: cost = -7.922374192271718 shots used = 736000
Step 93: cost = -7.904676929818973 shots used = 744000
Step 94: cost = -7.909417248833883 shots used = 752000
Step 95: cost = -8.06033491620787 shots used = 760000
Step 96: cost = -7.765636196903123 shots used = 768000
Step 97: cost = -7.801666008865329 shots used = 776000
Step 98: cost = -8.066513329432457 shots used = 784000
Step 99: cost = -7.8942080196569675 shots used = 792000
Step 0: cost = -0.38250000000000006 shots used = 0
Step 1: cost = -1.7450000000000006 shots used = 8000
Step 2: cost = -2.54875 shots used = 16000
Step 3: cost = -2.91 shots used = 24000
Step 4: cost = -3.4762500000000003 shots used = 32000
Step 5: cost = -4.08875 shots used = 40000
Step 6: cost = -4.586250000000001 shots used = 48000
Step 7: cost = -4.805 shots used = 56000
Step 8: cost = -4.925 shots used = 64000
Step 9: cost = -5.385000000000001 shots used = 72000
Step 10: cost = -5.4725 shots used = 80000
Step 11: cost = -5.63875 shots used = 88000
Step 12: cost = -5.796250000000001 shots used = 96000
Step 13: cost = -6.308750000000001 shots used = 104000
Step 14: cost = -6.2524999999999995 shots used = 112000
Step 15: cost = -6.706249999999999 shots used = 120000
Step 16: cost = -6.711250000000001 shots used = 128000
Step 17: cost = -6.803749999999999 shots used = 136000
Step 18: cost = -6.94375 shots used = 144000
Step 19: cost = -7.2837499999999995 shots used = 152000
Step 20: cost = -7.4 shots used = 160000
Step 21: cost = -7.38375 shots used = 168000
Step 22: cost = -7.40125 shots used = 176000
Step 23: cost = -7.4775 shots used = 184000
Step 24: cost = -7.58 shots used = 192000
Step 25: cost = -7.623749999999999 shots used = 200000
Step 26: cost = -7.49625 shots used = 208000
Step 27: cost = -7.58375 shots used = 216000
Step 28: cost = -7.6312500000000005 shots used = 224000
Step 29: cost = -7.13375 shots used = 232000
Step 30: cost = -7.47 shots used = 240000
Step 31: cost = -7.6075 shots used = 248000
Step 32: cost = -7.34875 shots used = 256000
Step 33: cost = -7.6525 shots used = 264000
Step 34: cost = -7.572500000000001 shots used = 272000
Step 35: cost = -7.390000000000001 shots used = 280000
Step 36: cost = -7.76375 shots used = 288000
Step 37: cost = -7.49 shots used = 296000
Step 38: cost = -7.61625 shots used = 304000
Step 39: cost = -7.695 shots used = 312000
Step 40: cost = -7.702499999999999 shots used = 320000
Step 41: cost = -7.59625 shots used = 328000
Step 42: cost = -7.733750000000001 shots used = 336000
Step 43: cost = -7.6875 shots used = 344000
Step 44: cost = -7.75875 shots used = 352000
Step 45: cost = -7.796250000000001 shots used = 360000
Step 46: cost = -7.7387500000000005 shots used = 368000
Step 47: cost = -7.92375 shots used = 376000
Step 48: cost = -7.6225 shots used = 384000
Step 49: cost = -7.8425 shots used = 392000
Step 50: cost = -7.74 shots used = 400000
Step 51: cost = -7.661250000000001 shots used = 408000
Step 52: cost = -7.786250000000001 shots used = 416000
Step 53: cost = -7.78875 shots used = 424000
Step 54: cost = -7.62375 shots used = 432000
Step 55: cost = -7.9375 shots used = 440000
Step 56: cost = -7.71625 shots used = 448000
Step 57: cost = -7.72375 shots used = 456000
Step 58: cost = -7.741250000000001 shots used = 464000
Step 59: cost = -7.811249999999999 shots used = 472000
Step 60: cost = -7.89 shots used = 480000
Step 61: cost = -7.74 shots used = 488000
Step 62: cost = -7.751250000000001 shots used = 496000
Step 63: cost = -7.71875 shots used = 504000
Step 64: cost = -7.695 shots used = 512000
Step 65: cost = -7.7325 shots used = 520000
Step 66: cost = -7.819999999999999 shots used = 528000
Step 67: cost = -7.981249999999999 shots used = 536000
Step 68: cost = -7.8 shots used = 544000
Step 69: cost = -7.89 shots used = 552000
Step 70: cost = -7.7125 shots used = 560000
Step 71: cost = -7.993750000000001 shots used = 568000
Step 72: cost = -7.772499999999999 shots used = 576000
Step 73: cost = -8.01125 shots used = 584000
Step 74: cost = -8.116249999999999 shots used = 592000
Step 75: cost = -7.9662500000000005 shots used = 600000
Step 76: cost = -7.7125 shots used = 608000
Step 77: cost = -7.8925 shots used = 616000
Step 78: cost = -7.967499999999999 shots used = 624000
Step 79: cost = -7.91375 shots used = 632000
Step 80: cost = -7.797499999999999 shots used = 640000
Step 81: cost = -7.9975000000000005 shots used = 648000
Step 82: cost = -7.99 shots used = 656000
Step 83: cost = -7.7124999999999995 shots used = 664000
Step 84: cost = -7.76875 shots used = 672000
Step 85: cost = -7.62 shots used = 680000
Step 86: cost = -7.822500000000001 shots used = 688000
Step 87: cost = -7.74625 shots used = 696000
Step 88: cost = -7.9137499999999985 shots used = 704000
Step 89: cost = -7.86125 shots used = 712000
Step 90: cost = -7.975 shots used = 720000
Step 91: cost = -7.89375 shots used = 728000
Step 92: cost = -8.1075 shots used = 736000
Step 93: cost = -7.775 shots used = 744000
Step 94: cost = -7.8999999999999995 shots used = 752000
Step 95: cost = -7.85625 shots used = 760000
Step 96: cost = -7.925000000000001 shots used = 768000
Step 97: cost = -8.0 shots used = 776000
Step 98: cost = -7.825000000000001 shots used = 784000
Step 99: cost = -7.999999999999999 shots used = 792000
Step 0: cost = -5.976611864639143, shots_used = 240
Step 1: cost = -3.9696542358660727, shots_used = 288
Step 2: cost = -4.960189727105254, shots_used = 360
Step 3: cost = -4.580003760087767, shots_used = 456
Step 4: cost = -2.230216749128693, shots_used = 552
Step 5: cost = -3.6390262209635624, shots_used = 696
Step 6: cost = -6.407579837465835, shots_used = 1050
Step 7: cost = -7.4366536874312565, shots_used = 1578
Step 8: cost = -7.259604321778904, shots_used = 2250
Step 9: cost = -7.062132684694287, shots_used = 2970
Step 10: cost = -7.5539381823528915, shots_used = 3738
Step 11: cost = -7.530120251217975, shots_used = 4866
Step 12: cost = -7.620064018172076, shots_used = 6474
Step 13: cost = -7.749105026853709, shots_used = 8288
Step 14: cost = -7.7584669100105454, shots_used = 10388
Step 15: cost = -7.547668090788587, shots_used = 12404
Step 16: cost = -7.802606000681813, shots_used = 14660
Step 17: cost = -7.819375105495885, shots_used = 17180
Step 18: cost = -7.813893056373781, shots_used = 19700
Step 19: cost = -7.818976697763795, shots_used = 22796
Step 20: cost = -7.847655565015213, shots_used = 26372
Step 21: cost = -7.854512274045721, shots_used = 30810
Step 22: cost = -7.855665819254089, shots_used = 35538
Step 23: cost = -7.843276666680198, shots_used = 40770
Step 24: cost = -7.82813895796069, shots_used = 45762
Step 25: cost = -7.796501914990248, shots_used = 51162
Step 26: cost = -7.871130124788932, shots_used = 56466
Step 27: cost = -7.866190872563943, shots_used = 62010
Step 28: cost = -7.780118268373553, shots_used = 68250
Step 29: cost = -7.843565291223448, shots_used = 74946
Step 30: cost = -7.840084824878835, shots_used = 81762
Step 31: cost = -7.863430860462219, shots_used = 88962
Step 32: cost = -7.863400771365601, shots_used = 96786
Step 33: cost = -7.828392469226825, shots_used = 104730
Step 34: cost = -7.845758777555817, shots_used = 114532
Step 35: cost = -7.862280441095794, shots_used = 122908
Step 36: cost = -7.866212335569502, shots_used = 131836
Step 37: cost = -7.859430128177042, shots_used = 140500
Step 38: cost = -7.856087432905534, shots_used = 150076
Step 39: cost = -7.850323433779115, shots_used = 159676
Step 40: cost = -7.834403598788763, shots_used = 170116
Step 41: cost = -7.849769789802028, shots_used = 181300
Step 42: cost = -7.86693841353118, shots_used = 192700
Step 43: cost = -7.865653895759861, shots_used = 204460
Step 44: cost = -7.853522061269157, shots_used = 217900
Step 45: cost = -7.885272132729725, shots_used = 231748
Step 46: cost = -7.88224395467864, shots_used = 245644
Step 47: cost = -7.884376349618622, shots_used = 259852
Step 48: cost = -7.8808911781003825, shots_used = 275164
Step 49: cost = -7.881035167671664, shots_used = 292444
Step 50: cost = -7.881931152903569, shots_used = 310300
Step 51: cost = -7.873486288144938, shots_used = 329452
Step 52: cost = -7.842973314288795, shots_used = 348532
Step 53: cost = -7.87101794797729, shots_used = 368644
Step 54: cost = -7.880857865087542, shots_used = 388828
Step 55: cost = -7.884163217633474, shots_used = 409132
Step 56: cost = -7.866452206380498, shots_used = 429076
Step 57: cost = -7.876255345278057, shots_used = 451468
Step 58: cost = -7.87369984074766, shots_used = 475348
Step 59: cost = -7.890243502630163, shots_used = 501460
2400
Step 0: cost = -2.03376839972733 shots_used = 2400
Step 1: cost = -3.0397515887713897 shots_used = 4800
Step 2: cost = -3.8459175082365666 shots_used = 7200
Step 3: cost = -4.505506895275778 shots_used = 9600
Step 4: cost = -5.0488106623708084 shots_used = 12000
Step 5: cost = -5.482162129547712 shots_used = 14400
Step 6: cost = -5.83880726147689 shots_used = 16800
Step 7: cost = -6.143933494222608 shots_used = 19200
Step 8: cost = -6.412317130720796 shots_used = 21600
Step 9: cost = -6.6534666682698 shots_used = 24000
Step 10: cost = -6.86746547637287 shots_used = 26400
Step 11: cost = -7.057043661341395 shots_used = 28800
Step 12: cost = -7.219548494479429 shots_used = 31200
Step 13: cost = -7.3445177518694456 shots_used = 33600
Step 14: cost = -7.435753942420535 shots_used = 36000
Step 15: cost = -7.497138548636965 shots_used = 38400
Step 16: cost = -7.529946318655265 shots_used = 40800
Step 17: cost = -7.537070813893377 shots_used = 43200
Step 18: cost = -7.525225697166624 shots_used = 45600
Step 19: cost = -7.5048251159723405 shots_used = 48000
Step 20: cost = -7.481487171246212 shots_used = 50400
Step 21: cost = -7.461106527571478 shots_used = 52800
Step 22: cost = -7.4490325775024075 shots_used = 55200
Step 23: cost = -7.444817343084735 shots_used = 57600
Step 24: cost = -7.4494913586937574 shots_used = 60000
Step 25: cost = -7.462969617594349 shots_used = 62400
Step 26: cost = -7.484518392550573 shots_used = 64800
Step 27: cost = -7.509533957688121 shots_used = 67200
Step 28: cost = -7.535240804873656 shots_used = 69600
Step 29: cost = -7.560642729685874 shots_used = 72000
Step 30: cost = -7.586205677180162 shots_used = 74400
Step 31: cost = -7.61260475402048 shots_used = 76800
Step 32: cost = -7.637117815005769 shots_used = 79200
Step 33: cost = -7.661716123608457 shots_used = 81600
Step 34: cost = -7.6852319189727165 shots_used = 84000
Step 35: cost = -7.708583289744081 shots_used = 86400
Step 36: cost = -7.729551671925802 shots_used = 88800
Step 37: cost = -7.7462558125604595 shots_used = 91200
Step 38: cost = -7.758965992155235 shots_used = 93600
Step 39: cost = -7.764889692835303 shots_used = 96000
Step 40: cost = -7.770298814247658 shots_used = 98400
Step 41: cost = -7.771938304013664 shots_used = 100800
Step 42: cost = -7.771490419427766 shots_used = 103200
Step 43: cost = -7.771665932203987 shots_used = 105600
Step 44: cost = -7.771775966399097 shots_used = 108000
Step 45: cost = -7.772019786144459 shots_used = 110400
Step 46: cost = -7.774409408800273 shots_used = 112800
Step 47: cost = -7.777544198411677 shots_used = 115200
Step 48: cost = -7.78057842461007 shots_used = 117600
Step 49: cost = -7.7865146226898805 shots_used = 120000
Step 50: cost = -7.793839215454196 shots_used = 122400
Step 51: cost = -7.802144039740554 shots_used = 124800
Step 52: cost = -7.809859012081808 shots_used = 127200
Step 53: cost = -7.818330164675909 shots_used = 129600
Step 54: cost = -7.826930993976666 shots_used = 132000
Step 55: cost = -7.834969848723968 shots_used = 134400
Step 56: cost = -7.842454395123664 shots_used = 136800
Step 57: cost = -7.849335152675151 shots_used = 139200
Step 58: cost = -7.853951071633944 shots_used = 141600
Step 59: cost = -7.858296868696565 shots_used = 144000
Step 60: cost = -7.862867672169834 shots_used = 146400
Step 61: cost = -7.865540080202736 shots_used = 148800
Step 62: cost = -7.867577632485199 shots_used = 151200
Step 63: cost = -7.869035010771334 shots_used = 153600
Step 64: cost = -7.870496374034538 shots_used = 156000
Step 65: cost = -7.871678720443278 shots_used = 158400
Step 66: cost = -7.872542373444428 shots_used = 160800
Step 67: cost = -7.873739299675017 shots_used = 163200
Step 68: cost = -7.874314293738313 shots_used = 165600
Step 69: cost = -7.875793149514538 shots_used = 168000
Step 70: cost = -7.877051911492931 shots_used = 170400
Step 71: cost = -7.878207264678217 shots_used = 172800
Step 72: cost = -7.879198045006914 shots_used = 175200
Step 73: cost = -7.880726987471535 shots_used = 177600
Step 74: cost = -7.882055795432435 shots_used = 180000
Step 75: cost = -7.88215282515028 shots_used = 182400
Step 76: cost = -7.881947191378357 shots_used = 184800
Step 77: cost = -7.881566349945106 shots_used = 187200
Step 78: cost = -7.881659168988012 shots_used = 189600
Step 79: cost = -7.881276797156975 shots_used = 192000
Step 80: cost = -7.879976174007023 shots_used = 194400
Step 81: cost = -7.878714918643873 shots_used = 196800
Step 82: cost = -7.877964404670651 shots_used = 199200
Step 83: cost = -7.8771022016203665 shots_used = 201600
Step 84: cost = -7.875562772172711 shots_used = 204000
Step 85: cost = -7.875602350174969 shots_used = 206400
Step 86: cost = -7.877141380119034 shots_used = 208800
Step 87: cost = -7.87925788505365 shots_used = 211200
Step 88: cost = -7.881144761009377 shots_used = 213600
Step 89: cost = -7.882250363744701 shots_used = 216000
Step 90: cost = -7.881748113564451 shots_used = 218400
Step 91: cost = -7.883533319932514 shots_used = 220800
Step 92: cost = -7.884779159318079 shots_used = 223200
Step 93: cost = -7.8868911005436555 shots_used = 225600
Step 94: cost = -7.888524224480213 shots_used = 228000
Step 95: cost = -7.888123287772768 shots_used = 230400
Step 96: cost = -7.8867800801467896 shots_used = 232800
Step 97: cost = -7.8853107450636415 shots_used = 235200
Step 98: cost = -7.883507674089132 shots_used = 237600
 </code>
 </pre>
 </details>

---

## 15. tutorial_multiclass_classification.html <a name="demo14"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_multiclass_classification.html):

```
Iter:    29 | Cost: 0.0748657 | Acc train: 0.6785714 | Acc test: 0.7105263
Iter:    93 | Cost: 0.0339653 | Acc train: 0.8750000 | Acc test: 0.8684211
/opt/hostedtoolcache/Python/3.7.12/x64/lib/python3.7/site-packages/pennylane/templates/embeddings/amplitude.py:136: UserWarning: The pad argument will be replaced by the pad_with option in future versions of PennyLane.
Iter:    82 | Cost: 0.0479530 | Acc train: 0.9375000 | Acc test: 0.9473684
Iter:    86 | Cost: 0.0964098 | Acc train: 0.9553571 | Acc test: 0.9736842
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_multiclass_classification.html):

```
Iter:    29 | Cost: 0.0748658 | Acc train: 0.6785714 | Acc test: 0.7105263
Iter:    93 | Cost: 0.0339652 | Acc train: 0.8750000 | Acc test: 0.8684211
/opt/hostedtoolcache/Python/3.7.12/x64/lib/python3.7/site-packages/pennylane/templates/embeddings/amplitude.py:137: UserWarning: The pad argument will be replaced by the pad_with option in future versions of PennyLane.
Iter:    82 | Cost: 0.0479531 | Acc train: 0.9375000 | Acc test: 0.9473684
Iter:    86 | Cost: 0.0964097 | Acc train: 0.9553571 | Acc test: 0.9736842
```

---

## 16. tutorial_QGAN.html <a name="demo15"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_QGAN.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Step 0: cost = -0.05727687478065491
Step 5: cost = -0.26348111033439636
Step 10: cost = -0.4273917004466057
Step 15: cost = -0.47261590510606766
Step 20: cost = -0.48406896367669106
Step 25: cost = -0.48946382384747267
Step 30: cost = -0.49281889386475086
Step 35: cost = -0.4949494309257716
Step 40: cost = -0.49627021909691393
Step 45: cost = -0.49707187968306243
Prob(real classified as real):  0.9985871425596997
Prob(fake classified as real):  0.5011128038167953
Step 0: cost = -0.5833386033773422
Step 5: cost = -0.8915732949972153
Step 10: cost = -0.9784244522452354
Step 15: cost = -0.9946483590174466
Step 20: cost = -0.9984995491686277
Step 25: cost = -0.9995636216044659
Step 30: cost = -0.9998718172573717
Step 35: cost = -0.9999619696027366
Step 40: cost = -0.9999888275397097
Step 45: cost = -0.999996672290763
Prob(fake classified as real):  0.99999862746688
Discriminator cost:  0.0014114849071802382
Real Bloch vector: [-0.2169418   0.45048445 -0.86602525]
Generator Bloch vector: [-0.2840465   0.41893208 -0.86244407]
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_QGAN.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Step 0: cost = -0.05727699398994446
Step 5: cost = -0.26348118484020233
Step 10: cost = -0.4273917078971863
Step 15: cost = -0.47261589020490646
Step 20: cost = -0.48406901210546494
Step 25: cost = -0.4894639030098915
Step 30: cost = -0.49281900376081467
Step 35: cost = -0.4949493855237961
Step 40: cost = -0.49627020210027695
Step 45: cost = -0.49707192927598953
Prob(real classified as real):  0.9985870718955994
Prob(fake classified as real):  0.5011127963662148
Step 0: cost = -0.583338625729084
Step 5: cost = -0.8915732204914093
Step 10: cost = -0.9784243106842041
Step 15: cost = -0.9946482479572296
Step 20: cost = -0.9984994232654572
Step 25: cost = -0.9995635747909546
Step 30: cost = -0.9998717308044434
Step 35: cost = -0.9999619424343109
Step 40: cost = -0.9999886155128479
Step 45: cost = -0.9999965727329254
Prob(fake classified as real):  0.9999985992908478
Discriminator cost:  0.001411527395248413
Real Bloch vector: [-0.21694186  0.45048442 -0.86602521]
Generator Bloch vector: [-0.28404653  0.41893214 -0.86244416]
 </code>
 </pre>
 </details>

---

## 17. tutorial_backprop.html <a name="demo16"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_backprop.html):

```
180
0.8947771876917632
Forward pass (best of 3): 0.008421205499962526 sec per loop
Gradient computation (best of 3): 3.249689813399982 sec per loop
3.031633979986509
0.9358535378025419
Forward pass (best of 3): 0.06279191759995228 sec per loop
Backward pass (best of 3): 0.12324959990000935 sec per loop
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_backprop.html):

```
/home/runner/work/qml/qml/demonstrations/tutorial_backprop.py:173: UserWarning: The init module will be deprecated soon, since templates can now provide a method that returns the shape of parameter tensors.
180
0.8947771876917632
Forward pass (best of 3): 0.0059497190000001865 sec per loop
Gradient computation (best of 3): 2.2336992747000295 sec per loop
2.141898840000067
/home/runner/work/qml/qml/demonstrations/tutorial_backprop.py:270: UserWarning: The init module will be deprecated soon, since templates can now provide a method that returns the shape of parameter tensors.
0.9358535378025419
```

---

## 18. tutorial_qnn_module_tf.html <a name="demo17"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_qnn_module_tf.html):

```
30/30 - 11s - loss: 0.3931 - accuracy: 0.7067 - val_loss: 0.2683 - val_accuracy: 0.8600
30/30 - 10s - loss: 0.2107 - accuracy: 0.8600 - val_loss: 0.1992 - val_accuracy: 0.8200
30/30 - 11s - loss: 0.1670 - accuracy: 0.8800 - val_loss: 0.1854 - val_accuracy: 0.8600
30/30 - 11s - loss: 0.1602 - accuracy: 0.8800 - val_loss: 0.1732 - val_accuracy: 0.8600
30/30 - 11s - loss: 0.1514 - accuracy: 0.8800 - val_loss: 0.1692 - val_accuracy: 0.8600
30/30 - 11s - loss: 0.1433 - accuracy: 0.8800 - val_loss: 0.1787 - val_accuracy: 0.8200
30/30 - 21s - loss: 0.4068 - accuracy: 0.6600 - val_loss: 0.3008 - val_accuracy: 0.7400
30/30 - 21s - loss: 0.2845 - accuracy: 0.7733 - val_loss: 0.2298 - val_accuracy: 0.8200
30/30 - 21s - loss: 0.2180 - accuracy: 0.8067 - val_loss: 0.1976 - val_accuracy: 0.8200
30/30 - 21s - loss: 0.1904 - accuracy: 0.8533 - val_loss: 0.1809 - val_accuracy: 0.8200
30/30 - 21s - loss: 0.1702 - accuracy: 0.8600 - val_loss: 0.1719 - val_accuracy: 0.8600
30/30 - 21s - loss: 0.1538 - accuracy: 0.8600 - val_loss: 0.1862 - val_accuracy: 0.8400
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_qnn_module_tf.html):

```
30/30 - 6s - loss: 0.3931 - accuracy: 0.7067 - val_loss: 0.2683 - val_accuracy: 0.8600
30/30 - 6s - loss: 0.2107 - accuracy: 0.8600 - val_loss: 0.1992 - val_accuracy: 0.8200
30/30 - 7s - loss: 0.1670 - accuracy: 0.8800 - val_loss: 0.1854 - val_accuracy: 0.8600
30/30 - 6s - loss: 0.1602 - accuracy: 0.8800 - val_loss: 0.1732 - val_accuracy: 0.8600
30/30 - 6s - loss: 0.1514 - accuracy: 0.8800 - val_loss: 0.1692 - val_accuracy: 0.8600
30/30 - 7s - loss: 0.1433 - accuracy: 0.8800 - val_loss: 0.1787 - val_accuracy: 0.8200
30/30 - 13s - loss: 0.4068 - accuracy: 0.6600 - val_loss: 0.3008 - val_accuracy: 0.7400
30/30 - 12s - loss: 0.2845 - accuracy: 0.7733 - val_loss: 0.2298 - val_accuracy: 0.8200
30/30 - 13s - loss: 0.2180 - accuracy: 0.8067 - val_loss: 0.1976 - val_accuracy: 0.8200
30/30 - 13s - loss: 0.1904 - accuracy: 0.8533 - val_loss: 0.1809 - val_accuracy: 0.8200
30/30 - 13s - loss: 0.1702 - accuracy: 0.8600 - val_loss: 0.1719 - val_accuracy: 0.8600
30/30 - 12s - loss: 0.1538 - accuracy: 0.8600 - val_loss: 0.1862 - val_accuracy: 0.8400
```

---

## 19. tutorial_vqe_qng.html <a name="demo18"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_vqe_qng.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
Iteration = 0,  Energy = 0.51052556 Ha,  Convergence parameter = 0.06664604 Ha
Iteration = 20,  Energy = -0.90729965 Ha,  Convergence parameter = 0.05006082 Ha
Iteration = 40,  Energy = -1.35504644 Ha,  Convergence parameter = 0.00713113 Ha
Iteration = 60,  Energy = -1.40833787 Ha,  Convergence parameter = 0.00072399 Ha
Iteration = 80,  Energy = -1.41364035 Ha,  Convergence parameter = 0.00007078 Ha
Iteration = 100,  Energy = -1.41415774 Ha,  Convergence parameter = 0.00000689 Ha
Final value of the energy = -1.41420585 Ha
Number of iterations =  117
Number of qubits =  4
Iteration = 0,  Energy = -0.09424332 Ha
Iteration = 20,  Energy = -0.55156842 Ha
Iteration = 40,  Energy = -1.12731586 Ha
Iteration = 60,  Energy = -1.13583263 Ha
Iteration = 80,  Energy = -1.13602366 Ha
Iteration = 100,  Energy = -1.13611095 Ha
Iteration = 120,  Energy = -1.13615238 Ha
Final convergence parameter = 0.00000097 Ha
Number of iterations =  130
Final value of the ground-state energy = -1.13616398 Ha
Accuracy with respect to the FCI energy: 0.00002547 Ha (0.01598216 kcal/mol)
Final circuit parameters =
 [3.44829694e+00 6.28318531e+00 3.78727399e+00 3.42360201e+00
 5.09234512e-08 4.05827240e+00 2.74944154e+00 6.07360302e+00
 6.24620659e+00 2.40923412e+00 6.28318531e+00 3.32314479e+00]
Iteration = 0,  Energy = -0.32164518 Ha
Iteration = 4,  Energy = -0.46875033 Ha
Iteration = 8,  Energy = -0.85091055 Ha
Iteration = 12,  Energy = -1.13575339 Ha
Iteration = 16,  Energy = -1.13618916 Ha
Final convergence parameter = 0.00000022 Ha
Number of iterations =  17
Final value of the ground-state energy = -1.13618938 Ha
Accuracy with respect to the FCI energy: 0.00000008 Ha (0.00004854 kcal/mol)
Final circuit parameters =
 [3.44829694e+00 6.28318510e+00 3.78727399e+00 3.42360201e+00
 4.03252161e-04 4.05827240e+00 2.74944154e+00 6.07375181e+00
 6.28402001e+00 2.40923412e+00 6.28318525e+00 3.32314479e+00]
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_vqe_qng.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
/opt/hostedtoolcache/Python/3.7.12/x64/lib/python3.7/site-packages/pennylane/transforms/metric_tensor.py:192: UserWarning: The keyword argument diag_approx is deprecated. Please use approx='diag' instead.
Iteration = 0,  Energy = 0.51052556 Ha,  Convergence parameter = 0.06664604 Ha
Iteration = 20,  Energy = -0.90729965 Ha,  Convergence parameter = 0.05006082 Ha
Iteration = 40,  Energy = -1.35504644 Ha,  Convergence parameter = 0.00713113 Ha
Iteration = 60,  Energy = -1.40833787 Ha,  Convergence parameter = 0.00072399 Ha
Iteration = 80,  Energy = -1.41364035 Ha,  Convergence parameter = 0.00007078 Ha
Iteration = 100,  Energy = -1.41415774 Ha,  Convergence parameter = 0.00000689 Ha
Final value of the energy = -1.41420585 Ha
Number of iterations =  117
Number of qubits =  4
Iteration = 0,  Energy = -0.09424332 Ha
Iteration = 20,  Energy = -0.55156842 Ha
Iteration = 40,  Energy = -1.12731586 Ha
Iteration = 60,  Energy = -1.13583263 Ha
Iteration = 80,  Energy = -1.13602366 Ha
Iteration = 100,  Energy = -1.13611095 Ha
Iteration = 120,  Energy = -1.13615238 Ha
Final convergence parameter = 0.00000097 Ha
Number of iterations =  130
Final value of the ground-state energy = -1.13616398 Ha
Accuracy with respect to the FCI energy: 0.00002547 Ha (0.01598216 kcal/mol)
Final circuit parameters =
 [3.44829694e+00 6.28318531e+00 3.78727399e+00 3.42360201e+00
 5.09234513e-08 4.05827240e+00 2.74944154e+00 6.07360302e+00
 6.24620659e+00 2.40923412e+00 6.28318531e+00 3.32314479e+00]
/opt/hostedtoolcache/Python/3.7.12/x64/lib/python3.7/site-packages/pennylane/transforms/metric_tensor.py:192: UserWarning: The keyword argument diag_approx is deprecated. Please use approx='diag' instead.
Iteration = 0,  Energy = -0.32164518 Ha
Iteration = 4,  Energy = -0.46875033 Ha
Iteration = 8,  Energy = -0.85091055 Ha
Iteration = 12,  Energy = -1.13575339 Ha
Iteration = 16,  Energy = -1.13618916 Ha
Final convergence parameter = 0.00000022 Ha
Number of iterations =  17
Final value of the ground-state energy = -1.13618938 Ha
Accuracy with respect to the FCI energy: 0.00000008 Ha (0.00004854 kcal/mol)
Final circuit parameters =
 [3.44829694e+00 6.28318510e+00 3.78727399e+00 3.42360201e+00
 </code>
 </pre>
 </details>

---

## 20. tutorial_doubly_stochastic.html <a name="demo19"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_doubly_stochastic.html):

```
Vanilla gradient descent min energy =  -4.605247234069292
Stochastic gradient descent (shots=100) min energy =  -4.60065517691614
Stochastic gradient descent (shots=1) min energy =  -4.457668962761634
Doubly stochastic gradient descent min energy =  -4.4990195930951575
Adaptive QSGD min energy =  -4.592548741613157
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_doubly_stochastic.html):

```
/home/runner/work/qml/qml/demonstrations/tutorial_doubly_stochastic.py:158: UserWarning: The init module will be deprecated soon, since templates can now provide a method that returns the shape of parameter tensors.
Vanilla gradient descent min energy =  -4.605247234069292
Stochastic gradient descent (shots=100) min energy =  -4.60065517691614
Stochastic gradient descent (shots=1) min energy =  -4.457668962761634
Doubly stochastic gradient descent min energy =  -4.4990195930951575
```

---

## 21. tutorial_quanvolution.html <a name="demo20"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_quanvolution.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
 1056768/11490434 [=>............................] - ETA: 0s
 8273920/11490434 [====================>.........] - ETA: 0s
11493376/11490434 [==============================] - 0s 0us/step
Quantum pre-processing of train images:
1/50
2/50
3/50
4/50
5/50
6/50
7/50
8/50
9/50
10/50
11/50
12/50
13/50
14/50
15/50
16/50
17/50
18/50
19/50
20/50
21/50
22/50
23/50
24/50
25/50
26/50
27/50
28/50
29/50
30/50
31/50
32/50
33/50
34/50
35/50
36/50
37/50
38/50
39/50
40/50
41/50
42/50
43/50
44/50
45/50
46/50
47/50
48/50
49/50
50/50
Quantum pre-processing of test images:
1/30
2/30
3/30
4/30
5/30
6/30
7/30
8/30
9/30
10/30
11/30
12/30
13/30
14/30
15/30
16/30
17/30
18/30
19/30
20/30
21/30
22/30
23/30
24/30
25/30
26/30
27/30
28/30
29/30
30/30
Epoch 1/30
13/13 - 0s - loss: 3.0160 - accuracy: 0.1000 - val_loss: 2.0646 - val_accuracy: 0.2000
Epoch 2/30
13/13 - 0s - loss: 2.2510 - accuracy: 0.1800 - val_loss: 1.9801 - val_accuracy: 0.3333
Epoch 3/30
13/13 - 0s - loss: 1.7851 - accuracy: 0.4000 - val_loss: 1.8177 - val_accuracy: 0.2667
Epoch 4/30
13/13 - 0s - loss: 1.3652 - accuracy: 0.5400 - val_loss: 1.6107 - val_accuracy: 0.4667
Epoch 5/30
13/13 - 0s - loss: 1.1317 - accuracy: 0.7800 - val_loss: 1.4723 - val_accuracy: 0.6000
Epoch 6/30
13/13 - 0s - loss: 0.9360 - accuracy: 0.8600 - val_loss: 1.4686 - val_accuracy: 0.5333
Epoch 7/30
13/13 - 0s - loss: 0.7383 - accuracy: 0.9400 - val_loss: 1.3536 - val_accuracy: 0.5667
Epoch 8/30
13/13 - 0s - loss: 0.5846 - accuracy: 0.9800 - val_loss: 1.2785 - val_accuracy: 0.6667
Epoch 9/30
13/13 - 0s - loss: 0.4987 - accuracy: 0.9800 - val_loss: 1.2253 - val_accuracy: 0.6333
Epoch 10/30
13/13 - 0s - loss: 0.3921 - accuracy: 1.0000 - val_loss: 1.2655 - val_accuracy: 0.6333
Epoch 11/30
13/13 - 0s - loss: 0.3617 - accuracy: 1.0000 - val_loss: 1.1555 - val_accuracy: 0.7000
Epoch 12/30
13/13 - 0s - loss: 0.3078 - accuracy: 1.0000 - val_loss: 1.2107 - val_accuracy: 0.6667
Epoch 13/30
13/13 - 0s - loss: 0.2618 - accuracy: 1.0000 - val_loss: 1.1166 - val_accuracy: 0.7333
Epoch 14/30
13/13 - 0s - loss: 0.2463 - accuracy: 1.0000 - val_loss: 1.0624 - val_accuracy: 0.7000
Epoch 15/30
13/13 - 0s - loss: 0.2033 - accuracy: 1.0000 - val_loss: 1.0904 - val_accuracy: 0.7333
Epoch 16/30
13/13 - 0s - loss: 0.1799 - accuracy: 1.0000 - val_loss: 1.0865 - val_accuracy: 0.7333
Epoch 17/30
13/13 - 0s - loss: 0.1682 - accuracy: 1.0000 - val_loss: 1.0385 - val_accuracy: 0.7333
Epoch 18/30
13/13 - 0s - loss: 0.1484 - accuracy: 1.0000 - val_loss: 1.0676 - val_accuracy: 0.7000
Epoch 19/30
13/13 - 0s - loss: 0.1349 - accuracy: 1.0000 - val_loss: 1.0447 - val_accuracy: 0.7000
Epoch 20/30
13/13 - 0s - loss: 0.1255 - accuracy: 1.0000 - val_loss: 0.9935 - val_accuracy: 0.7333
Epoch 21/30
13/13 - 0s - loss: 0.1135 - accuracy: 1.0000 - val_loss: 1.0451 - val_accuracy: 0.7333
Epoch 22/30
13/13 - 0s - loss: 0.1041 - accuracy: 1.0000 - val_loss: 1.0142 - val_accuracy: 0.7333
Epoch 23/30
13/13 - 0s - loss: 0.0983 - accuracy: 1.0000 - val_loss: 0.9893 - val_accuracy: 0.7333
Epoch 24/30
13/13 - 0s - loss: 0.0913 - accuracy: 1.0000 - val_loss: 0.9807 - val_accuracy: 0.7000
Epoch 25/30
13/13 - 0s - loss: 0.0868 - accuracy: 1.0000 - val_loss: 0.9715 - val_accuracy: 0.7333
Epoch 26/30
13/13 - 0s - loss: 0.0788 - accuracy: 1.0000 - val_loss: 0.9850 - val_accuracy: 0.7333
Epoch 27/30
13/13 - 0s - loss: 0.0749 - accuracy: 1.0000 - val_loss: 0.9750 - val_accuracy: 0.7333
Epoch 28/30
13/13 - 0s - loss: 0.0730 - accuracy: 1.0000 - val_loss: 0.9570 - val_accuracy: 0.7667
Epoch 29/30
13/13 - 0s - loss: 0.0681 - accuracy: 1.0000 - val_loss: 0.9895 - val_accuracy: 0.7333
Epoch 30/30
13/13 - 0s - loss: 0.0635 - accuracy: 1.0000 - val_loss: 0.9560 - val_accuracy: 0.7333
Epoch 1/30
13/13 - 0s - loss: 2.3619 - accuracy: 0.1400 - val_loss: 2.0567 - val_accuracy: 0.3667
Epoch 2/30
13/13 - 0s - loss: 1.9696 - accuracy: 0.4200 - val_loss: 1.9381 - val_accuracy: 0.4667
Epoch 3/30
13/13 - 0s - loss: 1.6671 - accuracy: 0.6400 - val_loss: 1.8300 - val_accuracy: 0.4333
Epoch 4/30
13/13 - 0s - loss: 1.4340 - accuracy: 0.7400 - val_loss: 1.7113 - val_accuracy: 0.4333
Epoch 5/30
13/13 - 0s - loss: 1.2342 - accuracy: 0.7600 - val_loss: 1.6044 - val_accuracy: 0.5000
Epoch 6/30
13/13 - 0s - loss: 1.0721 - accuracy: 0.8600 - val_loss: 1.5232 - val_accuracy: 0.5333
Epoch 7/30
13/13 - 0s - loss: 0.9348 - accuracy: 0.9000 - val_loss: 1.4596 - val_accuracy: 0.5667
Epoch 8/30
13/13 - 0s - loss: 0.8178 - accuracy: 0.9200 - val_loss: 1.3921 - val_accuracy: 0.6000
Epoch 9/30
13/13 - 0s - loss: 0.7223 - accuracy: 0.9400 - val_loss: 1.3404 - val_accuracy: 0.6333
Epoch 10/30
13/13 - 0s - loss: 0.6404 - accuracy: 0.9600 - val_loss: 1.3065 - val_accuracy: 0.6667
Epoch 11/30
13/13 - 0s - loss: 0.5772 - accuracy: 1.0000 - val_loss: 1.2644 - val_accuracy: 0.6333
Epoch 12/30
13/13 - 0s - loss: 0.5199 - accuracy: 1.0000 - val_loss: 1.2558 - val_accuracy: 0.6667
Epoch 13/30
13/13 - 0s - loss: 0.4695 - accuracy: 1.0000 - val_loss: 1.2258 - val_accuracy: 0.6667
Epoch 14/30
13/13 - 0s - loss: 0.4238 - accuracy: 1.0000 - val_loss: 1.1897 - val_accuracy: 0.6667
Epoch 15/30
13/13 - 0s - loss: 0.3848 - accuracy: 1.0000 - val_loss: 1.1651 - val_accuracy: 0.6667
Epoch 16/30
13/13 - 0s - loss: 0.3525 - accuracy: 1.0000 - val_loss: 1.1503 - val_accuracy: 0.7333
Epoch 17/30
13/13 - 0s - loss: 0.3245 - accuracy: 1.0000 - val_loss: 1.1374 - val_accuracy: 0.7000
Epoch 18/30
13/13 - 0s - loss: 0.2992 - accuracy: 1.0000 - val_loss: 1.1174 - val_accuracy: 0.6667
Epoch 19/30
13/13 - 0s - loss: 0.2745 - accuracy: 1.0000 - val_loss: 1.1119 - val_accuracy: 0.6667
Epoch 20/30
13/13 - 0s - loss: 0.2551 - accuracy: 1.0000 - val_loss: 1.0903 - val_accuracy: 0.7000
Epoch 21/30
13/13 - 0s - loss: 0.2370 - accuracy: 1.0000 - val_loss: 1.0877 - val_accuracy: 0.6667
Epoch 22/30
13/13 - 0s - loss: 0.2199 - accuracy: 1.0000 - val_loss: 1.0776 - val_accuracy: 0.6667
Epoch 23/30
13/13 - 0s - loss: 0.2050 - accuracy: 1.0000 - val_loss: 1.0675 - val_accuracy: 0.7000
Epoch 24/30
13/13 - 0s - loss: 0.1919 - accuracy: 1.0000 - val_loss: 1.0592 - val_accuracy: 0.7000
Epoch 25/30
13/13 - 0s - loss: 0.1812 - accuracy: 1.0000 - val_loss: 1.0554 - val_accuracy: 0.6667
Epoch 26/30
13/13 - 0s - loss: 0.1691 - accuracy: 1.0000 - val_loss: 1.0477 - val_accuracy: 0.7000
Epoch 27/30
13/13 - 0s - loss: 0.1599 - accuracy: 1.0000 - val_loss: 1.0377 - val_accuracy: 0.7000
Epoch 28/30
13/13 - 0s - loss: 0.1515 - accuracy: 1.0000 - val_loss: 1.0341 - val_accuracy: 0.6667
Epoch 29/30
13/13 - 0s - loss: 0.1426 - accuracy: 1.0000 - val_loss: 1.0291 - val_accuracy: 0.7000
Epoch 30/30
 </code>
 </pre>
 </details>

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_quanvolution.html):

<details> 
 <summary>
 More 
 </summary>
 <pre>
 <code>
 3915776/11490434 [=========>....................] - ETA: 0s
11493376/11490434 [==============================] - 0s 0us/step
Quantum pre-processing of train images:
1/50
2/50
3/50
4/50
5/50
6/50
7/50
8/50
9/50
10/50
11/50
12/50
13/50
14/50
15/50
16/50
17/50
18/50
19/50
20/50
21/50
22/50
23/50
24/50
25/50
26/50
27/50
28/50
29/50
30/50
31/50
32/50
33/50
34/50
35/50
36/50
37/50
38/50
39/50
40/50
41/50
42/50
43/50
44/50
45/50
46/50
47/50
48/50
49/50
50/50
Quantum pre-processing of test images:
1/30
2/30
3/30
4/30
5/30
6/30
7/30
8/30
9/30
10/30
11/30
12/30
13/30
14/30
15/30
16/30
17/30
18/30
19/30
20/30
21/30
22/30
23/30
24/30
25/30
26/30
27/30
28/30
29/30
30/30
Epoch 1/30
13/13 - 0s - loss: 3.0160 - accuracy: 0.1000 - val_loss: 2.0646 - val_accuracy: 0.2000
Epoch 2/30
13/13 - 0s - loss: 2.2510 - accuracy: 0.1800 - val_loss: 1.9801 - val_accuracy: 0.3333
Epoch 3/30
13/13 - 0s - loss: 1.7851 - accuracy: 0.4000 - val_loss: 1.8177 - val_accuracy: 0.2667
Epoch 4/30
13/13 - 0s - loss: 1.3652 - accuracy: 0.5400 - val_loss: 1.6107 - val_accuracy: 0.4667
Epoch 5/30
13/13 - 0s - loss: 1.1317 - accuracy: 0.7800 - val_loss: 1.4723 - val_accuracy: 0.6000
Epoch 6/30
13/13 - 0s - loss: 0.9360 - accuracy: 0.8600 - val_loss: 1.4686 - val_accuracy: 0.5333
Epoch 7/30
13/13 - 0s - loss: 0.7383 - accuracy: 0.9400 - val_loss: 1.3536 - val_accuracy: 0.5667
Epoch 8/30
13/13 - 0s - loss: 0.5846 - accuracy: 0.9800 - val_loss: 1.2785 - val_accuracy: 0.6667
Epoch 9/30
13/13 - 0s - loss: 0.4987 - accuracy: 0.9800 - val_loss: 1.2253 - val_accuracy: 0.6333
Epoch 10/30
13/13 - 0s - loss: 0.3921 - accuracy: 1.0000 - val_loss: 1.2655 - val_accuracy: 0.6333
Epoch 11/30
13/13 - 0s - loss: 0.3617 - accuracy: 1.0000 - val_loss: 1.1555 - val_accuracy: 0.7000
Epoch 12/30
13/13 - 0s - loss: 0.3078 - accuracy: 1.0000 - val_loss: 1.2107 - val_accuracy: 0.6667
Epoch 13/30
13/13 - 0s - loss: 0.2618 - accuracy: 1.0000 - val_loss: 1.1166 - val_accuracy: 0.7333
Epoch 14/30
13/13 - 0s - loss: 0.2463 - accuracy: 1.0000 - val_loss: 1.0624 - val_accuracy: 0.7000
Epoch 15/30
13/13 - 0s - loss: 0.2033 - accuracy: 1.0000 - val_loss: 1.0904 - val_accuracy: 0.7333
Epoch 16/30
13/13 - 0s - loss: 0.1799 - accuracy: 1.0000 - val_loss: 1.0865 - val_accuracy: 0.7333
Epoch 17/30
13/13 - 0s - loss: 0.1682 - accuracy: 1.0000 - val_loss: 1.0385 - val_accuracy: 0.7333
Epoch 18/30
13/13 - 0s - loss: 0.1484 - accuracy: 1.0000 - val_loss: 1.0676 - val_accuracy: 0.7000
Epoch 19/30
13/13 - 0s - loss: 0.1349 - accuracy: 1.0000 - val_loss: 1.0447 - val_accuracy: 0.7000
Epoch 20/30
13/13 - 0s - loss: 0.1255 - accuracy: 1.0000 - val_loss: 0.9935 - val_accuracy: 0.7333
Epoch 21/30
13/13 - 0s - loss: 0.1135 - accuracy: 1.0000 - val_loss: 1.0451 - val_accuracy: 0.7333
Epoch 22/30
13/13 - 0s - loss: 0.1041 - accuracy: 1.0000 - val_loss: 1.0142 - val_accuracy: 0.7333
Epoch 23/30
13/13 - 0s - loss: 0.0983 - accuracy: 1.0000 - val_loss: 0.9893 - val_accuracy: 0.7333
Epoch 24/30
13/13 - 0s - loss: 0.0913 - accuracy: 1.0000 - val_loss: 0.9807 - val_accuracy: 0.7000
Epoch 25/30
13/13 - 0s - loss: 0.0868 - accuracy: 1.0000 - val_loss: 0.9715 - val_accuracy: 0.7333
Epoch 26/30
13/13 - 0s - loss: 0.0788 - accuracy: 1.0000 - val_loss: 0.9850 - val_accuracy: 0.7333
Epoch 27/30
13/13 - 0s - loss: 0.0749 - accuracy: 1.0000 - val_loss: 0.9750 - val_accuracy: 0.7333
Epoch 28/30
13/13 - 0s - loss: 0.0730 - accuracy: 1.0000 - val_loss: 0.9570 - val_accuracy: 0.7667
Epoch 29/30
13/13 - 0s - loss: 0.0681 - accuracy: 1.0000 - val_loss: 0.9895 - val_accuracy: 0.7333
Epoch 30/30
13/13 - 0s - loss: 0.0635 - accuracy: 1.0000 - val_loss: 0.9560 - val_accuracy: 0.7333
Epoch 1/30
13/13 - 0s - loss: 2.3619 - accuracy: 0.1400 - val_loss: 2.0567 - val_accuracy: 0.3667
Epoch 2/30
13/13 - 0s - loss: 1.9696 - accuracy: 0.4200 - val_loss: 1.9381 - val_accuracy: 0.4667
Epoch 3/30
13/13 - 0s - loss: 1.6671 - accuracy: 0.6400 - val_loss: 1.8300 - val_accuracy: 0.4333
Epoch 4/30
13/13 - 0s - loss: 1.4340 - accuracy: 0.7400 - val_loss: 1.7113 - val_accuracy: 0.4333
Epoch 5/30
13/13 - 0s - loss: 1.2342 - accuracy: 0.7600 - val_loss: 1.6044 - val_accuracy: 0.5000
Epoch 6/30
13/13 - 0s - loss: 1.0721 - accuracy: 0.8600 - val_loss: 1.5232 - val_accuracy: 0.5333
Epoch 7/30
13/13 - 0s - loss: 0.9348 - accuracy: 0.9000 - val_loss: 1.4596 - val_accuracy: 0.5667
Epoch 8/30
13/13 - 0s - loss: 0.8178 - accuracy: 0.9200 - val_loss: 1.3921 - val_accuracy: 0.6000
Epoch 9/30
13/13 - 0s - loss: 0.7223 - accuracy: 0.9400 - val_loss: 1.3404 - val_accuracy: 0.6333
Epoch 10/30
13/13 - 0s - loss: 0.6404 - accuracy: 0.9600 - val_loss: 1.3065 - val_accuracy: 0.6667
Epoch 11/30
13/13 - 0s - loss: 0.5772 - accuracy: 1.0000 - val_loss: 1.2644 - val_accuracy: 0.6333
Epoch 12/30
13/13 - 0s - loss: 0.5199 - accuracy: 1.0000 - val_loss: 1.2558 - val_accuracy: 0.6667
Epoch 13/30
13/13 - 0s - loss: 0.4695 - accuracy: 1.0000 - val_loss: 1.2258 - val_accuracy: 0.6667
Epoch 14/30
13/13 - 0s - loss: 0.4238 - accuracy: 1.0000 - val_loss: 1.1897 - val_accuracy: 0.6667
Epoch 15/30
13/13 - 0s - loss: 0.3848 - accuracy: 1.0000 - val_loss: 1.1651 - val_accuracy: 0.6667
Epoch 16/30
13/13 - 0s - loss: 0.3525 - accuracy: 1.0000 - val_loss: 1.1503 - val_accuracy: 0.7333
Epoch 17/30
13/13 - 0s - loss: 0.3245 - accuracy: 1.0000 - val_loss: 1.1374 - val_accuracy: 0.7000
Epoch 18/30
13/13 - 0s - loss: 0.2992 - accuracy: 1.0000 - val_loss: 1.1174 - val_accuracy: 0.6667
Epoch 19/30
13/13 - 0s - loss: 0.2745 - accuracy: 1.0000 - val_loss: 1.1119 - val_accuracy: 0.6667
Epoch 20/30
13/13 - 0s - loss: 0.2551 - accuracy: 1.0000 - val_loss: 1.0903 - val_accuracy: 0.7000
Epoch 21/30
13/13 - 0s - loss: 0.2370 - accuracy: 1.0000 - val_loss: 1.0877 - val_accuracy: 0.6667
Epoch 22/30
13/13 - 0s - loss: 0.2199 - accuracy: 1.0000 - val_loss: 1.0776 - val_accuracy: 0.6667
Epoch 23/30
13/13 - 0s - loss: 0.2050 - accuracy: 1.0000 - val_loss: 1.0675 - val_accuracy: 0.7000
Epoch 24/30
13/13 - 0s - loss: 0.1919 - accuracy: 1.0000 - val_loss: 1.0592 - val_accuracy: 0.7000
Epoch 25/30
13/13 - 0s - loss: 0.1812 - accuracy: 1.0000 - val_loss: 1.0554 - val_accuracy: 0.6667
Epoch 26/30
13/13 - 0s - loss: 0.1691 - accuracy: 1.0000 - val_loss: 1.0477 - val_accuracy: 0.7000
Epoch 27/30
13/13 - 0s - loss: 0.1599 - accuracy: 1.0000 - val_loss: 1.0377 - val_accuracy: 0.7000
Epoch 28/30
13/13 - 0s - loss: 0.1515 - accuracy: 1.0000 - val_loss: 1.0341 - val_accuracy: 0.6667
Epoch 29/30
13/13 - 0s - loss: 0.1426 - accuracy: 1.0000 - val_loss: 1.0291 - val_accuracy: 0.7000
Epoch 30/30
13/13 - 0s - loss: 0.1344 - accuracy: 1.0000 - val_loss: 1.0264 - val_accuracy: 0.7000
 </code>
 </pre>
 </details>

---

## 22. tutorial_ensemble_multi_qpu.html <a name="demo21"></a>

---

[Master](https://pennylane.ai/qml/demos/tutorial_ensemble_multi_qpu.html):

```
Choices counts: Counter({0: 112, 1: 38})
Counter({2: 57, 0: 55})
Choices: [0 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0 0 1 1 0 0 1 0 1 1 0 0 0 1 0 0 1 0 1 0 0 0
Counter({1: 35, 0: 3})
```

[Dev](http://pennylane.ai-dev.s3-website-us-east-1.amazonaws.com/qml/demos/tutorial_ensemble_multi_qpu.html):

```
Choices counts: Counter({0: 110, 1: 40})
Counter({0: 55, 2: 55})
Choices: [0 0 1 1 0 0 1 1 0 0 1 0 0 0 0 0 0 1 1 0 0 1 0 1 1 0 0 0 1 0 0 1 0 1 0 0 0
Counter({1: 37, 0: 3})
```

---

