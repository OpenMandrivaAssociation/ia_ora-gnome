# SOURCE IS STORED IN SVN (soft/theme/ia_ora-gnome), 
# DO NOT PATCH IT

%define libname %{_lib}ia_ora-gnome

Summary:        Ia Ora Mandriva GNOME theme
Name:           ia_ora-gnome
Version:        1.0.20
Release:        %mkrel 3
License:        GPL
Group: Graphical desktop/GNOME
URL:            http://www.mandrivalinux.com/
BuildRequires:  gtk+2-devel
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: gnome-icon-theme
Requires: ia_ora-gnome-gtk2-engine

%description
Mandriva Ia Ora GNOME theme

%package -n %{libname}
Summary: GTK2 engine for Ia Ora theme
Group: System/Libraries
Provides: ia_ora-gnome-gtk2-engine

%description -n %{libname}
GTK2 engine for Ia Ora theme
 
%prep
%setup -q 

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

#remove unpackaged files 
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la 

mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/Ia\ Ora\ Free $RPM_BUILD_ROOT%{_datadir}/themes/Ia\ Ora\ One

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -d %{_datadir}/themes/Ia\ Ora\ Free -a ! -L %{_datadir}/themes/Ia\ Ora\ Free ]; then 
 /bin/rm -rf %{_datadir}/themes/Ia\ Ora\ Free/* || /bin/true
fi

if [ -d %{_datadir}/themes/Ia\ Ora\ One -a ! -L %{_datadir}/themes/Ia\ Ora\ One ]; then 
 /bin/rm -rf %{_datadir}/themes/Ia\ Ora\ One/* || bin/true
fi

%posttrans
# create compatibility symlinks
ln -f -s ../Ia\ Ora\ Smooth/metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/Ia\ Ora\ One/metacity-1
ln -f -s ../Ia\ Ora\ Smooth/gtk-2.0 $RPM_BUILD_ROOT%{_datadir}/themes/Ia\ Ora\ One/gtk-2.0
ln -f -s ../Ia\ Ora\ Arctic/metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/Ia\ Ora\ Free/metacity-1
ln -f -s ../Ia\ Ora\ Arctic/gtk-2.0 $RPM_BUILD_ROOT%{_datadir}/themes/Ia\ Ora\ Free/gtk-2.0

%preun 
if [ "$1" = "0" ]; then
 /bin/rm -f %{_datadir}/themes/Ia\ Ora\ Free/* %{_datadir}/themes/Ia\ Ora\ One/*   || /bin/true
fi


%files 
%defattr(-,root,root,-)
%doc README 
%{_datadir}/themes/*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/gtk-2.0/*/engines/*.so

