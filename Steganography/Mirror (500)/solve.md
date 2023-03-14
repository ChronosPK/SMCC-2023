## Solve:
<br>

1. FIrst 16 bytes from the PNG header have been reversed 2 by 2 <br>
  `mv mirror.txt mirror.png ; hexeditor mirror` <br><br>
  from `98 05 E4 74  D0 A0 A1 A0   00 00 00 D0  94 84 44 25`<br>
  to   `89 50 4E 47  0D 0A 1A 0A   00 00 00 0D  49 48 44 52`

<br>

2. decode qr code with `zbarimg` <br>
  `zbarimg mirror.png`<br><br>
  QR-Code: 
  ```plain
  h_t_t_p_s_:_/_/_d_r_i_v_e_._g_o_o_g_l_e_._c_o_m_/_u_c_?_e_x_p_o_r_t_=_d_o_w_n_l_o_a_d_&_i_d_=_1_g_z_a_t_l_P_w_D_G_A_8_j_Z_P_Q_Q_F_z_J_9_E_e_T_b_n___-_X_b_d_a_k
  ```

<br>

3. remove extra "`_`" and download file  
https://drive.google.com/uc?export=download&id=1gzatlPwDGA8jZPQQFzJ9EeTbn_-Xbdak <br>
```python3
$ python3
>>> link='h_t_t_p_s_:_/_/_d_r_i_v_e_._g_o_o_g_l_e_._c_o_m_/_u_c_?_e_x_p_o_r_t_=_d_o_w_n_l_o_a_d_&_i_d_=_1_g_z_a_t_l_P_w_D_G_A_8_j_Z_P_Q_Q_F_z_J_9_E_e_T_b_n___-_X_b_d_a_k'
>>> print(''.join([link[i] for i in range(0,len(link),2)]))
```
<br>

4. crack hashes online 
  get flag: `f5b480afec38e90861cff0df8a52d685` -> `iloveyou14`

<br><br>

## Flag:
`flag{iloveyou14}`
