%define		zope_subname	ZSyncer
Summary:	Project allows multiple Zopes to easily be manually synchronized
Summary(pl):	Projekt pozwala synchronizowaæ obiekty miêdzy ró¿nymi serwisami Zope
Name:		Zope-%{zope_subname}
Version:	0.6.0
%define		sub_ver beta2
Release:	0.%{sub_ver}.1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/zsyncer/%{zope_subname}-%{version}-%{sub_ver}.tgz
# Source0-md5:	04d448c64c37caf1aff00dab222b1803
URL:		http://sourceforge.net/projects/zsyncer/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZSyncer project allows multiple Zopes to easily be manually
synchronized by transferring data between them using xml-rpc.

%description -l pl
Projekt ZSyncer pozwala synchronizowaæ obiekty miêdzy ró¿nymi
serwisami Zope, korzystaj±c z xml-rpc.

%prep
%setup -q -n %{zope_subname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,help,skin,skins,www,*.py,*.gif,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc credits.txt README.txt changes.txt TODO.txt
%{_datadir}/%{name}
