Name:       hesabdesk
Version:    1.5.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://hesabdesk.com
Vendor:     hesabdesk <info@hesabdesk.com>
Requires:   gtk3 libxcb libXfixes alsa-lib libva gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3 libxdo
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/hesabdesk" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/hesabdesk"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/hesabdesk.service -t "%{buildroot}/usr/share/hesabdesk/files"
install -Dm 644 $HBB/res/hesabdesk.desktop -t "%{buildroot}/usr/share/hesabdesk/files"
install -Dm 644 $HBB/res/hesabdesk-link.desktop -t "%{buildroot}/usr/share/hesabdesk/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/hesabdesk.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/hesabdesk.svg"

%files
/usr/share/hesabdesk/*
/usr/share/hesabdesk/files/hesabdesk.service
/usr/share/icons/hicolor/256x256/apps/hesabdesk.png
/usr/share/icons/hicolor/scalable/apps/hesabdesk.svg
/usr/share/hesabdesk/files/hesabdesk.desktop
/usr/share/hesabdesk/files/hesabdesk-link.desktop

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop hesabdesk || true
  ;;
esac

%post
cp /usr/share/hesabdesk/files/hesabdesk.service /etc/systemd/system/hesabdesk.service
cp /usr/share/hesabdesk/files/hesabdesk.desktop /usr/share/applications/
cp /usr/share/hesabdesk/files/hesabdesk-link.desktop /usr/share/applications/
ln -sf /usr/share/hesabdesk/hesabdesk /usr/bin/hesabdesk
systemctl daemon-reload
systemctl enable hesabdesk
systemctl start hesabdesk
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop hesabdesk || true
    systemctl disable hesabdesk || true
    rm /etc/systemd/system/hesabdesk.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/bin/hesabdesk || true
    rmdir /usr/lib/hesabdesk || true
    rmdir /usr/local/hesabdesk || true
    rmdir /usr/share/hesabdesk || true
    rm /usr/share/applications/hesabdesk.desktop || true
    rm /usr/share/applications/hesabdesk-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
    rmdir /usr/lib/hesabdesk || true
    rmdir /usr/local/hesabdesk || true
  ;;
esac
