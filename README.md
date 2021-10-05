# :rocket: FasterTransfer

[![](https://pic.stackoverflow.wiki/uploadImages/117/24/20/154/2021/08/24/23/08/8cd61849-6a34-4e2d-ad3a-c6056adef05e.svg)](https://github.com/Fallen-Breath/MCDReforged)

让 **任何 MCDR 插件**，比如 QuickBackupM 的网络文件传输更迅速！

## :warning: 注意

:earth_asia:  **此插件仅对网络传输（如备份到 NAS）的用户有效。**

:gear: **此插件仅对使用 `shutil.copy*` 方法的插件有效。**

:question: **理论上，此插件不会造成文件传输异常。但如果你发现其他插件出现了未知原因的文件传输异常，尝试禁用此插件。**

:open_file_folder:  **只有当源文件和目标文件都在同一个 SMB1(CIFS)/2/3 文件系统上时，此插件生效。**

## :door:		前置

- speedcopy

## :page_facing_up: 使用说明

只需要扔进插件文件夹并正常载入。无需任何配置。

### :arrow_forward:	启用插件

```plain
若已禁用:
!!MCDR plugin enable FasterTransfer-vx.x.x.mcdr.disabled
若未禁用:
!!MCDR plugin enable FasterTransfer-vx.x.x.mcdr
```

### :stop_button: 禁用插件

```plain
!!MCDR plugin disable faster_transfer
```

## :gear: 原理

使用 [speedcopy](https://github.com/antirotor/speedcopy) 库对 `shutil.copyfile` 进行补丁。speedcopy 对其的描述如下：

> Patched python shutil.copyfile using native call CopyFile2 on windows to accelerate transfer on windows shares. On Linux, it issues special ioctl command CIFS_IOC_COPYCHUNK_FILE to enable server-side copy.

## 🧪 测试

使用 speedcopy 自带的 [benchmark.py](https://github.com/antirotor/speedcopy/blob/develop/benchmark.py) 进行测试。

#### Windows 本地传输

| File Size (Mb) | shutil    | speedcopy | Boost |
|----------------|-----------|-----------|-------|
| 1              | 0.001648  | 0.001188  | 1.39  |
| 2              | 0.002469  | 0.002038  | 1.21  |
| 4              | 0.004557  | 0.004314  | 1.06  |
| 8              | 0.008214  | 0.007292  | 1.13  |
| 16             | 0.014797  | 0.015179  | 0.97  |
| 32             | 0.031783  | 0.029366  | 1.08  |
| 64             | 0.577100  | 0.564356  | 1.02  |
| 128            | 0.117948  | 0.110211  | 1.07  |
| 256            | 0.289941  | 0.223379  | 1.30  |
| 512            | 1.144847  | 1.259522  | 0.91  |

#### Windows 局域网传输

| File Size (Mb) | shutil     | speedcopy  | Boost  |
|----------------|------------|------------|--------|
| 1              | 0.043559   | 0.025601   | 1.70   |
| 2              | 0.140894   | 0.068142   | 2.07   |
| 4              | 0.317707   | 0.120199   | 2.64   |
| 8              | 0.624333   | 0.050211   | 12.43  |
| 16             | 1.304758   | 0.105648   | 12.35  |
| 32             | 2.312098   | 0.066612   | 34.71  |
| 64             | 25.437534  | 6.052502   | 4.20   |
| 128            | 19.883221  | 0.203415   | 97.75  |
| 256            | 63.355960  | 15.306027  | 4.14   |
| 512            | 32.945394  | 21.032490  | 1.57   |

#### Linux 本地传输

| File Size (Mb) | shutil    | speedcopy | Boost |
|----------------|-----------|-----------|-------|
| 1              | 0.005928  | 0.007161  | 0.83  |
| 2              | 0.014908  | 0.014864  | 1.00  |
| 4              | 0.029801  | 0.029778  | 1.00  |
| 8              | 0.060115  | 0.059993  | 1.00  |
| 16             | 0.120967  | 0.119723  | 1.01  |
| 32             | 0.240052  | 0.239115  | 1.00  |

#### Linux 局域网传输（speedcopy 官方数据）

| File Size (Mb) | shutil | speedcopy | Boost |
| --- | --- | --- | --- |
| 1 | 0.0682 | 0.0099 | 6.88 |
| 2 | 0.0894 | 0.0105 | 8.51 |
| 4 | 0.1337 | 0.012 | 11.14 |
| 8 | 0.1922 | 0.0145 | 13.25 |
| 16 | 0.2853 | 0.0193 | 14.78 |
| 32 | 0.4724 | 0.0288 | 16.4 |
| 64 | 8.0071 | 0.4724 | 16.94 |
| 128 | 1.3338 | 0.2311 | 5.77 |
| 256 | 2.6599 | 0.4788 | 5.55 |
| 512 | 5.3798 | 0.9796 | 5.49 |
| 1024 | 10.3328 | 2.9180 | 3.54 |

### 💯 结论
只建议使用网络文件传输（NAS 等）的用户使用。

