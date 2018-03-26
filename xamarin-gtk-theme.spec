Summary:        Xamarin theme engine and themes for GTK+ 2.0
Name:           xamarin-gtk-theme
Version:        0.2017.05.24.11.51
Release:	0.xamarin.0
# for details on which engines are GPL vs LGPL, see COPYING
License:        LGPLv2+
Group:          System Environment/Libraries
Source:         %{name}-%{version}.tar.gz
Source1:        gtkrc-dark.patch
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  pkgconfig
URL:           	https://github.com/mono/xamarin-gtk-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
Package with Xamarin Gtk+2 themes, for better look inside MonoDevelop

%prep
%setup -q -n xamarin-gtk-theme-master

%build
./autogen.sh
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/Xamarin-Dark/gtk-2.0
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/Xamarin-Dark/gtk-2.0/gtkrc

# no .la, please
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs rm

# sanitize permissions
find $RPM_BUILD_ROOT%{_datadir}/themes -type d -exec chmod 755 {} \;
find $RPM_BUILD_ROOT%{_datadir}/themes -type f -name "*.png" -exec chmod 644 {} \;
find $RPM_BUILD_ROOT%{_datadir}/themes -name "gtkrc*" -perm +111 -exec chmod 644 {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README AUTHORS NEWS COPYING
%attr (755, root, root) %{_libdir}/gtk-2.0/2.10.0/engines/*.so
%{_datadir}/themes/*
%{_datadir}/gtk-engines
