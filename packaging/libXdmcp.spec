
Name:       libXdmcp
Summary:    X.Org X11 libXdmcp runtime library
Version:    1.1.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}


%package devel
Summary:    Development components for the libXdmcp library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXdmcp.so.6
%{_libdir}/libXdmcp.so.6.0.0


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/
%{_includedir}/X11/Xdmcp.h
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_docdir}/%{name}

