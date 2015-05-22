# TODO:
# - dir /usr/include/KF5 not packaged
# /usr/share/kservicetypes5 not packaged
%define		kdeframever	5.10
%define		qtver		5.3.2
%define		kfname		kservice

Summary:	Plugin framework for desktop services
Name:		kf5-%{kfname}
Version:	5.10.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	204fc310ebcbd7e15e8da30fac48416f
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kcrash-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KService provides a plugin framework for handling desktop services.
Services can be applications or libraries. They can be bound to MIME
types or handled by application specific code.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/menus/applications.menu
%attr(755,root,root) %{_bindir}/kbuildsycoca5
%attr(755,root,root) %ghost %{_libdir}/libKF5Service.so.5
%attr(755,root,root) %{_libdir}/libKF5Service.so.*.*
%{_datadir}/kservicetypes5/application.desktop
%{_datadir}/kservicetypes5/kplugininfo.desktop
%{_mandir}/man8/kbuildsycoca5.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KService
%{_includedir}/KF5/kservice_version.h
%{_libdir}/cmake/KF5Service
%attr(755,root,root) %{_libdir}/libKF5Service.so
%{qt5dir}/mkspecs/modules/qt_KService.pri
