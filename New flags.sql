rollback;
begin;

alter table public.mntr
add column flag_340B varchar(50);
alter table public.mntr
add column flag_medicare_part_d varchar(50);
alter table public.mntr
add column flag_medicare_part_d varchar(50);
alter table public.mntr
add column flag_fda_modernization varchar(50);
alter table public.mntr
add column flag_intellectual_property varchar(50);

update public.mntr
set flag_340B=
    case 
    when content_sans_https like '%340b program%' then 'Yes'
    when content_sans_https like '%help act%' then 'Yes'
    when content_sans_https like '%340b pause act%' then 'Yes'
    when content_sans_https like '%contract pharmacy%' then 'Yes'
    when content_sans_https like '%child site%' then 'Yes'
    when content_sans_https like '%drug discount program%' then  'Yes'
    when content_sans_https like '%disproportionate share hospital%' then  'Yes'
    when content_sans_https like '%dsh hospital%' then  'Yes'
    when content_sans_https like '%safety-net programs%' then  'Yes'
    when content_sans_https like '%charity care%' then  'Yes'
    when content_sans_https like '%drug discounts%' then  'Yes'
    when content_sans_https like '%340 b program%' then  'Yes'
    when content_sans_https like '%340 b pause act%' then 'Yes'
    else 'No'
    end;

update public.mntr
set flag_medicare_part_d=
    case
    when content_sans_https like '%medicare part d%' then  'Yes'
    when content_sans_https like '%extra help program%' then  'Yes'
    when content_sans_https like '%prescription drug benefit program%' then  'Yes'
    when content_sans_https like '%private negotiation%' then  'Yes'
    when content_sans_https like '%manufacturer rebates%' then  'Yes'
    when content_sans_https like '%non-interference clause%' then  'Yes'
    when content_sans_https like '%negotiated discounts%' then  'Yes'
    when content_sans_https like '%negotiated rebates%' then  'Yes'
    when content_sans_https like '%point-of sale%' then  'Yes'
    else 'No'
    end;
    
update public.mntr
set flag_medicare_part_b=
    case
    when content_sans_https like '%medicare part b%' then  'Yes'
    when content_sans_https like '%average sales price%' then  'Yes'
    when content_sans_https like '%asp%' then  'Yes' --i feel this will pull up random words like aspect, aspire etc.
    when content_sans_https like '%physician-administered medicines%' then  'Yes'
    when content_sans_https like '%physician-administered drugs%' then  'Yes'
    when content_sans_https like '%outpatient drugs%' then  'Yes'
    when content_sans_https like '%outpatient medicines%' then  'Yes'
    when content_sans_https like '%medicare outpatient benefit%' then  'Yes'
    else 'No'
    end;
    
update public.mntr
set flag_fda_modernization=
    case
    when content_sans_https like '%bsufa%' then  'Yes'
    when content_sans_https like '%biosimilar user fee agreement%' then  'Yes'
    when content_sans_https like '%biosimilar user fee act%' then  'Yes'
    when content_sans_https like '%pdufa%' then  'Yes'
    when content_sans_https like '%prescription drug user fee agreement%' then  'Yes'
    when content_sans_https like '%prescription drug user fee act%' then  'Yes'
    when content_sans_https like '%gdufa%' then  'Yes'
    when content_sans_https like '%generic drug user fee act%' then  'Yes'
    when content_sans_https like '%generic drug user fee agreement%' then  'Yes'
    when content_sans_https like '%right to try%' then  'Yes'
    when content_sans_https like '%right-to-try%' then  'Yes'
    when content_sans_https like '%creates act%' then  'Yes'
    when content_sans_https like '%rems%' then  'Yes'
    when content_sans_https like '%the creating and restoring equal access to equivalent samples act%' then  'Yes'
    when content_sans_https like '%risk evaluation and mitigation strategies%' then  'Yes'
    when content_sans_https like '%fda reauthorization act%' then  'Yes'
    when content_sans_https like '%scott gottlieb%' then  'Yes'
    when content_sans_https like '%clinical trial design%' then  'Yes'
    when content_sans_https like '%real-world evidence%' then  'Yes'
    when content_sans_https like '%abbreviated new drug application%' then  'Yes'
    when content_sans_https like '%anda%' then  'Yes'
    when content_sans_https like '%modernize the fda%' then  'Yes'
    when content_sans_https like '%fda modernization%' then  'Yes'
    when content_sans_https like '%innovative drug development%' then  'Yes'
    when content_sans_https like '%generic backlog%' then  'Yes'
    else 'No'
    end;

update public.mntr
set flag_intellectual_property=
    case
    when content_sans_https like '%intellectual property protections%' then  'Yes'
    when content_sans_https like '%patent%' then  'Yes'
    when content_sans_https like '%ip%' then  'Yes'
    when content_sans_https like '%hatch waxman%' then  'Yes'
    when content_sans_https like '%hatch-waxman%' then  'Yes'
    when content_sans_https like '%data protection%' then  'Yes'
    else 'No'
    end;

commit