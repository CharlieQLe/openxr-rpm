Name:           monado
Version:        24.0.0
Release:        %autorelease
Summary:        XR runtime
License:        MIT
URL:            https://gitlab.freedesktop.org/monado/monado

Source0:        https://gitlab.freedesktop.org/monado/monado/-/archive/v%version/monado-v%version.tar.gz

Patch0:         now_ns_and_no_dropped_frames.patch

BuildRequires:  cmake >= 3.13.0
BuildRequires:  python >= 3.6
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(libonnxruntime)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libuvc)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xrandr)

%description
Monado is an open source XR runtime delivering immersive
experiences such as VR and AR on mobile, PC/desktop, and
other devices.

%package        devel
Summary:        Development files for %name
Requires:       %name%{?_isa} = %version

%description    devel
Development files for %name.

%package        steamvr
Summary:        SteamVR driver for %name
Requires:       %name%{?_isa} = %version

%description    steamvr
SteamVR driver for %name.

%prep
%autosetup -n %name-v%version -S git
%cmake -DXRT_HAVE_STEAM=YES

%build
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/monado-ctl
%{_bindir}/monado-cli
%{_bindir}/monado-gui
%caps(cap_sys_nice=eip) %{_bindir}/monado-service
%{_libdir}/libmonado.so.24
%{_libdir}/libmonado.so.24.0.0
%{_libdir}/libmonado.so
%{_libdir}/libopenxr_monado.so
%{_datadir}/openxr/1/openxr_monado.json
%{_userunitdir}/monado.socket
%{_userunitdir}/monado.service

%files devel
%{_includedir}/%name/

%files steamvr
%{_datadir}/steamvr-monado/

%changelog
%autochangelog
