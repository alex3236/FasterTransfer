# :rocket: FasterTransfer

[![](https://pic.stackoverflow.wiki/uploadImages/117/24/20/154/2021/08/24/23/08/8cd61849-6a34-4e2d-ad3a-c6056adef05e.svg)](https://github.com/Fallen-Breath/MCDReforged)

让 **任何 MCDR 插件**，比如 QuickBackupM 的网络文件传输更迅速！

## :warning: 声明

:earth_asia:  此插件仅对网络传输（如备份到 NAS）的用户有效。

:gear: 此插件仅对使用 `shutil.copy*` 方法的插件有效。

:question: 理论上，此插件不会造成文件传输异常。但如果你发现其他插件出现了未知原因的文件传输异常，尝试禁用此插件。

:open_file_folder:  只有当源文件和目标文件都在同一个 SMB1(CIFS)/2/3 文件系统上时，此插件生效。

## :door:		前置

- speedcopy

## :page_facing_up: 使用说明

只需要扔进插件文件夹并正常载入。无需任何配置。

### :arrow_forward:	启用插件

```plain
!!MCDR plugin enable faster_transfer
```

### :stop_button: 禁用插件

```plain
!!MCDR plugin disable faster_transfer
```

## :gear: 原理

使用 [speedcopy](https://github.com/antirotor/speedcopy) 库对 `shutil.copyfile` 进行补丁。speedcopy 对其的描述如下：

> Patched python shutil.copyfile using native call CopyFile2 on windows to accelerate transfer on windows shares. On Linux, it issues special ioctl command CIFS_IOC_COPYCHUNK_FILE to enable server-side copy.
