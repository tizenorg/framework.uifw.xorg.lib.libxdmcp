Summary: X Display Manager Control Protocol library
Name: libXdmcp
Version: 1.1.1
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
X Display Manager Control Protocol library.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: libxdmcp-devel
Requires: %{name} = %{version}-%{release}

%description devel
libXdmcp development package.

%prep
%setup -q

%build
%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# manual fixup later
rm -rf $RPM_BUILD_ROOT%{_docdir}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc AUTHORS COPYING ChangeLog Wraphelp.README.crypto
%{_libdir}/libXdmcp.so.6
%{_libdir}/libXdmcp.so.6.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/Xdmcp.h
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc

