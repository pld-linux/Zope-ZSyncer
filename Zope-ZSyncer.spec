%define		zope_subname	ZSyncer
%define		sub_ver beta3
Summary:	Project allows multiple Zopes to easily be manually synchronized
Summary(pl.UTF-8):   Projekt pozwalający na synchronizowanie obiektów między różnymi serwisami Zope
Name:		Zope-%{zope_subname}
Version:	0.6.0
Release:	0.%{sub_ver}.2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/zsyncer/%{zope_subname}-%{version}-%{sub_ver}.tgz
# Source0-md5:	0615800bc97be463dabe11c46c848bb0
URL:		http://sourceforge.net/projects/zsyncer/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZSyncer project allows multiple Zopes to easily be manually
synchronized by transferring data between them using xml-rpc.

%description -l pl.UTF-8
Projekt ZSyncer pozwala synchronizować obiekty między różnymi
serwisami Zope, korzystając z xml-rpc.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,help,skins,www,*.py,*.gif,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc credits.txt README.txt changes.txt TODO.txt
%{_datadir}/%{name}
