%define name ii
%define version 1.4
%define release 4

Name:		%name
Version:	%version
Release:	%release
Group:		Networking/Other
URL:		http://tools.suckless.org/ii
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
Source0:	http://code.suckless.org/dl/tools/%{name}-%{version}.tar.gz
Summary:	Minimalist FIFO and filesystem-based IRC client
%description
ii is a minimalist FIFO and filesystem-based IRC client. It creates an
irc directory tree with server, channel and nick name directories. In
every directory a FIFO in file and a normal out file is created.

The in file is used to communicate with the servers and the out files
contain the server messages. For every channel and every nick name there
are related in and out files created. This allows IRC communication from
command line and adheres to the Unix philosophy. example

Join a channel as follows: $ echo "/j #wmii" > in and ii creates a
new #wmii (channel) directory with in and out files.

It consists of <= 500 lines of code and is the big brother of sic (simple
irc client).

%prep
%setup -q

%build
make

%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install
%{__rm} -Rf $RPM_BUILD_ROOT/usr/share/doc/ii

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE FAQ query.sh
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2011.0
+ Revision: 619612
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.4-2mdv2010.0
+ Revision: 437956
- rebuild

* Fri Mar 20 2009 Nicolas Vigier <nvigier@mandriva.com> 1.4-1mdv2009.1
+ Revision: 359083
- version 1.4

* Fri Feb 13 2009 Michael Scherer <misc@mandriva.org> 1.3-4mdv2009.1
+ Revision: 340023
- new url

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 247212
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.3-1mdv2008.1
+ Revision: 168420
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 13 2007 Nicolas Vigier <nvigier@mandriva.com> 1.3-1mdv2008.0
+ Revision: 62425
- new version 1.3

* Tue Jun 19 2007 Nicolas Vigier <nvigier@mandriva.com> 1.1-1mdv2008.0
+ Revision: 41290
- Import ii

