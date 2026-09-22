Name:       hesabdesk
Version:    1.5.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://hesabdesk.com
Vendor:     hesabdesk <info@hesabdesk.com>
Requires:   gtk3 libxcb libXfixes alsa-lib libva2 gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3 libxdo

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/hesabdesk/
mkdir -p %{buildroot}/usr/share/hesabdesk/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/hesabdesk %{buildroot}/usr/bin/hesabdesk
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/hesabdesk/libsciter-gtk.so
install $HBB/res/hesabdesk.service %{buildroot}/usr/share/hesabdesk/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/hesabdesk.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/hesabdesk.svg
install $HBB/res/hesabdesk.desktop %{buildroot}/usr/share/hesabdesk/files/
install $HBB/res/hesabdesk-link.desktop %{buildroot}/usr/share/hesabdesk/files/

%files
/usr/bin/hesabdesk
/usr/share/hesabdesk/libsciter-gtk.so
/usr/share/hesabdesk/files/hesabdesk.service
/usr/share/icons/hicolor/256x256/apps/hesabdesk.png
/usr/share/icons/hicolor/scalable/apps/hesabdesk.svg
/usr/share/hesabdesk/files/hesabdesk.desktop
/usr/share/hesabdesk/files/hesabdesk-link.desktop
/usr/share/hesabdesk/files/__pycache__/*

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
    rm /usr/share/applications/hesabdesk.desktop || true
    rm /usr/share/applications/hesabdesk-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
